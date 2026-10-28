---
name: give-up
description: Give up on a problem and see its solution. Only the student invokes this (/give-up <problem>); it tells them the command to run, which records the give-up in git.
argument-hint: "<problem>"
disable-model-invocation: true
allowed-tools: Read, Bash(python3 scripts/tutor_catalog.py:*), Bash(python3 scripts/tutor_state.py status:*)
---

# Give up on a problem

Problem: $ARGUMENTS (if empty, the problem being discussed; if unclear, ask).

Never run `scripts/reveal.py` for this: the student runs it in their own terminal.

1. Find the problem with `python3 scripts/tutor_catalog.py find "<problem>"` (any capability: archive
   problems can be given up too).
   Read `python3 scripts/tutor_state.py status "<problem>"` to know how many steps they used.
2. Confirm, in the student's language, in one or two sentences: they will see the full solution,
   and `reveal.py` commits a line to `progress/give-ups.md` (problem, date, hints used) before
   installing the files. If they have steps left on the ladder, mention once that the next step is
   still available as an alternative, without pushing.
3. If they confirm, give them the exact command to run from the repository root:

   ```
   python3 scripts/reveal.py "<problem>"
   ```

   Run it in a real terminal: it asks for confirmation. From a non-interactive shell (e.g. Claude
   Code's `!` prefix) it refuses unless the student adds `--yes` themselves.
   It needs a git identity (`git config user.name` / `user.email`); if it is missing, the script
   says how to set it. It never overwrites `attempt.*` and never pushes. Running it again after an
   interruption finishes the installation without a second record.
4. Do not run it, and do not print the solution yourself (no `--peek` here).
5. When they come back with the solution installed, offer to go over it with them, compare it with
   their attempt, and offer further reading and similar problems.
