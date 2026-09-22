---
description: Print this folder's file tree for the room. Usage /files
allowed-tools: Glob, Bash(ls:*), Bash(find:*)
---
Print the file tree of this folder in a code block and nothing else. Include `COACH-PROMPT.md`, `SPEC.md`, `BUILD-BRIEF.md`, `templates/` with its four files, `tests/`, and `runs/` (list the run files by name). Exclude `.claude/`, `demo/captures/`, and `prompts/`. Two-space indentation, directories with a trailing slash. No commentary.
