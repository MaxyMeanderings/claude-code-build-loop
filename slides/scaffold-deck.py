"""One-time scaffold: copy the coach build and assets into this repo and write the scrubbed deck.
Run from anywhere: python C:/Users/Tyler/Desktop/claude-code-build-loop/slides/scaffold-deck.py
Safe to re-run; it overwrites slides.md and the copied files.
"""
import json, os, re, shutil

S = "C:/Users/Tyler/Desktop/hackhers-2026/slides"
R = "C:/Users/Tyler/Desktop/claude-code-build-loop"
COACH_SRC = "C:/Users/Tyler/Desktop/bit-404-coach"
REPO = "https://github.com/MaxyMeanderings/claude-code-build-loop"
PAGES = "https://maxymeanderings.github.io/claude-code-build-loop/"

# --- copy the build and the assets ---
os.makedirs(f"{R}/coach", exist_ok=True)
os.makedirs(f"{R}/slides/public/assets/bit-404", exist_ok=True)
shutil.copytree(COACH_SRC, f"{R}/coach", dirs_exist_ok=True)
for a in ("tyler.jpeg", "claude-logo.svg", "copilot-autopilot-post.png"):
    shutil.copy(f"{S}/public/assets/{a}", f"{R}/slides/public/assets/{a}")
for a in os.listdir(f"{S}/public/assets/bit-404"):
    shutil.copy(f"{S}/public/assets/bit-404/{a}", f"{R}/slides/public/assets/bit-404/{a}")

# --- package.json with the same dependency versions ---
d = json.load(open(f"{S}/package.json", encoding="utf-8"))
pkg = {
    "name": "claude-code-build-loop-slides", "private": True,
    "scripts": {
        "dev": "slidev slides.md --port 3132",
        "build": "slidev build slides.md --base /claude-code-build-loop/ --router-mode hash",
        "export": "slidev export slides.md --output slides.pdf",
    },
    "dependencies": d["dependencies"],
}
with open(f"{R}/slides/package.json", "w", encoding="utf-8") as f:
    json.dump(pkg, f, indent=2); f.write("\n")

# --- the deck ---
s = open(f"{S}/bit-404.md", encoding="utf-8").read()

def rep(old, new, count=1):
    global s
    assert old in s, "missing: " + old[:80]
    s = s.replace(old, new, count)

rep("title: Build with AI. Own the evidence. · 30-minute cut", "title: Beyond Chat · Build with Claude Code")
rep("info: Beyond chat. How to stand up systems and workflows for yourself with Claude Code. Abridged from the HackHers 2026 workshop for the BIT Atlanta 404 Tech Summit. One worked example, one loop you take home.",
    "info: Beyond chat. How to stand up systems and workflows for yourself with Claude Code. One worked example, one loop you take home. BIT Atlanta 404 Tech Summit, Sept 22, 2026.")
s = s.replace('<div class="slide-number">HackHers · 30-minute cut', '<div class="slide-number">SZD Labs · Beyond chat')
rep('<div class="sponsor-note">Abridged from the HackHers 2026 workshop, built with Drew Schillinger</div>', '')
rep("It's an abridged version of a two-hour workshop we ran last week for software developers; the framing holds for any process.",
    "It's cut down from a two-hour hands-on build workshop; the framing holds for any process.")
rep("This workshop was built with Drew Schillinger for GSU HackHers 2026 and is cut to thirty minutes for this room.",
    "Runs hands-on workshops for teams and communities across Atlanta. This is a thirty-minute cut of a two-hour build workshop.")
rep('<div class="intro-linkedin"><a href="https://www.linkedin.com/in/tyler-sztuka-283937123/" target="_blank" rel="noopener noreferrer"><img src="/assets/qr-tyler.png" alt="QR code: Tyler on LinkedIn" /><span>Connect with Tyler<br />on LinkedIn ↗</span></a></div>',
    '<div class="intro-linkedin"><a href="https://www.linkedin.com/in/tyler-sztuka-283937123/" target="_blank" rel="noopener noreferrer">linkedin.com/in/tyler-sztuka-283937123 ↗</a></div>')
rep('<div class="source"><a href="https://szdlabs.io/">Tyler: SZD Labs</a> · Co-author: <a href="https://www.linkedin.com/in/andrew-schillinger/" target="_blank" rel="noopener noreferrer">Drew Schillinger</a> · <a href="https://github.com/doctor-ew/hackhers-2026" target="_blank" rel="noopener noreferrer">workshop repository</a></div>',
    f'<div class="source"><a href="https://szdlabs.io/">szdlabs.io</a> · <a href="{REPO}" target="_blank" rel="noopener noreferrer">github.com/MaxyMeanderings/claude-code-build-loop</a></div>')
rep("Name the ambassador bias out loud. Credit Drew by name; the repo is his.", "Name the ambassador bias out loud.")
rep('<WorkshopLinks />\n\n<div class="source">Scan now. The full 90-minute deck, the starter kit, and the build steps live here. You will want them at 5:01.</div>',
    '<Links />\n\n<div class="source">Type either one now. The build and these slides live there. You will want them at 5:01.</div>')
rep("Say plainly that the whole run is recorded: the spec and the implementation were built last night in my own folder from the same starter kit you can download,",
    "Say plainly that the whole run is recorded: the spec and the implementation were built last night in my own folder from the brief and the build steps that are in the repo,")
