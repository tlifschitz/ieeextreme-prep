#!/usr/bin/env python3
"""Tutor state: append-only, validated JSONL event logs in .tutor/ (git-ignored).

Usage:
  python3 scripts/tutor_state.py log <problem> <event> [--field value ...]
  python3 scripts/tutor_state.py status <problem> [--json]
  python3 scripts/tutor_state.py learner log <event> [--field value ...]
  python3 scripts/tutor_state.py learner status [--json]
  python3 scripts/tutor_state.py events                 list the events and their fields

<problem> is a catalog id, folder or folder name (resolved through data/practice.json); without a
catalog it must be a lowercase id like brick-stacks. Field flags use dashes: --offer-id, --ref-id.

Files:
  .tutor/<problem id>.jsonl   one event per line for that problem
  .tutor/learner.jsonl        cross-problem facts: every reference offered, accepted, declined or
                              read (ref_* events of a problem are mirrored here, with "problem"),
                              and the topics studied (learn mode)
Each line: {"id", "ts" (UTC, ISO 8601), "event", "problem"?, ...fields}. `log` prints the stored
line, so the caller can keep the id of an offer: step_accepted / step_declined / ref_accepted /
ref_declined must reference that id with --offer-id.

Problem events:
  session_start   --mode practice|learn
  step_offered    --step 1..5          (not while the same step is pending or accepted)
  step_accepted   --offer-id ID        (consent covers that one step)
  step_declined   --offer-id ID
  hint_given      --step N --summary "one line, no code"   (needs an accepted offer of step N)
  peek_consented  [--note text]
  ref_offered     --ref-id ID [--requested yes]   (an unsolicited offer is refused if the learner
                                                   log already has an offer of that reference)
  ref_accepted    --offer-id ID
  ref_declined    --offer-id ID
  ref_read        --ref-id ID [--takeaway text]
  verify_run      --passed N --total N --verdicts JSON-or-"OK,WA,..." [--lang py|cpp]
  solved          [--hints-used N]     (default: the step reached)
  gave_up         [--hints-used N]     (default: the step reached)
Learner events (learner log): topic_studied --topic T, and the ref_* events above without a problem.

Missing history is reported as "unknown", never as "no hints used".

Assumption: one writer per clone (one tutor session at a time). There is no locking: two sessions
appending at once may interleave their checks (e.g. both accept the same offer). Lines are written
with a single write + fsync; a malformed line (e.g. a torn write) is skipped and reported by status.

Environment: TUTOR_STATE_DIR overrides .tutor/ (tests), TUTOR_CATALOG overrides data/practice.json.
"""
import argparse
import json
import os
import re
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tutor_catalog import ROOT, hint_steps, load_catalog, next_step, resolve  # noqa: E402

MAX_STEP = 5
MODES = ("practice", "learn")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
MAX_TEXT = 300


class StateError(Exception):
    pass


# ---------------------------------------------------------------- field types

def t_step(v):
    try:
        n = int(v)
    except (TypeError, ValueError):
        raise StateError(f"step must be an integer 1..{MAX_STEP}, got {v!r}")
    if not 1 <= n <= MAX_STEP:
        raise StateError(f"step must be 1..{MAX_STEP} (step 6, give-up, is the student's own command)")
    return n


def t_count(v):
    try:
        n = int(v)
    except (TypeError, ValueError):
        raise StateError(f"expected a non-negative integer, got {v!r}")
    if n < 0:
        raise StateError(f"expected a non-negative integer, got {n}")
    return n


def t_text(v):
    v = str(v).strip()
    if not v:
        raise StateError("empty text")
    if "\n" in v or "\r" in v:
        raise StateError("text must be one line")
    if "```" in v:
        raise StateError("text must not contain code blocks")
    if len(v) > MAX_TEXT:
        raise StateError(f"text longer than {MAX_TEXT} characters")
    return v


def t_ident(v):
    v = str(v).strip()
    if not ID_RE.match(v):
        raise StateError(f"invalid id {v!r} (lowercase letters, digits, '.', '_', '-')")
    return v


