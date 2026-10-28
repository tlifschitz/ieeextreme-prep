#!/usr/bin/env python3
"""Reveal a problem's spoiler: give up, or let the tutor read a hint.

Usage:
  python3 scripts/reveal.py <problem> [--yes]            give up: record it, then install the solution
  python3 scripts/reveal.py --hint <problem> --step N    hint blocks up to ladder step N (no code)
  python3 scripts/reveal.py --peek <problem>             solution code, for the tutor (Claude Code only)
  python3 scripts/reveal.py --validate <problem> <test input> <output>
        checker verdict only: one line, OK or WA <reason>; the expected output is the
        sibling NN.out / NN.out.gz of the test input NN.in / NN.in.gz
  python3 scripts/reveal.py --interact <problem> <test input> --time-limit <seconds> -- <command...>
        run the problem's interactor against the command: one line, OK, WA, RE or TLE
        (never the dialogue)
  python3 scripts/reveal.py --learn <technique>          a technique and its problems, easy to hard

<problem> is the catalog id (data/practice.json), the folder name (quote it if it has spaces or
apostrophes) or the path to the folder.

Giving up is one transaction, safe to run again if it was interrupted:
  1. preflight: the problem is in the catalog, its spoiler.bin exists, git knows who you are;
  2. the spoiler is decoded and verified into a temporary folder;
  3. the destinations are checked: nothing of yours is overwritten (attempt.* never is);
  4. a line (problem, date, hints used) is appended to progress/give-ups.md and only that file
     is committed, whatever else is staged;
  5. the files are installed into the problem folder.
If the record is already committed, a rerun only finishes step 5, without a second record.
Nothing is ever pushed. The give-up is also logged as a gave_up event in .tutor/
(scripts/tutor_state.py) when that is available.

Checkers (--validate) are checker.py in the spoiler, run in memory: check(input_text,
candidate_text, expected_text) returns True / None / "OK" for an accepted output, or False,
a message, or (False, message) for a wrong one; any exception is "WA checker could not read
the output". Interactors (--interact) are interactor.py, run from a temporary folder outside
the repository as `python3 interactor.py <secret file>`, ending their stderr with
"VERDICT OK" or "VERDICT <reason>".

This is friction, not security: the key is in scripts/spoiler.py.
"""
import argparse
import contextlib
import datetime
import gzip
import io
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import spoiler  # noqa: E402

GIVE_UPS = "progress/give-ups.md"
GIVE_UPS_HEAD = "# Give-ups\n\n| Problem | Folder | Date | Hints used |\n|---|---|---|---|\n"
NOT_AVAILABLE = 3


class Abort(Exception):
    pass


def git(*args, check=True):
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    if check and r.returncode:
        raise Abort(f"git {' '.join(args)} failed:\n{(r.stderr or r.stdout).strip()}")
    return r


def entry_for(arg):
    try:
        catalog = spoiler.load_catalog()
    except OSError:
        raise Abort("data/practice.json not found: run this from a clone of the practice repo") from None
    try:
        return spoiler.resolve(arg, catalog)
    except LookupError as e:
        raise Abort(str(e)) from None


def spoiler_root():
    """Where spoiler.bin and data/techniques.bin are read from: the clone, or REVEAL_SPOILER_ROOT
    (maintainers: a tree built by build_spoilers.py --out, e.g. to run checkers on solutions)."""
    return Path(os.environ.get("REVEAL_SPOILER_ROOT") or ROOT)


def read_spoiler(entry):
    path = spoiler_root() / entry["folder"] / spoiler.SPOILER_NAME
    try:
        return path.read_bytes()
    except OSError:
        raise Abort(f"{entry['folder']}/{spoiler.SPOILER_NAME} is missing: update your clone") from None


def archive_notice(entry, what):
    print(f"{entry['longName']} is an archive problem: {what} not available for it yet.\n"
          f"  Statement: {entry['folder']}/PROBLEM.md\n"
          f"  Judge:     {spoiler.cs_academy_url(entry)}\n"
          f"  Give up:   python3 scripts/reveal.py {entry['id']}")
    return NOT_AVAILABLE


