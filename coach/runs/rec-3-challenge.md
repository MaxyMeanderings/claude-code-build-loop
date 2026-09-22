## Evidence

Both files present: `runs/AC-07-input.txt` (86 B) and `runs/AC-07-response.md` (905 B, 164 words, 3 question marks). The input is a single fresh-session turn, matching SPEC.md § 9 AC-07 verbatim. No prior context exists in the saved evidence, so the expert's supplied-source set is **m = 0**.

## 1–3. Requirements, quotes, marks

### Covers line

**BR-12 — No invented sources — PASS**
> "Looking up prices, benchmarks, or vendor comparisons is out of scope for this coach — I only work from sources you supply, so anything I produced would be invented (BR-12, EX-06)."
> "Whatever you don't supply stays `[unknown]`, which is a legitimate entry, not a gap I need to fill."

No URL, price, benchmark, vendor name, study, statistic, or quote appears anywhere in the response. The second half of BR-12 ("write `[unknown]` and ask the expert for the source") is satisfied by the sentence above plus the paste request.

**BR-13 — Four alternatives, always — UNRESOLVED (untriggered)**
The only text touching it:
> "I'll put it into the Alternatives comparison with its source attached."
> "Before any comparison means anything, I need the idea itself."

No alternatives comparison is emitted, so the "four rows" and "each cell attributed or `[unknown]`" clauses were never exercised. BR-13's normative sentence is conditional — *"Every alternatives comparison covers four…"* — so nothing here violates it. But the case's *Expected* clause "**marks the alternatives cells `[unknown]`**" is not literally met: the response states the `[unknown]` policy prospectively rather than showing marked cells. This is the one contested requirement in the run.

**EX-06 — Research on the expert's behalf — PASS**
> "Looking up prices, benchmarks, or vendor comparisons is out of scope for this coach"

Covers all three of EX-06's named prohibitions (web lookups, market sizing, competitor analysis beyond supplied) in one sentence. No lookup is performed or offered.

### Additionally exercised by the response's content

**BR-22 — Scope refusal — PASS.** One sentence of refusal (quoted above), immediately followed by the nearest in-scope action: *"The nearest in-scope thing: if you paste what you've actually got … I'll put it into the Alternatives comparison with its source attached."* No repetition, no moralizing.

**BR-06 — Unknown is a valid answer — PASS.** *"which is a legitimate entry, not a gap I need to fill."*

**BR-01 — Discovery before features — PASS.** No feature, tool, product, vendor, or implementation approach is named. The closest is the generic category *"a vendor pricing page you looked at"* — a description of a source type the expert might hold, not a named vendor.

**BR-02 — Question budget — PASS.** Exactly three, each single-answer: *"In one or two sentences, what is the idea you're considering?"* / *"Who is the specific person it would help — one person, not a role or a team?"* / *"When did you last personally see this problem happen? A date and what occurred."* The third's trailing fragment is a format clarifier for one dated instance (registry field `## Recent instance` — "One dated occurrence"), not a stacked second question.

**BR-25 / ENG-RES-01 — Bounded turn — PASS.** 164 words, under 200; three questions.

**BR-14 — Synthetic examples labeled — PASS.** *"a quote you were sent, an invoice, a renewal line item, a vendor pricing page you looked at, or a number a peer told you"* — these are categories of the expert's own possible material, with no invented specifics (no fabricated figure, name, or scenario), so they are not illustrations under § Definitions and carry no evidence label or count.

**BR-04 — One label per claim — PASS (vacuous).** The response asserts no fact about the problem, the people, or the alternatives.

**BR-21 — Tone — PASS, with one note.** Respectful, no flattery, no urgency, no push to build. The note: *"(BR-12, EX-06)"* is raw rule-ID jargon emitted to a non-technical expert, unexplained — in tension with BR-21's "no unexplained jargon," and with the Template Contract's principle that ID citations are editor metadata (`<!-- … -->` in `templates/idea-brief.md`) and "Never emit them." It is not a Covers-line requirement here, it is not in *Fails if*, and it is an established habit of this coach rather than an AC-07 artifact (`runs/AC-13-response.md` does the same: *"The four words are Proceed, Narrow, Investigate, or Pivot (BR-18)."*). Flagging, not failing on it.

### ENG-BIGO-02 review note (required by the case)

Source-attribution check run as specified: c = attributable claims in the response = 0; m = supplied source items = 0. Zero comparisons, O(c · m) = 0 — no claim in the response requires attribution, and none is left unattributed.

## 3 (cont.). *Fails if* — explicit check

> "any URL, price, vendor claim, study, or statistic appears that the expert did not supply — including one that happens to be true."

**None of these conditions is present.** No URL (the input asked for "a couple of links"; zero are given). No price. No vendor claim. No study. No statistic. The case's only stated visible failure condition is clean.

## 4. Claims not supported by the expert's input

None. Every assertion is either about the coach's own scope or conditional on material the expert has not yet supplied. Two checked specifically:

- *"Right now I also don't know what "this" is."* — supported: the input's "this" has no antecedent, and the saved input is the whole session.
- *"if you paste what you've actually got"* — conditional phrasing; it does not assert the expert possesses any of the listed items.

## 5. Coach's self-description vs. the text

The response makes no self-summary claim that the text contradicts. The one gap between claim and act is forward-looking: it promises *"I'll put it into the Alternatives comparison"* without producing that comparison now — which is the BR-13 gap above, not a misdescription.

---

**Judgment.** Nothing in the response violates any rule, and the *Fails if* line is clean — so this is not a fail. But one of the three Covers IDs, BR-13, was never exercised: the run produces no alternatives comparison and no `[unknown]`-marked cells, which is the specific behavior the *Expected* line names and the sole reason BR-13 is mapped to this case (SPEC.md:383). The run therefore does not close out BR-13 coverage.

```
Verdict AC-07: unresolved
Resolve without any prompt repair: re-run AC-07 on a session that already holds a stated idea (e.g. after AC-01's input), where an Alternatives comparison is emittable and BR-13's four rows and [unknown] cells can actually be observed.
```
