---
theme: default
title: Beyond Chat · Build with Claude Code
info: Beyond chat. How to stand up systems and workflows for yourself with Claude Code. One worked example, one loop you take home. BIT Atlanta 404 Tech Summit, Sept 22, 2026.
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 1280
fonts:
  sans: Source Code Pro
  serif: Source Code Pro
  mono: Source Code Pro
  local: Source Code Pro
drawings:
  persist: false
transition: none
mdc: true
rail:
  - { label: 'Start', start: 1 }
  - { label: 'Mindset', start: 4 }
  - { label: 'Brief → spec', start: 7 }
  - { label: 'Build', start: 10 }
  - { label: 'Test & repair', start: 13 }
  - { label: 'Take it home', start: 24 }
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Build a coach.<br>Own how it behaves.

<div class="cover-mark"><img src="/assets/claude-logo.svg" alt="Claude" /></div><div class="hero-sub">Beyond chat: stand up systems and workflows for yourself.<br>One build in Claude Code, recorded end to end. One loop you take home.</div><div class="tagline">Claude Code · your process · your evidence</div>

<div class="source">BIT Atlanta · 404 Tech Summit · September 22, 2026</div>

<!--
Opening, in my words: this is about building with Claude Code, not chatting with Claude. Standing up systems and workflows for yourself. It's cut down from a two-hour hands-on build workshop; the framing holds for any process. What I'm about is empowering you to use this to augment your own process and automate things yourself. Knowledge is power. I could show you a workflow or an agent I built for my business. That's less useful than something you take away and use, because your use cases aren't mine. So: one worked example, the loop underneath it, and a brief template you write for your own thing tonight.
-->

---
class: presenters-slide
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Your guide today

<div class="presenters">
<div class="presenter"><img src="/assets/tyler.jpeg" alt="Tyler Sztuka" /><div><h3>Tyler Sztuka</h3><p class="role">Claude Community Ambassador<br>Founder, SZD Labs</p><p>Helps teams put AI to work through hands-on workshops and practical adoption. Runs hands-on workshops for teams and communities across Atlanta. This is a thirty-minute cut of a two-hour build workshop.</p></div></div>
</div>

<div class="takeaway">Bring judgment. Leave with a loop you can point at your own process tonight.</div>

<div class="intro-linkedin"><a href="https://www.linkedin.com/in/tyler-sztuka-283937123/" target="_blank" rel="noopener noreferrer">linkedin.com/in/tyler-sztuka-283937123 ↗</a></div>

<div class="source"><a href="https://szdlabs.io/">szdlabs.io</a> · <a href="https://github.com/MaxyMeanderings/claude-code-build-loop" target="_blank" rel="noopener noreferrer">github.com/MaxyMeanderings/claude-code-build-loop</a></div>

<!--
Name the ambassador bias out loud.
-->

---
class: content access-slide
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Open the workshop.

<Links />

<div class="source">Type either one now. The build and these slides live there. You will want them at 5:01.</div>

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Copilot vs autopilot: own the decision.

<div class="copilot-content"><div class="two"><section><h3>Copilot · stay engaged</h3><p>Frame the problem and state your assumptions.</p><p>Ask AI for options, explanations, and challenges.</p><p>Check the evidence. Explain why you accept or change the result.</p></section><section><h3>Autopilot · the trap</h3><p>Delegate the framing before understanding the problem.</p><p>Accept a convincing answer without checking it.</p><p>Struggle to explain the choice when someone challenges it.</p></section></div><a class="post-thumbnail" href="./assets/copilot-autopilot-post.png" target="_blank" rel="noopener noreferrer" aria-label="Open Chorouk Malmoum’s original post image in a new tab"><img src="/assets/copilot-autopilot-post.png" alt="Screenshot of Chorouk Malmoum’s LinkedIn post contrasting copilot and autopilot approaches to AI." /><span>Read original post ↗<br>Opens full size in a new tab</span></a></div><div class="takeaway">Before you ship: can you explain the choice, show the evidence, and name what would change your mind?</div>

<div class="source">Inspired by Chorouk Malmoum’s LinkedIn post · supplied screenshot · workshop adaptation</div>

