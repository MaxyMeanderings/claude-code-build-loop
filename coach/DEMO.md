# DEMO — BIT Atlanta 404, Sept 22, 4:30 PM

> **Sept 21, late: the session is recorded, not live.** The deck now carries seven rendered frames of the actual run (slides 16, 17, 19, 21–24), text verbatim from `runs/`. This file is the optional live path and the fallback: the three slash commands still work in this folder, and the whole loop takes about six minutes if the room asks to see it for real. The frames were rendered from the saved transcripts by `demo/captures/render-frames.js` (run from `claude-code-build-loop/slides`).

The live beats are slides 10 through 24 of `claude-code-build-loop/slides/slides.md`. Everything below is one paste or one slash command. Three slash commands live in `.claude/commands/` and are the workflow you script for yourself, which is the point of the talk.

## Before the room (4:00 PM)

Run `demo\start.cmd`. It opens VS Code on this folder with `COACH-PROMPT.md` at line 151, `SPEC.md`, `BUILD-BRIEF.md` and this file, then a Windows Terminal window with three tabs:

| Tab | Folder | Running | Role |
|---|---|---|---|
| DECK | `claude-code-build-loop\slides` | `npm run dev` | slides on http://localhost:3132 |
| BUILDER | this folder | `claude` | spec, files, `/challenge`, `/repair` |
| COACH | this folder | `claude` | `/coach`, the live test, `save AC-<id>` |

Projector shows the DECK tab in the browser, fullscreen (`f` in Slidev). Alt-tab to VS Code or the terminal for the live beats. If `start.cmd` misbehaves, open the three tabs by hand with the same commands.

Hotspot on. Do not rely on venue wifi.

## Slide by slide

**Slides 1–7.** Deck only. Slide 5 says what is being built; say the thesis on slide 6. Say what is pre-baked and what is live.

**Slide 8 · the brief.** Alt-tab to VS Code, `BUILD-BRIEF.md`. Thirty seconds. Back to the deck.

**Slide 9 · what a conversation looks like.** Deck only. Say "recorded last night, not live."

**Slide 10 · ask for a spec before code.** VS Code, `SPEC.md`. Scroll section 4 (behavior requirements) and section 10 (the questions it asked before building). Say "drafted last night from this prompt."
Ask which requirement they would try to break, hands only. There is no room input on Sept 22 (no time); the live test at slide 15 uses `demo\paste.txt`.

**Slide 12 · approve.** Deck only. Read the approve prompt. Say the approval was given last night and the decisions are recorded in SPEC.md section 11.

**Slide 13 · files.** Terminal BUILDER tab, or VS Code explorer. Show the tree: `COACH-PROMPT.md`, `templates/` (four files, the last is the Build Brief), `tests/acceptance-cases.md`, `runs/`.

**Slide 14 · the rule.** VS Code, `COACH-PROMPT.md` line 151, BR-12. Read "even for something you believe to be true" aloud. Point at AC-07 in `tests/acceptance-cases.md` if there is time.

**Slide 15 · live test.** COACH tab. It is a fresh session. Type:

```
/coach
```

It reads the prompt and the four templates and says "Your move." Then paste TURN A from `demo\paste.txt` (warm start), answer its three questions with TURN B, then paste TURN C (the AC-07 input). Read the whole response aloud. Ask the room: pass, fail, or unresolved, against the *Fails if* line on the slide. Then type:

```
save AC-07
```

(the id matches the case sheet). It writes `runs/AC-07-input.txt` and `runs/AC-07-response.md` and prints the two paths. Claude Code asks permission for the write; approve it and say why that prompt exists.

**Slide 16 · challenger.** BUILDER tab, a separate session. Type:

```
/challenge AC-07
```

It reads the spec, the prompt, the case sheet, and the saved run, quotes the response text per requirement, and ends with a verdict line. Read the verdict. If it disagrees with the room, stay there for a minute.

**Slide 17 · repair, or a harder case.**
- If the verdict is fail: in BUILDER, `/repair <BR id> <paste the challenger's last two lines>`. It changes one rule and shows before and after. Then in COACH: `/clear`, `/coach`, rerun the same input, `save AC-07`. Then rerun one passing case (AC-13 is quick) the same way.
- If the verdict is pass or unresolved: say so. The BR-02 repair from the recorded run is **already applied** to `COACH-PROMPT.md` (lines 104–109), so a live `/repair BR-02` will report nothing to fix. The recorded fail and its repair are on deck slides 19 and 21; point there instead of re-running them.
- Never manufacture a failure. The recorded one is real and already on the slides.

**Slides 25–29.** Deck only.

## Desktop app path (Sept 22)

Same folder, same three commands plus two display helpers (`/show`, `/files`), run from the Claude desktop app (Code tab) instead of VS Code and the terminal tabs. This folder is not a git repo, so sessions share `runs/` directly; no worktrees.

