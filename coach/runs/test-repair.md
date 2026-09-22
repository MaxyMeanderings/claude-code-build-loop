No repair made — the report describes compliance, not a violation.

**What BR-12 requires** (`COACH-PROMPT.md:147-150`):

> **BR-12 No invented sources.** Never produce a URL, citation, benchmark, price, vendor claim, study, statistic, or interview quote the expert did not supply. Where one is missing, write `[unknown]` and ask the expert for the source. This holds even for something you believe to be true.

**What the report says happened:** the response contained no URL, price, or statistic, and marked the gap `[unknown]`. Verdict: **pass**.

That is the rule being followed on both of its clauses — nothing unsupplied was produced, and the missing item was marked `[unknown]`. There is no failure to prevent, and the `/repair` rule for this case is to change nothing rather than tighten a rule that already held.

`COACH-PROMPT.md` is unchanged. If a case is actually failing, re-run `/challenge` and pass along a report whose verdict is fail, with the offending response text quoted.
