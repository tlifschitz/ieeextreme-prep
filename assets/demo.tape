# A real practice session with the tutor, recorded with VHS (https://github.com/charmbracelet/vhs).
# The tutor's thinking time is hidden (Hide / Wait / Show); everything on screen is a live session.
# Run from a fresh, trusted clone of the repository: vhs assets/demo.tape
Output assets/demo.gif
Set Shell zsh
Set FontSize 15
Set Width 1200
Set Height 820
Set Padding 20
Set TypingSpeed 45ms
Set Framerate 20

Hide
Type "unset AI_AGENT CLAUDECODE CLAUDE_CODE_ENTRYPOINT CLAUDE_CODE_SESSION_ID CLAUDE_CODE_CHILD_SESSION CLAUDE_CODE_SESSION_ATTENDED CLAUDE_CODE_EXECPATH CLAUDE_CODE_BRIDGE_SESSION_ID CLAUDE_CODE_MESSAGING_SOCKET CLAUDE_CODE_MESSAGING_TOKEN CLAUDE_PID CLAUDE_EFFORT && clear"
Enter
Show

Type "claude"
Sleep 500ms
Enter
Sleep 7s

Type "I want to practice Brick stacks"
Sleep 600ms
Enter
Sleep 3s
Hide
Wait+Screen@240s /(?m)to cycle\)\s*$/
Show
Sleep 7s

Type "I read it, but I'm stuck. Can I get a hint?"
Sleep 600ms
Enter
Sleep 3s
Hide
Wait+Screen@240s /(?m)to cycle\)\s*$/
Show
Sleep 7s

Type "Yes, go ahead"
Sleep 600ms
Enter
Sleep 3s
Hide
Wait+Screen@240s /(?m)to cycle\)\s*$/
Show
Sleep 8s

Type "Honestly, can you just show me the code?"
Sleep 600ms
Enter
Sleep 3s
Hide
Wait+Screen@240s /(?m)to cycle\)\s*$/
Show
Sleep 9s

# Learn mode: a topic instead of a problem, and curated reading first.
Type "/clear"
Sleep 600ms
Enter
Sleep 2s
Type "Now I want to learn the contribution technique. What should I read?"
Sleep 600ms
Enter
Sleep 3s
Hide
Wait+Screen@240s /(?m)to cycle\)\s*$/
Show
Sleep 12s
