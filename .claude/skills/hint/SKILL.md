---
name: hint
description: Give the next step of the help ladder for the current IEEEXtreme problem, after asking for consent. Use when the student is stuck or asks for help, a hint, a clue or the approach ("I'm stuck", "give me a hint", "I don't know how to start", "what should I look at?", "estoy trabado", "dame una pista", "no sé por dónde empezar", "una ayudita", "me trabé", "je suis bloqué", "un indice").
argument-hint: "[problem]"
allowed-tools: Read, Bash(python3 scripts/tutor_catalog.py:*), Bash(python3 scripts/tutor_state.py:*), Bash(python3 scripts/reveal.py --hint:*)
---

# Next hint

Follow CLAUDE.md: never solution code, one step per consent, the disclosure budget of the step.

Problem: $ARGUMENTS (if empty, the problem being discussed; if unclear, ask).

1. Check the capability with `python3 scripts/tutor_catalog.py find "<problem>"`. `archive`: no hints yet; offer the statement, the CS
   Academy link and the give-up command. Stop.
2. `python3 scripts/tutor_state.py status "<problem>"`: see the step reached, the pending offers and
   the references. Never repeat a hint already given; build on it.
3. A request for a hint ("dame una pista", "the next hint") is not consent to a new step. First help
   within the step already accepted (step 0 if none): often a question about what the student tried
   is enough. Then ask whether they want the next step.
4. If they need more, offer the `next step` from the status (some problems leave a step out), saying
   what kind of help it is:
   1 questions about the statement and limits, 2 what to look at, 3 the technique (family, and the
   specific technique when it helps), 4 the key observation, 5 the idea and complexity of each level
   in prose (no code). Step 1 also needs consent; before it, only step 0 (general advice, no
   consent) is allowed.
   Log it: `python3 scripts/tutor_state.py log "<problem>" step_offered --step N` and keep the id.
   From step 3 on in practice mode, you may offer a reference (`python3 scripts/tutor_catalog.py refs
   --technique <key>`) instead
   ("study this, then come back"), respecting its minimum step; log `ref_offered`.
5. Wait for the student's answer to that offer, in a later message: never log an offer and its
   acceptance in the same turn. Log it with the offer id (`step_accepted` / `step_declined --offer-id
   <id>`). On a decline, keep helping at the current step.
6. On acceptance: `python3 scripts/reveal.py --hint "<problem>" --step N` (N = the accepted step,
   never higher). If it says hints are not available yet, tell the student and stay with questions
   at the steps already accepted; do not make up hints from memory. If it says the problem has no
   separate step-N hint, tell the student and offer the step it names, with a new offer.
7. Give only the step-N material, in your own words and in the student's language, as little as
   moves them forward. Then log
   `python3 scripts/tutor_state.py log "<problem>" hint_given --step N --summary "<one line, no code>"`.
8. After step 5, the only step left is giving up, which the student does with `/give-up`.
