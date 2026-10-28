#!/usr/bin/env python3
"""Run your attempt.py / attempt.cpp against a problem's local tests, like a judge would.

Usage:
  python3 scripts/verify.py <problem> [--lang py|cpp] [--time-factor F] [--show] [--only 01,03]
  python3 scripts/verify.py --setup          check Python, numpy and the C++ compiler

<problem> is a catalog id, folder or folder name (e.g. "Brick stacks"). The student's file is
attempt.py or attempt.cpp in the problem folder (start from templates/attempt/); with both present,
pass --lang. Tests are tests/NN.in with tests/NN.out (either may be gzipped: NN.in.gz).

Verdicts per test: OK, WA (wrong answer, or output over the size limit), RE (runtime error),
TLE (time limit exceeded), CE (compilation error), N/A (this kind of judging is not available yet).
The time limit is the CS Academy limit (data/csacademy_dump.json) times a factor: 2x for Python,
1x for C++ by default (--time-factor). Local times are approximate, and memory is not limited.
The summary is "passed X/Y local cases": the judge's tests are different, so it is not a score.

C++: compiled once in a temporary directory, outside the timing, with $CXX (default g++-14 when
installed, else g++) -std=c++17 -O2; an attempt that includes "lib/..." headers is bundled first
with scripts/bundle.py. Python: run with this interpreter and the repo root on PYTHONPATH, so
`from lib.x import y` works (bundle it before submitting).

Judging modes (from data/practice.json): tokens (whitespace-insensitive), float (1e-6 absolute or
relative), checker and interactive, which go through scripts/reveal.py (the checkers and
interactors are packed in the spoilers). Interfaces used, probed with `reveal.py --help` first:
  reveal.py --validate <problem id> <test input path> <output path>
      prints one line starting with OK or WA (anything else: N/A)
  reveal.py --interact <problem id> <test input path> --time-limit <seconds> -- <command...>
      runs the interactor against the command, prints only one line starting with
      OK, WA, RE or TLE (never the dialogue)

Each run is logged as a verify_run event through scripts/tutor_state.py (--no-log to skip).
Exit code: 0 all passed, 1 some failed, 2 not available or usage error, 3 could not be judged.
"""
import argparse
import gzip
import os
import platform
import re
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tutor_catalog import ROOT, cs_academy_url, judge_mode, load_catalog, resolve, time_limit_ms  # noqa: E402

REVEAL = ROOT / "scripts" / "reveal.py"
DEFAULT_TL_MS = 2000
DEFAULT_FACTOR = {"py": 2.0, "cpp": 1.0}
OUTPUT_LIMIT = 64 << 20   # bytes of stdout before the run is stopped
STDERR_LIMIT = 8 << 20
SHOW_LIMIT = 2000         # --show prints a failing case only when each part is at most this many bytes
COMPILE_TIMEOUT = 180
VERDICTS = ("OK", "WA", "RE", "TLE", "CE", "N/A")
CPP_LIB_INCLUDE = re.compile(r'^\s*#include\s+"(?:[^"]*/)?lib/[^"/]+"', re.M)


class Unavailable(Exception):
    """Verification cannot run for this problem (exit 2)."""


# ---------------------------------------------------------------- problem and files

def locate(arg, judge_override):
    """-> dict(id, name, folder, entry, judge). Uncatalogued folders are allowed (no logging)."""
    catalog = load_catalog()
    entry = None
    if catalog is not None:
        try:
            entry = resolve(arg, catalog)
        except LookupError as e:
            if not Path(arg).is_dir():
                raise Unavailable(str(e))
    elif not Path(arg).is_dir():
        raise Unavailable(f"no catalog (data/practice.json) yet: pass the problem folder instead of {arg!r}")
    if entry is None:
        folder = Path(arg).resolve()
        return {"id": None, "name": folder.name, "folder": folder, "entry": None,
                "judge": judge_override or "tokens"}
    folder = ROOT / entry["folder"]
    name = entry.get("longName") or folder.name
    if entry.get("capability") != "practice":
        url = cs_academy_url(entry)
        raise Unavailable(
            f"{name} is an archive problem: local verification is not available yet.\n"
            f"Statement: {entry['folder']}/PROBLEM.md" + (f"\nSubmit it on CS Academy: {url}" if url else ""))
    return {"id": entry["id"], "name": name, "folder": folder, "entry": entry, "judge": judge_mode(entry)}


