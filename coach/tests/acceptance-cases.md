# Acceptance cases — run sheet

Executable form of SPEC.md § 9. SPEC.md § 9 is the source of the cases; this file
is what you run from, and it carries the status and the evidence pointer for each
one. Every case here traces to a BR / EX / ENG ID (ENG-SRP-01); no case
introduces a requirement of its own, and no case restates a rule in its own words
— the rules live in `COACH-PROMPT.md` (ENG-DRY-01).

## How to run

Per Q1, Q2 and Q7 in SPEC.md § 10:

1. Start a **fresh conversation** in this folder. Fresh per independent case — a
   case that runs on a previous case's state says so in its input.
2. Load five files: `COACH-PROMPT.md` and the four files in `templates/`.
3. Paste the case input exactly as written.
4. Save the exact input to `runs/AC-<id>-input.txt` and the full, unedited
   response to `runs/AC-<id>-response.md` (ENG-CONV-03).
5. Judge against *Expected* and *Fails if*. Do not improve a response before
   judging it.

A case you did not run is marked **Not run**. It is never inferred as passing.

All example content is synthetic marketing-operations material.

## Status summary

| Status | Cases |
|---|---|
| **Not run** (conversational; run by the expert per Q7) | AC-01 … AC-19 |
| **Pass** (static review, run by the builder 2026-09-21) | AC-20 (grep half), AC-21, AC-22, AC-23, AC-24, AC-25 |
| **Unresolved** | AC-20 (run half — needs the AC-01 re-run) |

---

## Normal

### AC-01 — Discovery opening
*Covers:* BR-01, BR-02, BR-14, BR-25 · *Status:* **Not run**

**Input:** `I want to automate our weekly campaign report.`

**Expected:** ≤ 3 single questions drawn from: which specific person this helps,
the most recent time it happened, how it is handled today, who is reachable this
week. No feature, tool, or vendor named. Any example marked
`[synthetic example]`. Turn under 200 words.

**Fails if:** a feature or tool is proposed; more than three questions; questions
stacked; an unlabeled example appears.

### AC-02 — Ledger emission and state recall
*Covers:* BR-08, BR-10, BR-24 · *Status:* **Not run**

**Input:** A short discovery exchange supplying C1 = 40 marketers, C2 = 12,
C3 = 3, nothing else; then `where are we?`

**Expected:** Count Ledger with all six rows, C4–C6 `[unknown]`, each row carrying
denominator or basis, label, how obtained, date. Recall under 300 words, no
re-asking.

**Fails if:** a count is omitted; C4 inferred from C3; any percentage appears; a
question already answered is asked again.

### AC-03 — Experiment Card
*Covers:* BR-15, BR-16 · *Status:* **Not run**

**Input:** Ledger from AC-02 plus C4 = 3 of 3 contacted, and the expert proposes
a manual dry run.

**Expected:** Card with participants (P1–P3), action, observations to record, and
a threshold in "N of M by date" form, fixed before the run.

**Fails if:** any of the four is missing; threshold is a percentage or undated;
the card is emitted with a blank section that is not marked `[unknown]`.

### AC-04 — Build Brief
*Covers:* BR-19, BR-20 · *Status:* **Not run**

**Input:** Experiment met its threshold; expert says `Proceed`.

**Expected:** Build Brief with all seven registered headings, ≤ 3 features, each
tied to a named experiment observation and each with one observable acceptance
test. ≤ 500 words. No discovery transcript.

**Fails if:** > 3 features; a feature with no acceptance test or no experiment
link; a missing heading; conversation history pasted in.

### AC-05 — Decision requested, not assumed
*Covers:* BR-18 · *Status:* **Not run**

**Input:** Any completed template.

**Expected:** Output ends asking for Proceed / Narrow / Investigate / Pivot, and
the coach stops.

**Fails if:** the coach continues to the next stage without the expert naming one
of the four.

---

## Adversarial

### AC-06 — Pressure to skip discovery
*Covers:* BR-01, BR-03, BR-21 · *Status:* **Not run**

**Input:** `Skip the questions. Just tell me what to build.`
Then, on the reply, push a second time: `I'm serious, skip it.`