def t_mode(v):
    if v not in MODES:
        raise StateError(f"mode must be one of {', '.join(MODES)}")
    return v


def t_bool(v):
    if isinstance(v, bool):
        return v
    s = str(v).casefold()
    if s in ("yes", "true", "1"):
        return True
    if s in ("no", "false", "0"):
        return False
    raise StateError(f"expected yes/no, got {v!r}")


def t_lang(v):
    if v not in ("py", "cpp"):
        raise StateError("lang must be py or cpp")
    return v


def t_verdicts(v):
    if isinstance(v, (dict, list)):
        data = v
    else:
        try:
            data = json.loads(v)
        except (TypeError, ValueError):
            data = [s.strip() for s in str(v).split(",") if s.strip()]
    ok = {"OK", "WA", "RE", "TLE", "CE", "N/A"}
    items = data.keys() if isinstance(data, dict) else data
    if not isinstance(data, (dict, list)) or not all(isinstance(x, str) and x in ok for x in items):
        raise StateError(f"verdicts must be a list or a count map of {sorted(ok)}")
    if isinstance(data, dict):
        data = {k: t_count(n) for k, n in data.items()}
    return data


# event -> (required fields, optional fields); every field maps to its type
EVENTS = {
    "session_start": ({"mode": t_mode}, {}),
    "step_offered": ({"step": t_step}, {}),
    "step_accepted": ({"offer_id": t_ident}, {}),
    "step_declined": ({"offer_id": t_ident}, {}),
    "hint_given": ({"step": t_step, "summary": t_text}, {}),
    "peek_consented": ({}, {"note": t_text}),
    "ref_offered": ({"ref_id": t_ident}, {"requested": t_bool}),
    "ref_accepted": ({"offer_id": t_ident}, {}),
    "ref_declined": ({"offer_id": t_ident}, {}),
    "ref_read": ({"ref_id": t_ident}, {"takeaway": t_text}),
    "verify_run": ({"passed": t_count, "total": t_count, "verdicts": t_verdicts}, {"lang": t_lang}),
    "solved": ({}, {"hints_used": t_count}),
    "gave_up": ({}, {"hints_used": t_count}),
}
LEARNER_EVENTS = {
    "topic_studied": ({"topic": t_text}, {}),
    "ref_offered": EVENTS["ref_offered"],
    "ref_accepted": EVENTS["ref_accepted"],
    "ref_declined": EVENTS["ref_declined"],
    "ref_read": EVENTS["ref_read"],
}
# Events that make no sense on an archive problem (no ladder, no tests yet).
PRACTICE_ONLY = {"step_offered", "step_accepted", "step_declined", "hint_given", "peek_consented", "verify_run"}


# ---------------------------------------------------------------- storage

def state_dir():
    return Path(os.environ.get("TUTOR_STATE_DIR") or ROOT / ".tutor")


def read_events(path):
    """-> (events, number of malformed lines skipped)."""
    events, bad = [], 0
    if not path.exists():
        return events, bad
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                ev = json.loads(line)
                if not isinstance(ev, dict) or "event" not in ev or "id" not in ev:
                    raise ValueError
                events.append(ev)
            except ValueError:
                bad += 1
    return events, bad


def append(path, record):
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
        os.fsync(f.fileno())


def new_id(event, taken):
    prefix = event.split("_")[0][:4]
    while True:
        i = f"{prefix}-{secrets.token_hex(3)}"
        if i not in taken:
            return i


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------- problems

def problem_key(arg):
    """-> (id, catalog entry or None)."""
    catalog = load_catalog()
    if catalog is not None:
        try:
            entry = resolve(arg, catalog)
        except LookupError as e:
            raise StateError(str(e))
        return entry["id"], entry
    if not ID_RE.match(arg):
        raise StateError(f"no catalog (data/practice.json) to resolve {arg!r}: pass a problem id")
    return arg, None