def find_attempt(folder, lang):
    found = {k: folder / f"attempt.{k}" for k in ("py", "cpp") if (folder / f"attempt.{k}").exists()}
    if lang:
        if lang not in found:
            raise Unavailable(f"{folder / f'attempt.{lang}'} does not exist")
        return lang, found[lang]
    if len(found) == 2:
        raise Unavailable("both attempt.py and attempt.cpp exist: pass --lang py or --lang cpp")
    if not found:
        raise Unavailable(f"no attempt.py or attempt.cpp in {folder}\n"
                          f"Start from a template: cp templates/attempt/attempt.py \"{folder}/\"  "
                          "(or attempt.cpp)")
    return next(iter(found.items()))


def natural(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def find_tests(folder, need_out):
    tests_dir = folder / "tests"
    if not tests_dir.is_dir():
        raise Unavailable(f"{folder.name} has no tests/ folder yet: local verification is not available yet")
    tests = []
    for p in tests_dir.iterdir():
        m = re.fullmatch(r"(.+)\.in(\.gz)?", p.name)
        if not m:
            continue
        stem = m.group(1)
        out = next((q for q in (tests_dir / f"{stem}.out", tests_dir / f"{stem}.out.gz") if q.exists()), None)
        if out is None and need_out:
            print(f"warning: {p.name} has no {stem}.out, skipped", file=sys.stderr)
            continue
        tests.append((stem, p, out))
    if not tests:
        raise Unavailable(f"{tests_dir} has no tests: local verification is not available yet")
    return sorted(tests, key=lambda t: natural(t[0]))


def read_bytes(path):
    return gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_bytes()


def plain_copy(path, work):
    """A path to the uncompressed file (a copy in work/ when gzipped)."""
    if path.suffix != ".gz":
        return path
    dst = work / path.name[:-3]
    dst.write_bytes(read_bytes(path))
    return dst


# ---------------------------------------------------------------- build

def compiler():
    if os.environ.get("CXX"):
        return shlex.split(os.environ["CXX"])
    return [shutil.which("g++-14") or "g++"]


def build(lang, src, work):
    """-> (command, None) or (None, compiler message)."""
    if lang == "py":
        return [sys.executable, str(src)], None
    text = src.read_text(encoding="utf-8", errors="replace")
    code = work / "attempt.cpp"
    if CPP_LIB_INCLUDE.search(text):
        from bundle import bundle_cpp
        try:
            code.write_text(bundle_cpp(src))
        except OSError as e:
            return None, f"could not bundle the lib headers: {e}"
    else:
        shutil.copyfile(src, code)
    exe = work / "attempt"
    cmd = compiler() + ["-std=c++17", "-O2", "-o", str(exe), str(code)]
    try:
        r = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=COMPILE_TIMEOUT)
    except FileNotFoundError:
        return None, f"compiler not found: {cmd[0]} (set $CXX, or run verify.py --setup)"
    except subprocess.TimeoutExpired:
        return None, f"compilation took more than {COMPILE_TIMEOUT} s"
    if r.returncode != 0:
        return None, r.stderr
    return [str(exe)], None


# ---------------------------------------------------------------- running

def kill_group(p):
    try:
        if os.name == "posix":
            os.killpg(p.pid, signal.SIGKILL)
        else:
            p.kill()
    except (ProcessLookupError, PermissionError, OSError):
        pass
    p.wait()