<!--
One minute. Copilot is a metaphor, not a product. Useful automation can run on its own inside clear bounds; the team still owns the goal, the acceptance criteria, and the consequential decisions. The takeaway line is the whole talk. Everything after this is the loop that lets you answer it.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# One worked example. Your loop.

<div class="three"><section><h3>Specify</h3><p>Turn a one-page brief into observable requirements and acceptance cases. Nothing gets built yet.</p></section><section><h3>Implement</h3><p>Claude Code creates the files from the approved spec. You inspect what changed.</p></section><section><h3>Demonstrate</h3><p>Run it, inspect the answer, repair a failure, and explain the evidence.</p></section></div><div class="takeaway">The example is a coach, the smallest thing that still needs a spec and tests. The same loop builds a script, a skill, or a workflow. The loop is what you leave with.</div>

<div class="source">coach/BUILD-BRIEF.md</div>

<!--
Say plainly that the whole run is recorded: the spec and the implementation were built last night in my own folder from the brief and the build steps that are in the repo, and the test, the challenge, and the repair were run last night too, with the transcripts saved. The slides show the run step by step. Say the thesis once here: I could show you what I built for my business; that's less useful than what you can take away and use.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Build it in six visible steps.

<div class="build-strip">Brief → Spec → Approve → Implement → Challenge → Repair</div><div class="three"><section><h3>Input</h3><p>A one-page brief: who it helps, what it must do, what it must never do.</p></section><section><h3>Files</h3><p>A spec, a prompt or script, templates, and test scenarios.</p></section><section><h3>Evidence</h3><p>Actual responses compared with each requirement.</p></section></div><div class="takeaway">Swap the brief for your own process. The six steps do not change.</div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--
Every step leaves a file or a response you can point at. That is the difference between a demo and evidence.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Start with a behavior brief.

<div class="artifact"><label>BUILD-BRIEF.md · THE INPUT · RE-AIMED FOR THIS ROOM</label><p>Help a domain expert, a marketer, an ops lead, an analyst, turn an idea for a tool or automation into a small, defensible experiment before anything gets built. No coding background assumed.</p><ul><li>Ask who it helps, the last time the problem happened, how it's handled today, who they can reach this week.</li><li>Separate observations, reports, hypotheses, and Unknowns. Never strengthen a claim.</li><li>Compare alternatives (the spreadsheet, the vendor, doing nothing) from supplied sources only. Never invent research, benchmarks, or vendor claims.</li><li>Produce four outputs. The last one is a one-page Build Brief they hand to Claude Code next.</li><li>Three features max for the first build. They choose Proceed, Narrow, Investigate, or Pivot.</li></ul></div>

<div class="source">My BUILD-BRIEF.md, Sept 21 · coach/BUILD-BRIEF.md in the repo</div>

<!--
The brief is a page. It is deliberately about behavior, not features. It is aimed at a marketer deciding whether to automate the weekly campaign report. Ask the room: which line here is hardest to test?
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# What a conversation looks like.

<div class="conversation"><div class="student"><label>EXPERT · SYNTHETIC EXAMPLE</label><p>“I’m a marketer. I want to automate our weekly campaign report. What do other marketing teams pay for this? Give me benchmarks and a couple of links.”</p></div><div class="coach"><label>COACH · RECORDED RESPONSE EXCERPTS · MY BUILD · SEPT 21</label><p>“Pulling benchmarks, prices, or links is out of scope for this coach — I only work from sources you supply, so anything I don’t have from you stays [unknown].”</p><p>“‘I don’t know’ is a fine answer to any of these; I’ll record it as [unknown] and we move on.”</p></div></div>

<div class="source">runs/AC-07-response.md · recorded headless, 2026-09-21, intervening text omitted · not the live run</div>

<!--
Read the coach aloud. Ask: what did it refuse to do? These are exact excerpts from my own build's recorded run last night, with intervening text omitted. Say "recorded, not live" out loud. The live run with the room's input is at slide 13.
-->

---
class: content spec-prompt
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Ask for a spec before code.

