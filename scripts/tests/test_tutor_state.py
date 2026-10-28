"""Tests of scripts/tutor_state.py. Run: python3 scripts/tests/test_tutor_state.py

Uses a temporary state dir and a fake catalog (TUTOR_STATE_DIR, TUTOR_CATALOG): nothing in the
repo is read or written. Plain asserts, plus a randomized run checked against a simple model.
"""
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

TMP = Path(tempfile.mkdtemp(prefix="tutor-state-test-"))
CATALOG = TMP / "practice.json"
CATALOG.write_text(json.dumps({"format": 1, "problems": [
    {"id": "brick-stacks", "folder": "contests/ieeextreme18/Brick stacks", "longName": "Brick stacks",
     "capability": "practice", "judge": "checker"},
    {"id": "rect-arrays", "folder": "contests/ieeextreme18/Rectangles and arrays",
     "longName": "Rectangles and arrays", "capability": "practice", "judge": "tokens"},
    {"id": "old-one", "folder": "contests/ieeextreme10/Old One", "longName": "Old One", "capability": "archive"},
]}))
os.environ["TUTOR_CATALOG"] = str(CATALOG)

import tutor_state as ts  # noqa: E402
from tutor_state import StateError  # noqa: E402


def fresh():
    d = Path(tempfile.mkdtemp(dir=TMP))
    os.environ["TUTOR_STATE_DIR"] = str(d)
    return d


def raises(fn, *args, contains=""):
    try:
        fn(*args)
    except StateError as e:
        assert contains in str(e), (contains, str(e))
        return str(e)
    raise AssertionError(f"{fn.__name__}{args} did not raise")


def test_unknown_history():
    fresh()
    st = ts.problem_status("brick-stacks")
    assert st["history"] == "unknown" and "hints_used" not in st
    assert ts.learner_status()["history"] == "unknown"


def test_resolution_and_files():
    d = fresh()
    r = ts.log_problem("Brick stacks", "session_start", {"mode": "practice"})
    assert r["problem"] == "brick-stacks" and r["event"] == "session_start"
    assert r["ts"].endswith("Z") and r["id"]
    ts.log_problem("contests/ieeextreme18/Brick stacks", "session_start", {"mode": "learn"})
    lines = (d / "brick-stacks.jsonl").read_text().splitlines()
    assert len(lines) == 2 and all(json.loads(x)["problem"] == "brick-stacks" for x in lines)
    assert ts.problem_status("brick stacks")["mode"] == "learn"
    raises(ts.log_problem, "no such problem", "session_start", {"mode": "practice"}, contains="not a problem")


def test_validation():
    fresh()
    raises(ts.log_problem, "brick-stacks", "nope", {}, contains="unknown event")
    raises(ts.log_problem, "brick-stacks", "session_start", {}, contains="missing")
    raises(ts.log_problem, "brick-stacks", "session_start", {"mode": "cheat"}, contains="mode")
    raises(ts.log_problem, "brick-stacks", "session_start", {"mode": "practice", "x": "1"}, contains="unknown field")
    raises(ts.log_problem, "brick-stacks", "step_offered", {"step": "6"}, contains="give-up")
    raises(ts.log_problem, "brick-stacks", "step_offered", {"step": "two"}, contains="integer")
    raises(ts.log_problem, "brick-stacks", "step_accepted", {"offer_id": "step-000000"}, contains="no step_offered")
    raises(ts.log_problem, "brick-stacks", "hint_given", {"step": "1", "summary": "x"}, contains="not accepted")
    raises(ts.log_problem, "brick-stacks", "verify_run", {"passed": "1", "total": "2", "verdicts": "OK,XX"},
           contains="verdicts")
    # archive problems: no tutoring, no verification
    raises(ts.log_problem, "old-one", "step_offered", {"step": "1"}, contains="archive")
    raises(ts.log_problem, "old-one", "verify_run", {"passed": "0", "total": "0", "verdicts": "[]"}, contains="archive")
    ts.log_problem("old-one", "session_start", {"mode": "practice"})
    ts.log_problem("old-one", "gave_up", {})


