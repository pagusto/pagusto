---
name: terminal-title
description: "Automatically updates terminal window title to reflect the current Claude Code task. Helps developers manage multiple Claude Code terminals by providing clear, at-a-glance identification. Triggers on: terminal title, window title, rename terminal, set title, identify terminal, multiple terminals, terminal management."
argument-hint: "<task description for title>"
license: MIT
---

# terminal-title -- Terminal Window Title Skill

Automatically sets descriptive terminal window titles based on the task Claude is working on. Essential for developers running multiple Claude Code instances.

## Usage

When the user starts a new task or switches to a different high-level task, run the title script:

```bash
bash /home/user/pagusto/claude-config/skills/terminal-title/temp_extract/terminal-title/scripts/set_title.sh "Your Title Here"
```

### When to Trigger

- At the start of every new Claude Code session (after receiving the first user prompt)
- When switching to a substantially different task

### When NOT to Trigger

- Follow-up questions about the same task
- Small refinements to current work
- Debugging the same feature

### Title Format

Use the pattern: `[Action/Category]: [Specific Focus]` (max 40 characters)

**Good titles:**
- "API Integration: Auth Flow"
- "Fix: Login Bug"
- "DB Migration: Users Table"
- "Build: Dashboard UI"
- "Test: Payment Module"

The script automatically prefixes titles with the current directory name for project context.

### Examples

```bash
# User asks: "Help me debug the authentication flow"
bash scripts/set_title.sh "Debug: Auth API Flow"

# User asks: "Create a React dashboard component"
bash scripts/set_title.sh "Build: Dashboard UI"

# User asks: "Write tests for payment processing"
bash scripts/set_title.sh "Test: Payment Module"
```

## Detailed Reference

For complete trigger rules, formatting guidelines, and common mistakes:

```bash
cat /home/user/pagusto/claude-config/skills/terminal-title/temp_extract/terminal-title/SKILL.md
```

## Important

- This skill runs silently in the background -- no confirmation message needed
- The script uses ANSI escape sequences compatible with macOS Terminal, iTerm2, and most modern terminal emulators
- Users can set `CLAUDE_TITLE_PREFIX` environment variable for a custom prefix
