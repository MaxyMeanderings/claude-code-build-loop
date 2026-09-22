# Build your own coach

This folder is your workshop starting point. It contains a build brief and a
sequence of instructions. You create the specification and implementation.

## Start here

1. Open this folder in your editor and terminal.
2. Use the organizer’s Claude Code installation and API access instructions.
3. Run `claude --version`, then `claude` in this folder.
4. Ask: “Read BUILD-BRIEF.md. Summarize what we must build and questions to resolve.
   Do not implement yet.”
5. Follow [BUILD-STEPS.md](BUILD-STEPS.md) through specification, approval,
   implementation, testing, and repair.

[Workshop slides](https://doctor-ew.github.io/hackhers-2026/)
provide timed checkpoints. [Claude Code quickstart](https://code.claude.com/docs/en/quickstart)
provides installation help. Never put account keys in your project files.

## What you will create

- An approved SPEC.md with observable requirements and acceptance cases.
- Your coach prompt and four output templates.
- Test cases, exact inputs and responses, and pass/fail/unresolved decisions.
- Repairs and repeated checks where needed.

Let your builder propose implementation filenames. Open the actual files and
trace one requirement through its instruction and test evidence. Start a fresh
conversation to test the coach prompt you created. Mark tests you did not run
as Not run. Use synthetic practice data or anonymous participant labels.

## Ready to demonstrate

Show your partner what you built, which requirement it satisfies, the actual
result of a test, and what remains unresolved. A model-generated summary alone
is not evidence that the behavior works.
