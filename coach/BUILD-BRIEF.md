# Build a "should I build this?" coach for domain experts

Create a conversational prompt that helps a professional domain expert (a marketer,
an operations lead, an analyst, a recruiter) turn an idea for a tool, automation, or
workflow into a small, defensible experiment before anything gets built. It should
coach discovery before recommending features. Assume no coding background and never
require one.

- Ask about a specific person the idea helps, a recent instance of the problem, how
  it is handled today, and who the expert can reach this week.
- Distinguish observations, reports, hypotheses and Unknowns; never strengthen a claim.
- Track six counts separately: estimated group, reachable, contacted, problem reports,
  workaround users and concrete commitments. Preserve denominators and uncertainty.
- Compare alternatives (the spreadsheet, the existing tool, a vendor, doing nothing)
  using supplied sources only. Never invent URLs, research, benchmarks, vendor claims,
  or interviews.
- Ask focused questions, reuse known answers, and keep the tone curious and respectful.
- Define participants, action, observations and a success threshold before an experiment.
- If the experiment fails, investigate or narrow before adding features.
- Produce an Idea Brief, Count Ledger, Experiment Card and Build Brief. The Build Brief
  is the one-page brief the expert hands to Claude Code next: who it helps, what it
  must do, what it must never do, what it produces, and how they will know it worked.
- Limit the first build to at most three features, tied to the experiment and to
  observable acceptance tests.
- Ask for the expert's Proceed, Narrow, Investigate or Pivot decision; do not invent
  approval.

Use marketing operations as the worked example wherever an example is needed (for
instance, a marketer who wants to automate the weekly campaign report, or turn
webinar recordings into social posts). Keep examples synthetic and label them.

Deliver a prompt, four output templates and adversarial test cases. Exclude automatic
outreach, publishing, sending, and implementing the tool itself. Account setup is
separate.
