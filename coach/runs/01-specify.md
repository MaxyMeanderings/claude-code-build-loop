`SPEC.md` is drafted at `C:\Users\Tyler\Desktop\bit-404-coach\SPEC.md`. Nothing implemented.

**What's in it**

- **§2 File plan** — 8 files total: `COACH-PROMPT.md`, four `templates/*.md`, `tests/acceptance-cases.md`, evidence in the existing `runs/`. No app, database, class hierarchy, or config.
- **§3 Definitions** — evidence labels, the six counts C1–C6, the count invariants (C3 ≤ C2 ≤ C1; C4/C5/C6 ≤ C3), the four decisions. One authoritative home.
- **§4 Behavior requirements** — BR-01…BR-25, each written so a single transcript can be marked pass/fail.
- **§5 Exclusions** — EX-01…EX-08.
- **§6 Engineering requirements** — assessed per principle, below.
- **§7 Template Registry** — exact ordered headings per template; this is the contract the coach depends on.
- **§8 Traceability** — every requirement → planned file → acceptance case.
- **§9 Acceptance cases** — AC-01…AC-25, split normal / adversarial / boundary, each with input, expected behavior, and an explicit "Fails if".
- **§10 Open questions** — Q1–Q8, each with a stated default.

**Engineering calls worth your eye**

| Principle | Verdict |
|---|---|
| DRY | Applies — ENG-DRY-01/02/03; audit is AC-22 |
| SRP | Applies — behavior / format / evaluation in three separate homes (AC-24) |
| Open/closed | Applies in limited form — fifth template = one registry row + one file (AC-21) |
| Liskov | **Classical LSP N/A** (no type hierarchy). Applies only as template-file substitution against the registry contract (AC-20) |
| ISP | Applies — each template names its consumer; Build Brief carries no transcript (AC-25) |
| DIP | Applies in limited form — coach binds to registry headings, not template prose (AC-20 + grep) |
| ACID | **N/A** — no database, no transactions, and a prompt cannot guarantee them. Substitute is BR-11 whole-ledger restatement, explicitly labeled a presentation convention, not a guarantee (AC-19) |
| Big O | **N/A for model reasoning** — no complexity class assigned. Real analysis given for two deterministic review procedures: invariant check O(1) over n=6; source-attribution check O(c·m). Resource use is separate: ENG-RES-01 caps + AC-18 long-input test |
| Convention over configuration | Applies — SCREAMING-KEBAB at root / lower-kebab in folders, reusing `prompts/` and `runs/`; fixed headings, zero settings (AC-23) |

**Questions I'd rather you answer than guess** — all have defaults, so approving as-is is fine, but these three actually change the build:

1. **Q1 packaging** — separate template files means a test run loads five files. It's what makes the OCP/LSP/DIP checks real. A single self-contained prompt is easier to run but collapses those checks.
2. **Q3 outreach boundary** — I defaulted to "interview question lists yes, ready-to-send bulk copy no." If you want the coach to stay further back, say so.
3. **Q4 Experiment Card gate** — I defaulted to requiring C3 ≥ 1 and C4 ≥ 1 (at least one person contacted who reported the problem) before a card is emitted. That's a judgment call the brief doesn't settle.

Waiting for your explicit approval before building.

Unrelated: the claude.ai Stripe, claude.ai Vercel, and Supabase MCP servers need authorization before their tools work — Stripe and Vercel via your claude.ai connector settings, Supabase via `claude mcp` or `/mcp` in an interactive session. Not needed for this task.
