---
name: Prospect Analysis Prompt (run after data files ready)
description: Full 6-step prospect analysis prompt to run after user confirms data files and answers 4 qualifying questions
type: project
---

**Sequence for tomorrow (2026-03-23):**
1. User answers which platforms they have data from (LinkedIn, Facebook, Instagram, Gmail)
2. If they don't have export files, walk them through exporting step by step
3. Once files are confirmed, run the prompt below

---

## The Prompt to Run

Ask these 4 questions ONE AT A TIME, waiting for full answer before next:

**Q1:** "What job titles or types of people represent your ideal prospect: the people who could actually hire you or buy from you? Be as specific as you like."

**Q2:** "What industries or types of companies do you want to target? And is there anything specific: a topic, challenge, or initiative: that would make someone extra interesting to you?"

**Q3:** "How would you describe your own communication voice? I'll write every outreach message to sound exactly like you: so describe how you actually talk. Are you formal or casual? Funny or straight? What do you never say?"

**Q4:** "What do you want to happen after someone reads your message: what's the ideal next step or call to action?"

## After all 4 answered, execute this analysis:

1. Read data file(s) — LinkedIn CSV, Facebook JSON, Instagram JSON, Gmail CSV, or combo — filter contacts matching Q1 criteria
2. Report: how many decision-makers found vs total contacts across all files
3. Research top 25 filtered results via public web search only — company size, AI/transformation signals, recent company news. No platform scraping.
4. Score each person out of 100:
   - Authority: 30pts
   - Scale: 20pts
   - Network: 25pts
   - Proximity to user's industry: 15pts
   - Warmth/email present: 10pts
5. For top 10 ranked: write 2-3 sentence personalized outreach message in user's voice — reference something real and specific about their company, end with user's stated CTA. Sound like a smart friend, not a vendor.
6. Ask one question about dashboard look (colors, feel, vibe) — then generate:
   - CSV with all ranked prospects
   - Custom-designed HTML dashboard with copy button on every outreach message
