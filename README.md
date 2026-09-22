# Beyond Chat · Build with Claude Code

A thirty-minute session for the BIT Atlanta 404 Tech Summit, September 22, 2026, by Tyler Sztuka (SZD Labs, Claude Community Ambassador).

The point: stop chatting with Claude and start standing up systems and workflows for yourself. One worked example, built in Claude Code from a one-page brief, tested by a separate reviewer, repaired once, with every step's evidence left on disk. The example is a coach. The loop is what you take home.

- **Slides:** https://maxymeanderings.github.io/claude-code-build-loop/
- **The build:** [`coach/`](coach/)
- **Your turn:** [`YOUR-BRIEF.md`](YOUR-BRIEF.md)

## The loop

```
Brief → Spec → Approve → Implement → Challenge → Repair
```

Every step leaves a file or a response you can point at. That is the difference between a demo and evidence.

| Step | What you do | What exists afterwards |
|---|---|---|
| Brief | Write one page: who it helps, what it must do, what it must never do, what it produces, how you know it worked | `BUILD-BRIEF.md` |
| Spec | Ask Claude Code for numbered, observable requirements and acceptance cases. Nothing gets built yet. | `SPEC.md` |
| Approve | Read the contract. Say so. | recorded decisions in `SPEC.md` |
| Implement | Claude Code creates the files from the approved spec. You inspect what changed. | `COACH-PROMPT.md`, `templates/`, `tests/` |
| Challenge | A separate session judges a saved run against the spec, quoting the response text | `runs/AC-*-response.md` and a verdict |
| Repair | Change one rule, show before and after, rerun the failing case and one that passed | the edit, and new runs |

## What is in `coach/`

The worked example: a "should I build this?" coach for professional domain experts (a marketer is the archetype) who want to build or automate something for their own process. Its fourth output is the one-page Build Brief they would hand to Claude Code next.

| Path | What it is |
|---|---|
| `coach/BUILD-BRIEF.md` | The one-page brief. The only thing a human wrote. |
| `coach/BUILD-STEPS.md` | The exact prompts for each step of the loop. |
| `coach/SPEC.md` | The drafted contract: rules, exclusions, engineering requirements, 25 acceptance cases, recorded decisions. |
| `coach/COACH-PROMPT.md` | The coach. Every rule stated once. |
| `coach/templates/` | Four blank output forms. No rule text in them. |
| `coach/tests/acceptance-cases.md` | The run sheet. Cases you have not run are marked Not run, on purpose. |
| `coach/runs/` | Saved inputs and full responses, including the recorded run shown on the slides. See `coach/runs/README.md`. |
| `coach/.claude/commands/` | Three slash commands: `/coach`, `/challenge`, `/repair`. |
| `coach/DEMO.md` | How the live loop runs in two terminals. |

## Run it yourself

You need [Claude Code](https://code.claude.com/docs/en/quickstart) on any account.

```bash
git clone https://github.com/MaxyMeanderings/claude-code-build-loop.git
cd claude-code-build-loop/coach
claude
```

Then, in that session: `/coach`, paste an input from `demo/inputs.txt`, read the answer, and `save AC-07-mine`. In a second session in the same folder: `/challenge AC-07-mine`. Read the verdict. If it fails, `/repair` with the challenger's last two lines, then rerun.

To build your own thing instead of the coach, copy `YOUR-BRIEF.md` into an empty folder as `BUILD-BRIEF.md`, fill in the five lines, start Claude Code there, and follow `coach/BUILD-STEPS.md` from step 1. The six steps do not change.

## Slides

```bash
cd slides
npm ci
npm run dev
```

The published deck is the `gh-pages` branch, which holds the output of `npm run build`. To republish after editing `slides/slides.md`: build, then push the contents of `slides/dist` (plus an empty `.nojekyll`) to `gh-pages`. A ready-made GitHub Actions workflow sits in `slides/ci/deploy-slides.workflow.yml`; move it to `.github/workflows/` and set the repository's Pages source to GitHub Actions to publish on every push instead. The seven recorded-run frames in `slides/public/assets/bit-404/` were rendered from the saved transcripts in `coach/runs/` by `coach/demo/captures/render-frames.js`; the text on them is verbatim.

## Honesty notes

- The recorded run is a headless run of the real files on 2026-09-21. Frames are rendered from the saved transcripts, not pixel captures of a terminal.
- The challenger's third verdict was unresolved, not pass. That is on the slides on purpose: the acceptance case's own input never forces the alternatives table to appear, so the next fix belongs in the test, not the prompt.
- The copilot-versus-autopilot slide adapts a LinkedIn post by Chorouk Malmoum and is credited on the slide.

## License

MIT. Copy it.