**Before the room (4:00 PM)**

1. Deck in the browser at http://localhost:3132 (the `deck` launch config) or the published URL. `f` for fullscreen. Slide 1. Hotspot on.
2. Desktop app: New session on `C:/Users/Tyler/Desktop/bit-404-coach`. Name it COACH. Permission mode: default (ask), never bypass.
3. Second new session, same folder. Name it BUILDER. Put the two side by side.
4. No VS Code, no terminal. Files are shown from BUILDER with `/show <file>[:line]`, which opens the app's Files pane beside the conversation, and the tree with `/files`. (`demo/start.cmd` still opens the terminal tabs as the fallback.)
5. Rehearse in throwaway sessions: in one, `/coach`, expect the one line "Coach loaded from COACH-PROMPT.md and four templates. Your move." In BUILDER, `/show COACH-PROMPT.md:151` and confirm the Files pane opens at BR-12, then `/files`. Then open a fresh COACH session and leave it empty so the room sees the load happen.
6. Collapse the sidebar, zoom the text, check it reads from the back.

**On stage**

| Slide | Step | You do | Type | Expect |
|---|---|---|---|---|
| 1-7 | | Deck only. Slide 5 says what is being built; slide 6 the thesis; slide 7 the six steps. | | |
| 8 | 1 Brief | BUILDER. Thirty seconds on the brief. Ask: which line is hardest to test? | `/show BUILD-BRIEF.md` | Files pane, the brief |
| 9 | 1 Brief | Deck. Say "recorded last night, not live." | | |
| 10 | 2 Spec | BUILDER. Section 4 is the behavior requirements, section 10 the questions it asked before building. Ask which requirement they would try to break, hands only; no room input. | `/show SPEC.md:95` then `/show SPEC.md:597` | Files pane at each section |
| 11 | 2 Spec | Deck. Where the spec comes from: the brief, the Specify prompt with its engineering bar, the builder's eight questions. Name the five principles and how each landed. | | |
| 12 | 3 Approve | Deck, then BUILDER for the recorded approval and accepted defaults. | `/show SPEC.md:649` | Files pane, section 11 |
| 14 | 4 Implement | BUILDER. Point at `COACH-PROMPT.md`, `templates/` (four, last is the Build Brief), `tests/acceptance-cases.md`, `runs/`. | `/files` | the tree in a code block |
| 14 | 4 Implement | BUILDER. BR-12. Read "even for something you believe to be true." If there is time, the case it maps to. | `/show COACH-PROMPT.md:151` then `/show tests/acceptance-cases.md:116` | Files pane at BR-12, then AC-07 |
| 15 | 5 Test | COACH session, fresh. | `/coach` | "Your move." |
| 15 | 5 Test | Paste `demo/paste.txt` TURN A (warm start), answer its three questions with TURN B, then TURN C (AC-07). Read the response aloud. Room votes pass / fail / unresolved against the *Fails if* line. | turns A, B, C from `demo/paste.txt` | the coach's answer |
| 15 | 5 Test | Save the evidence. Approve the write prompt if it appears and say why it exists. | `save AC-07` | two paths under `runs/` |
| 16-17 | 5 Test | Recorded frames of the same beat, if you stay on the recorded path. | | |
| 18-19 | 5 Challenge | BUILDER session. Read the verdict aloud. If it disagrees with the room, stay there a minute. | `/challenge AC-07` | quotes per requirement, then a `Verdict AC-07:` line and the smallest repair |
| 20 | 6 Repair | If fail: BUILDER. It changes one rule, shows before and after, stops. | `/repair BR-xx` plus the challenger's last two lines | before / after |
| 20 | 6 Repair | Then COACH, new session, same input, save; then one passing case (AC-13 is quick); then BUILDER challenges again. | `/coach` ... `save AC-07` ... `/challenge AC-07` | repair holds or not |
| 21-24 | 6 Repair | If pass or unresolved: say so. The BR-02 repair is already applied (lines 104-109), so a live `/repair BR-02` reports nothing to fix. Point at the recorded fail and repair here instead. | | |
| 25-29 | | Deck only. | | |

Fresh conversation = new session, not `/clear`. Never manufacture a failure; the recorded one is real and on the slides. Do not improve a response before the room judges it.

## Fresh conversations

`/clear` in the COACH tab between independent cases. The challenger runs in BUILDER so the coach's context never leaks into the review.

## If Claude Code will not start

Fallbacks are plain text you paste into any Claude conversation, in order: `demo\load-coach.txt` (then the input), `demo\challenge.txt` (then paste the response), `demo\repair.txt`. Evidence from last night is already in `runs/AC-06-*`, `AC-07-*`, `AC-13-*`; slide 9 quotes AC-07. Say "recorded, headless, last night."

## Do not

- Do not say "proprietary." The repo is public and this folder is four files and a prompt.
- Do not improve a response before the room judges it.
