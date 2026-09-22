---
description: Fix exactly one reported rule violation in COACH-PROMPT.md and nothing else. Usage /repair BR-12 then what the challenger reported
allowed-tools: Read, Edit, Grep
---
Repair exactly one violation in `COACH-PROMPT.md`. The report from the challenger: $ARGUMENTS

Rules:

- Change only the rule text needed to prevent the reported failure. Do not touch other rules, the templates, SPEC.md, or tests/.
- Keep the rule's ID and its position. One rule has one authoritative statement; do not add a second statement elsewhere.
- Show the exact before and after text, then stop.
- Do not run any case. The operator reruns the failing case and one previously passing case per BUILD-STEPS.md section 7.
- If the report does not describe a violation of a specific BR, or the quoted response text does not actually violate it, say so plainly and change nothing.
