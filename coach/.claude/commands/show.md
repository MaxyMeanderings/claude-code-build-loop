---
description: Open a file from this folder in the app's Files pane, optionally at a line. Usage /show COACH-PROMPT.md:151
allowed-tools: mcp__ccd_view__show_pane, Read, Glob
---
Open the file named in `$ARGUMENTS` for the room to read. If the argument ends in `:N`, that is the 1-based line to scroll to.

- In the Claude desktop app, call the show_pane tool with pane "file", the path, and the line. Then reply with one short line naming the file and line, nothing else.
- If no show_pane tool is available (terminal), print the file from that line, about forty lines, in a code block, and nothing else.
- Do not summarize, explain, or edit the file.
