---
name: notebooklm
description: "NotebookLM integration skill. Creates notebooks, uploads YouTube URLs and other sources, generates artifacts (infographics, audio podcasts, quizzes, flashcards, slide decks, mind maps), and chats with notebook sources for deep analysis. Triggers on: notebooklm, notebook, research analysis, create infographic, generate podcast, study guide, deep research."
argument-hint: "create <name> | add-sources <id> <urls...> | generate <id> <type> | download <id> <type> <path> | chat <id> <question>"
license: MIT
---

# notebooklm — NotebookLM Integration Skill

Connects Claude Code to Google's NotebookLM via the notebooklm-py library.
Create notebooks, add sources, generate deliverables, and run analysis.

## Prerequisites

- `notebooklm-py` must be installed: `pip install "notebooklm-py[browser]"`
- User must authenticate first by running `notebooklm login` in a **separate terminal**

## Usage

### Create a Notebook
```bash
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py create "Research Topic Name"
```
Returns `notebook_id` — save this for subsequent commands.

### Add YouTube URLs as Sources
```bash
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py add-sources <notebook_id> "https://youtube.com/watch?v=..." "https://youtube.com/watch?v=..."
```

### Generate Artifacts
```bash
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py generate <notebook_id> infographic
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py generate <notebook_id> audio --instructions "make it engaging"
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py generate <notebook_id> quiz
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py generate <notebook_id> flashcards
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py generate <notebook_id> slide-deck
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py generate <notebook_id> mind-map
```

Supported artifact types: `audio`, `infographic`, `quiz`, `flashcards`, `slide-deck`, `mind-map`

### Download Artifacts
```bash
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py download <notebook_id> infographic ./output.png
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py download <notebook_id> audio ./podcast.mp3
```

### Chat / Ask Questions
```bash
python3 /home/user/pagusto/claude-config/skills/notebooklm/notebooklm_skill.py chat <notebook_id> "What are the top findings across all sources?"
```

## You can also use the CLI directly

The `notebooklm` CLI is also available for quick operations:

```bash
notebooklm create "My Research"
notebooklm use <notebook_id>
notebooklm source add "https://youtube.com/watch?v=..."
notebooklm generate infographic --orientation portrait
notebooklm generate audio "make it engaging" --wait
notebooklm download infographic ./output.png
```

## Typical Research Pipeline Workflow

1. User provides a topic
2. Use `yt-research` skill to find videos on the topic
3. Create a NotebookLM notebook with `create`
4. Add the YouTube URLs with `add-sources`
5. Use `chat` to get analysis and top findings
6. Generate deliverables (infographic, podcast, quiz, etc.) with `generate`
7. Download the artifacts with `download`

## Important

- The user MUST run `notebooklm login` in a **separate terminal window** before using this skill.
- If authentication fails, remind the user to open a fresh terminal and run the login command.
- Google may rate-limit artifact generation. If it fails, wait 5 minutes and retry.