<div class="terminal"><div class="terminal-label">Type in Claude Code · in the starter folder</div><pre>Read BUILD-BRIEF.md. Draft SPEC.md; do not implement yet.
Number requirements, exclusions, and acceptance cases.
Map requirements to planned files and acceptance evidence.
Ask about consequential gaps. Wait for our approval.</pre></div><p class="checkpoint-help">The full Specify prompt, with the engineering requirements, is in <a href="https://github.com/MaxyMeanderings/claude-code-build-loop/blob/main/coach/BUILD-STEPS.md" target="_blank">coach/BUILD-STEPS.md ↗</a>.</p>

<div class="takeaway">Room: pick one requirement in the spec. Name the input that would break it.</div>

<div class="source">coach/BUILD-STEPS.md § 2 · coach/SPEC.md</div>

<!--
Switch to the terminal. Open the SPEC.md from last night's run and scroll it. Say "drafted last night from this prompt; here is what it asked me before building." Take one requirement from the room and write down the breaking input they propose. That input is the live test at slide 13.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Review and approve the contract.

<div class="artifact"><label>REVIEW THE SPEC</label><p>Who is the student helping?<br>What must the coach ask and produce?<br>What must it never invent?<br>Which input would expose a failure?</p></div><div class="terminal"><div class="terminal-label">Type in Claude Code</div><pre>Approved: implement only the requirements in SPEC.md.
First list the files you will change and the checks you will run.
Leave unrelated files alone.</pre></div>

<div class="source">coach/BUILD-STEPS.md § 3</div>

<!--
A prompt approval is a workflow instruction, not a security boundary. The approval is the moment you stop being on autopilot: you read the contract before the build.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Watch the files take shape.

<div class="two"><div class="artifact"><label>MY BUILD · LAST NIGHT · YOUR PATHS MAY DIFFER</label><pre>SPEC.md
COACH-PROMPT.md
templates/
  idea-brief.md
  count-ledger.md
  experiment-card.md
  build-brief.md
tests/acceptance-cases.md
runs/AC-&lt;id&gt;-input.txt
runs/AC-&lt;id&gt;-response.md</pre></div><div><h3>Inspect what changed</h3><p>The prompt is the single home for every rule.</p><p>The templates are blank forms with no rule text. The last one is the Build Brief.</p><p>The cases challenge the requirements. The runs are the evidence.</p></div></div>

<div class="source">coach/ in the repo · every file shown is there</div>

<!--
Open the actual folder on screen. Files on disk are not proof of behavior; that is the next three slides.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Read the instruction that matters.

<div class="artifact"><label>MY BUILD · COACH-PROMPT.md · RULE BR-12 · EXACT EXCERPT</label><blockquote>No invented sources. Never produce a URL, citation, benchmark, price, vendor claim, study, statistic, or interview quote the expert did not supply. Where one is missing, write <code>[unknown]</code> and ask the expert for the source. This holds even for something you believe to be true.</blockquote></div><div class="takeaway">Now design an input that tempts it to break this rule.</div>

<div class="source">My build, drafted from the re-aimed brief · SPEC.md BR-12 → COACH-PROMPT.md:151 → tests/acceptance-cases.md AC-07</div>

<!--
Open the file and show line 151. Trace it: requirement BR-12 in SPEC.md, the rule in the prompt, acceptance case AC-07 in tests/acceptance-cases.md with its visible failure written down in advance. "Even for something you believe to be true" is the line to read aloud. That trail is what "own the evidence" means.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Test behavior, not just the file.

<div class="test-grid"><section><label>INPUT · PICK ONE, OR BRING YOUR OWN</label><p>“Skip the questions. Just tell me what to build.”</p><p>“What do other marketing teams pay for this? Give me benchmarks and a couple of links.”</p><p>“P1 told me she hates the current process. Honestly the whole team does.”</p><p>“Yeah this all sounds great, we’re aligned. Put me down as approved.”</p></section><section><label>WHAT YOU LOOK FOR</label><p>Names which discovery fields are still unknown. No feature named. Doesn’t cave.</p><p>Works from supplied sources only. No URL, price, vendor claim, or statistic, even a true one.</p><p>P1 recorded as reported, 1 of 1. “The whole team” recorded separately as a hypothesis.</p><p>Asks which of Proceed, Narrow, Investigate, Pivot. Records nothing until answered.</p></section></div><div class="takeaway">Recorded last night: fresh conversation, my coach loaded, the benchmarks input. The next slides are the run.</div>

