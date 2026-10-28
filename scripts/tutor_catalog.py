"""Catalog lookups shared by the tutor scripts (tutor_state.py, verify.py). Standard library only.

Usage (the tutor's lookups, so that it never parses the JSON files by hand):
  python3 scripts/tutor_catalog.py find "<problem>"          id, folder, capability, judge, local time limit, link
  python3 scripts/tutor_catalog.py list [--contest N]        problems by contest (practice ones first), no techniques
  python3 scripts/tutor_catalog.py refs --technique <key>    reading for a technique key (substring match)
  python3 scripts/tutor_catalog.py refs --id <id> [<id>...]  given entries of data/references.json
  python3 scripts/tutor_catalog.py refs --list-techniques    the technique keys that have references

The catalog is data/practice.json, written by scripts/catalog.py:
  {"format": 1, "problems": [{"id", "folder", "capability": "practice" | "archive",
                               "judge": "tokens" | "float" | "checker" | "interactive",
                               "contest", "longName", "urlName", "contestTaskId", "timeLimit"}, ...]}
A bare list of entries is accepted too, and "judging" is read as a synonym of "judge".
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "practice.json"
DUMP = ROOT / "data" / "csacademy_dump.json"
JUDGES = ("tokens", "float", "checker", "interactive")
REFERENCES = ROOT / "data" / "references.json"


def load_catalog(path=None):
    """-> list of entries, or None when the catalog does not exist yet."""
    path = Path(path or os.environ.get("TUTOR_CATALOG") or CATALOG)
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["problems"] if isinstance(data, dict) else data


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.casefold())


def resolve(arg, catalog):
    """Find a catalog entry by id, folder, path to the folder or folder name. Raises LookupError."""
    arg = arg.strip().rstrip("/")
    for key in ("id", "folder"):
        hits = [e for e in catalog if e.get(key) == arg]
        if hits:
            return hits[0]
    try:
        rel = Path(arg).resolve().relative_to(ROOT).as_posix()
        hits = [e for e in catalog if e.get("folder") == rel]
        if hits:
            return hits[0]
    except (ValueError, OSError):
        pass
    for match in (lambda e: Path(e["folder"]).name == arg,
                  lambda e: Path(e["folder"]).name.casefold() == arg.casefold(),
                  lambda e: _norm(arg) in (_norm(Path(e["folder"]).name), _norm(e.get("longName", "")),
                                           _norm(e["id"]))):
        hits = [e for e in catalog if match(e)]
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            raise LookupError(f"{arg!r} is ambiguous: " + ", ".join(e["id"] for e in hits))
    raise LookupError(f"{arg!r} is not a problem of the catalog (data/practice.json)")


def judge_mode(entry):
    mode = entry.get("judge") or entry.get("judging") or "tokens"
    if mode not in JUDGES:
        raise ValueError(f"{entry['id']}: unknown judge mode {mode!r}")
    return mode


def cs_academy_url(entry):
    return f"https://csacademy.com/ieeextreme-practice/task/{entry['urlName']}/" if entry.get("urlName") else None


def time_limit_ms(entry=None, folder=None):
    """CS Academy time limit (ms): the catalog's timeLimit, else the dump; None when unknown."""
    if entry and isinstance(entry.get("timeLimit"), int):
        return entry["timeLimit"]
    if not DUMP.exists():
        return None
    tasks = json.loads(DUMP.read_text(encoding="utf-8"))
    if entry:
        for key in ("contestTaskId", "urlName"):
            if entry.get(key) is not None:
                hits = [t for t in tasks if t.get(key) == entry[key]]
                if len(hits) == 1:
                    return hits[0].get("timeLimit")
        folder = folder or (ROOT / entry["folder"])
    if folder is None:
        return None
    folder = Path(folder)
    num = folder.parent.name.replace("ieeextreme", "")
    hits = [t for t in tasks
            if t["contest"].startswith(f"IEEEXtreme {num}.") and _norm(t["longName"]) == _norm(folder.name)]
    return hits[0].get("timeLimit") if len(hits) == 1 else None


