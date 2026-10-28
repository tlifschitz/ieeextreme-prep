# IEEEXtreme practice archive

Practice for the IEEEXtreme programming competition on the problems of the CS Academy IEEEXtreme
practice archive (editions 10-19).

- `contests/ieeextremeNN/<problem>/PROBLEM.md`: the statement, with a link to the problem on CS
  Academy, where you can submit to the real judge. `input.txt` holds a sample input.
- `spoiler.bin`: the solutions, the ladder from naive to optimal and the notes of that problem,
  packed so that you do not read them by accident. It looks like binary noise on purpose.
- `tests/` (practice problems, as they get them): local test cases for `scripts/verify.py`.
- `data/practice.json`: the solved problems. `practice` ones have a tutor and, as they get them,
  local tests; `archive` ones have the statement and the spoiler for now.
- `lib/`: a contest library (Python and C++) with tests; `scripts/bundle.py` inlines it into a
  single submittable file.

## Practicing

1. Pick a `practice` problem and read its `PROBLEM.md`.
2. Start from a template: `cp templates/attempt/attempt.py "contests/ieeextremeNN/<problem>/"`
   (or `attempt.cpp`).
3. Check it against the local tests: `python3 scripts/verify.py "<problem>"`
   (`python3 scripts/verify.py --setup` checks Python, numpy and the C++ compiler).
4. Stuck? Open the repository in Claude Code: it acts as a tutor (`CLAUDE.md`), with hints one
   step at a time, never the solution code. The first time you open the repository, accept Claude
   Code's workspace trust dialog: until you do, it ignores `.claude/settings.json`, which lets the
   tutor's skills (`/practice`, `/hint`, `/verify`, `/learn`, `/give-up`) run without asking for
   permission each time.

## Giving up

Solve the problem first. If you decide to see the solution:

    python3 scripts/reveal.py "<problem folder name or id>"

This records the give-up in `progress/give-ups.md` (a commit in your clone) and then installs the
solution, the levels and the notes into the problem folder. `reveal.py` never pushes, but if you
push your clone or fork, your give-ups go with it, and that is on purpose: the record is part of
practicing honestly. It never overwrites your own `attempt.py` / `attempt.cpp`.

## Attribution

The problem statements, images and sample tests come from the IEEEXtreme Programming Competition
(IEEE) as published in the CS Academy IEEEXtreme practice archive
(https://csacademy.com/ieeextreme-practice/tasks). They belong to their authors and are included here
only as practice material.
