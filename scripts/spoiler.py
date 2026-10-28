#!/usr/bin/env python3
"""Spoiler packages: the per-problem `spoiler.bin` format, the catalog, and problem lookup.

Usage: python3 scripts/spoiler.py verify [--manifest data/publication.json]

`verify` decodes every catalog problem's spoiler.bin and checks its hash, decodes
data/techniques.bin when it exists, and, with a publication manifest, checks that every
artifact still has the hash it was published with.

Format, version 1 (all integers big-endian):

    magic        8 bytes   b"XTSPOIL\\0"
    version      uint16    SPOILER_FORMAT
    id length    uint16    length of the problem id in bytes
    sha256       32 bytes  of the plain payload (the tar, before compression)
    problem id   UTF-8     the catalog id the package belongs to
    body         rest      zlib(tar) XOR keystream

The keystream is the concatenation of sha256(KEY + 0x00 + id + 0x00 + counter as 8 bytes),
counter = 0, 1, 2... The tar holds only regular files, sorted, with mtime 0, uid/gid 0 and
empty owner names, so building twice gives the same bytes. The key is in this file: this is
obfuscation, so that a solution is not readable by accident in an editor or a search, not
security.

The technique index, data/techniques.bin, uses the same format with the fixed id
"techniques" and a single member, techniques.json (see techniques_package).

Which files are spoilers is decided by one rule (`is_public_asset`): in a problem folder,
PROBLEM.md, input.txt, images/ and tests/ are public; every other tracked file is a spoiler.
Python standard library only.
"""
import hashlib
import io
import json
import re
import struct
import sys
import tarfile
import zlib
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "practice.json"
MANIFEST = ROOT / "data" / "publication.json"
SPOILER_NAME = "spoiler.bin"
TECHNIQUES_ID = "techniques"
TECHNIQUES_BIN = "data/techniques.bin"
TECHNIQUES_MEMBER = "techniques.json"
TECHNIQUES_FORMAT = 1

SPOILER_FORMAT = 1
CATALOG_FORMAT = 1
MAGIC = b"XTSPOIL\0"
HEADER = struct.Struct(">8sHH32s")
KEY = b"ieeextreme-practice/spoiler/v1: friction, not security"

# Files the spoiler may never contain: the student's own work and the public assets.
ATTEMPT = re.compile(r"^attempt(\.[^/]*)?$")


class SpoilerError(Exception):
    pass


def is_public_asset(rel):
    """True for the files of a problem folder that are published as they are.

    rel is a POSIX path relative to the problem folder. PROBLEM.md, input.txt and images/ are
    the statement; tests/ (inputs and expected outputs) checks the student's code without an
    oracle. Everything else is a spoiler. spoiler.bin itself is neither.
    """
    return rel in ("PROBLEM.md", "input.txt") or rel.startswith(("images/", "tests/"))


def check_member_name(name):
    """Reject names that could escape the problem folder or clobber the student's files."""
    p = PurePosixPath(name)
    if not name or name.startswith("/") or "\\" in name or p.is_absolute():
        raise SpoilerError(f"unsafe path in spoiler: {name!r}")
    if any(part in ("", ".", "..") for part in name.split("/")):
        raise SpoilerError(f"unsafe path in spoiler: {name!r}")
    if ATTEMPT.match(p.name) or is_public_asset(name) or name == SPOILER_NAME:
        raise SpoilerError(f"file not allowed in a spoiler: {name!r}")