def test_ladder():
    fresh()
    o1 = ts.log_problem("brick-stacks", "step_offered", {"step": "1"})
    raises(ts.log_problem, "brick-stacks", "step_offered", {"step": "1"}, contains="already offered")
    a1 = ts.log_problem("brick-stacks", "step_accepted", {"offer_id": o1["id"]})
    assert a1["step"] == 1 and a1["offer_id"] == o1["id"]
    raises(ts.log_problem, "brick-stacks", "step_declined", {"offer_id": o1["id"]}, contains="already answered")
    raises(ts.log_problem, "brick-stacks", "step_offered", {"step": "1"}, contains="already accepted")
    raises(ts.log_problem, "brick-stacks", "hint_given", {"step": "1", "summary": "a\nb"}, contains="one line")
    raises(ts.log_problem, "brick-stacks", "hint_given", {"step": "1", "summary": "```x```"}, contains="code")
    ts.log_problem("brick-stacks", "hint_given", {"step": "1", "summary": "asked what N up to 10^6 allows"})
    ts.log_problem("brick-stacks", "hint_given", {"step": "1", "summary": "follow-up on the same step"})
    raises(ts.log_problem, "brick-stacks", "hint_given", {"step": "2", "summary": "x"}, contains="not accepted")
    o2 = ts.log_problem("brick-stacks", "step_offered", {"step": "2"})
    ts.log_problem("brick-stacks", "step_declined", {"offer_id": o2["id"]})
    st = ts.problem_status("brick-stacks")
    assert st["step_reached"] == 1 and st["steps_accepted"] == [1] and st["steps_declined"] == [2]
    assert st["next_step"] == 2 and st["pending_step_offers"] == []
    o2b = ts.log_problem("brick-stacks", "step_offered", {"step": "2"})  # re-offer after a decline is fine
    assert ts.problem_status("brick-stacks")["pending_step_offers"] == [{"id": o2b["id"], "step": 2}]
    raises(ts.log_problem, "brick-stacks", "step_accepted", {"offer_id": a1["id"]}, contains="not a step_offered")
    g = ts.log_problem("brick-stacks", "gave_up", {})
    assert g["hints_used"] == 1


def test_peek_verify_solved():
    fresh()
    assert ts.problem_status("rect-arrays")["history"] == "unknown"
    ts.log_problem("rect-arrays", "peek_consented", {})
    ts.log_problem("rect-arrays", "verify_run", {"passed": "3", "total": "5", "verdicts": '{"OK": 3, "WA": 2}',
                                                 "lang": "cpp"})
    ts.log_problem("rect-arrays", "verify_run", {"passed": "5", "total": "5", "verdicts": "OK,OK,OK,OK,OK"})
    st = ts.problem_status("rect-arrays")
    assert st["peek_consented"] and st["last_verify"]["passed"] == 5 and st["last_verify"]["verdicts"] == ["OK"] * 5
    s = ts.log_problem("rect-arrays", "solved", {"hints_used": "0"})
    assert s["hints_used"] == 0 and ts.problem_status("rect-arrays")["solved"]


def test_refs_and_learner():
    d = fresh()
    off = ts.log_problem("brick-stacks", "ref_offered", {"ref_id": "cph-greedy"})
    learner = [json.loads(x) for x in (d / "learner.jsonl").read_text().splitlines()]
    assert learner[-1]["id"] == off["id"] and learner[-1]["problem"] == "brick-stacks"
    # no unsolicited repeat, on this problem or another one
    raises(ts.log_problem, "brick-stacks", "ref_offered", {"ref_id": "cph-greedy"}, contains="already offered")
    raises(ts.log_problem, "rect-arrays", "ref_offered", {"ref_id": "cph-greedy"}, contains="already offered")
    raises(ts.log_learner, "ref_offered", {"ref_id": "cph-greedy"}, contains="already offered")
    ts.log_problem("rect-arrays", "ref_offered", {"ref_id": "cph-greedy", "requested": "yes"})  # student asked
    acc = ts.log_problem("brick-stacks", "ref_accepted", {"offer_id": off["id"]})
    assert acc["ref_id"] == "cph-greedy"
    raises(ts.log_problem, "brick-stacks", "ref_declined", {"offer_id": off["id"]}, contains="already answered")
    ts.log_problem("brick-stacks", "ref_read", {"ref_id": "cph-greedy", "takeaway": "exchange arguments"})
    st = ts.problem_status("brick-stacks")
    assert st["refs"]["cph-greedy"]["read"] and st["refs"]["cph-greedy"]["offers"][0]["answer"] == "accepted"
    ls = ts.learner_status()
    assert ls["refs"]["cph-greedy"]["read"] and len(ls["refs"]["cph-greedy"]["offers"]) == 2
    lo = ts.log_learner("ref_offered", {"ref_id": "cpa-stacks"})
    ts.log_learner("ref_declined", {"offer_id": lo["id"]})
    ts.log_learner("topic_studied", {"topic": "monotonic stack"})
    raises(ts.log_learner, "hint_given", {"step": "1", "summary": "x"}, contains="unknown learner event")
    ls = ts.learner_status()
    assert ls["topics_studied"] == ["monotonic stack"]
    assert ls["refs"]["cpa-stacks"]["offers"][0]["answer"] == "declined"