rep('<div class="source">My BUILD-BRIEF.md, Sept 21 · re-aimed from the HackHers starter brief, same shape, same rules</div>',
    '<div class="source">My BUILD-BRIEF.md, Sept 21 · coach/BUILD-BRIEF.md in the repo</div>')
rep("The original was written for student hackathon teams; this one is the same rules aimed at a marketer deciding whether to automate the weekly campaign report.",
    "It is aimed at a marketer deciding whether to automate the weekly campaign report.")
rep('<p class="checkpoint-help">The full Specify prompt, with the engineering requirements, is in <a href="https://github.com/doctor-ew/hackhers-2026/blob/main/starter/BUILD-STEPS.md" target="_blank">starter/BUILD-STEPS.md ↗</a>.</p>',
    f'<p class="checkpoint-help">The full Specify prompt, with the engineering requirements, is in <a href="{REPO}/blob/main/coach/BUILD-STEPS.md" target="_blank">coach/BUILD-STEPS.md ↗</a>.</p>')
rep('<div class="source">starter/BUILD-STEPS.md · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/docs/AGENT-SPEC.md#L23">docs/AGENT-SPEC.md:23</a></div>',
    '<div class="source">coach/BUILD-STEPS.md § 2 · coach/SPEC.md</div>')
rep('<div class="source">starter/BUILD-STEPS.md</div>\n\n<!--\nA prompt approval', '<div class="source">coach/BUILD-STEPS.md § 3</div>\n\n<!--\nA prompt approval')
rep('<div class="source"><a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/README.md">coach/README.md</a></div>',
    '<div class="source">coach/ in the repo · every file shown is there</div>')
rep(' · Reference coach’s version: <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md#L16">coach/PROMPT.md:16</a></div>', '</div>')
rep('<div class="source">starter/BUILD-STEPS.md</div>\n\n<!--\nAdversarial review', '<div class="source">coach/BUILD-STEPS.md § 6 · .claude/commands/challenge.md</div>\n\n<!--\nAdversarial review')
rep('<div class="source">starter/BUILD-STEPS.md · <a href="https://github.com/doctor-ew/hackhers-2026/blob/reference/completed-coach/coach/PROMPT.md#L14">coach/PROMPT.md:14</a></div>',
    '<div class="source">coach/BUILD-STEPS.md § 7 · .claude/commands/repair.md</div>')

# slide "Run the full loop tonight": replace the two-column link block
i = s.index("# Run the full loop tonight.")
j = s.index('<div class="takeaway">Any Claude Code account works.', i)
block = (f'\n\n<div class="two"><section><h3>Build your own</h3><p><a href="{REPO}" target="_blank">Clone the repo ↗</a></p>'
         f'<p><a href="{REPO}/blob/main/coach/BUILD-STEPS.md" target="_blank">Follow coach/BUILD-STEPS.md ↗</a></p>'
         f'<p><a href="{REPO}/blob/main/YOUR-BRIEF.md" target="_blank">Start from YOUR-BRIEF.md ↗</a></p>'
         f'<p>Save your spec, prompt, templates, test cases, and actual responses.</p></section>'
         f'<section><h3>Compare and continue</h3><p><a href="{REPO}/blob/main/coach/COACH-PROMPT.md" target="_blank">My coach prompt ↗</a></p>'
         f'<p><a href="{REPO}/tree/main/coach/runs" target="_blank">The recorded runs ↗</a></p>'
         f'<p><a href="{PAGES}" target="_blank">These slides ↗</a></p></section></div>')
s = s[: i + len("# Run the full loop tonight.")] + block + s[j:]
rep('<div class="source">starter/BUILD-BRIEF.md · starter/BUILD-STEPS.md</div>\n\n<!--\nNo sponsored credits',
    '<div class="source">github.com/MaxyMeanderings/claude-code-build-loop</div>\n\n<!--\nNo sponsored credits')
rep('<SpeakerLinks />\n\n<div class="source">Built with Drew Schillinger for HackHers 2026. Thanks for judging with us.</div>',
    '<div class="connect"><img class="speaker-photo" src="/assets/tyler.jpeg" alt="Tyler Sztuka" /><div><h3>Tyler Sztuka</h3><p>SZD Labs · Claude Community Ambassador</p>'
    '<p><a href="https://www.linkedin.com/in/tyler-sztuka-283937123/" target="_blank" rel="noopener noreferrer">linkedin.com/in/tyler-sztuka-283937123 ↗</a></p>'
    '<p><a href="https://szdlabs.io/" target="_blank" rel="noopener noreferrer">szdlabs.io ↗</a></p></div></div>\n\n'
    '<div class="source">Thanks for judging with me. Everything shown is in the repo. Copy it.</div>')
rep('<WorkshopLinks />\n\n<div class="source">Slides, starter, and source. Scan or click to return anytime.</div>',
    '<Links />\n\n<div class="source">Slides and source. Type it or click it.</div>')
s = s.replace("starter/BUILD-BRIEF.md · Workshop learning objectives", "coach/BUILD-BRIEF.md")

leftover = [l for l in s.splitlines() if re.search(r"hackhers|drew|doctor-ew|schillinger|starter/|qr-", l, re.I)]
open(f"{R}/slides/slides.md", "w", encoding="utf-8").write(s)
print("slides.md written; slides:", s.count("\n---\nclass:") + 1)
print("leftover references:", leftover if leftover else "none")