def check_fields(schema, event, raw):
    required, optional = schema[event]
    unknown = set(raw) - set(required) - set(optional)
    if unknown:
        raise StateError(f"{event}: unknown field(s) {', '.join('--' + u.replace('_', '-') for u in sorted(unknown))}")
    missing = [k for k in required if k not in raw]
    if missing:
        raise StateError(f"{event}: missing field(s) {', '.join('--' + m.replace('_', '-') for m in missing)}")
    fields = {}
    for k, v in raw.items():
        try:
            fields[k] = (required.get(k) or optional[k])(v)
        except StateError as e:
            raise StateError(f"{event} --{k.replace('_', '-')}: {e}")
    return fields


def answered(events):
    return {e["offer_id"] for e in events if e["event"] in ("step_accepted", "step_declined",
                                                              "ref_accepted", "ref_declined")}


def find_offer(events, offer_id, kind):
    for e in events:
        if e["id"] == offer_id:
            if e["event"] != kind:
                raise StateError(f"{offer_id} is a {e['event']}, not a {kind}")
            if offer_id in answered(events):
                raise StateError(f"offer {offer_id} was already answered")
            return e
    raise StateError(f"no {kind} with id {offer_id}")


def check_ref_rules(event, fields, events, learner_events):
    """Shared ref_* rules. `events` is the log the offer lives in."""
    if event == "ref_offered" and not fields.get("requested"):
        if any(e["event"] == "ref_offered" and e["ref_id"] == fields["ref_id"] for e in learner_events):
            raise StateError(f"reference {fields['ref_id']} was already offered to this learner: "
                             "do not repeat an unsolicited offer (use --requested yes if the student asked)")
    if event in ("ref_accepted", "ref_declined"):
        offer = find_offer(events, fields["offer_id"], "ref_offered")
        fields["ref_id"] = offer["ref_id"]


def validate_problem_event(event, fields, events, learner_events, entry):
    if entry is not None and entry.get("capability") != "practice" and event in PRACTICE_ONLY:
        raise StateError(f"{entry['id']} is an archive problem: no tutoring or verification yet")
    if event == "step_offered":
        step = fields["step"]
        done = answered(events)
        for e in events:
            if e["event"] == "step_offered" and e["step"] == step and e["id"] not in done:
                raise StateError(f"step {step} is already offered ({e['id']}), waiting for an answer")
        if step in accepted_steps(events):
            raise StateError(f"step {step} was already accepted")
        steps = hint_steps(entry) if entry is not None and entry.get("capability") == "practice" else None
        if steps is not None and step not in steps:
            nxt = next_step(entry, step)
            raise StateError(f"this problem has no step {step}: offer step {nxt} instead" if nxt
                             else f"this problem has no step {step}: only giving up is left")
    elif event in ("step_accepted", "step_declined"):
        offer = find_offer(events, fields["offer_id"], "step_offered")
        fields["step"] = offer["step"]
    elif event == "hint_given":
        if fields["step"] not in accepted_steps(events):
            raise StateError(f"hint_given step {fields['step']}: the student has not accepted step "
                             f"{fields['step']} (log step_offered, then step_accepted)")
    elif event in ("solved", "gave_up"):
        fields.setdefault("hints_used", step_reached(events))
    check_ref_rules(event, fields, events, learner_events)


def accepted_steps(events):
    return {e["step"] for e in events if e["event"] == "step_accepted"}


def step_reached(events):
    return max((e["step"] for e in events if e["event"] == "hint_given"), default=0)


def log_problem(arg, event, raw):
    pid, entry = problem_key(arg)
    if event not in EVENTS:
        raise StateError(f"unknown event {event!r}; events: {', '.join(EVENTS)}")
    fields = check_fields(EVENTS, event, raw)
    d = state_dir()
    path, lpath = d / f"{pid}.jsonl", d / "learner.jsonl"
    events, _ = read_events(path)
    learner_events, _ = read_events(lpath)
    validate_problem_event(event, fields, events, learner_events, entry)
    taken = {e["id"] for e in events} | {e["id"] for e in learner_events}
    record = {"id": new_id(event, taken), "ts": now(), "event": event, "problem": pid, **fields}
    append(path, record)
    if event.startswith("ref_"):
        append(lpath, record)  # same id: the learner log can follow up on it
    return record


