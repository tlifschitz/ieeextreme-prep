---
name: verify
description: Run the student's attempt.py or attempt.cpp against the problem's local tests and report like a judge. Use when the student asks whether their solution or code is right, wants to test or check it, or asks why it fails ("is my solution right?", "check my code", "test my attempt", "does it pass?", "why WA?", "¿está bien mi solución?", "revisá mi código", "probá mi solución", "¿pasa los tests?", "est-ce que ma solution est correcte ?").
argument-hint: "[problem] [--lang py|cpp] [--show]"
allowed-tools: Read, Bash(python3 scripts/tutor_catalog.py:*), Bash(python3 scripts/verify.py:*), Bash(python3 scripts/tutor_state.py status:*), Bash(python3 scripts/tutor_state.py log:*)
---

# Verify the attempt

Problem and options: $ARGUMENTS (if no problem is given, use the one being discussed).

1. Check the capability with `python3 scripts/tutor_catalog.py find "<problem>"`. `archive`: say that local verification is not
   available yet and give the CS Academy link to submit there. Stop.
2. Read `python3 scripts/tutor_state.py status "<problem>"`; if this conversation has not logged a
   `session_start` for the problem, log `session_start --mode practice` first. Then run
   `python3 scripts/verify.py "<problem>"` (add `--lang py|cpp` if both files exist). It
   compiles C++ once, runs every test with an approximate time limit, prints the verdict per test
   and logs a `verify_run` event. If there is no attempt file, offer to copy a template.
3. Report it like a judge, in the student's language: "passed X/Y local cases" and the verdicts
   (OK, WA, RE, TLE, CE, N/A). Never call it a contest score: the judge's tests are different. TLE
   is approximate, measured on this machine.
4. Explain failures within the disclosure budget of AGENTS.md:
   - CE and RE: explain the compiler message or the crash in their code. Always fine.
   - WA: if they want to see a small failing case, rerun with `--show`. Say what you can observe:
     which test fails, what their code outputs on the small case, which line produces it. If fixing
     it needs a fact about the statement or an observation they do not have yet, do not explain it,
     even when they ask "just tell me the bug": offer the step it belongs to (`hint` skill protocol)
     and explain only after the yes.
   - TLE: compare the complexity of their approach with the limits (N, time limit). Saying "this is
     O(N^2) and N is 10^6" is fine; saying what faster approach to use is a hint and needs consent
     for its step (use the `hint` skill protocol).
   - N/A: the checker or interactor is not available yet; say so, do not guess a verdict.
5. Never print the test files of failing big tests, and never the expected output of a checker or
   interactive problem.
6. All passed: suggest submitting on CS Academy (`https://csacademy.com/ieeextreme-practice/task/<urlName>/`).
   When the student says it was accepted, log `python3 scripts/tutor_state.py log "<problem>" solved`.
