#!/usr/bin/env python3
"""CI of the public branch: the published tests agree with the published spoilers.

Usage: python3 scripts/ci_public.py structure
       python3 scripts/ci_public.py tests [-j JOBS] [--time-factor F] [problem...]
       python3 scripts/ci_public.py links [-j JOBS] [--retries N] [--timeout S]

The public branch holds no plaintext solution, so everything is checked through the
spoilers. Spoilers are read from REVEAL_SPOILER_ROOT when set, else from the checkout. On the
solutions branch (no spoiler.bin, scripts/build_spoilers.py present) they are first built from
HEAD into a temporary spoiler root, so the same checks run before a publication.

structure  every practice problem of data/practice.json has tests/ (each NN.in with its
           NN.out, except for checker and interactive problems), and its spoiler decodes and
           holds a solution, hints.json, and the checker.py / interactor.py its judge needs.
           With data/publication.json: the tracked files are exactly the manifest's
           artifacts plus the manifest itself.
tests      every practice problem's spoiler is decoded into a temporary directory outside
           the checkout; its optimal (solution.cpp when present, else solution.py, as in
           ci_verify_optimal.py) is judged by `verify.py <id> --solution <file> --no-log`
           against the published tests. Checker and interactive problems go through
           reveal.py --validate / --interact, which read the same spoilers. Every test must
           be OK. The decoded files are deleted afterwards, and a failure prints only the
           verdict lines (never a stderr tail, which could quote the solution: the logs of a
           public repository are public).
links      every http(s) URL of data/references.json answers (HEAD, then GET), with retries.
           Network dependent: run it in a non-blocking job.
"""
import argparse
import json
import re
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import spoiler  # noqa: E402

JUDGE_FILES = {"checker": "checker.py", "interactive": "interactor.py"}
OPTIMAL = ("solution.cpp", "solution.py")
REFERENCES = ROOT / "data" / "references.json"


def practice(catalog):
    return [e for e in catalog if e["capability"] == "practice"]


def outside_checkout(prefix):
    tmp = Path(tempfile.mkdtemp(prefix=prefix)).resolve()
    if tmp.is_relative_to(ROOT.resolve()):
        shutil.rmtree(tmp, ignore_errors=True)
        raise SystemExit(f"the temp dir {tmp} is inside the checkout: set TMPDIR elsewhere")
    return tmp


class Spoilers:
    """The spoiler root: REVEAL_SPOILER_ROOT, the checkout, or (solutions) a temporary build."""

    def __init__(self, catalog):
        self.built = None
        env = os.environ.get("REVEAL_SPOILER_ROOT")
        if env:
            self.root = Path(env)
        elif all((ROOT / e["folder"] / spoiler.SPOILER_NAME).is_file() for e in catalog) \
                or not (ROOT / "scripts" / "build_spoilers.py").is_file():
            self.root = ROOT
        else:
            self.built = self.root = outside_checkout("ci-public-spoilers-")
            r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_spoilers.py"), "--out", str(self.root)],
                               cwd=ROOT, capture_output=True, text=True)
            if r.returncode:
                self.close()
                raise SystemExit(f"build_spoilers.py --out failed:\n{r.stdout}{r.stderr}")
            print(f"no spoiler.bin in the checkout: {r.stdout.strip()}")

    def decode(self, entry):
        return spoiler.decode((self.root / entry["folder"] / spoiler.SPOILER_NAME).read_bytes(), entry["id"])

    def env(self):
        return dict(os.environ, REVEAL_SPOILER_ROOT=str(self.root))

    def close(self):
        if self.built:
            shutil.rmtree(self.built, ignore_errors=True)


# ---------------------------------------------------------------- structure

def check_tests_dir(entry):
    tests = ROOT / entry["folder"] / "tests"
    if not tests.is_dir():
        return ["no tests/ folder"]
    ins = [p for p in tests.iterdir() if p.name.endswith((".in", ".in.gz"))]
    if not ins:
        return ["tests/ has no NN.in"]
    if entry["judge"] in JUDGE_FILES:
        return []
    errors = []
    for p in ins:
        stem = p.name[: p.name.index(".in")]
        if not any((tests / f"{stem}.out{gz}").is_file() for gz in ("", ".gz")):
            errors.append(f"tests/{p.name} has no {stem}.out")
    return errors


def tracked_vs_manifest():
    manifest = ROOT / "data" / "publication.json"
    if not manifest.is_file():
        return []
    r = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True)
    if r.returncode:
        return [f"git ls-files failed: {r.stderr.decode().strip()}"]
    tracked = {p for p in r.stdout.decode().split("\0") if p}
    listed = set(json.loads(manifest.read_text())["artifacts"]) | {"data/publication.json"}
    errors = [f"{p}: in the manifest but not tracked" for p in sorted(listed - tracked)]
    errors += [f"{p}: tracked but not in the publication manifest" for p in sorted(tracked - listed)]
    return errors


def structure(catalog, spoilers):
    errors = []
    for e in practice(catalog):
        errs = check_tests_dir(e)
        try:
            files = spoilers.decode(e)
            if not any(n in files for n in OPTIMAL):
                errs.append("spoiler has no solution.cpp or solution.py")
            if "hints.json" not in files:
                errs.append("spoiler has no hints.json")
            need = JUDGE_FILES.get(e["judge"])
            if need and need not in files:
                errs.append(f"spoiler has no {need} ({e['judge']} judge)")
        except (OSError, spoiler.SpoilerError) as err:
            errs.append(f"spoiler: {err}")
        errors += [f"{e['id']}: {m}" for m in errs]
    errors += tracked_vs_manifest()
    return errors


