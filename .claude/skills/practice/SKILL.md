---
name: practice
description: Start or resume practicing a specific IEEEXtreme problem with the technique hidden. Use when the student wants to work on, try, solve or continue a problem ("I want to practice <problem>", "let's do this IEEEXtreme 18 problem", "give me a problem to solve", "quiero practicar <problema>", "quiero resolver un problema", "sigamos con el problema de ayer", "je veux m'entraîner sur ...").
argument-hint: "[problem]"
allowed-tools: Read, Bash(python3 scripts/tutor_catalog.py:*), Glob, Bash(python3 scripts/tutor_state.py:*), Bash(cp templates/attempt/*)
---

# Practice a problem

Follow the rules in AGENTS.md (no solution code, the ladder, consent, the disclosure budget). The
technique stays hidden in this mode.

Problem: $ARGUMENTS (if empty, ask which one; to suggest one, pick from `python3 scripts/tutor_catalog.py list`
by contest or name, never by technique).

1. Find the problem with `python3 scripts/tutor_catalog.py find "<problem>"` and check its `capability`. For `archive`: give the
   statement path, the CS Academy link (`https://csacademy.com/ieeextreme-practice/task/<urlName>/`)
   and say that tutoring and verification are not available yet; the give-up command is the only
   other option. Stop there.
2. Read the state: `python3 scripts/tutor_state.py status "<problem>"`.
   - New ("unknown"): log `python3 scripts/tutor_state.py log "<problem>" session_start --mode practice`.
   - No problem named ("sigamos con el de ayer"): `python3 scripts/tutor_state.py learner status`
     lists the recent problems; confirm the most recent one with the student.
   - Resumed: log a new `session_start` too, recap where they were (steps already given, last
     verification) in one or two sentences, and follow up on any reference they accepted
     ("did you read it? what did you take from it?").
3. Point to the statement (`<folder>/PROBLEM.md`) and let the student read it. Do not summarize the
   solution-relevant parts for them; ask what they understood instead.
4. If there is no `attempt.py` / `attempt.cpp` yet, offer to copy a starter template:
   `cp templates/attempt/attempt.py "<folder>/"` (or `attempt.cpp`). It has no algorithm in it.
5. Start at step 0 of the ladder: general good practices that fit what the student is doing (no
   consent, nothing from this problem's hints). Step 1 (questions about the statement, the samples
   and the limits) and every step after it go through the `hint` skill protocol (offer, consent,
   log).
6. When they think they are done, run the `verify` skill. When they report an accepted submission,
   log `solved`, then offer further reading from `data/references.json` (if any) and similar
   problems.
