"""Tests of scripts/verify.py on fake problems in a temporary directory.

Run: python3 scripts/tests/test_verify.py   (needs a C++ compiler for the C++ cases; set $CXX)

Nothing is written into contests/ or .tutor/: the problems live in a temp dir whose path has
spaces, the catalog is a temp file (TUTOR_CATALOG) and so is the state dir (TUTOR_STATE_DIR).
A fake reveal.py exercises the --validate / --interact protocols.
"""
import contextlib
import gzip
import io
import json
import os
import shutil
import sys
import tempfile
import textwrap
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

TMP = Path(tempfile.mkdtemp(prefix="verify test "))  # a space on purpose
STATE = TMP / "state"
CATALOG = TMP / "practice.json"
os.environ["TUTOR_STATE_DIR"] = str(STATE)
os.environ["TUTOR_CATALOG"] = str(CATALOG)

import verify  # noqa: E402

SUM_PY = "import sys\nprint(sum(map(int, sys.stdin.read().split())))\n"
SUM_CPP = textwrap.dedent("""\
    #include <iostream>
    int main() { long long s = 0, x; while (std::cin >> x) s += x; std::cout << s << "\\n"; }
    """)


def problem(name, tests, judge=None, catalog_entry=None):
    """Create a fake problem folder with tests {stem: (input, output)}; gz when stem ends in 'z'."""
    folder = TMP / "contests" / name
    (folder / "tests").mkdir(parents=True, exist_ok=True)
    for stem, (inp, out) in tests.items():
        if stem.endswith("z"):
            (folder / "tests" / f"{stem}.in.gz").write_bytes(gzip.compress(inp.encode(), mtime=0))
            (folder / "tests" / f"{stem}.out.gz").write_bytes(gzip.compress(out.encode(), mtime=0))
        else:
            (folder / "tests" / f"{stem}.in").write_text(inp)
            if out is not None:
                (folder / "tests" / f"{stem}.out").write_text(out)
    return folder


def attempt(folder, lang, code):
    for old in folder.glob("attempt.*"):
        old.unlink()
    (folder / f"attempt.{lang}").write_text(code)


