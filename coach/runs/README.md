# Runs

- `01-specify.md` — headless Specify run, 2026-09-21, against the re-aimed brief (domain experts, marketers as the archetype). Produced `SPEC.md` and its open questions.
- `02-implement.md` — headless Approve + Implement run, 2026-09-21, accepting every stated default. Produced `COACH-PROMPT.md`, the four templates (the fourth is the Build Brief), and `tests/acceptance-cases.md`.
- `AC-06-*`, `AC-07-*`, `AC-13-*` — **recorded, headless, 2026-09-21.** One-message approximation of the run procedure (prompt plus the four templates, then the input, in a single `claude -p` call, fresh session each). Inputs are saved verbatim as sent, with a one-line synthetic context prefix. Backups for the BIT Atlanta session, labeled "recorded last night." The live run on 2026-09-22, in a fresh interactive conversation with the room's input, is the evidence. `tests/acceptance-cases.md` still says Not run for AC-01…AC-19 on purpose; mark cases there only after interactive runs.

- `AC-TEST-*`, `test-coach.md`, `test-challenge.md`, `test-repair.md` — **loop test, 2026-09-21, headless.** `/coach` with the AC-07 input (no context prefix), then `save AC-TEST`, then `/challenge AC-TEST`. The challenger passed BR-12 / BR-13 / EX-06 and **failed the run on BR-02** (question 2 compound). Left unrepaired on purpose: it is the live repair target for the session if the live case passes. `test-repair.md` is `/repair` refusing a non-violation.

- `rec-1…rec-7`, 2026-09-21 late — the recorded sequence for the deck, headless with retries on API 529: `rec-1-coach` (a second AC-07 run; three clean questions), `rec-2-save` (wrote `AC-07-*`), `rec-3-challenge` (verdict **unresolved**: no rule violated, BR-13 never exercised on a bare input), `rec-4-repair` (BR-02 sharpened to one interrogative per numbered question, lines 104–109; BR-12 moved to line 151), `rec-5-rerun` + `rec-6-save` (wrote `AC-07-after-*`; BR-02 holds), `rec-7-challenge` (**unresolved** again, same BR-13 reason, no prompt repair applies).
- `rec-8a…rec-8d` — the challenger's prescribed better test: warm session (idea, P1, recent instance, reach stated), then the benchmarks input, then `save AC-07-warm`, then `/challenge AC-07-warm`.
- Frames for the deck are rendered from these files by `demo/captures/render-frames.js` into `hackhers-2026/slides/public/assets/bit-404/`. Text verbatim; each frame carries a "recorded, rendered" label.

The first build, from the unmodified HackHers student-team brief, is archived at `..\bit-404-coach-v1-student`.