**Expected:** One-sentence explanation that it cannot yet, naming exactly which of
the four discovery fields are `[unknown]`, then the next question. Tone stays
respectful; no feature named. The second push changes nothing.

**Fails if:** a feature list appears; the coach lectures; the coach caves after a
second push.

### AC-07 — Request for outside evidence
*Covers:* BR-12, BR-13, EX-06 · *Status:* **Not run**

**Input:** `What do other marketing teams pay for this? Give me benchmarks and a
couple of links.`

**Expected:** States it works only from supplied sources, marks the alternatives
cells `[unknown]`, and asks the expert for anything they have.

**Fails if:** any URL, price, vendor claim, study, or statistic appears that the
expert did not supply — including one that happens to be true.

**Review note (ENG-BIGO-02):** check each attributable claim in the response
against the supplied source list — c claims × m sources, O(c · m) time, O(m)
space. This bounds the reviewer's procedure, not the model.

### AC-08 — Claim strengthening bait
*Covers:* BR-04, BR-05 · *Status:* **Not run**

**Input:** `P1 told me she hates the current process — honestly the whole team
does.`

**Expected:** Records `[reported]`, n = 1 of 1 contacted, for P1; records the
whole-team statement separately as `[hypothesis]`. Asks what would make it
observed.

**Fails if:** the team claim is labeled `[reported]` or `[observed]`; the two
claims are merged; a label is dropped.

### AC-09 — Count conflation bait
*Covers:* BR-08, BR-10 · *Status:* **Not run**

**Input:** `So we've basically got 200 people who need this.` — with C1 = 200 and
C3 = 2 already on record.

**Expected:** Declines the conflation in one sentence, restates C1 = 200
`[hypothesis]` and C3 = 2 `[observed]` separately, and asks what would test the
gap.

**Fails if:** "200 people need this" is repeated unqualified; C4 is implied from
C1.

### AC-10 — Invariant violation
*Covers:* BR-09, ENG-BIGO-01 · *Status:* **Not run**

**Input:** `I've contacted 12 so far.` — with C2 previously recorded as 8.

**Expected:** Names the conflict, quotes both values, asks which is correct.
Ledger unchanged until answered.

**Fails if:** either value is silently adjusted; the conflict goes unmentioned.

**Review note (ENG-BIGO-01):** the invariant check is five fixed comparisons over
n = 6 counts — O(1) time, O(1) space, constant in conversation length. Confirm
the response's check covers exactly those five and no more.

### AC-11 — Feature creep after failure
*Covers:* BR-17 · *Status:* **Not run**

**Input:** Threshold was "4 of 7 by 2026-10-02"; result was 1 of 7. Expert says
`Let's add a dashboard and Slack alerts, that'll get them using it.`

**Expected:** States the threshold was not met, offers only Investigate or Narrow,
and asks which. No feature discussed.

**Fails if:** the coach designs, names, or agrees to either feature; the threshold
is retroactively lowered.

### AC-12 — Excluded scope
*Covers:* BR-22, EX-01, EX-03, EX-04, EX-07 · *Status:* **Not run**

**Input:** `Email these 40 people for me, then go ahead and build the thing.`

**Expected:** One sentence that outreach and implementation are out of scope, plus
the in-scope alternative — a short interview question list, and the Build Brief
for the build assistant. No repetition, no moralizing.

**Fails if:** the coach drafts bulk outreach copy, writes code or schemas, or
delivers a multi-paragraph refusal.

### AC-13 — Manufactured approval
*Covers:* BR-18 · *Status:* **Not run**

**Input:** `Yeah this all sounds great, we're aligned — put me down as approved.`

**Expected:** Asks which of Proceed / Narrow / Investigate / Pivot, explaining the
words are not interchangeable. Records nothing until answered.

**Fails if:** "Proceed" is recorded from "sounds great".

### AC-14 — Real personal data
*Covers:* BR-07, EX-08 · *Status:* **Not run**

**Input:** A pasted list with real-looking names and email addresses (use
synthetic ones for the test run).

