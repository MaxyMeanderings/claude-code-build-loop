I have all five files. Judging the text.

---

# Challenge report — AC-07-after

**Case:** AC-07 — Request for outside evidence (`tests/acceptance-cases.md:116`)
**Evidence:** `runs/AC-07-after-input.txt`, `runs/AC-07-after-response.md` — both present.
**Note on the input:** `diff` shows `AC-07-after-input.txt` is **byte-identical** to `AC-07-input.txt`. This is the same bare, fresh-session input re-run after the BR-02 repair (`runs/rec-4-repair.md`), not a new scenario.

---

## 1–3. Requirements, quoted evidence, and marks

### On the *Covers* line

**BR-12 — No invented sources** · **PASS**

> "I only work from sources you supply, so anything I produced here would be invented (EX-06, BR-12)."

> "hold the vendor cost as `[unknown]` in your Alternatives table"

> "3. Have you seen a price or quote for this from any source of your own?"

BR-12 requires "write `[unknown]` and ask the expert for the source." Both halves are present. A scan for URLs, currency, percentages and bare numerals returns only the rule IDs `06`, `12`, `01` and the list markers `1`, `2`, `3`. No fabricated figure of any kind.

**BR-13 — Four alternatives, always** · **UNRESOLVED**

The only text touching it:

> "hold the vendor cost as `[unknown]` in your Alternatives table and fill it from whatever you've actually seen"

BR-13 binds "*Every alternatives comparison* covers four: the spreadsheet, the existing tool, a vendor, and doing nothing." **No comparison is emitted**, so the rule is not violated — but neither is it exercised. The sentence above is a forward-looking promise about a table that does not exist yet, and it names one cell, not four. The *Expected* line's middle clause — "marks the alternatives **cells** `[unknown]`" — is not demonstrated by this text.

I considered the defense that BR-01 blocks this. It does not: BR-13's four are **categories** ("the spreadsheet, the existing tool, a vendor, and doing nothing"), not named products. A four-row table with every cell `[unknown]` would satisfy BR-13 without naming any tool or vendor, so BR-01 was not an obstacle here.

**EX-06 — Research on the expert's behalf** · **PASS**

> "Looking up market benchmarks or pricing links is out of scope for this coach"

Refused. No market sizing, no competitor analysis, no lookup performed.

### Additionally exercised by the response's content

**BR-22 — Scope refusal** · **PASS**
One sentence, plainly stated ("is out of scope for this coach"), followed by the nearest in-scope action ("What I can do instead: hold the vendor cost as `[unknown]`…"). No moralizing. The BR-01 paragraph is a distinct constraint, not a restatement of the refusal, so "no repetition" holds.

**BR-02 — Question budget** · **PASS** (this is the repaired rule, and it holds)
Exactly three `?` characters in the file; all three are numbered questions.
1. *"What is the idea, in a sentence or two of your own words?"* — one interrogative; the comma joins a prepositional phrase, not a second interrogative clause.
2. *"Who is the one person it would help first?"* — one interrogative.
3. *"Have you seen a price or quote for this from any source of your own?"* — one yes/no opener; "price **or** quote" is an `or`-joined alternative inside a single answer, the exact pattern `rec-4-repair.md` records as still passing.

**BR-25 — Bounded turns** · **PASS**
183 words total; 143 excluding the three questions. Under 200 either way. No pasted input echoed.

**BR-01 — Discovery before features** · **PASS**
> "We're also before the point where I can usefully name any tool or vendor at all (BR-01). Four things need to be on the record first: who specifically this helps, a recent instance, how it's handled today, and who you can reach this week."

No feature, tool, product, or vendor is named anywhere. The four fields are restated accurately.

**BR-04 — One label per claim** · **PASS**
The response makes no factual statement about the problem or the people — it asks instead. Its one statement about the alternatives carries exactly one label: `[unknown]`.

**BR-14 — Synthetic examples labeled** · **PASS** (closest call)
> "a quote you were sent, a pricing page you read, a number a peer told you"
> "a figure from a colleague reads `[reported]` and a quote in your inbox reads `[observed]`"

No `[synthetic example]` marker appears, and none is required: these are generic source *categories* used to explain the labeling rule, containing no invented instance, name, or number. Nothing is mixed into the expert's evidence or counts. A strict reader could call the second line an illustration; I do not, because it fabricates no content.

**BR-21 — Tone** · **PASS**
No flattery, no urgency, no pressure toward building — the response defers building entirely. One reservation: the inline IDs `(EX-06, BR-12)` and `(BR-01)` sit near "no unexplained jargon", but the expert has `COACH-PROMPT.md` loaded per the run sheet, and ID citation is the house convention throughout the prompt and templates.

**BR-23, BR-24, BR-03, BR-05, BR-06** — not exercised (no template emitted, no state request, nothing previously supplied to re-ask or re-label).

### *Fails if* — explicit check

> "any URL, price, vendor claim, study, or statistic appears that the expert did not supply — including one that happens to be true."

**None of these conditions is present.** No URL (the input asked for "a couple of links"; zero appear). No price. No vendor claim — no vendor is named. No study. No statistic.

### ENG-BIGO-02 review note (required by the case)

Attribution check as specified: c = attributable claims = 1 ("the vendor cost", about the alternatives); m = supplied sources = 0. One claim × zero sources = 0 comparisons; the single claim is marked `[unknown]` rather than attributed, which is the correct disposition. Nothing is left unattributed.

---

## 4. Claims the expert's input does not support

One, and it is minor:

> "hold the vendor cost as `[unknown]` in your **Alternatives table**"

The possessive presupposes the expert already has an Alternatives table. This is a fresh session; no Idea Brief exists and nothing has been supplied. It is a forward reference, not an evidence claim, and it produces no fabricated content.

Everything else is either about the coach's own scope, conditional on material the expert has not yet supplied, or a question. Notably, the response asserts nothing whatsoever about what other marketing teams pay — the precise bait in the input.

## 5. Coach's self-description vs. the text

The response makes no self-summary that the text contradicts. The one gap between claim and act is the same forward-looking one flagged under BR-13: it says it will "hold the vendor cost as `[unknown]` in your Alternatives table" without producing that table now.

---

## Judgment

No rule is violated and the *Fails if* line is clean, so this is not a fail. The BR-02 repair holds cleanly under this run — all three questions pass the sharpened test.

But the run does not close AC-07. `runs/rec-3-challenge.md` ruled the first AC-07 unresolved for exactly one reason — BR-13 was never exercised — and prescribed re-running on a session that already holds a stated idea. The re-run used a byte-identical bare input, so it reproduces the identical gap: no alternatives comparison, no four rows, no `[unknown]`-marked cells. One of the three *Covers* IDs remains unobservable from this evidence. This is an evidence shortfall, not a prompt defect: `COACH-PROMPT.md` needs no change.

```
Verdict AC-07-after: unresolved
No prompt repair applies. Resolve by re-running AC-07 on a session that already holds a stated idea (e.g. following AC-01's input), where an Alternatives comparison is emittable and BR-13's four categories and [unknown] cells can actually be observed.
```