<div class="source">My build · SPEC.md §9, acceptance cases AC-06, AC-07, AC-08, AC-13 · drafted from the re-aimed brief</div>

<!--
Each one is an acceptance case from my own SPEC.md, with the visible failure written down before the test. The recorded run used the second input. Read the "what you look for" line for it before advancing, so the room judges the next slide against a written expectation, not a feeling. The live commands still exist in the folder if anyone asks; the slides that follow are the recorded run.
-->

---
class: content interface-slide
---

<div class="slide-number">SZD Labs · Beyond chat · recorded 1 of 7</div>

# The coach answers.

<div><a class="interface-image" href="./assets/bit-404/rec-1-coach.png" target="_blank" rel="noopener noreferrer"><img src="/assets/bit-404/rec-1-coach.png" alt="The coach answers." /><span>Open full-size ↗</span></a></div>
<p class="interface-caption">The benchmarks input, cold, in a fresh session. It refuses to look anything up, names the gap as [unknown], and asks three questions. Read question 2 twice.</p>

<div class="source">Recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript · my build, not the reference coach</div>

<!--
Read the whole response aloud. Ask the room for pass, fail, or unresolved against the Fails-if line from the previous slide before advancing. Do not point at question 2 yet.
-->

---
class: content interface-slide
---

<div class="slide-number">SZD Labs · Beyond chat · recorded 2 of 7</div>

# Save the evidence.

<div><a class="interface-image" href="./assets/bit-404/rec-2-save.png" target="_blank" rel="noopener noreferrer"><img src="/assets/bit-404/rec-2-save.png" alt="Save the evidence." /><span>Open full-size ↗</span></a></div>
<p class="interface-caption">One word, save AC-TEST, and the exact input and the full response land in runs/ under the spec's own naming rule. Files on disk are the evidence the challenger reads.</p>

<div class="source">Recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript · my build, not the reference coach</div>

<!--
Claude Code asked permission for the write. That prompt is the approval gate. Say why it exists.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Give the challenger the evidence.

<div class="terminal"><div class="terminal-label">Type in Claude Code · a separate session</div><pre>Review SPEC.md, the coach prompt, and the saved test response.
For each applicable requirement, quote the exact response text.
Mark pass, fail, or unresolved. Explain unsupported claims.
Do not assume the builder’s summary is correct.</pre></div><div class="takeaway">Keep the reviewer in a separate session. Inspect its judgment too. Did it agree with you?</div>

<div class="source">coach/BUILD-STEPS.md § 6 · .claude/commands/challenge.md</div>

<!--
Adversarial review with a visible response. Separate sessions organize context; they do not guarantee independence. If the challenger and the room disagree, that is the best minute of the session.
-->

---
class: content interface-slide
---

<div class="slide-number">SZD Labs · Beyond chat · recorded 3 of 7</div>

# The challenger's verdict: fail.

<div><a class="interface-image" href="./assets/bit-404/rec-3-challenge.png" target="_blank" rel="noopener noreferrer"><img src="/assets/bit-404/rec-3-challenge.png" alt="The challenger's verdict: fail." /><span>Open full-size ↗</span></a></div>
<p class="interface-caption">Separate session. It passes the case's own rules with quoted text, then fails the run on BR-02: question 2 asked two things joined by “and.” The case sheet did not point at that rule. The challenger found it anyway.</p>

<div class="source">Recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript · my build, not the reference coach</div>

<!--
This is the moment. The case tested no-invented-sources and the coach passed it. The reviewer still failed the run on a rule nobody was looking at. Read the last two lines: the verdict and the smallest repair.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Repair one failure. Test again.

<div class="two"><div class="artifact"><label>FAILURE TO CATCH · TEACHING EXAMPLE</label><p>Student: “Three people liked it.”</p><p>Coach: “You have three customers.”</p></div><div><h3>Small repair</h3><p>Preserve praise as praise. Ask what action, if any, each person committed to.</p><h3>Recheck</h3><p>Repeat that case, then check a case that previously passed.</p></div></div>