# ---------------------------------------------------------------- tests

def judge(entry, spoilers, factor):
    """Decode the spoiler outside the checkout and judge its optimal with verify.py."""
    tmp = outside_checkout("ci-public-optimal-")
    try:
        files = spoilers.decode(entry)
        for rel, (data, executable) in files.items():
            dest = tmp.joinpath(*rel.split("/"))
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            dest.chmod(0o755 if executable else 0o644)
        sol = next((tmp / n for n in OPTIMAL if n in files), None)
        if sol is None:
            return entry, 1, "spoiler has no solution.cpp or solution.py"
        cmd = [sys.executable, str(ROOT / "scripts" / "verify.py"), entry["id"], "--solution", str(sol), "--no-log"]
        if factor:
            cmd += ["--time-factor", str(factor)]
        r = subprocess.run(cmd, capture_output=True, text=True, env=spoilers.env(), cwd=ROOT)
        return entry, r.returncode, (r.stdout + r.stderr).strip()
    except (OSError, spoiler.SpoilerError) as err:
        return entry, 1, f"spoiler: {err}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def tests(catalog, spoilers, problems, jobs, factor):
    if problems:
        try:
            entries = [spoiler.resolve(p, catalog) for p in problems]
        except LookupError as e:
            raise SystemExit(str(e)) from None
    else:
        entries = practice(catalog)
    with ThreadPoolExecutor(max(1, jobs)) as pool:
        results = list(pool.map(lambda e: judge(e, spoilers, factor), entries))
    failed = 0
    for entry, rc, out in results:
        lines = out.splitlines()
        summary = next((ln for ln in lines if ln.startswith("passed ")), lines[-1] if lines else "")
        failed += rc != 0
        print(f"[{'OK' if rc == 0 else 'FAIL'}] {entry['id']}: {summary}")
        if rc:  # an allowlist of verdict lines: compiler and runtime messages quote the solution's source
            shown = [m.group(0).strip() for m in map(VERDICT_LINE.match, lines) if m]
            print("    " + "\n    ".join(shown))
    print(f"{len(results) - failed}/{len(results)} problems: the spoiler's optimal passes every published test")
    return 1 if failed else 0


# The only lines of a failing verify.py run that reach the (public) CI log: per-test verdicts with
# their time, the summary and the compile-failure headline. Never messages, diagnostics or excerpts.
VERDICT_LINE = re.compile(r"^\s+\S+\s+(OK|WA|RE|TLE|CE|N/A)\s+\S+ s|^passed \d+/\d+ local cases|^CE: compilation failed$")


# ---------------------------------------------------------------- links

def urls(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from urls(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from urls(v)
    elif isinstance(obj, str) and obj.startswith(("http://", "https://")):
        yield obj


def probe(url, retries, timeout):
    last = ""
    for attempt in range(retries + 1):
        if attempt:
            time.sleep(2 ** attempt)
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, method=method, headers={
                "User-Agent": "Mozilla/5.0 (compatible; references-link-check)"})
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return url, True, f"{resp.status}"
            except urllib.error.HTTPError as e:
                last = f"HTTP {e.code}"
                if e.code in (404, 410):
                    return url, False, last
            except (urllib.error.URLError, OSError, ValueError) as e:
                last = str(getattr(e, "reason", e))
    return url, False, last


def links(jobs, retries, timeout):
    if not REFERENCES.is_file():
        print("no data/references.json: nothing to check")
        return 0
    found = sorted(set(urls(json.loads(REFERENCES.read_text()))))
    with ThreadPoolExecutor(max(1, jobs)) as pool:
        results = list(pool.map(lambda u: probe(u, retries, timeout), found))
    # Publishers (ACM, Elsevier, MIT Press...) answer 403 to scripts, and some hosts are just slow:
    # those links are unverified, not broken. Only a real error (404, 410, 5xx, DNS) fails the job.
    unverified = [(u, why) for u, ok, why in results if not ok and (why == "HTTP 403" or "timed out" in why)]
    bad = [(u, why) for u, ok, why in results if not ok and (u, why) not in unverified]
    gha = os.environ.get("GITHUB_ACTIONS")
    for u, why in unverified:
        print(f"::notice::unverified reference link {u} ({why}: blocks scripts or is slow)" if gha else
              f"UNVERIFIED {u} ({why})")
    for u, why in bad:
        print(f"::warning::broken reference link {u} ({why})" if gha else f"BROKEN {u} ({why})")
    print(f"{len(found) - len(bad) - len(unverified)}/{len(found)} reference links answer, "
          f"{len(unverified)} unverified, {len(bad)} broken")
    return 1 if bad else 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=("structure", "tests", "links"))
    ap.add_argument("problems", nargs="*")
    ap.add_argument("-j", "--jobs", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--time-factor", type=float, help="passed to verify.py (CI machines are slower)")
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--timeout", type=float, default=20)
    a = ap.parse_args(argv)
    if a.command == "links":
        return links(a.jobs * 2, a.retries, a.timeout)
    catalog = spoiler.load_catalog()
    spoilers = Spoilers(catalog)
    try:
        if a.command == "structure":
            errors = structure(catalog, spoilers)
            for err in errors:
                print(err, file=sys.stderr)
            print(f"{len(practice(catalog))} practice problems checked: {len(errors)} errors")
            return 1 if errors else 0
        return tests(catalog, spoilers, a.problems, a.jobs, a.time_factor)
    finally:
        spoilers.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