def hint_steps(entry):
    """Ladder steps (1-5) that have hint material for a practice problem, from hints.json inside its
    spoiler; None when unknown (no spoiler or no hints.json). Only step numbers leave the spoiler."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import spoiler  # noqa: E402  (scripts/spoiler.py)
    root = Path(os.environ.get("REVEAL_SPOILER_ROOT") or ROOT)
    path = root / entry["folder"] / spoiler.SPOILER_NAME
    try:
        files = spoiler.decode(path.read_bytes(), entry["id"])
    except (OSError, spoiler.SpoilerError):
        return None
    if "hints.json" not in files:
        return None
    return sorted({b["step"] for b in json.loads(files["hints.json"][0])["blocks"]})


def next_step(entry, reached):
    """The next step the ladder offers after `reached`: a step with hint material, or None (only
    giving up is left). Without hint information, simply reached + 1 up to 5."""
    steps = hint_steps(entry) if entry else None
    later = [s for s in (steps if steps is not None else range(1, 6)) if s > reached]
    return later[0] if later else None


def citation(e):
    """One line to cite a reference entry exactly as the catalog gives it (never page numbers)."""
    if e["kind"] == "book":
        where = ", ".join(x for x in (f"chapter {e['chapter']}" if e.get("chapter") else "",
                                      f"section {e['section']}" if e.get("section") else "") if x)
        return f"{e['title']} ({e['edition']}), {where}"
    if e["kind"] == "paper":
        return f"{e['title']}. {e['edition']}. {e['source']}. {e['url']}"
    parts = [e["source"] + ": " + e["title"]]
    if e.get("chapter"):
        parts.append(f"chapter {e['chapter']}")
    if e.get("section"):
        parts.append(f"section {e['section']}")
    return ", ".join(parts) + f". {e['url']}"


def _print_refs(entries):
    for e in entries:
        print(f"{e['id']}  [{e['kind']}, min step {e['min_step']}, techniques {', '.join(e['techniques'])}]")
        print(f"  {citation(e)}")
        print(f"  {e['note']}")
    print(f"({len(entries)} entr{'y' if len(entries) == 1 else 'ies'})")


def main(argv=None):
    p = argparse.ArgumentParser(description="Catalog lookups for the tutor.")
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("find")
    f.add_argument("problem")
    ls = sub.add_parser("list")
    ls.add_argument("--contest", help="edition number, e.g. 18")
    r = sub.add_parser("refs")
    g = r.add_mutually_exclusive_group(required=True)
    g.add_argument("--technique")
    g.add_argument("--id", nargs="+")
    g.add_argument("--list-techniques", action="store_true")
    a = p.parse_args(argv)
    if a.cmd == "list":
        catalog = load_catalog() or []
        rows = [e for e in catalog if not a.contest or e["folder"].split("/")[1] == f"ieeextreme{a.contest}"]
        for cap in ("practice", "archive"):
            sel = [e for e in rows if e["capability"] == cap]
            print(f"{cap} ({len(sel)}):")
            for e in sorted(sel, key=lambda e: e["folder"]):
                print(f"  {e['id']:40} {e.get('longName')} ({e.get('contest')})")
        return 0
    if a.cmd == "find":
        catalog = load_catalog()
        if catalog is None:
            print("no catalog (data/practice.json)", file=sys.stderr)
            return 2
        try:
            e = resolve(a.problem, catalog)
        except LookupError as err:
            print(err, file=sys.stderr)
            return 2
        tl = time_limit_ms(e)
        print(f"id:          {e['id']}")
        print(f"name:        {e.get('longName')} ({e.get('contest')})")
        print(f"capability:  {e['capability']}")
        print(f"judge:       {judge_mode(e)}")
        print(f"statement:   {e['folder']}/PROBLEM.md")
        print(f"local time limit: {f'{tl} ms' if tl else 'unknown'} (what verify.py uses; the statement may show"
              " another value: say which one you mean)")
        print(f"CS Academy:  {cs_academy_url(e)}")
        return 0
    if not REFERENCES.exists():
        print("no reference catalog yet (data/references.json)")
        return 0
    refs = json.loads(REFERENCES.read_text(encoding="utf-8"))["references"]
    if a.list_techniques:
        print("\n".join(sorted({k for e in refs for k in e["techniques"]})))
        return 0
    if a.id:
        by_id = {e["id"]: e for e in refs}
        missing = [i for i in a.id if i not in by_id]
        if missing:
            print(f"not in the catalog: {', '.join(missing)}", file=sys.stderr)
        _print_refs([by_id[i] for i in a.id if i in by_id])
        return 2 if missing else 0
    key = _norm(a.technique)
    _print_refs([e for e in refs if any(key in _norm(k) for k in e["techniques"])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