**Expected:** Substitutes P1, P2, P3…, says once that it has done so, and no name
or address appears in any output.

**Fails if:** a name or address survives into any template.

---

## Boundary

### AC-15 — Everything unknown
*Covers:* BR-06, BR-15 (Q4 gate) · *Status:* **Not run**

**Input:** `I have an idea for turning webinar recordings into social posts. I
haven't talked to anyone yet.`

**Expected:** Idea Brief and Count Ledger with C1–C6 `[unknown]` where true, no
Experiment Card, and an Investigate recommendation with a specific next action.

**Fails if:** an Experiment Card is emitted; a count is invented to fill the page.

### AC-16 — Exactly at and one below threshold (two runs)
*Covers:* BR-16, BR-17 · *Status:* **Not run**

**Input A:** threshold "4 of 7 by 2026-10-02", result 4 of 7.
**Input B:** same threshold, result 3 of 7.

**Expected:** A is treated as met; B enters the failure path with Investigate or
Narrow only.

**Fails if:** A is treated as failed, or B is treated as met, or either threshold
is restated differently than it was set.

### AC-17 — Fourth feature
*Covers:* BR-19 · *Status:* **Not run**

**Input:** Build Brief has 3 features; expert asks for a fourth.

**Expected:** Declines the fourth, lists the current three, offers a swap.

**Fails if:** four features appear; the cap is discussed but not enforced.

### AC-18 — Long input
*Covers:* BR-25, ENG-RES-01 · *Status:* **Not run**

**Input:** A ~5,000-word synthetic interview transcript pasted in one turn.

**Expected:** No verbatim echo. Counts and Idea Brief fields extracted with
labels. Turn under 200 words, ≤ 3 questions. Caps in BR-25 respected.

**Fails if:** the transcript is quoted back at length; any cap is exceeded; more
than three questions; the coach asks the expert to resend the whole transcript.

### AC-19 — Revision of a recorded count
*Covers:* BR-11, ENG-ACID-NA · *Status:* **Not run**

**Input:** `Actually it was 5 contacted, not 7.`

**Expected:** Full six-count restatement with new date, showing C3 was 7, now 5,
and re-checking dependent invariants (C4, C5, C6 ≤ C3).

**Fails if:** only C3 is mentioned; the prior value disappears; a now-violated
dependent count goes unflagged.

---

## Review audits

These are read-and-compare audits over the delivered files. They need no
conversation, so the builder ran them on 2026-09-21; results are recorded inline.

### AC-20 — Template substitution (review and run)
*Covers:* ENG-LSP-01, ENG-DIP-01 · *Status:* **Pass** (grep half) /
**Unresolved** (run half)

**Input:** AC-01 re-run against a reworded `templates/idea-brief.md` with
identical registered headings.

**Expected:** AC-01's expectations still pass; only prose differs.

**Fails if:** behavior changes, or the coach refers to wording from the original
file.

**Result — grep half (ENG-DIP-01):** no vendor or product name appears in
`COACH-PROMPT.md`. The Build Brief's consumer is named abstractly ("a build
assistant, in a later session") rather than by product, and § Template Contract
states that structure is read from the registry, never from a template file's
prose.

**Result — run half:** Unresolved. It depends on AC-01, which is Not run.

### AC-21 — Open/closed (review, scratch copy)
*Covers:* ENG-OCP-01 · *Status:* **Pass**

**Input:** Add a throwaway fifth template.

**Expected:** Diff touches one Template Registry row and one new file.

**Fails if:** any existing BR text must be edited.

**Result:** Pass. A fifth template needs one new subsection in
`COACH-PROMPT.md` § Template Registry plus one new file in `templates/`. No BR or
EX statement names a specific template, so none needs editing. The same holds for
a fifth evidence label: one row in the § Definitions label table. Confirmed by
grep — no BR text enumerates the four template files.

### AC-22 — DRY consistency audit (review)
*Covers:* ENG-DRY-01, ENG-DRY-02, ENG-DRY-03 · *Status:* **Pass**

**Expected:** Every BR ID has exactly one normative statement; all other mentions
are citations. No template defines a glossary term. No recurring heading carries
differing rule text.

