---
name: yt-research
description: "YouTube research skill. Scrapes YouTube metadata (titles, views, author, duration, URLs) based on a search query using yt-dlp. Use for competitive intel, market research, trend analysis, or any topic-based YouTube research. Triggers on: youtube research, yt research, find videos, trending videos, youtube search, video research."
argument-hint: "<search query> [--num-results N]"
license: MIT
---

# yt-research — YouTube Research Skill

Searches YouTube for videos on any topic and returns structured metadata
including titles, view counts, authors, durations, and URLs.

## Usage

When the user asks to research YouTube videos on a topic, run the Python script:

```bash
python3 /home/user/pagusto/claude-config/skills/yt-research/yt_research.py "<search query>" -n <number_of_results> --json
```

### Parameters
- `query` (required): The YouTube search query
- `-n` / `--num-results` (optional): Number of results to fetch (default: 25)
- `--json` (optional): Output as JSON for programmatic use

### Example

```bash
python3 /home/user/pagusto/claude-config/skills/yt-research/yt_research.py "AI agents 2026" -n 25 --json
```

### Output Format (JSON)

Each video object contains:
- `title`: Video title
- `url`: Full YouTube URL
- `author`: Channel/uploader name
- `views`: View count
- `duration`: Video length (MM:SS or HH:MM:SS)
- `upload_date`: Upload date (YYYYMMDD)
- `description`: First 200 chars of description

## Workflow

1. User provides a topic and optional result count
2. Run the script with the search query
3. Parse the JSON output
4. Present results in a formatted table or summary
5. The URLs can be passed to the `notebooklm` skill for deep analysis

## Important

- If the user does not specify a topic, **ask them what topic they want to research** before proceeding.
- Default to 25 results unless the user specifies otherwise.