def _keystream(problem_id, n):
    seed = KEY + b"\0" + problem_id.encode() + b"\0"
    blocks = (hashlib.sha256(seed + i.to_bytes(8, "big")).digest() for i in range((n + 31) // 32))
    return b"".join(blocks)[:n]


def _xor(data, problem_id):
    n = len(data)
    if n == 0:
        return b""
    ks = _keystream(problem_id, n)
    return (int.from_bytes(data, "big") ^ int.from_bytes(ks, "big")).to_bytes(n, "big")


def make_tar(files):
    """files: {relpath: (bytes, executable)} -> deterministic tar bytes."""
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for name in sorted(files):
            check_member_name(name)
            data, executable = files[name]
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mtime = 0
            info.mode = 0o755 if executable else 0o644
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            tar.addfile(info, io.BytesIO(data))
    return buf.getvalue()


def encode(problem_id, files):
    """Pack files ({relpath: (bytes, executable)}) into spoiler.bin bytes."""
    if not files:
        raise SpoilerError(f"{problem_id}: nothing to pack")
    tar = make_tar(files)
    pid = problem_id.encode()
    head = HEADER.pack(MAGIC, SPOILER_FORMAT, len(pid), hashlib.sha256(tar).digest())
    return head + pid + _xor(zlib.compress(tar, 9), problem_id)


def decode(blob, problem_id=None):
    """spoiler.bin bytes -> {relpath: (bytes, executable)}, verified. Raises SpoilerError."""
    if len(blob) < HEADER.size:
        raise SpoilerError("spoiler too short")
    magic, version, id_len, digest = HEADER.unpack_from(blob)
    if magic != MAGIC:
        raise SpoilerError("not a spoiler package (bad magic)")
    if version != SPOILER_FORMAT:
        raise SpoilerError(f"spoiler format {version} not supported (expected {SPOILER_FORMAT})")
    pid = blob[HEADER.size:HEADER.size + id_len].decode()
    if problem_id is not None and pid != problem_id:
        raise SpoilerError(f"spoiler belongs to {pid!r}, not {problem_id!r}")
    try:
        tar_bytes = zlib.decompress(_xor(blob[HEADER.size + id_len:], pid))
    except zlib.error as e:
        raise SpoilerError(f"corrupt spoiler: {e}") from None
    if hashlib.sha256(tar_bytes).digest() != digest:
        raise SpoilerError("corrupt spoiler: hash mismatch")
    files = {}
    with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode="r:") as tar:
        for m in tar.getmembers():
            if not m.isreg():
                raise SpoilerError(f"non-regular member in spoiler: {m.name!r}")
            check_member_name(m.name)
            if m.name in files:
                raise SpoilerError(f"duplicate member in spoiler: {m.name!r}")
            files[m.name] = (tar.extractfile(m).read(), bool(m.mode & 0o111))
    return files


def spoiler_id(blob):
    """The problem id stored in a spoiler header, without decoding the body."""
    magic, _, id_len, _ = HEADER.unpack_from(blob)
    if magic != MAGIC:
        raise SpoilerError("not a spoiler package (bad magic)")
    return blob[HEADER.size:HEADER.size + id_len].decode()


# Catalog and problem lookup.

def load_catalog(path=CATALOG, text=None):
    data = json.loads(text if text is not None else Path(path).read_text())
    if data.get("format") != CATALOG_FORMAT:
        raise SystemExit(f"{path}: catalog format {data.get('format')} not supported")
    return data["problems"]


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.casefold())


def resolve(arg, catalog):
    """Find a catalog entry by id, folder path or folder/problem name (spaces, quotes...)."""
    arg = arg.strip().rstrip("/")
    for key in ("id", "folder"):
        hits = [e for e in catalog if e[key] == arg]
        if hits:
            return hits[0]
    try:  # a path to the folder, absolute or relative to the current directory
        rel = Path(arg).resolve().relative_to(ROOT).as_posix()
        hits = [e for e in catalog if e["folder"] == rel]
        if hits:
            return hits[0]
    except (ValueError, OSError):
        pass
    for match in (lambda e: Path(e["folder"]).name == arg,
                  lambda e: Path(e["folder"]).name.casefold() == arg.casefold(),
                  lambda e: _norm(arg) in (_norm(Path(e["folder"]).name), _norm(e["longName"]), _norm(e["id"]))):
        hits = [e for e in catalog if match(e)]
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            raise LookupError(f"{arg!r} is ambiguous: " + ", ".join(e["id"] for e in hits))
    raise LookupError(f"{arg!r} is not a solved problem of the catalog (data/practice.json)")