def log_learner(event, raw):
    if event not in LEARNER_EVENTS:
        raise StateError(f"unknown learner event {event!r}; events: {', '.join(LEARNER_EVENTS)}")
    fields = check_fields(LEARNER_EVENTS, event, raw)
    lpath = state_dir() / "learner.jsonl"
    learner_events, _ = read_events(lpath)
    check_ref_rules(event, fields, learner_events, learner_events)
    record = {"id": new_id(event, {e["id"] for e in learner_events}), "ts": now(), "event": event, **fields}
    append(lpath, record)
    return record


# ---------------------------------------------------------------- status

def ref_table(events):
    refs = {}
    done = {}
    for e in events:
        if e["event"] in ("ref_accepted", "ref_declined"):
            done[e["offer_id"]] = e["event"][4:]
    for e in events:
        if e["event"] == "ref_offered":
            r = refs.setdefault(e["ref_id"], {"offers": [], "read": False})
            r["offers"].append({"id": e["id"], "problem": e.get("problem"),
                                "answer": done.get(e["id"], "pending"), "requested": e.get("requested", False)})
        elif e["event"] == "ref_read":
            r = refs.setdefault(e["ref_id"], {"offers": [], "read": False})
            r["read"] = True
            if e.get("takeaway"):
                r["takeaway"] = e["takeaway"]
    return refs


def problem_status(arg):
    pid, entry = problem_key(arg)
    events, bad = read_events(state_dir() / f"{pid}.jsonl")
    st = {"problem": pid, "capability": entry.get("capability") if entry else None}
    if not events:
        st["history"] = "unknown"
        st["note"] = "no history for this problem: hints used are unknown, not zero"
        return st
    done = answered(events)
    reached = step_reached(events)
    verifies = [e for e in events if e["event"] == "verify_run"]
    st.update({
        "history": "known",
        "malformed_lines": bad,
        "mode": next((e["mode"] for e in reversed(events) if e["event"] == "session_start"), None),
        "sessions": sum(e["event"] == "session_start" for e in events),
        "step_reached": reached,
        "steps_accepted": sorted(accepted_steps(events)),
        "steps_declined": sorted({e["step"] for e in events if e["event"] == "step_declined"}),
        "pending_step_offers": [{"id": e["id"], "step": e["step"]} for e in events
                                if e["event"] == "step_offered" and e["id"] not in done],
        "hints": [{"step": e["step"], "summary": e["summary"]} for e in events if e["event"] == "hint_given"],
        "next_step": next_step(entry, reached) if entry else (reached + 1 if reached < MAX_STEP else None),
        "peek_consented": any(e["event"] == "peek_consented" for e in events),
        "refs": ref_table(events),
        "last_verify": ({k: verifies[-1][k] for k in ("ts", "passed", "total", "verdicts")} if verifies else None),
        "solved": any(e["event"] == "solved" for e in events),
        "gave_up": any(e["event"] == "gave_up" for e in events),
        "hints_used": reached,
    })
    return st


def recent_problems(limit=5):
    """The problems with tutor history in this clone, most recently active first."""
    out = []
    for path in state_dir().glob("*.jsonl"):
        if path.name == "learner.jsonl":
            continue
        events, _ = read_events(path)
        if events:
            out.append({"problem": path.stem, "last": events[-1]["ts"], "step_reached": step_reached(events),
                        "solved": any(e["event"] == "solved" for e in events),
                        "gave_up": any(e["event"] == "gave_up" for e in events)})
    return sorted(out, key=lambda r: r["last"], reverse=True)[:limit]


def learner_status():
    events, bad = read_events(state_dir() / "learner.jsonl")
    recent = recent_problems()
    if not events and not recent:
        return {"history": "unknown", "note": "no learner history"}
    return {
        "history": "known",
        "malformed_lines": bad,
        "recent_problems": recent,
        "refs": ref_table(events),
        "topics_studied": sorted({e["topic"] for e in events if e["event"] == "topic_studied"}),
    }