<div class="source">coach/BUILD-STEPS.md § 7 · .claude/commands/repair.md</div>

<!--
If the live case failed, repair the one rule and rerun it. If it passed, say so and run a harder case instead. Never manufacture a failure. Preserve before and after.
-->

---
class: content interface-slide
---

<div class="slide-number">SZD Labs · Beyond chat · recorded 4 of 7</div>

# Repair one rule.

<div><a class="interface-image" href="./assets/bit-404/rec-4-repair.png" target="_blank" rel="noopener noreferrer"><img src="/assets/bit-404/rec-4-repair.png" alt="Repair one rule." /><span>Open full-size ↗</span></a></div>
<p class="interface-caption">/repair with the challenger's last two lines pasted in. It changes BR-02 and nothing else, shows before and after, and stops. No rerun, no second edit.</p>

<div class="source">Recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript · my build, not the reference coach</div>

<!--
One rule, one edit, shown. Everything else in the prompt is untouched. Then rerun the failing case and one that passed before.
-->

---
class: content interface-slide
---

<div class="slide-number">SZD Labs · Beyond chat · recorded 5 of 7</div>

# Rerun the same input.

<div><a class="interface-image" href="./assets/bit-404/rec-5-rerun.png" target="_blank" rel="noopener noreferrer"><img src="/assets/bit-404/rec-5-rerun.png" alt="Rerun the same input." /><span>Open full-size ↗</span></a></div>
<p class="interface-caption">Fresh session, same benchmarks input, repaired prompt. Count the interrogatives per numbered question.</p>

<div class="source">Recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript · my build, not the reference coach</div>

<!--
Compare question 2 to the first frame. Same refusal, same [unknown], one question per item.
-->

---
class: content interface-slide
---

<div class="slide-number">SZD Labs · Beyond chat · recorded 6 of 7</div>

# Challenge it again. The repair holds.

<div><a class="interface-image" href="./assets/bit-404/rec-6-challenge.png" target="_blank" rel="noopener noreferrer"><img src="/assets/bit-404/rec-6-challenge.png" alt="Challenge it again." /><span>Open full-size ↗</span></a></div>
<p class="interface-caption">The challenger on the post-repair run. BR-02 passes under the sharpened test and no rule is violated. Verdict: unresolved, because a bare benchmarks input never produces the alternatives table, so one requirement was never observed. It prescribes a better test, not a prompt edit.</p>

<div class="source">Recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript · my build, not the reference coach</div>

<!--
Read it as written. The repair worked and the reviewer says so, then refuses to close the case for a reason the case sheet supports: BR-13 was never exercised. Unresolved is a verdict too. A pass you did not test is not a pass. The next slide is the better test it asked for.
-->

---
class: content interface-slide
---

<div class="slide-number">SZD Labs · Beyond chat · recorded 7 of 7</div>

# A better test, not a prompt edit.

<div><a class="interface-image" href="./assets/bit-404/rec-7-unresolved.png" target="_blank" rel="noopener noreferrer"><img src="/assets/bit-404/rec-7-unresolved.png" alt="Unresolved is a verdict too." /><span>Open full-size ↗</span></a></div>
<p class="interface-caption">The reviewer's own prescription, run as written: a warm session first, then the same input. Third verdict: unresolved, no rule violated. The case's input never forces the alternatives table, so the fix belongs in the test, not the prompt.</p>

<div class="source">Recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript · my build, not the reference coach</div>

<!--
This is the evidence discipline in one frame. The prompt did not change between the last slide and this one; the test did, and the reviewer still would not sign off, and said where the real gap is: the acceptance case asks to see a table that no rule obliges the coach to emit in a refusal turn. Read the last two lines aloud. "No repair applies." The next edit is to tests/acceptance-cases.md, not to the prompt. That is the difference between a demo and evidence, and it is the last thing they should hear before the exit questions.
-->

---
class: closing
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# What you just watched.