def run_case(cmd, stdin_path, limit_s, work, env):
    """-> dict(status: ok|re|tle|ole, time, out_path, rc, stderr_tail)."""
    out_path, err_path = work / "out.txt", work / "err.txt"
    with open(stdin_path, "rb") as fin, open(out_path, "wb") as fout, open(err_path, "wb") as ferr:
        t0 = time.perf_counter()
        p = subprocess.Popen(cmd, stdin=fin, stdout=fout, stderr=ferr, cwd=work, env=env,
                             start_new_session=(os.name == "posix"))
        status = None
        while True:
            try:
                p.wait(timeout=0.01)
                break
            except subprocess.TimeoutExpired:
                pass
            if time.perf_counter() - t0 > limit_s:
                status = "tle"
            elif os.path.getsize(out_path) > OUTPUT_LIMIT or os.path.getsize(err_path) > STDERR_LIMIT:
                status = "ole"
            if status:
                kill_group(p)
                break
        elapsed = time.perf_counter() - t0
    if status is None:
        status = "ok" if p.returncode == 0 else "re"
    with open(err_path, "rb") as f:
        f.seek(max(0, os.path.getsize(err_path) - 1500))
        tail = f.read().decode("utf-8", "replace").strip().splitlines()[-6:]
    return {"status": status, "time": elapsed, "out_path": out_path, "rc": p.returncode, "stderr_tail": tail}


def describe_rc(rc):
    if rc is not None and rc < 0:
        try:
            return f"killed by {signal.Signals(-rc).name}"
        except ValueError:
            return f"killed by signal {-rc}"
    return f"exit code {rc}"


# ---------------------------------------------------------------- judging

def first_token_diff(got, exp):
    """-> None when equal, else a message that does not reveal expected values."""
    for i, (g, e) in enumerate(zip(got, exp)):
        if g != e:
            return f"token {i + 1} differs"
    if len(got) != len(exp):
        return f"{len(got)} tokens printed, {len(exp)} expected"
    return None


def floats_close(g, e):
    if g == e:
        return True
    try:
        a, b = float(g), float(e)
    except ValueError:
        return False
    return abs(a - b) <= 1e-6 * max(1.0, abs(b))


def judge_tokens(got_b, exp_b, mode):
    got, exp = got_b.split(), exp_b.split()
    if mode == "tokens":
        return first_token_diff(got, exp)
    for i, (g, e) in enumerate(zip(got, exp)):
        if not floats_close(g.decode("utf-8", "replace"), e.decode("utf-8", "replace")):
            return f"token {i + 1} differs (tolerance 1e-6)"
    if len(got) != len(exp):
        return f"{len(got)} tokens printed, {len(exp)} expected"
    return None