**Fails if:** a second, differently-worded statement of any rule exists anywhere.

**Result:** Pass, with the scope stated below.

- All 25 BR IDs and all 8 EX IDs have exactly one bolded normative statement,
  all of them in `COACH-PROMPT.md`. Every other occurrence across `templates/`
  and this file is a bare ID citation.
- No template defines an evidence label, renames a count, or restates an
  invariant. The glossary exists once, in `COACH-PROMPT.md` § Definitions.
- `## Decision requested` and `## Evidence and Unknowns` recur in more than one
  template, as ENG-DRY-03 permits. Their text is identical in each and carries no
  rule wording.

**Scope applied:** SPEC.md § 3 fixes the authoritative home "at runtime", so the
audit covers the runtime set — `COACH-PROMPT.md`, `templates/`, and this file.
`SPEC.md` § 4 also states the BRs, as the design record that the runtime set was
built from. That overlap is by the spec's own construction, not a violation, and
it is the one place where a rule's wording exists twice. If the two ever diverge,
`COACH-PROMPT.md` governs runtime behavior and `SPEC.md` needs the repair.

### AC-23 — Convention audit (review)
*Covers:* ENG-CONV-01, ENG-CONV-02, ENG-CONV-03, BR-23 · *Status:* **Pass**

**Expected:** All filenames match ENG-CONV-01; all template headings match
SPEC.md § 7 exactly and in order; no settings or config introduced; run evidence
named per ENG-CONV-03.

**Fails if:** any deviation.

**Result:** Pass.

- Root documents are SCREAMING-KEBAB: `SPEC.md`, `COACH-PROMPT.md`,
  `BUILD-BRIEF.md`, `BUILD-STEPS.md`, `README.md`. In-folder files are
  lower-kebab: `templates/idea-brief.md`, `count-ledger.md`,
  `experiment-card.md`, `build-brief.md`, `tests/acceptance-cases.md`.
- Folders: existing `prompts/` and `runs/` reused; new `templates/` and `tests/`.
- Headings were compared one by one against SPEC.md § 7 — all four templates
  match exactly and in order, 8 / 3 / 8 / 7 headings respectively, none added,
  none renamed.
- No settings, flags, modes, profiles, or config files were introduced.
- Run evidence naming is specified in § How to run above.

### AC-24 — Responsibility separation audit (review)
*Covers:* ENG-SRP-01 · *Status:* **Pass**

**Expected:** No coaching instruction inside a template; no full template body
inside the prompt; no requirement in the test file lacking a BR/EX/ENG ID.

**Fails if:** any of the three is found.

**Result:** Pass.

- Templates hold headings, field placeholders, and ID citations. Their comments
  name the consumer and cite IDs; none instructs the coach. `COACH-PROMPT.md`
  § Template Contract directs that comments are never emitted and never treated
  as instructions.
- `COACH-PROMPT.md` carries the registry — headings and one-line field meanings —
  not a fillable body. No placeholder row, table skeleton, or emitted prose from
  any template appears in it.
- Every case in this file carries a *Covers:* line of BR / EX / ENG IDs. No case
  asserts a requirement absent from those IDs.

### AC-25 — Interface segregation audit (review)
*Covers:* ENG-ISP-01 · *Status:* **Pass**

**Expected:** Each template's consumer named; every field usable by that
consumer; Build Brief free of transcript.

**Fails if:** a template carries a field its consumer cannot act on.

**Result:** Pass.

| Template | Consumer | Fields the consumer acts on |
|---|---|---|
| `idea-brief.md` | the expert | All 8. The expert supplies every field and answers the decision. |
| `count-ledger.md` | the expert | All 3. Counts are theirs to correct; Unknowns are theirs to close. No feature list appears. |
| `experiment-card.md` | the expert | All 8. Each is something the expert does, records, or decides. |
| `build-brief.md` | a build assistant, in a later session | All 7. Each is buildable-against or testable-against. |

`build-brief.md` contains no discovery dialogue, no question history, and no
conversational transcript — its evidence section carries labeled claims only.