def run(*argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = verify.main([str(a) for a in argv])
    return code, buf.getvalue()


def write_catalog(entries):
    CATALOG.write_text(json.dumps({"format": 1, "problems": entries}))


def test_python_verdicts():
    f = problem("Sum it", {"01": ("1 2\n", "3\n"), "02": ("5 5 5\n", "15\n"), "10": ("0\n", "0\n"),
                           "03z": ("7 8\n", "15")})
    attempt(f, "py", SUM_PY)
    code, out = run(f)
    assert code == 0 and "passed 4/4 local cases" in out, out
    assert out.index("  02 ") < out.index("  03z") < out.index("  10 "), out  # natural order
    assert "not a contest score" in out
    attempt(f, "py", "print(3)\n")
    code, out = run(f, "--show")
    assert code == 1 and "passed 1/4" in out and "WA" in out and "token 1 differs" in out, out
    assert "expected:" in out and "your output:" in out
    code, out = run(f)
    assert "expected:" not in out and "--show" in out
    attempt(f, "py", "import sys\nsys.stderr.write('boom\\n')\nraise SystemExit(3)\n")
    code, out = run(f, "--only", "01")
    assert code == 1 and "RE" in out and "exit code 3" in out and "| boom" in out and "passed 0/1" in out, out
    attempt(f, "py", "import time\ntime.sleep(30)\n")
    code, out = run(f, "--only", "01", "--time-factor", "0.1")
    assert code == 1 and "TLE" in out and ">0.20 s" in out, out


def test_output_limit_and_big_cases_hidden():
    big_in = "1 " * 3000 + "\n"
    f = problem("Big", {"01": (big_in, "3000\n")})
    attempt(f, "py", "while True: print('x' * 1000)\n")
    old = verify.OUTPUT_LIMIT
    verify.OUTPUT_LIMIT = 100_000
    try:
        code, out = run(f, "--show")
    finally:
        verify.OUTPUT_LIMIT = old
    assert code == 1 and "WA" in out and "output over" in out and "too big to show" in out, out
    assert "3000" not in out.replace("passed", "")  # the expected output is never printed


def test_float_and_tokens():
    f = problem("Floats", {"01": ("x\n", "0.3333333333\n")}, judge="float")
    attempt(f, "py", "print(0.33333334)\n")
    code, out = run(f, "--judge", "float")
    assert code == 0, out
    code, out = run(f)  # tokens: exact comparison
    assert code == 1, out
    attempt(f, "py", "print(0.334)\n")
    code, out = run(f, "--judge", "float")
    assert code == 1 and "tolerance" in out, out
    attempt(f, "py", "print('  0.3333333333   ')\nprint()\n")  # whitespace does not matter
    code, out = run(f)
    assert code == 0, out


def test_attempt_selection():
    f = problem("Choose", {"01": ("1 2\n", "3\n")})
    attempt(f, "py", SUM_PY)
    (f / "attempt.cpp").write_text(SUM_CPP)
    code, out = run(f)
    assert code == 2 and "--lang" in out, out
    code, out = run(f, "--lang", "py")
    assert code == 0, out
    for p in f.glob("attempt.*"):
        p.unlink()
    code, out = run(f)
    assert code == 2 and "templates/attempt" in out, out


def test_cpp():
    f = problem("Cpp one", {"01": ("1 2\n", "3\n"), "02": ("4 4\n", "8\n")})
    attempt(f, "cpp", SUM_CPP)
    code, out = run(f)
    assert code == 0 and "C++17" in out and "passed 2/2" in out, out
    attempt(f, "cpp", "int main() { this is not c++ }\n")
    code, out = run(f)
    assert code == 1 and "CE: compilation failed" in out and "passed 0/2" in out, out
    attempt(f, "cpp", textwrap.dedent("""\
        #include <iostream>
        #include <vector>
        using namespace std;
        using ll = long long;
        using vl = vector<ll>;
        #define sz(x) ((int)(x).size())
        #include "lib/modular.h"
        int main() { ll a, b; cin >> a >> b; cout << power(2, 0, 7) * (a + b) << "\\n"; }
        """))
    code, out = run(f)
    assert code == 0, out  # bundled before compiling
    attempt(f, "cpp", "#include <cstdlib>\nint main() { abort(); }\n")
    code, out = run(f, "--only", "01")
    assert code == 1 and "RE" in out and "SIGABRT" in out, out


def test_catalog_capabilities_and_logging():
    arch = TMP / "contests" / "Archived"
    arch.mkdir(parents=True, exist_ok=True)
    notests = TMP / "contests" / "No tests"
    notests.mkdir(parents=True, exist_ok=True)
    good = problem("Logged", {"01": ("1 2\n", "3\n"), "02": ("2 2\n", "4\n")})
    write_catalog([
        {"id": "archived", "folder": str(arch), "longName": "Archived", "urlName": "archived",
         "capability": "archive"},
        {"id": "no-tests", "folder": str(notests), "longName": "No tests", "capability": "practice",
         "judge": "tokens"},
        {"id": "logged", "folder": str(good), "longName": "Logged", "capability": "practice", "judge": "tokens"},
    ])
    try:
        code, out = run("archived")
        assert code == 2 and "archive problem" in out and "csacademy.com/ieeextreme-practice/task/archived/" in out
        code, out = run("no-tests")
        assert code == 2 and "not available yet" in out, out
        attempt(good, "py", "print(3)\n")
        code, out = run("Logged")
        assert code == 1 and "passed 1/2" in out, out
        ev = [json.loads(x) for x in (STATE / "logged.jsonl").read_text().splitlines()]
        assert ev[-1]["event"] == "verify_run" and ev[-1]["passed"] == 1 and ev[-1]["total"] == 2
        assert ev[-1]["verdicts"] == {"OK": 1, "WA": 1} and ev[-1]["lang"] == "py"
        code, out = run("logged", "--no-log")
        assert len((STATE / "logged.jsonl").read_text().splitlines()) == 1
    finally:
        CATALOG.unlink()


FAKE_REVEAL = textwrap.dedent("""\
    import subprocess, sys
    args = sys.argv[1:]
    if args == ["--help"]:
        print("usage: reveal.py ... {flags}")
        sys.exit(0)
    if args[0] == "--validate":
        pid, test, out = args[1:]
        got = open(out).read().split()
        print("OK" if got and got[0] == "yes" else "WA wrong stacks")
    elif args[0] == "--interact":
        cmd = args[args.index("--") + 1:]
        p = subprocess.run(cmd, input="ping\\n", capture_output=True, text=True)
        print("OK" if p.stdout.strip() == "pong" else "WA bad answer")
    """)


def fake_reveal(flags):
    path = TMP / "reveal fake" / "reveal.py"
    path.parent.mkdir(exist_ok=True)
    path.write_text(FAKE_REVEAL.replace("{flags}", flags))
    return path


def test_checker_and_interactive():
    chk = problem("Checked", {"01": ("x\n", "meta\n"), "02": ("y\n", "meta\n")})
    inter = problem("Inter", {"01": ("secret\n", None)})
    write_catalog([
        {"id": "checked", "folder": str(chk), "longName": "Checked", "capability": "practice", "judge": "checker"},
        {"id": "inter", "folder": str(inter), "longName": "Inter", "capability": "practice",
         "judge": "interactive"},
    ])
    old = verify.REVEAL
    try:
        verify.REVEAL = TMP / "missing" / "reveal.py"
        attempt(chk, "py", "print('yes')\n")
        code, out = run("checked", "--no-log")
        assert code == 3 and "N/A" in out and "checker not available yet" in out and "2 could not be judged" in out
        attempt(inter, "py", "print(input().replace('ping', 'pong'))\n")
        code, out = run("inter", "--no-log")
        assert code == 3 and "interactive verification is not available yet" in out, out

        verify.REVEAL = fake_reveal("--validate")  # no --interact yet
        code, out = run("checked", "--no-log")
        assert code == 0 and "passed 2/2" in out, out
        attempt(chk, "py", "print('no')\n")
        code, out = run("checked", "--no-log", "--show")
        assert code == 1 and "wrong stacks" in out and "expected:" not in out and "your output:" in out, out
        code, out = run("inter", "--no-log")
        assert code == 3 and "not available yet" in out, out

        verify.REVEAL = fake_reveal("--validate --interact")
        code, out = run("inter", "--no-log")
        assert code == 0 and "passed 1/1" in out, out
        attempt(inter, "py", "print('nope')\n")
        code, out = run("inter", "--no-log", "--show")
        assert code == 1 and "bad answer" in out and "secret" not in out, out
    finally:
        verify.REVEAL = old
        CATALOG.unlink()


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    try:
        for t in tests:
            t()
            print(f"ok  {t.__name__}")
    finally:
        shutil.rmtree(TMP)
    print(f"{len(tests)} tests passed")
