#!/usr/bin/env python3
"""Inline `from lib.<module> import <names>` into a single submittable file.

Usage: python3 scripts/bundle.py path/to/solution.{py,cpp} [-o submit.{py,cpp}]

Python: each imported name is replaced by its source from lib/<module>.py,
together with the lib definitions and imports it depends on, in lib file order.
C++: each `#include "lib/<file>"` line (any path ending in lib/<file>) is
replaced by the whole file, recursively, once per file.
Without -o the result goes to submit.<ext> next to the solution.
"""
import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "lib"


def defined_names(node):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return [node.name]
    if isinstance(node, ast.Assign):
        return [t.id for t in node.targets if isinstance(t, ast.Name)]
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return [(a.asname or a.name).split(".")[0] for a in node.names]
    return []


def used_names(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def module_snippet(module, names):
    path = LIB / f"{module}.py"
    src = path.read_text()
    lines = src.splitlines()
    nodes = ast.parse(src).body
    by_name = {}
    for node in nodes:
        for name in defined_names(node):
            by_name[name] = node

    missing = [n for n in names if n not in by_name]
    if missing:
        sys.exit(f"lib/{module}.py does not define: {', '.join(missing)}")

    needed, todo = set(), list(names)
    while todo:
        node = by_name[todo.pop()]
        if id(node) in needed:
            continue
        needed.add(id(node))
        todo.extend(n for n in used_names(node) if n in by_name and id(by_name[n]) not in needed)

    imports, defs = [], []
    for node in nodes:
        if id(node) in needed:
            start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
            chunk = "\n".join(lines[start - 1 : node.end_lineno])
            (imports if isinstance(node, (ast.Import, ast.ImportFrom)) else defs).append(chunk)
    body = "\n".join(imports) + ("\n\n" if imports else "") + "\n\n\n".join(defs)
    return f"# ---- lib/{module}.py ----\n{body}\n# ---- end lib/{module}.py ----"


CPP_INCLUDE = re.compile(r'^\s*#include\s+"(?:[^"]*/)?lib/([^"/]+)"\s*(?://.*)?$')


def bundle_cpp(solution):
    done = set()

    def expand(text):
        out = []
        for line in text.splitlines():
            if line.strip() == "#pragma once":
                continue
            m = CPP_INCLUDE.match(line)
            if m:
                name = m.group(1)
                if name in done:
                    continue
                done.add(name)
                body = expand((LIB / name).read_text()).strip("\n")
                line = f"// ---- lib/{name} ----\n{body}\n// ---- end lib/{name} ----"
            out.append(line)
        return "\n".join(out)

    return expand(solution.read_text()) + "\n"


def bundle(solution):
    if solution.suffix == ".cpp":
        return bundle_cpp(solution)
    src = solution.read_text()
    lines = src.splitlines()
    replacements = []
    for node in ast.parse(src).body:
        if isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("lib."):
            module = node.module.split(".", 1)[1]
            names = [a.name for a in node.names]
            replacements.append((node.lineno, node.end_lineno, module_snippet(module, names)))
    for start, end, text in reversed(replacements):
        lines[start - 1 : end] = text.splitlines()
    return "\n".join(lines) + "\n"


def main():
    args = sys.argv[1:]
    solution = Path(args[0])
    out = Path(args[args.index("-o") + 1]) if "-o" in args else solution.with_name("submit" + solution.suffix)
    out.write_text(bundle(solution))
    print(out)


if __name__ == "__main__":
    main()
