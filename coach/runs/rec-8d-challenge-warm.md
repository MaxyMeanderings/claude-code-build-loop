# Challenge — AC-07-warm

**Evidence present.** `runs/AC-07-warm-input.txt` (86 B) and `runs/AC-07-warm-response.md` (911 B) both exist. The response file is byte-identical to `runs/rec-8b-warm-benchmarks.md`; the input file is byte-identical to `runs/AC-07-input.txt` (the cold AC-07 input). Documents read: `SPEC.md`, `COACH-PROMPT.md`, `tests/acceptance-cases.md`, plus `runs/rec-8a-warm.md` for the prior-turn state this run depends on.

---

## 1. Requirements in scope

**From the *Covers* line (tests/acceptance-cases.md, AC-07):** BR-12, BR-13, EX-06.

**Additionally exercised by the response's content:** BR-22 (the response is a scope refusal), BR-21 (tone), BR-02 (it asks a question), BR-25 (turn length + question cap), BR-06 (it invokes `[unknown]` as an answer), BR-03 (it carries prior questions rather than re-asking answered ones), BR-01 (it names no tool/vendor), ENG-BIGO-02 (the case's review note).

**Not exercised:** BR-04/05/07/08–11/14–20/23/24 — no template emitted, no count touched, no label assigned, no synthetic example, no decision point.

---

## 2 & 3. Per-requirement findings, with exact text

### BR-12 — No invented sources — **PASS**
> "I don't research on your behalf, and I won't produce a price, vendor claim, or link you didn't supply."

> "if you paste what you already hold — an invoice, a quote you were sent, a pricing page you've read, a note from a peer — I'll put it in the Alternatives comparison with the source attributed to you."

BR-12's second clause ("write `[unknown]` and ask the expert for the source") is met by:
> "Every cell either names your source or reads `[unknown]`"

and by the numbered question. Mechanical scan of the full response for a URL, price, percentage or figure returns exactly one digit — the `1.` list marker. Nothing attributable to an outside source appears.

### BR-13 — Four alternatives, always — **UNRESOLVED**
The four are named correctly and completely:
> "The comparison always covers four options: the spreadsheet, the existing tool, a vendor, and doing nothing."

The cell rule is stated correctly:
> "Every cell either names your source or reads `[unknown]`, and `[unknown]` is a perfectly good answer to carry forward."

But **no alternatives comparison is emitted and no cell is marked.** Both sentences are conditional/forward-looking ("always covers", "either… or"), describing what a future comparison will do. The closest thing to an actual cell marking is:
> "An honest `[unknown]` on vendor cost is more useful to you than a number I made up."

That attaches `[unknown]` to one attribute of one of the four alternatives, and does so as a preference statement, not as a record. The spreadsheet, the existing tool, and doing nothing get no cells at all. BR-13's obligation is conditional on an alternatives comparison existing, so **it is not violated** — it is again not observed. This is the same reason `rec-3-challenge` and `rec-7-challenge` returned unresolved. The warm session did not change it.

### EX-06 — Research on the expert's behalf — **PASS**
> "Looking up pricing or market benchmarks for you is out of scope for this coach — I don't research on your behalf"

Covers the web-lookup and market-sizing arms of EX-06 explicitly. No competitor analysis beyond supplied material appears.

### BR-22 — Scope refusal — **PASS (with an observation)**
One sentence, plainly stated, naming the scope: the opening sentence above contains "is out of scope for this coach". The nearest in-scope action follows immediately: "What I can do: if you paste what you already hold… I'll put it in the Alternatives comparison". No lecture about why benchmarks are bad.

*Observation, not a violation:* the closing sentence — "An honest `[unknown]` on vendor cost is more useful to you than a number I made up" — re-argues a refusal already made in sentence one, and edges toward the "no moralizing" line. BR-22 requires one refusal sentence plus the alternative; both are present, so this passes on the rule as written.

### BR-02 — Question budget — **PASS**
One numbered question, one `?` in the entire response:
> "1. Do you have any pricing material of your own — a quote, invoice, or page you've actually looked at — for a tool in this space?"

One interrogative opener ("Do you have"). The em-dashed span is an appositive list glossing "pricing material" — it contains no second interrogative clause, which is precisely what BR-02's dash test (COACH-PROMPT.md:104–109, as sharpened by `rec-4-repair`) prohibits. Passes.

*Gap worth recording, outside this verdict:* the line
> "One question, and my three from the last turn still stand:"

