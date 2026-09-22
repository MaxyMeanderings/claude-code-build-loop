# DEMO — BIT Atlanta 404, Sept 22, 4:30 PM

> **Sept 21, late: the session is recorded, not live.** The deck now carries seven rendered frames of the actual run (slides 14, 15, 17, 19–22), text verbatim from `runs/`. This file is the optional live path and the fallback: the three slash commands still work in this folder, and the whole loop takes about six minutes if the room asks to see it for real. The frames were rendered from the saved transcripts by `demo/captures/render-frames.js` (run from `hackhers-2026/slides` with `NODE_PATH` pointed at its `node_modules`).

The live beats are slides 9 through 15 of `hackhers-2026/slides/bit-404.md`. Everything below is one paste or one slash command. Three slash commands live in `.claude/commands/` and are the workflow you script for yourself, which is the point of the talk.

## Before the room (4:00 PM)

Run `demo\start.cmd`. It opens VS Code on this folder with `COACH-PROMPT.md` at line 151, `SPEC.md`, `BUILD-BRIEF.md` and this file, then a Windows Terminal window with three tabs:

| Tab | Folder | Running | Role |
|---|---|---|---|
| DECK | `hackhers-2026\slides` | `npm run dev:bit404` | slides on http://localhost:3132 |
| BUILDER | this folder | `claude` | spec, files, `/challenge`, `/repair` |
| COACH | this folder | `claude` | `/coach`, the live test, `save AC-<id>` |

Projector shows the DECK tab in the browser, fullscreen (`f` in Slidev). Alt-tab to VS Code or the terminal for the live beats. If `start.cmd` misbehaves, open the three tabs by hand with the same commands.

Hotspot on. Do not rely on venue wifi.

## Slide by slide

**Slides 1–6.** Deck only. Say the thesis on slide 5. Say what is pre-baked and what is live.

**Slide 7 · the brief.** Alt-tab to VS Code, `BUILD-BRIEF.md`. Thirty seconds. Back to the deck.

**Slide 8 · what a conversation looks like.** Deck only. Say "recorded last night, not live."

**Slide 9 · ask for a spec before code.** VS Code, `SPEC.md`. Scroll section 4 (behavior requirements) and section 10 (the questions it asked before building). Say "drafted last night from this prompt."
Then: **"Pick a requirement. Name the input that would break it."** Type the room's input into `demo\room-input.txt` so it is on screen and saved. That is the live test at slide 13.

**Slide 10 · approve.** Deck only. Read the approve prompt. Say the approval was given last night and the decisions are recorded in SPEC.md section 11.

**Slide 11 · files.** Terminal BUILDER tab, or VS Code explorer. Show the tree: `COACH-PROMPT.md`, `templates/` (four files, the last is the Build Brief), `tests/acceptance-cases.md`, `runs/`.

**Slide 12 · the rule.** VS Code, `COACH-PROMPT.md` line 151, BR-12. Read "even for something you believe to be true" aloud. Point at AC-07 in `tests/acceptance-cases.md` if there is time.

**Slide 13 · live test.** COACH tab. It is a fresh session. Type:

```
/coach
```

It reads the prompt and the four templates and says "Your move." Then paste the room's input from `demo\room-input.txt`, or one of the four in `demo\inputs.txt`. Read the whole response aloud. Ask the room: pass, fail, or unresolved, against the *Fails if* line on the slide. Then type:

```
save AC-07
```

(or `save AC-ROOM` for the room's own input). It writes `runs/AC-07-input.txt` and `runs/AC-07-response.md` and prints the two paths. Claude Code asks permission for the write; approve it and say why that prompt exists.

**Slide 14 · challenger.** BUILDER tab, a separate session. Type:

```
/challenge AC-07
```

It reads the spec, the prompt, the case sheet, and the saved run, quotes the response text per requirement, and ends with a verdict line. Read the verdict. If it disagrees with the room, stay there for a minute.

**Slide 15 · repair, or a harder case.**
- If the verdict is fail: in BUILDER, `/repair <BR id> <paste the challenger's last two lines>`. It changes one rule and shows before and after. Then in COACH: `/clear`, `/coach`, rerun the same input, `save AC-07`. Then rerun one passing case (AC-13 is quick) the same way.
- If the verdict is pass or unresolved: say so. The BR-02 repair from the recorded run is **already applied** to `COACH-PROMPT.md` (lines 104–109), so a live `/repair BR-02` will report nothing to fix. The recorded fail and its repair are on deck slides 17 and 19; point there instead of re-running them.
- Never manufacture a failure. The recorded one is real and already on the slides.

**Slides 16–20.** Deck only.

## Fresh conversations

`/clear` in the COACH tab between independent cases. The challenger runs in BUILDER so the coach's context never leaks into the review.

## If Claude Code will not start

Fallbacks are plain text you paste into any Claude conversation, in order: `demo\load-coach.txt` (then the input), `demo\challenge.txt` (then paste the response), `demo\repair.txt`. Evidence from last night is already in `runs/AC-06-*`, `AC-07-*`, `AC-13-*`; slide 8 quotes AC-07. Say "recorded, headless, last night."

## Do not

- Do not say "proprietary." The repo is public and this folder is four files and a prompt.
- Do not present the reference coach on `reference/completed-coach` as this build.
- Do not improve a response before the room judges it.