def techniques_package(index_text, catalog):
    """data/techniques.json text (solutions branch) -> data/techniques.bin bytes.

    Only what `reveal.py --learn` prints is kept: per technique its name, family, aliases,
    description and its problems easy to hard (catalog id, folder, name). The per-problem
    notes, difficulties and primary/secondary split stay on the solutions branch.
    """
    src = json.loads(index_text)
    if src.get("version") != 1:
        raise SpoilerError(f"techniques.json version {src.get('version')} not supported")
    by_folder = {e["folder"]: e for e in catalog}
    out = {}
    for key, t in sorted(src["techniques"].items()):
        problems = []
        for p in src["progressions"].get(key, []):
            e = by_folder.get(f"contests/{p}")
            if e is None or e["capability"] != "practice":
                raise SpoilerError(f"techniques.json: {key}: {p!r} is not a practice problem of the catalog")
            problems.append({"id": e["id"], "folder": e["folder"], "longName": e["longName"]})
        out[key] = {"name": t["name"], "family": t["family"], "aliases": list(t.get("aliases", [])),
                    "description": t["description"], "problems": problems}
    unknown = set(src["progressions"]) - set(src["techniques"])
    if unknown:
        raise SpoilerError(f"techniques.json: progressions of unknown techniques {sorted(unknown)}")
    doc = {"format": TECHNIQUES_FORMAT, "techniques": out}
    data = (json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True) + "\n").encode()
    return encode(TECHNIQUES_ID, {TECHNIQUES_MEMBER: (data, False)})


def read_techniques(blob):
    """data/techniques.bin bytes -> the index dict, verified."""
    files = decode(blob, TECHNIQUES_ID)
    if set(files) != {TECHNIQUES_MEMBER}:
        raise SpoilerError(f"technique index holds {sorted(files)}, expected {TECHNIQUES_MEMBER}")
    doc = json.loads(files[TECHNIQUES_MEMBER][0])
    if doc.get("format") != TECHNIQUES_FORMAT:
        raise SpoilerError(f"technique index format {doc.get('format')} not supported")
    return doc


def cs_academy_url(entry):
    return f"https://csacademy.com/ieeextreme-practice/task/{entry['urlName']}/"


def verify(root=ROOT, manifest=None):
    """Decode every catalog spoiler under root; check manifest hashes. Returns a list of errors."""
    errors = []
    for e in load_catalog(Path(root) / "data" / "practice.json"):
        path = Path(root) / e["folder"] / SPOILER_NAME
        try:
            files = decode(path.read_bytes(), e["id"])
            if not any(PurePosixPath(n).stem == "solution" and "/" not in n for n in files):
                errors.append(f"{e['id']}: spoiler has no solution file")
        except (OSError, SpoilerError) as err:
            errors.append(f"{e['id']}: {err}")
    tech = Path(root) / TECHNIQUES_BIN
    if tech.exists():
        try:
            read_techniques(tech.read_bytes())
        except (SpoilerError, ValueError) as err:
            errors.append(f"{TECHNIQUES_BIN}: {err}")
    if manifest:
        m = json.loads(Path(manifest).read_text())
        if m.get("versions", {}).get("spoiler") != SPOILER_FORMAT:
            errors.append(f"manifest spoiler format {m.get('versions', {}).get('spoiler')} != {SPOILER_FORMAT}")
        for rel, digest in m["artifacts"].items():
            p = Path(root) / rel
            if not p.is_file():
                errors.append(f"{rel}: missing")
            elif hashlib.sha256(p.read_bytes()).hexdigest() != digest:
                errors.append(f"{rel}: hash differs from the publication manifest")
    return errors


def main(argv):
    if not argv or argv[0] != "verify":
        raise SystemExit(__doc__.split("\n\n")[1])
    manifest = None
    if "--manifest" in argv:
        manifest = argv[argv.index("--manifest") + 1]
    elif MANIFEST.exists():
        manifest = MANIFEST
    errors = verify(ROOT, manifest)
    for err in errors:
        print(err, file=sys.stderr)
    n = len(load_catalog())
    print(f"{n} spoilers checked, {len(errors)} errors" + (f", manifest {manifest}" if manifest else ""))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