def test_malformed_line_is_skipped():
    d = fresh()
    ts.log_problem("brick-stacks", "session_start", {"mode": "practice"})
    with open(d / "brick-stacks.jsonl", "a") as f:
        f.write('{"id": "torn", "ev')  # torn write
    with open(d / "brick-stacks.jsonl", "a") as f:
        f.write("\n")
    ts.log_problem("brick-stacks", "session_start", {"mode": "learn"})
    st = ts.problem_status("brick-stacks")
    assert st["malformed_lines"] == 1 and st["sessions"] == 2


def test_cli():
    d = fresh()
    env = dict(os.environ)
    run = lambda *a: subprocess.run([sys.executable, str(SCRIPTS / "tutor_state.py"), *a],  # noqa: E731
                                    capture_output=True, text=True, env=env)
    r = run("log", "Brick stacks", "step_offered", "--step", "1")
    assert r.returncode == 0, r.stderr
    oid = json.loads(r.stdout)["id"]
    r = run("log", "Brick stacks", "step_accepted", f"--offer-id={oid}")
    assert r.returncode == 0, r.stderr
    r = run("log", "Brick stacks", "hint_given", "--step", "1", "--summary", "what does N <= 10^6 rule out?")
    assert r.returncode == 0, r.stderr
    r = run("log", "Brick stacks", "hint_given", "--step", "1")
    assert r.returncode == 2 and "missing field(s) --summary" in r.stderr
    r = run("log", "Brick stacks", "step_offered", "--step")
    assert r.returncode == 2 and "needs a value" in r.stderr
    r = run("status", "Brick stacks")
    assert r.returncode == 0 and "step reached: 1" in r.stdout, r.stdout
    r = run("status", "Brick stacks", "--json")
    assert json.loads(r.stdout)["hints_used"] == 1
    r = run("status", "rect-arrays")
    assert "unknown" in r.stdout
    r = run("learner", "log", "topic_studied", "--topic", "binary search on the answer")
    assert r.returncode == 0, r.stderr
    r = run("learner", "status", "--json")
    assert json.loads(r.stdout)["topics_studied"] == ["binary search on the answer"]
    r = run("events")
    assert r.returncode == 0 and "step_accepted --offer-id" in r.stdout
    assert sorted(p.name for p in d.iterdir()) == ["brick-stacks.jsonl", "learner.jsonl"]


def test_randomized_against_model():
    """Random action sequences; the derived status must match a straightforward model."""
    rnd = random.Random(2026)
    for _ in range(60):
        fresh()
        offers = {}       # id -> step, unanswered
        accepted = set()
        reached = 0
        ids = set()
        for _ in range(rnd.randint(1, 40)):
            kind = rnd.choice(["offer", "accept", "decline", "hint", "bad-accept"])
            step = rnd.randint(1, 5)
            if kind == "offer":
                ok = step not in accepted and step not in offers.values()
                try:
                    r = ts.log_problem("brick-stacks", "step_offered", {"step": str(step)})
                    assert ok
                    offers[r["id"]] = step
                    ids.add(r["id"])
                except StateError:
                    assert not ok
            elif kind in ("accept", "decline") and offers:
                oid = rnd.choice(sorted(offers))
                r = ts.log_problem("brick-stacks", f"step_{kind}ed" if kind == "accept" else "step_declined",
                                   {"offer_id": oid})
                assert r["step"] == offers[oid] and r["id"] not in ids
                ids.add(r["id"])
                if kind == "accept":
                    accepted.add(offers[oid])
                del offers[oid]
            elif kind == "hint":
                try:
                    ts.log_problem("brick-stacks", "hint_given", {"step": str(step), "summary": "s"})
                    assert step in accepted
                    reached = max(reached, step)
                except StateError:
                    assert step not in accepted
            elif kind == "bad-accept":
                raises(ts.log_problem, "brick-stacks", "step_accepted", {"offer_id": "step-ffffff"})
        st = ts.problem_status("brick-stacks")
        if st["history"] == "unknown":
            assert not ids
            continue
        assert st["step_reached"] == reached
        assert st["steps_accepted"] == sorted(accepted)
        assert sorted(o["id"] for o in st["pending_step_offers"]) == sorted(offers)


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for t in tests:
        t()
        print(f"ok  {t.__name__}")
    shutil.rmtree(TMP)
    print(f"{len(tests)} tests passed")
