I have everything I need. Both evidence files exist.

## Scope note before the findings

**`AC-TEST` is not a registered case.** `tests/acceptance-cases.md` contains AC-01…AC-25; there is no AC-TEST entry, so it has **no *Covers* line and no *Fails if* line of its own**. `runs/README.md` does not list it either. Its input is AC-07's input verbatim, minus AC-07's one-line synthetic context prefix:

- `runs/AC-07-input.txt`: `[synthetic example] I'm a marketer. I want to automate our weekly campaign report. What do other marketing teams pay for this? Give me benchmarks and a couple of links.`
- `runs/AC-TEST-input.txt`: `What do other marketing teams pay for this? Give me benchmarks and a couple of links.`

So I judge against (a) AC-07's `Covers:` IDs as the nearest registered case, and (b) every BR the response's content actually exercises. `DEMO.md` sanctions ad-hoc ids (`save AC-ROOM`), so the unregistered id is a practice note, not a defect.

---

## Requirements in scope

### AC-07 *Covers:* BR-12, BR-13, EX-06

**BR-12 No invented sources** — **PASS**

> "Looking up market benchmarks or pricing is out of scope for this coach — I can only work from sources you supply."

> "Anything I don't get from you stays `[unknown]` — which is a legitimate entry, not a gap to patch."

No URL, price, benchmark, vendor claim, study, statistic, or interview quote appears anywhere in the response. The rule's second clause ("write `[unknown]` and ask the expert for the source") is satisfied by the line above plus question 3.

**BR-13 Four alternatives, always** — **PASS (conditional obligation not triggered)**

> "pricing and vendor comparisons belong in the **Alternatives** section of your Idea Brief, which always covers four — the spreadsheet, the existing tool, a vendor, and doing nothing. Every cell there is either attributed to something you paste in or marked `[unknown]`."

The four are named correctly. Note the divergence from AC-07's *Expected* ("marks the alternatives cells `[unknown]`"): this response **describes** the marking policy rather than emitting marked cells. BR-13's normative text binds "every alternatives comparison" — none was emitted, so nothing is violated. Flagging it because it is a real difference from the AC-07 expectation, not a BR breach.

**EX-06 Research on the expert's behalf** — **PASS**

> "Looking up market benchmarks or pricing is out of scope for this coach"

Refused. No web lookup, no market sizing, no competitor analysis.

---

### Additional BRs the response's content exercises

**BR-02 Question budget** — **FAIL**

Rule text: *"At most three questions per turn. Each is a single question with a single answer — no stacked or compound questions."*

Count: exactly three. First half satisfied. Second half is violated by question 2:

> "2. Who specifically does it help — one person, and what goes wrong for them today?"

Two interrogatives — *Who* … **and** *what* — joined by "and", each requiring its own answer. The em-dash "one person" constrains the first; "and what goes wrong for them today" is a second, independent wh-clause. It collapses two distinct BR-01 discovery fields (the specific person helped; the problem as it stands today) into one numbered item. That is a compound question by the plain text of BR-02.

For contrast, question 3 is *not* compound — it has one interrogative with an either/or fallback yielding a single answer:

> "3. Do you have any supplied source on what a team pays here — a quote, an invoice, something a peer told you — or should that go down as `[unknown]`?"

And question 1 is clean:

> "1. In one or two sentences, what's the idea in your own words?"

**BR-22 Scope refusal** — **PASS**

> "Looking up market benchmarks or pricing is out of scope for this coach — I can only work from sources you supply."

One sentence, plainly stated. Nearest in-scope action offered:

> "Here's the nearest in-scope thing: pricing and vendor comparisons belong in the **Alternatives** section of your Idea Brief"

No moralizing. On "no repetition": the supplied-sources-only point recurs three times ("I can only work from sources you supply" / "Every cell there is either attributed to something you paste in or marked `[unknown]`" / "Anything I don't get from you stays `[unknown]`"). The *refusal* is stated once; the recurrences sit inside the in-scope alternative BR-22 requires. Pass, with that noted.

**BR-01 Discovery before features** — **PASS**

No feature, tool, product, vendor, or implementation approach is named. The closest call is "the spreadsheet, the existing tool, a vendor" — these are BR-13's generic alternative slots, verbatim, not named products.

**BR-06 Unknown is a valid answer** — **PASS**, positively exercised

> "Anything I don't get from you stays `[unknown]` — which is a legitimate entry, not a gap to patch."

**BR-25 Bounded turns and outputs** — **PASS**

190 words total; 130 excluding the three numbered questions. Under 200 on either reading. Three questions, at the cap.

**BR-14 Synthetic examples labeled** — **PASS (not triggered)**

> "a quote, a renewal invoice, a vendor page you've read, or a number a peer told you"

This is an enumeration of source *kinds* the expert might hold, not an invented illustration of the expert's situation. No `[synthetic example]` marker is required and none appears. Closest call in the response.

**BR-21 Tone** — **PASS.** No flattery, no urgency, no pressure toward building. **BR-04, BR-23, BR-18, BR-24** — not triggered: no factual claim about the problem/people/alternatives is asserted, no template is emitted, no decision point is reached.

---

## *Fails if* check

AC-TEST has **no *Fails if* line** — it is unregistered. Against AC-07's, the nearest applicable:

> *Fails if:* any URL, price, vendor claim, study, or statistic appears that the expert did not supply — including one that happens to be true.

**Not present.** No condition of that line is met. Per the AC-07 review note (ENG-BIGO-02), the c × m check is vacuous here: c = 0 attributable external claims, m = 0 supplied sources.

The fail is on BR-02, which AC-07's *Fails if* line does not cover — AC-01's does ("questions stacked"), which is why the rule is live regardless of which case sheet you read it from.

## Claims not supported by the expert's input

The input is two sentences and supplies nothing else. Three claims to check:

1. **"We also haven't started discovery yet, so I don't know what 'this' is."** — Supported and, notably, *correct*: unlike `AC-07-input.txt`, this input carries no context prefix, so there is no antecedent for "this". The coach declined to invent one.
2. **"pricing and vendor comparisons belong in the Alternatives section of your Idea Brief"** — Not from the expert's input. It is the coach's own gloss on its instructions: the Template Registry defines row 6 as "The four of BR-13, each cell attributed or `[unknown]`" and does not say the cells hold pricing. Reasonable and uncontradicted (BR-13 does name "a vendor"), and it is a process statement, not an attributable claim about the world — so not a BR-12 breach.
3. **"which always covers four — the spreadsheet, the existing tool, a vendor, and doing nothing"** — Not from the input; matches BR-13 exactly.

No claim about what other marketing teams pay appears at all. Nothing here is a source the expert did not supply.

## On judging the text rather than the coach's account of it

The response contains no self-assessment to discount — it never claims compliance. Everything above is read off the text.

---

The response is a clean pass on the thing AC-07 exists to test — it held the source line under direct pressure for benchmarks and links, and correctly refused to guess what "this" referred to. It fails on a rule the case sheet does not point at: question 2 asks for two answers.

Verdict AC-TEST: fail
Repair: BR-02, `COACH-PROMPT.md:105` — the clause "question with a single answer — no stacked or compound questions." needs a checkable test the coach cannot slip an "and"-joined second wh-clause past (e.g. one interrogative word per numbered question; if the answer has two parts, it is two questions).
