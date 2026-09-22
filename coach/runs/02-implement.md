Built. Q1–Q8 recorded in `SPEC.md` § 10 before building, as instructed.

## What was created

| File | Contents |
|---|---|
| `COACH-PROMPT.md` | Role, § Definitions (glossary), BR-01…BR-25, EX-01…EX-08, § Session flow, § Template Registry, § Template Contract |
| `templates/idea-brief.md` | 8 registered headings |
| `templates/count-ledger.md` | 3 headings, six-row C1–C6 table |
| `templates/experiment-card.md` | 8 headings |
| `templates/build-brief.md` | 7 headings |
| `tests/acceptance-cases.md` | AC-01…AC-25 with `Covers:` IDs, status, and run procedure |

`SPEC.md` was the only file edited. `BUILD-BRIEF.md`, `BUILD-STEPS.md`, `README.md`, `prompts/`, and existing `runs/` are untouched.

## Checks actually run

| Check | Result |
|---|---|
| AC-23 headings vs § 7 | Pass — 8 / 3 / 8 / 7, exact and in order |
| AC-22 DRY | Pass — 25 BR + 8 EX normative statements, each exactly once, all in `COACH-PROMPT.md`; zero bolded rule statements in `templates/` or `tests/` |
| AC-20 grep half (ENG-DIP-01) | Pass — no vendor/product name in `COACH-PROMPT.md` |
| AC-23 filenames (ENG-CONV-01) | Pass — root SCREAMING-KEBAB, in-folder lower-kebab |
| AC-24 SRP | Pass — 25/25 cases carry a BR/EX/ENG ID; no template body in the prompt |
| AC-21, AC-25 | Pass by review; reasoning recorded inline in the test file |

**AC-01…AC-19 are Not run.** They need fresh conversations, which per Q7 the expert runs, saving input and full response to `runs/`. AC-20's run half is Unresolved because it depends on AC-01.

## Engineering requirements — the N/As

- **ENG-ACID-NA** — genuinely N/A: no database, transactions, persistence, or concurrent writers. BR-11 (whole-ledger restatement) is in `COACH-PROMPT.md` and labeled there as a presentation convention, not a guarantee.
- **ENG-BIGO-NA** — no complexity class assigned to model reasoning. The two real analyses are attached where they belong: O(1) invariant check in AC-10's review note, O(c·m) attribution scan in AC-07's.
- **ENG-LSP-01** — classical subtype substitution is N/A (no type hierarchy). Implemented in the available form: § Template Contract, swap-by-heading.
- **ENG-OCP-01, ENG-DIP-01** — implemented in the limited form the spec allows: registry-row extension, and structure read from the registry rather than template prose. No abstraction was invented for either.

Two things to flag:

1. **A spec typo I corrected.** § 2 said the test file holds "AC-01 … AC-23"; § 9 defines 25 cases. I treated § 9 as authoritative and changed § 2's range.
2. **One DRY overlap I could not eliminate.** `SPEC.md` § 4 states the BRs normatively and so does `COACH-PROMPT.md` — the spec's own structure requires both. I scoped the AC-22 audit to the runtime set per § 3's "at runtime" wording, and recorded that scoping explicitly in the test file along with the tie-break: `COACH-PROMPT.md` governs runtime, `SPEC.md` gets repaired if they diverge. That is a judgment call on an ambiguity in the spec, not something the spec settles.