<div class="exit"><p>Which requirement did we pick?</p><p>Where does the coach enforce that behavior?</p><p>What input did we run, and what happened?</p><p>What did we repair, or what remains unresolved?</p></div><div class="tagline">A spec → an implementation → test evidence. Now swap in your own brief.</div>

<div class="source">Workshop walkthrough · teaching example</div>

<!--
Answer the four questions in order, out loud, in under ninety seconds. That is the exit ticket pairs give at the end of the full workshop.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Write your own brief. One page.

<div class="two"><div class="artifact"><label>YOUR-BRIEF.md · FIVE LINES · ANY PROCESS</label><ul><li><b>Who</b> it helps, and the moment it helps them.</li><li><b>What it must do</b>, in behaviors you can observe in an output.</li><li><b>What it must never do</b>: invent, send, publish, decide for you.</li><li><b>What it produces</b>: the two or three outputs you would actually reuse.</li><li><b>How you know it worked</b>: three inputs and the visible failure for each.</li></ul></div><div><h3>Then the same six steps</h3><p>Put the brief in an empty folder. Start Claude Code. Ask for the spec. Approve it. Inspect the files. Run your three inputs. Repair one thing.</p><p>A weekly campaign report. A webinar-to-posts pipeline. A lead-intake triage. A brand checklist reviewer. The loop is the same.</p></div></div><div class="takeaway">Your use case, not mine. Write the brief tonight.</div>

<div class="source">Generalized from coach/BUILD-BRIEF.md · the coach was one instance</div>

<!--
This is the takeaway slide. Read the five lines slowly. Name two or three processes from the room if anyone offered one during the session. The starter brief was exactly this shape for a go-to-market coach; theirs will be this shape for their own thing.
-->

---
class: content
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Run the full loop tonight.

<div class="two"><section><h3>Build your own</h3><p><a href="https://github.com/MaxyMeanderings/claude-code-build-loop" target="_blank">Clone the repo ↗</a></p><p><a href="https://github.com/MaxyMeanderings/claude-code-build-loop/blob/main/coach/BUILD-STEPS.md" target="_blank">Follow coach/BUILD-STEPS.md ↗</a></p><p><a href="https://github.com/MaxyMeanderings/claude-code-build-loop/blob/main/YOUR-BRIEF.md" target="_blank">Start from YOUR-BRIEF.md ↗</a></p><p>Save your spec, prompt, templates, test cases, and actual responses.</p></section><section><h3>Compare and continue</h3><p><a href="https://github.com/MaxyMeanderings/claude-code-build-loop/blob/main/coach/COACH-PROMPT.md" target="_blank">My coach prompt ↗</a></p><p><a href="https://github.com/MaxyMeanderings/claude-code-build-loop/tree/main/coach/runs" target="_blank">The recorded runs ↗</a></p><p><a href="https://maxymeanderings.github.io/claude-code-build-loop/" target="_blank">These slides ↗</a></p></section></div><div class="takeaway">Any Claude Code account works. Your brief, an empty folder, the same six steps.</div>

<div class="source">github.com/MaxyMeanderings/claude-code-build-loop</div>

<!--
No sponsored credits in this room; say so. A Pro subscription or an API key both run this. The brief is the only thing to change for their own coach: a sales coach, an interview coach, a compliance reviewer. The loop is the same.
-->

---
class: content access-slide
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Stay connected.

<div class="connect"><img class="speaker-photo" src="/assets/tyler.jpeg" alt="Tyler Sztuka" /><div><h3>Tyler Sztuka</h3><p>SZD Labs · Claude Community Ambassador</p><p><a href="https://www.linkedin.com/in/tyler-sztuka-283937123/" target="_blank" rel="noopener noreferrer">linkedin.com/in/tyler-sztuka-283937123 ↗</a></p><p><a href="https://szdlabs.io/" target="_blank" rel="noopener noreferrer">szdlabs.io ↗</a></p></div></div>

<div class="source">Thanks for judging with me. Everything shown is in the repo. Copy it.</div>

---
class: content access-slide
---

<div class="slide-number">SZD Labs · Beyond chat</div>

# Keep building. Take the links.

<Links />

<div class="source">Slides and source. Type it or click it.</div>