# Staging and installation (also used by build_spoilers.py --check).

def stage(blob, problem_id, tmp):
    """Decode and verify blob, write its files under tmp. -> {relpath: (staged path, executable)}."""
    files = spoiler.decode(blob, problem_id)  # verifies the hash and every member name
    tmp = Path(tmp)
    staged = {}
    for rel, (data, executable) in sorted(files.items()):
        p = tmp.joinpath(*rel.split("/"))
        if not p.resolve().is_relative_to(tmp.resolve()):
            raise spoiler.SpoilerError(f"unsafe path in spoiler: {rel!r}")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        staged[rel] = (p, executable)
    return staged


def plan(folder, staged):
    """-> (relpaths to install, conflicts). An identical existing file is already installed."""
    folder = Path(folder)
    base = folder.resolve()
    todo, conflicts = [], []
    for rel, (src, _) in sorted(staged.items()):
        dest = folder.joinpath(*rel.split("/"))
        parts = [folder.joinpath(*rel.split("/")[:i]) for i in range(1, rel.count("/") + 2)]
        if any(p.is_symlink() for p in parts) or not dest.resolve().is_relative_to(base):
            conflicts.append(f"{rel} (path leaves the problem folder)")
        elif any(p.exists() and not p.is_dir() for p in parts[:-1]):
            conflicts.append(f"{rel} (a parent is not a folder)")
        elif spoiler.ATTEMPT.match(dest.name):
            conflicts.append(f"{rel} (attempt files are never overwritten)")
        elif not dest.exists():
            todo.append(rel)
        elif not dest.is_file() or dest.read_bytes() != src.read_bytes():
            conflicts.append(rel)
    return todo, conflicts


