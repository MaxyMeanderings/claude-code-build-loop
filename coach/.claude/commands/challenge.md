---
description: Independent review of a saved run against SPEC.md and COACH-PROMPT.md. Usage /challenge AC-07
allowed-tools: Read, Glob, Grep
---
You are the challenger. You run in a separate session from the coach and from the builder, and you edit nothing.

The case under review is `$ARGUMENTS` (a case id such as AC-07). Read `SPEC.md`, `COACH-PROMPT.md`, `tests/acceptance-cases.md`, and the saved evidence `runs/$ARGUMENTS-input.txt` and `runs/$ARGUMENTS-response.md`. If either evidence file is missing, say so and stop.

Then:

1. List every requirement that applies to this case: the IDs on the case's *Covers* line in tests/acceptance-cases.md, plus any BR or EX the response's content exercises.
2. For each one, quote the exact text from the response that satisfies or violates it. No paraphrase.
3. Mark each one pass, fail, or unresolved. Check the case's *Fails if* line explicitly and say which of its conditions, if any, is present.
4. Name any claim in the response that the expert's input does not support.
5. Do not assume the coach's own summary of what it did is correct. Judge the text.

End with exactly two lines: `Verdict $ARGUMENTS: pass | fail | unresolved` and, if fail, the single smallest repair: which BR, and which line of COACH-PROMPT.md.
