---
name: sourcing_agents_architecture
description: Candidate sourcing platform architecture with SEEK, LinkedIn Sales Nav, and X-ray scrapers
type: project
---

The `candidate-sourcing/` directory contains a Python-based candidate sourcing platform.

**Architecture:**
- `config/roles.yaml`: All active roles with briefs, keywords, must-haves, disqualifiers, sources
- `config/settings.yaml`: Global defaults (max_pages, scan_mode, dedup_days)
- `references/seek_prompt.md`: SEEK Talent Search prompt template (speed-scan mode)
- `references/linkedin_sales_nav_prompt.md`: LinkedIn Sales Navigator prompt template
- `references/xray_prompt.md`: Google X-ray boolean search string generator
- `scrapers/seek_talent.py`: SEEK scraper (uses `claude -p` subprocess)
- `scrapers/linkedin.py`: LinkedIn scrapers (Sales Nav + X-ray, both use `claude -p`)
- `main.py`: CLI entry point (`--role`, `--source`, `--dry-run`)

**How it works:**
1. Reads role config from `roles.yaml`
2. Fills placeholders in the prompt template
3. Either prints the prompt (dry-run) or passes it to `claude -p` for execution
4. Prompts are also copy/pasteable into Claude in Chrome for manual runs

**Why:** Paul needs to scan 100-300 profiles per role and get top 10 candidates fast.

**How to apply:** When Paul asks to source candidates, use the existing `roles.yaml` config and prompt templates. Run `--dry-run` first to verify the prompt looks correct.