def install(folder, staged, todo):
    """Copy the planned files atomically (a crash leaves each file old or new, never half)."""
    for rel in todo:
        src, executable = staged[rel]
        dest = Path(folder).joinpath(*rel.split("/"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_name(f".{dest.name}.reveal-tmp")
        tmp.write_bytes(src.read_bytes())
        os.chmod(tmp, 0o755 if executable else 0o644)
        os.replace(tmp, dest)


# Give up.

def tutor_status(entry):
    """The problem's state from scripts/tutor_state.py (status --json), or None without it."""
    try:
        import tutor_state
        return tutor_state, tutor_state.problem_status(entry["id"])
    except Exception:  # noqa: BLE001 - the tutor state is optional for giving up
        return None, None


def hints_used(entry):
    """Highest hint step given, from the tutor state; "unknown" without a readable history."""
    _, st = tutor_status(entry)
    if not st or st.get("history") != "known":
        return "unknown"
    n = st.get("hints_used") or 0
    return f"up to step {n}" if n else "none"


def log_gave_up(entry):
    """Log a gave_up event in .tutor/ when the tutor state is available (never fatal)."""
    ts, st = tutor_status(entry)
    if ts is None or (st and st.get("gave_up")):
        return
    fields = {"hints_used": str(st["hints_used"])} if st and st.get("history") == "known" else {}
    try:
        ts.log_problem(entry["id"], "gave_up", fields)
    except Exception as e:  # noqa: BLE001
        print(f"(give-up not logged in the tutor state: {e})", file=sys.stderr)


def row_prefix(entry):
    return f"| {entry['id']} |"


def recorded_in_head(entry):
    r = git("show", f"HEAD:{GIVE_UPS}", check=False)
    return r.returncode == 0 and any(line.startswith(row_prefix(entry)) for line in r.stdout.splitlines())


def preflight(entry):
    if not (ROOT / ".git").exists():
        raise Abort(f"{ROOT} is not a git clone: giving up needs git to record it")
    top = git("rev-parse", "--show-toplevel").stdout.strip()
    if Path(top).resolve() != ROOT.resolve():
        raise Abort(f"unexpected git top level {top}")
    missing = [k for k in ("user.name", "user.email") if not git("config", "--get", k, check=False).stdout.strip()]
    missing = [k for k in missing if not os.environ.get("GIT_AUTHOR_" + k.split(".")[1].upper())]
    if missing:
        raise Abort("git does not know who you are, so the give-up cannot be recorded. Set it with:\n"
                    '  git config user.name "Your Name"\n'
                    '  git config user.email "you@example.com"\n'
                    "(add --global to use it in every repo), then run this again.")


def record(entry):
    """Append the give-up line and commit only progress/give-ups.md. Undone if the commit fails."""
    path = ROOT / GIVE_UPS
    before = path.read_text() if path.exists() else None
    text = before or GIVE_UPS_HEAD
    if not any(line.startswith(row_prefix(entry)) for line in text.splitlines()):
        if not text.endswith("\n"):
            text += "\n"
        today = datetime.date.today().isoformat()
        text += f"{row_prefix(entry)} {entry['folder']} | {today} | {hints_used(entry)} |\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    try:
        git("add", "--", GIVE_UPS)
        git("commit", "-q", "-m", f"chore: give up on {entry['id']}", "--", GIVE_UPS)
    except Abort:
        if before is None:
            git("rm", "-q", "--cached", "--ignore-unmatch", "--", GIVE_UPS, check=False)
            path.unlink(missing_ok=True)
            if path.parent.exists() and not any(path.parent.iterdir()):
                path.parent.rmdir()
        else:
            path.write_text(before)
            git("reset", "-q", "--", GIVE_UPS, check=False)
        raise


def confirm(entry, yes):
    if yes:
        return
    if not sys.stdin.isatty():
        raise Abort("giving up needs a confirmation: run it in a terminal, or pass --yes")
    print(f"Give up on {entry['longName']}? This commits a record to {GIVE_UPS} and installs\n"
          f"the solution, LEVELS.md and NOTES.md into {entry['folder']}.")
    if input(f"Type {entry['id']} to confirm: ").strip() != entry["id"]:
        raise Abort("not confirmed, nothing done")


def give_up(arg, yes):
    entry = entry_for(arg)
    blob = read_spoiler(entry)
    preflight(entry)
    already = recorded_in_head(entry)
    if not already:
        confirm(entry, yes)
    folder = ROOT / entry["folder"]
    with tempfile.TemporaryDirectory(prefix="reveal-") as tmp:
        try:
            staged = stage(blob, entry["id"], tmp)
        except spoiler.SpoilerError as e:
            raise Abort(f"{entry['folder']}/{spoiler.SPOILER_NAME}: {e}") from None
        todo, conflicts = plan(folder, staged)
        if conflicts:
            raise Abort("these files already exist with other content and would be overwritten:\n  "
                        + "\n  ".join(conflicts) + "\nMove or rename them, then run this again. Nothing was done.")
        if already:
            print(f"The give-up on {entry['id']} is already recorded; finishing the installation.")
        else:
            record(entry)
            print(f"Recorded in {GIVE_UPS} (committed, not pushed).")
        log_gave_up(entry)
        install(folder, staged, todo)
    if todo:
        print(f"Installed into {entry['folder']}:\n  " + "\n  ".join(todo))
    else:
        print(f"Everything was already installed in {entry['folder']}.")
    return 0


# Tutor access.

def peek(arg):
    entry = entry_for(arg)
    if os.environ.get("CLAUDECODE") != "1" or sys.stdout.isatty():
        print("--peek is only for the tutor (Claude Code), after you agree to it.\n"
              "To see the solution yourself, give up: python3 scripts/reveal.py "
              f"{entry['id']}", file=sys.stderr)
        return 1
    if entry["capability"] != "practice":
        return archive_notice(entry, "tutoring is")
    files = spoiler.decode(read_spoiler(entry), entry["id"])
    code = sorted(n for n in files if "/" not in n and Path(n).stem == "solution")
    for n in code:
        print(f"===== {n} =====")
        print(files[n][0].decode(errors="replace").rstrip("\n"))
    return 0


def hint(arg, step):
    entry = entry_for(arg)
    if entry["capability"] != "practice":
        return archive_notice(entry, "hints are")
    if step is None or not 1 <= step <= 5:
        raise Abort("--hint needs --step N with N from 1 to 5")
    files = spoiler.decode(read_spoiler(entry), entry["id"])
    if "hints.json" not in files:
        print(f"Hints for {entry['longName']} are not available yet.")
        return NOT_AVAILABLE
    doc = json.loads(files["hints.json"][0])
    if doc.get("format") != 1:
        raise Abort(f"hint format {doc.get('format')} not supported: update scripts/reveal.py")
    blocks = [b for b in doc["blocks"] if b["step"] <= step]
    for b in blocks:
        print(f"[step {b['step']}: {b['kind']}]\n{b['markdown']}\n")
    later = sorted({b["step"] for b in doc["blocks"] if b["step"] > step})
    nxt = f"step {later[0]}" if later else "giving up"
    if not blocks:
        print(f"No hints up to step {step}.")
    elif not any(b["step"] == step for b in blocks):
        # A step can be left out when it would say almost as much as a later one.
        print(f"This problem has no separate step-{step} hint: the next step up is {nxt}.")
    else:
        print(f"Next step up: {nxt}.")
    return 0


def expected_for(test):
    """The expected output of a test input NN.in[.gz]: the sibling NN.out or NN.out.gz ("" if none)."""
    test = Path(test)
    stem = re.sub(r"\.in(\.gz)?$", "", test.name)
    for cand in (test.with_name(f"{stem}.out"), test.with_name(f"{stem}.out.gz")):
        if cand.is_file():
            return read_text(cand)
    return ""


def read_text(path):
    data = Path(path).read_bytes()
    if str(path).endswith(".gz"):
        data = gzip.decompress(data)
    return data.decode("utf-8", errors="replace")


def judged_entry(arg, judge, what):
    """-> (entry, spoiler files) for a practice problem judged by `judge`, or (exit code, None)."""
    entry = entry_for(arg)
    if entry["capability"] != "practice":
        return archive_notice(entry, what), None
    if entry.get("judge") != judge:
        print(f"{entry['longName']} is judged by comparing tokens ({entry.get('judge')}), not with --"
              + ("validate" if judge == "checker" else "interact"))
        return NOT_AVAILABLE, None
    return entry, spoiler.decode(read_spoiler(entry), entry["id"])


def checker_verdict(code, inp, out, exp):
    """Run check(input, candidate, expected) from code in a fresh namespace -> (ok, message)."""
    ns = {"__name__": "checker", "__builtins__": __builtins__}
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            exec(compile(code, "checker.py", "exec"), ns)
            res = ns["check"](inp, out, exp)
    except BaseException as e:  # noqa: BLE001 - malformed output must never print a traceback
        if isinstance(e, KeyboardInterrupt):
            raise
        return False, "checker could not read the output"
    msg = ""
    if isinstance(res, tuple) and len(res) == 2:
        res, msg = res
    if res is None or res is True or (isinstance(res, str) and res.strip().upper() in ("", "OK")):
        return True, ""
    if isinstance(res, str):
        return False, res.strip().splitlines()[0]
    return False, (str(msg).strip().splitlines() or ["wrong answer"])[0] if msg else "wrong answer"


def validate(arg, test, output):
    entry, files = judged_entry(arg, "checker", "tests and checkers are")
    if files is None:
        return entry
    if "checker.py" not in files:
        print(f"Checking outputs of {entry['longName']} is not available yet.")
        return NOT_AVAILABLE
    try:
        inp, out, exp = read_text(test), read_text(output), expected_for(test)
    except (OSError, ValueError, EOFError) as e:
        raise Abort(f"could not read the test or the output: {e}") from None
    ok, msg = checker_verdict(files["checker.py"][0].decode(), inp, out, exp)
    print("OK" if ok else f"WA {msg}")
    return 0 if ok else 1


def kill_group(p):
    try:
        os.killpg(p.pid, signal.SIGKILL) if os.name == "posix" else p.kill()
    except (ProcessLookupError, PermissionError, OSError):
        pass
    try:
        p.wait(timeout=5)
    except subprocess.TimeoutExpired:
        pass


def last_line(path, limit=4096):
    with open(path, "rb") as f:
        f.seek(max(0, os.path.getsize(path) - limit))
        lines = f.read().decode("utf-8", "replace").strip().splitlines()
    return lines[-1].strip() if lines else ""


def interact(arg, test, time_limit, command):
    """Run the problem's interactor against command. Prints only the final verdict.

    The interactor gets the test input as its secret file and writes the dialogue and a last
    line "VERDICT OK [details]" (or "VERDICT <reason>") to its stderr, as in scripts/check.py; both stay
    in a temporary folder outside the repository, deleted afterwards.
    """
    if not command:
        raise Abort("--interact needs the command to run after --")
    if time_limit is None or time_limit <= 0:
        raise Abort("--interact needs --time-limit SECONDS")
    entry, files = judged_entry(arg, "interactive", "tests and interactors are")
    if files is None:
        return entry
    if "interactor.py" not in files:
        print(f"Interactive checking of {entry['longName']} is not available yet.")
        return NOT_AVAILABLE
    try:
        secret_text = read_text(test)
    except (OSError, ValueError, EOFError) as e:
        raise Abort(f"could not read the test: {e}") from None
    tmp = Path(tempfile.mkdtemp(prefix="interact-"))
    if tmp.resolve().is_relative_to(ROOT.resolve()):
        shutil.rmtree(tmp, ignore_errors=True)
        raise Abort("the temporary folder is inside the repository: set TMPDIR elsewhere")
    judge = prog = None
    try:
        (tmp / "interactor.py").write_bytes(files["interactor.py"][0])
        (tmp / "secret.txt").write_text(secret_text)
        posix = os.name == "posix"
        with open(tmp / "dialogue.txt", "wb") as dialogue:
            judge = subprocess.Popen([sys.executable, str(tmp / "interactor.py"), str(tmp / "secret.txt")],
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=dialogue,
                                     cwd=tmp, start_new_session=posix)
        try:
            prog = subprocess.Popen(command, stdin=judge.stdout, stdout=judge.stdin,
                                    stderr=subprocess.DEVNULL, start_new_session=posix)
        except OSError as e:
            print(f"RE could not start the program: {e.strerror or e}")
            return 1
        finally:
            judge.stdout.close()
            judge.stdin.close()
        verdict = None
        try:
            prog.wait(timeout=time_limit)
        except subprocess.TimeoutExpired:
            verdict = f"TLE over {time_limit:g} s"
        kill_group(prog)
        try:
            judge.wait(timeout=max(5.0, time_limit))
        except subprocess.TimeoutExpired:
            verdict = verdict or "WA the interactor did not finish"
        kill_group(judge)
        if verdict is None:
            rc = prog.returncode
            final = last_line(tmp / "dialogue.txt")
            if final == "VERDICT OK" or final.startswith("VERDICT OK "):
                verdict = "OK" if rc == 0 else f"RE {describe_rc(rc)}"
            elif rc not in (0, -getattr(signal, "SIGPIPE", 13)):
                verdict = f"RE {describe_rc(rc)}"
            else:
                verdict = "WA the interactor rejected the dialogue"
        print(verdict)
        return 0 if verdict == "OK" else 1
    finally:
        for p in (prog, judge):
            if p is not None and p.poll() is None:
                kill_group(p)
        shutil.rmtree(tmp, ignore_errors=True)


def describe_rc(rc):
    if rc is not None and rc < 0:
        try:
            return f"killed by {signal.Signals(-rc).name}"
        except ValueError:
            return f"killed by signal {-rc}"
    return f"exit code {rc}"


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.casefold())


def learn(technique):
    path = spoiler_root() / spoiler.TECHNIQUES_BIN
    if not path.is_file():
        print(f"The technique index ({spoiler.TECHNIQUES_BIN}) is not available yet.")
        return NOT_AVAILABLE
    try:
        index = spoiler.read_techniques(path.read_bytes())["techniques"]
    except (spoiler.SpoilerError, ValueError) as e:
        raise Abort(f"{spoiler.TECHNIQUES_BIN}: {e}") from None
    q = norm(technique)
    hits = [k for k, t in index.items() if q and q in (norm(k), norm(t["name"]))]
    if not hits:
        hits = [k for k, t in index.items() if q and q in {norm(a) for a in t["aliases"]}]
    if len(hits) == 1:
        t = index[hits[0]]
        print(f"{t['name']} ({hits[0]}, family: {t['family']})\n")
        print(textwrap.fill(t["description"], 96) + "\n")
        print("Problems, easy to hard:")
        for i, p in enumerate(t["problems"], 1):
            print(f"  {i}. {p['longName']} ({p['id']}): {p['folder']}/PROBLEM.md")
        return 0
    family = sorted(k for k, t in index.items() if q and norm(t["family"]) == q)
    if hits or family:
        print(f"{technique!r} matches several techniques; pick one:")
        for k in hits or family:
            print(f"  {index[k]['name']} ({k})")
        return NOT_AVAILABLE
    print(f"No technique matches {technique!r}. Techniques in the index:")
    by_family = {}
    for k, t in sorted(index.items(), key=lambda kv: kv[1]["name"].casefold()):
        by_family.setdefault(t["family"], []).append(f"{t['name']} ({k})")
    for fam, names in sorted(by_family.items()):
        print(textwrap.fill(f"{fam}: " + "; ".join(names), 96, initial_indent="  ", subsequent_indent="    "))
    return NOT_AVAILABLE


def main(argv):
    command = []
    if "--" in argv:
        i = argv.index("--")
        argv, command = argv[:i], argv[i + 1:]
    ap = argparse.ArgumentParser(prog="reveal.py", description=__doc__.split("\n\n")[0],
                                 usage=__doc__.split("\n\n")[1].replace("Usage:\n", "\n"))
    ap.add_argument("problem", nargs="?")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--hint", metavar="PROBLEM", help="hint blocks up to --step N (no code)")
    g.add_argument("--peek", metavar="PROBLEM", help="solution code, for the tutor in Claude Code only")
    g.add_argument("--validate", nargs=3, metavar=("PROBLEM", "TEST", "OUTPUT"),
                   help="checker verdict of OUTPUT for the test input TEST: one line, OK or WA")
    g.add_argument("--interact", nargs=2, metavar=("PROBLEM", "TEST"),
                   help="run the interactor of TEST against the command after --: one line, OK/WA/RE/TLE")
    g.add_argument("--learn", metavar="TECHNIQUE", help="a technique and its problems, easy to hard")
    ap.add_argument("--step", type=int)
    ap.add_argument("--time-limit", type=float, metavar="SECONDS", help="with --interact")
    ap.add_argument("--yes", action="store_true", help="give up without the confirmation prompt")
    a = ap.parse_args(argv)
    modes = [m for m in (a.hint, a.peek, a.validate, a.interact, a.learn) if m is not None]
    if (a.problem is None) == (not modes):
        ap.error("give a problem to give up on, or exactly one of --hint/--peek/--validate/--interact/--learn")
    if command and a.interact is None:
        ap.error("a command after -- is only for --interact")
    try:
        if a.hint is not None:
            return hint(a.hint, a.step)
        if a.peek is not None:
            return peek(a.peek)
        if a.validate is not None:
            return validate(*a.validate)
        if a.interact is not None:
            return interact(*a.interact, a.time_limit, command)
        if a.learn is not None:
            return learn(a.learn)
        return give_up(a.problem, a.yes)
    except Abort as e:
        print(e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
