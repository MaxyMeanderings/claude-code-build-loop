# Opens the BIT 404 demo: VS Code on the coach folder, then a Windows Terminal
# window with DECK / BUILDER / COACH tabs. Run via demo\start.cmd.
$coach  = Join-Path $env:USERPROFILE 'Desktop\bit-404-coach'
$slides = Join-Path $env:USERPROFILE 'Desktop\hackhers-2026\slides'

& code -g "$coach\COACH-PROMPT.md:151" "$coach\SPEC.md" "$coach\BUILD-BRIEF.md" "$coach\DEMO.md" "$coach\demo\room-input.txt"

wt -w 0 new-tab --title DECK -d "$slides" cmd /k "npm run dev:bit404" `; `
   new-tab --title BUILDER -d "$coach" cmd /k "claude" `; `
   new-tab --title COACH -d "$coach" cmd /k "claude"

Start-Sleep -Seconds 8
Start-Process 'http://localhost:3132/1'