def reveal_supports(flag):
    if not REVEAL.exists():
        return False
    try:
        r = subprocess.run([sys.executable, str(REVEAL), "--help"], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return flag in r.stdout


def first_verdict(stdout, allowed):
    line = (stdout.strip().splitlines() or [""])[0].strip()
    word = line.split()[0] if line.split() else ""
    return (word, line[len(word):].strip(" :-")) if word in allowed else (None, line)


def judge_checker(pid, test_in, out_path):
    try:
        r = subprocess.run([sys.executable, str(REVEAL), "--validate", pid, str(test_in), str(out_path)],
                           capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired:
        return "N/A", "the checker did not answer"
    verdict, msg = first_verdict(r.stdout, ("OK", "WA"))
    if verdict is None:
        return "N/A", "checker not available yet"
    return verdict, msg


def run_interactive(pid, test_in, cmd, limit_s, work, env):
    full = [sys.executable, str(REVEAL), "--interact", pid, str(test_in), "--time-limit", f"{limit_s:.3f}", "--"] + cmd
    t0 = time.perf_counter()
    p = subprocess.Popen(full, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd=work, env=env, text=True,
                         start_new_session=(os.name == "posix"))
    try:
        stdout, _ = p.communicate(timeout=limit_s + 30)
    except subprocess.TimeoutExpired:
        kill_group(p)
        return "TLE", time.perf_counter() - t0, "the interactor did not finish"
    verdict, msg = first_verdict(stdout, ("OK", "WA", "RE", "TLE"))
    if verdict is None:
        return "N/A", time.perf_counter() - t0, "interactive verification not available yet"
    return verdict, time.perf_counter() - t0, msg


# ---------------------------------------------------------------- report

def show_block(title, data):
    text = data.decode("utf-8", "replace").rstrip("\n")
    print(f"      {title}:")
    for line in text.splitlines() or [""]:
        print(f"        {line}")


def maybe_show(args, judge, stem, test_in, test_out, got_path, verdict):
    """Small failing cases only, and only with --show. Expected output never for checker problems."""
    if not args.show or judge == "interactive":
        return
    inp = read_bytes(test_in)
    if len(inp) > SHOW_LIMIT:
        print(f"      (test {stem} is too big to show)")
        return
    show_block("input", inp)
    if verdict == "WA":
        got = got_path.read_bytes() if got_path.stat().st_size <= SHOW_LIMIT else None
        if judge != "checker" and test_out is not None:
            exp = read_bytes(test_out)
            if len(exp) > SHOW_LIMIT:
                print("      (expected output too big to show)")
            else:
                show_block("expected", exp)
        if got is None:
            print("      (your output is too big to show)")
        else:
            show_block("your output", got)


def log_run(pid, passed, total, counts, lang):
    try:
        from tutor_state import StateError, log_problem
        log_problem(pid, "verify_run", {"passed": passed, "total": total, "verdicts": counts, "lang": lang})
    except StateError as e:
        print(f"(not logged: {e})", file=sys.stderr)


def verify(args):
    prob = locate(args.problem, args.judge)
    judge = prob["judge"]
    tests = find_tests(prob["folder"], need_out=judge in ("tokens", "float"))
    if args.solution:  # maintainers: judge another file (e.g. the optimal solution) instead of attempt.*
        src = Path(args.solution).resolve()
        if src.suffix not in (".py", ".cpp") or not src.is_file():
            raise Unavailable(f"--solution needs an existing .py or .cpp file, got {args.solution}")
        lang = src.suffix[1:]
    else:
        lang, src = find_attempt(prob["folder"], args.lang)
    if args.only:
        wanted = set(args.only.split(","))
        tests = [t for t in tests if t[0] in wanted]
        if not tests:
            raise Unavailable(f"no test named {args.only}")
    tl = time_limit_ms(prob["entry"], prob["folder"])
    factor = args.time_factor if args.time_factor is not None else DEFAULT_FACTOR[lang]
    limit_s = (tl or DEFAULT_TL_MS) * factor / 1000
    checker_ok = judge != "checker" or reveal_supports("--validate")
    interact_ok = judge != "interactive" or reveal_supports("--interact")

    lang_name = f"Python {platform.python_version()}" if lang == "py" else "C++17"
    print(f"{prob['name']}: {src.name} ({lang_name}), judge: {judge}")
    tl_text = f"CS Academy {tl} ms" if tl else f"CS Academy limit unknown, using {DEFAULT_TL_MS} ms"
    print(f"time limit ~{limit_s:.2f} s per case ({tl_text} x {factor:g} for {'Python' if lang == 'py' else 'C++'}; "
          "local timing is approximate)")

    results = []
    with tempfile.TemporaryDirectory(prefix="verify-") as tmp:
        work = Path(tmp)
        cmd, ce = build(lang, src, work)
        if ce is not None:
            print("CE: compilation failed")
            for line in ce.strip().splitlines()[:40]:
                print(f"    {line}")
            if CPP_LIB_INCLUDE.search(src.read_text(encoding="utf-8", errors="replace")):
                print("    (line numbers refer to the bundled file, with the lib headers inlined)")
            results = [(t[0], "CE") for t in tests]
        else:
            env = dict(os.environ)
            env["PYTHONPATH"] = str(ROOT) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
            if judge == "interactive" and not interact_ok:
                results = [(t[0], "N/A") for t in tests]
                print("interactive verification is not available yet for this problem")
            for stem, test_in, test_out in ([] if results else tests):
                if judge == "interactive":
                    verdict, elapsed, msg = run_interactive(prob["id"], test_in, cmd, limit_s, work, env)
                    print(f"  {stem:>4}  {verdict:<4} {elapsed:6.2f} s  {msg}".rstrip())
                    results.append((stem, verdict))
                    continue
                r = run_case(cmd, plain_copy(test_in, work), limit_s, work, env)
                msg = ""
                if r["status"] == "tle":
                    verdict, msg = "TLE", ""
                elif r["status"] == "ole":
                    verdict, msg = "WA", f"output over {OUTPUT_LIMIT >> 20} MB, stopped"
                elif r["status"] == "re":
                    verdict, msg = "RE", describe_rc(r["rc"])
                elif judge == "checker":
                    if checker_ok:
                        verdict, msg = judge_checker(prob["id"], test_in, r["out_path"])
                    else:
                        verdict, msg = "N/A", "checker not available yet"
                else:
                    diff = judge_tokens(r["out_path"].read_bytes(), read_bytes(test_out), judge)
                    verdict, msg = ("OK", "") if diff is None else ("WA", diff)
                shown = f">{limit_s:.2f}" if verdict == "TLE" else f"{r['time']:.2f}"
                print(f"  {stem:>4}  {verdict:<4} {shown:>6} s  {msg}".rstrip())
                if verdict == "RE":
                    for line in r["stderr_tail"]:
                        print(f"        | {line}")
                if verdict in ("WA", "RE", "TLE"):
                    maybe_show(args, judge, stem, test_in, test_out, r["out_path"], verdict)
                results.append((stem, verdict))

    total = len(results)
    passed = sum(v == "OK" for _, v in results)
    counts = {v: sum(x == v for _, x in results) for v in VERDICTS if any(x == v for _, x in results)}
    unjudged = counts.get("N/A", 0)
    print(f"passed {passed}/{total} local cases" + (f" ({unjudged} could not be judged)" if unjudged else ""))
    print("These are local tests, not the judge's: passing all of them is not a contest score.")
    if not args.show and any(v in ("WA", "RE", "TLE") for _, v in results) and judge != "interactive":
        print("Rerun with --show to see the small failing cases.")
    if prob["id"] and not args.no_log and not args.solution:
        log_run(prob["id"], passed, total, counts, lang)
    if passed == total:
        return 0
    return 3 if unjudged and passed + unjudged == total else 1


def setup_check():
    ok = True
    v = sys.version_info
    print(f"Python {platform.python_version()} ({sys.executable})"
          + ("" if v >= (3, 10) else "  -> needs 3.10 or newer"))
    ok &= v >= (3, 10)
    try:
        import numpy
        print(f"numpy {numpy.__version__}")
    except ImportError:
        print("numpy: not installed (some optimal Python solutions use it: pip install numpy)")
    cxx = compiler()
    with tempfile.TemporaryDirectory(prefix="verify-setup-") as tmp:
        try:
            r = subprocess.run(cxx + ["-std=c++17", "-O2", "-o", str(Path(tmp) / "a"),
                                      str(ROOT / "templates" / "attempt" / "attempt.cpp")],
                               capture_output=True, text=True, timeout=COMPILE_TIMEOUT)
            good = r.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            good = False
    print(f"C++ compiler: {' '.join(cxx)} -> {'ok' if good else 'not working (set $CXX to g++)'}")
    if good and shutil.which("g++-14") is None and platform.system() == "Darwin" and not os.environ.get("CXX"):
        print("  note: on macOS g++ is usually clang, which has no <bits/stdc++.h>; brew install gcc")
    return 0 if ok and good else 1


def main(argv=None):
    p = argparse.ArgumentParser(description="Run attempt.* against a problem's local tests.",
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    p.add_argument("problem", nargs="?")
    p.add_argument("--lang", choices=("py", "cpp"))
    p.add_argument("--time-factor", type=float, help="multiplier of the CS Academy time limit")
    p.add_argument("--show", action="store_true", help="show small failing cases (input, expected, got)")
    p.add_argument("--only", help="comma-separated test names, e.g. 01,03")
    p.add_argument("--no-log", action="store_true", help="do not log the run in .tutor/")
    p.add_argument("--judge", choices=("tokens", "float", "checker", "interactive"), help=argparse.SUPPRESS)
    p.add_argument("--solution", help=argparse.SUPPRESS)  # maintainers (CI): judge this file, never logged
    p.add_argument("--setup", action="store_true", help="check Python, numpy and the C++ compiler")
    args = p.parse_args(argv)
    if args.setup:
        return setup_check()
    if not args.problem:
        p.error("the problem is required")
    if args.time_factor is not None and args.time_factor <= 0:
        p.error("--time-factor must be positive")
    try:
        return verify(args)
    except Unavailable as e:
        print(e)
        return 2


if __name__ == "__main__":
    sys.exit(main())
