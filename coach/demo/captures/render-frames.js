// Renders terminal-styled frames from saved Claude Code transcripts.
// Run from hackhers-2026/slides so playwright-chromium resolves:
//   NODE_PATH=C:/Users/Tyler/Desktop/hackhers-2026/slides/node_modules node ../../bit-404-coach/demo/captures/render-frames.js
// Each frame: the command that was typed, then verbatim response text (optionally cropped to a section).
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-chromium');

const COACH = 'C:/Users/Tyler/Desktop/bit-404-coach';
const OUT = 'C:/Users/Tyler/Desktop/hackhers-2026/slides/public/assets/bit-404';
const INP = "What do other marketing teams pay for this? Give me benchmarks and a couple of links.";

// start: begin at the first occurrence of this text. stop: end before this text. tail: keep the last N lines.
const frames = [
  { file: 'AC-TEST-response.md',      out: 'rec-1-coach.png',      tab: 'COACH',   cmd: `/coach ${INP}` },
  { file: 'test-coach.md',            out: 'rec-2-save.png',       tab: 'COACH',   cmd: 'save AC-TEST', tail: 2 },
  { file: 'test-challenge.md',        out: 'rec-3-challenge.png',  tab: 'BUILDER', cmd: '/challenge AC-TEST', start: 'The response is a clean pass' },
  { file: 'rec-4-repair.md',          out: 'rec-4-repair.png',     tab: 'BUILDER', cmd: '/repair BR-02 <the challenger’s last two lines>', start: '**Before**', stop: 'Notes on the test' },
  { file: 'rec-5-rerun.md',           out: 'rec-5-rerun.png',      tab: 'COACH',   cmd: `/coach ${INP}` },
  { file: 'rec-7-challenge.md',       out: 'rec-6-challenge.png',  tab: 'BUILDER', cmd: '/challenge AC-07-after', start: 'But the run does not close' },
  { file: 'rec-8d-challenge-warm.md', out: 'rec-7-unresolved.png', tab: 'BUILDER', cmd: '/challenge AC-07-warm', start: 'That matters for what happens next' },
];

const NL = String.fromCharCode(10);
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function html(tab, cmd, body) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  body{margin:0;background:#0b0b0f;font-family:"Cascadia Mono","Consolas","Source Code Pro",monospace}
  .win{width:1600px;background:#141416;color:#e6e6e6;border:1px solid #2a2a30;border-radius:10px;overflow:hidden}
  .bar{display:flex;align-items:center;gap:10px;padding:10px 14px;background:#1c1c20;border-bottom:1px solid #2a2a30;font-size:15px;color:#9a9aa3}
  .dot{width:12px;height:12px;border-radius:50%;background:#3a3a42}
  .tab{margin-left:8px;padding:4px 12px;border-radius:6px;background:#26262c;color:#d6d6dc}
  .tab.on{background:#362821;color:#f2b29a}
  .cwd{margin-left:auto;font-size:13px}
  .body{padding:22px 28px 26px;font-size:23px;line-height:1.42;white-space:pre-wrap;word-wrap:break-word}
  .prompt{color:#d97757;font-weight:700}
  .cmd{color:#f5f5f7}
  .resp{margin-top:18px;color:#e6e6e6}
  .foot{padding:8px 28px 14px;font-size:14px;color:#8a8a93;border-top:1px solid #2a2a30}
  </style></head><body><div class="win">
  <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>
    <span class="tab ${tab==='COACH'?'on':''}">COACH</span><span class="tab ${tab==='BUILDER'?'on':''}">BUILDER</span>
    <span class="cwd">C:\\Users\\Tyler\\Desktop\\bit-404-coach · Claude Code</span></div>
  <div class="body"><span class="prompt">&gt; </span><span class="cmd">${esc(cmd)}</span>
<div class="resp">${esc(body)}</div></div>
  <div class="foot">recorded 2026-09-21, headless run · text verbatim from runs/ · frame rendered from the saved transcript</div>
  </div></body></html>`;
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  // The bundled headless shell is not installed on this machine; use the local Chrome.
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 });
  for (const f of frames) {
    const src = path.join(COACH, 'runs', f.file);
    if (!fs.existsSync(src) || fs.statSync(src).size === 0) { console.log('skip (missing/empty)', f.file); continue; }
    let text = fs.readFileSync(src, 'utf8').split(String.fromCharCode(13)).join('').trim();
    // Strip the unrelated MCP-authorization footer the harness appends in print mode.
    text = text.replace(/\n+(Unrelated[^\n]*\n?)+$/, '').replace(/\n+Separately:[^\n]*$/, '').trim();
    if (f.start) { const i = text.indexOf(f.start); if (i > 0) text = '…' + NL + text.slice(i); }
    if (f.stop) { const j = text.indexOf(f.stop); if (j > 0) text = text.slice(0, j).trimEnd() + NL + '…'; }
    if (f.tail) { const lines = text.split(NL); if (lines.length > f.tail) text = '…' + NL + lines.slice(-f.tail).join(NL); }
    await page.setContent(html(f.tab, f.cmd, text));
    const el = await page.$('.win');
    await el.screenshot({ path: path.join(OUT, f.out) });
    console.log('wrote', f.out);
  }
  await browser.close();
})();