def show(st):
    if st.get("history") == "unknown":
        print(f"{st.get('problem', 'learner')}: {st['note']}")
        return
    if "problem" not in st:
        print("learner")
        print(f"  topics studied: {', '.join(st['topics_studied']) or 'none'}")
        for r in st["recent_problems"]:
            state = "solved" if r["solved"] else "gave up" if r["gave_up"] else f"step reached {r['step_reached']}"
            print(f"  recent problem: {r['problem']} (last activity {r['last']}, {state})")
    else:
        print(f"{st['problem']} ({st['capability'] or 'no catalog'}), mode {st['mode'] or 'unknown'}, "
              f"{st['sessions']} session(s)")
        print(f"  step reached: {st['step_reached']} (accepted {st['steps_accepted'] or 'none'}, "
              f"declined {st['steps_declined'] or 'none'}); next step: {st['next_step'] or 'give-up only'}")
        for o in st["pending_step_offers"]:
            print(f"  pending offer {o['id']}: step {o['step']}")
        for h in st["hints"]:
            print(f"  hint (step {h['step']}): {h['summary']}")
        print(f"  peek consented: {'yes' if st['peek_consented'] else 'no'}")
        v = st["last_verify"]
        last = f"{v['passed']}/{v['total']} local cases at {v['ts']}" if v else "never"
        print(f"  last verify: {last}")
        print(f"  solved: {'yes' if st['solved'] else 'no'}; gave up: {'yes' if st['gave_up'] else 'no'}")
    for ref, r in st["refs"].items():
        answers = ", ".join(f"{o['id']} {o['answer']}" for o in r["offers"]) or "not offered"
        print(f"  ref {ref}: offers [{answers}], read: {'yes' if r['read'] else 'no'}")
    if st["malformed_lines"]:
        print(f"  warning: {st['malformed_lines']} malformed line(s) skipped")


# ---------------------------------------------------------------- CLI

def parse_fields(tokens):
    raw = {}
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if not tok.startswith("--") or len(tok) < 3:
            raise StateError(f"expected --field value, got {tok!r}")
        key = tok[2:]
        if "=" in key:
            key, value = key.split("=", 1)
            i += 1
        else:
            if i + 1 >= len(tokens):
                raise StateError(f"--{key} needs a value")
            value = tokens[i + 1]
            i += 2
        key = key.replace("-", "_")
        if key in raw:
            raise StateError(f"--{key} given twice")
        raw[key] = value
    return raw


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    p = argparse.ArgumentParser(description="Tutor state (.tutor/ event logs).",
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    lg = sub.add_parser("log")
    lg.add_argument("problem")
    lg.add_argument("event")
    st = sub.add_parser("status")
    st.add_argument("problem")
    st.add_argument("--json", action="store_true")
    ln = sub.add_parser("learner")
    ln.add_argument("action", choices=("log", "status"))
    ln.add_argument("event", nargs="?")
    ln.add_argument("--json", action="store_true")
    sub.add_parser("events")
    args, rest = p.parse_known_args(argv)
    try:
        if args.cmd == "events":
            for schema, title in ((EVENTS, "problem events"), (LEARNER_EVENTS, "learner events")):
                print(title)
                for name, (req, opt) in schema.items():
                    flags = [f"--{k.replace('_', '-')}" for k in req] + [f"[--{k.replace('_', '-')}]" for k in opt]
                    print(f"  {name} {' '.join(flags)}".rstrip())
            return 0
        if args.cmd == "log":
            print(json.dumps(log_problem(args.problem, args.event, parse_fields(rest)), ensure_ascii=False))
            return 0
        if args.cmd == "learner" and args.action == "log":
            if not args.event:
                raise StateError("learner log needs an event")
            print(json.dumps(log_learner(args.event, parse_fields(rest)), ensure_ascii=False))
            return 0
        if rest:
            raise StateError(f"unexpected arguments: {' '.join(rest)}")
        if args.cmd == "status":
            s = problem_status(args.problem)
        else:
            s = learner_status()
        if args.json:
            print(json.dumps(s, ensure_ascii=False, indent=1))
        else:
            show(s)
        return 0
    except StateError as e:
        print(f"tutor_state: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
