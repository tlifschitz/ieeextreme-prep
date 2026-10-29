---
name: learn
description: Study a technique or topic, with curated references first and then practice problems of that technique from easy to hard. Use when the student names a topic they want to learn or practice ("I want to learn about stacks", "teach me dynamic programming", "problems about binary search", "how does Dijkstra work?", "quiero aprender programación dinámica", "quiero aprender sobre grafos", "enseñame segment trees", "problemas de búsqueda binaria", "je veux apprendre les graphes").
---

# Learn a technique

Technique: $ARGUMENTS (if empty, ask which one).

Follow AGENTS.md. In this mode the technique is known, because the student chose it.

1. Log the topic: `python3 scripts/tutor_state.py learner log topic_studied --topic "<technique>"`,
   and read `python3 scripts/tutor_state.py learner status` to see what they already read or declined.
2. References: from the catalog only, never from memory: `python3 scripts/tutor_catalog.py refs
   --technique <key>` (`refs --list-techniques` lists the keys). Cite each entry's citation line, without
   page numbers. Offer the entries for that technique (in learn mode no minimum step applies before the first problem, except exact
   reductions of a specific problem, which stay at step 5). Log each offer and answer
   (`learner log ref_offered --ref-id <id>`, then `ref_accepted` / `ref_declined --offer-id <id>`,
   and `ref_read --ref-id <id> --takeaway "..."` when they come back). If the catalog does not exist
   or has nothing for the topic, say there is no curated reference yet. You may explain the
   technique itself in general terms (what it is, when it applies, its complexity), briefly and
   after the references, without solving any problem of the repository.
3. Problems: `python3 scripts/reveal.py --learn "<technique>"` lists the problems of that technique,
   easy to hard. If it says the index is not available yet, tell the student and suggest the
   `practice` skill instead. Never build such a list from memory or from tags.
4. When they pick a problem, continue as in the `practice` skill but log
   `session_start --mode learn`. Step 3 (the family) is already known for it; the key observation
   (step 4) and the levels (step 5) still need consent, one step at a time.
5. After they solve or give up, offer the next problem of the list and any further reading.