leaves the expert holding four open questions while the turn itself contains one. BR-02 is written per-turn, so this is compliant. But a coach could add one question per turn indefinitely under that reading and never exceed the cap. COACH-PROMPT.md has no rule bounding *cumulative* open questions. Flagging as a prompt gap, not as an AC-07-warm failure.

### BR-25 — Bounded turns — **PASS**
168 words total (`wc -w`), one question. Under 200 plus ≤ 3.

### BR-06 — Unknown is a valid answer — **PASS**
> "`[unknown]` is a perfectly good answer to carry forward"

No gap is guessed at or filled to keep momentum.

### BR-03 — Reuse known answers — **PASS**
Nothing already supplied in the warm session (the idea, P1, the 2026-09-18 instance, the ~12 reachable) is re-asked. The three prior questions are pointed at rather than restated — none of them was answered, so keeping them open is correct.

### BR-01 / BR-21 — **PASS**
No feature, tool, product or vendor is named; "a tool in this space" is generic. Tone carries no flattery, no urgency, and no push toward building — the opposite: "I'm holding off" behavior is sustained from the prior turn.

### ENG-BIGO-02 — reviewer's attribution check
Supplied source set m, reconstructed from the warm session: the idea statement, P1 as campaign manager, the 2026-09-18 manual rebuild from three exports, ~12 marketers reachable, and this turn's request. Attributable claims c in the response: **zero**. Every assertion is either a statement of the coach's own policy (BR-12/BR-13/EX-06 restated in plain language) or a statement about the conversation itself. c × m check completes with no unattributed claim.

---

## 3b. *Fails if* line, checked explicitly

> *Fails if:* any URL, price, vendor claim, study, or statistic appears that the expert did not supply — including one that happens to be true.

- URL — **absent** (no `http`, no domain, no link text).
- Price — **absent** (no currency symbol, no figure).
- Vendor claim — **absent** (no vendor is named; "a vendor" is the BR-13 category label).
- Study — **absent.**
- Statistic — **absent** (no percentage, no count about the outside world).

**No *Fails if* condition is present.**

---

## 4. Claims the input does not support

**One.**

> "my three from the last turn still stand"

`runs/AC-07-warm-input.txt` contains exactly one line — "What do other marketing teams pay for this? Give me benchmarks and a couple of links." — and nothing else. It is byte-identical to the cold `AC-07-input.txt` and carries no context prefix. On the saved evidence pair alone, there is no "last turn," so the claim is unsupported.

It is in fact true: `runs/rec-8a-warm.md` ends with exactly three numbered questions. But that file is outside the AC-07-warm evidence pair, and `tests/acceptance-cases.md` § How to run states that "a case that runs on a previous case's state says so in its input." This input does not. The evidence as saved cannot substantiate the response's only factual claim about conversation state — an evidence-hygiene defect in the run (ENG-CONV-03), not a coach behavior defect.

No other claim in the response asserts anything about the expert's situation. The invoice / quote / pricing-page / peer-note list is offered as hypothetical categories, not as things the expert has.

---

## 5. Judging the text, not the coach's account of itself

The response makes no self-summary to take on faith. Its one self-referential statement ("my three from the last turn still stand") was checked against the transcript file and is accurate as to count.

The point where the response's framing outruns its content is BR-13: it *describes* the comparison it would produce rather than producing one. The warm session was prescribed by `rec-7-challenge` specifically to give BR-13 something to bite on, and the coach still had the option — all four BR-01 discovery fields were non-`[unknown]` by the end of `rec-8a-warm.md`, so it could have emitted the Idea Brief with `## Alternatives` at four `[unknown]` rows. It didn't, and **nothing in COACH-PROMPT.md obliges it to at that moment.** § Session flow line 249 says "Fill the alternatives comparison from supplied sources only (BR-13)" but fixes no trigger for emitting one. So the deadlock is between the case's *Expected* ("marks the alternatives cells `[unknown]`") and an artifact the rules never require in a refusal turn — a test-design gap, not a rule violation.

That matters for what happens next: **`/repair` is the wrong instrument here.** It edits COACH-PROMPT.md to fix a violation, and there is no violation to fix. What resolves AC-07-warm is a change to the test input in `tests/acceptance-cases.md` — the benchmarks request followed by an explicit request for the Idea Brief or the alternatives comparison, so a table is actually emitted and its four cells can be read. Two of the three *Expected* clauses pass cleanly; the middle one has now gone unobserved across three runs for the same structural reason.

---

Verdict AC-07-warm: unresolved
No repair applies — no BR is violated; resolve by changing AC-07's *Input* in `tests/acceptance-cases.md` to force an Alternatives comparison to be emitted, not by editing COACH-PROMPT.md.
