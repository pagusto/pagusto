---
name: recruitment_session_2026_03_27
description: Full recruitment session summary — SEEK sourcing, dashboard, outreach emails, HVAC Solutions NQ pitch, pipeline plan
type: project
---

## Session Summary — 2026-03-27

### SEEK Talent Sourcing (18 of 30 CV credits used)

**4 active roles sourced, top 5 candidates per role (20 total):**

| Role | Location | Top Candidates |
|------|----------|----------------|
| **Aircon Service Tech** | Cairns & Far North QLD (5003) | Pierre-Louis Sejotte, Damon Plohl, Victor Pavese, Cale Fennell, Tendai Masumbanyika |
| **Contracts Administrator** | Brisbane (1004) | Fernando Miranda, Md Khairuzzaman, Jolene Mundl, Bree Bale, Alexey Davydov |
| **HVAC-R Installation Tech** | Gold Coast (1005) | Justin Zahra, Yi Sen Chen, Kiel Walkinshaw, Donavan Van Zyl, Alain Blignaut |
| **Refrigeration Mechanic** | Cairns (5003) | Jed Richards, Travis Calleja, Patrick Schandl, Jack Lister, Aidan Knight |

**SEEK Talent profile access states:**
- "Access profile" = not yet accessed (costs 200 credits)
- "Download profile" = already accessed
- "No CV and contact details" = cannot access
- Use Chrome MCP `find` tool to precisely locate buttons by candidate name

**SEEK location codes:** Gold Coast = 1005, Cairns = 5003, Brisbane = 1004, Sunshine Coast = 5002, Bundaberg = 5001

### Client Companies
- 102 total companies mapped across all roles
- ~40 HVAC-R Gold Coast companies from Google Maps + SEEK
- Sources: SEEK job ads, Google Maps, direct research

### Dashboard
- `src/dashboard/index.html` — Static HTML, dark theme, tabs per role
- DATA object at line 365 with all 20 candidates + all client companies
- Tabs: Overview, Aircon Tech, Contracts Admin, HVAC-R, Refrig Mechanic, All Clients

### Outreach Done
- **Harrison Mitchell email** (Cairns refrigeration opportunity) — Chris Voss "no-oriented" technique ("Would it be a bad idea to send you a few more details?")
- **Hot candidates blast template** for 2 Aircon Techs ready to go — for sending to employers

### HVAC Solutions NQ Research (Cairns)
- Website: hvacsolutionsnq.com.au — Family-owned, locally operated, owner Joel works alongside team
- Services: aircon, refrigeration, installs, electrical, solar
- Facebook: 450+ followers, 5-star reviews
- Commercial projects: Palm Cove Surf Club, Bentley Park College, working with AE Smith
- Phone pitch script created for calling candidates about switching to this company

### Pipeline Architecture (Approved, Not Yet Built)
Plan file: `.claude/plans/spicy-wishing-diffie.md`

**5 components:**
1. **Inbox Monitor** — Chrome MCP + Outlook Web (PAgusto@frontlineconstruction.com.au)
2. **CV Parser** — Extract phone/email from SEEK CV attachments
3. **Scoring Agent** — Score candidates vs roles.yaml
4. **Outreach Agent** — Email + SMS (Twilio, keys pending), confirm ALL before sending
5. **Orchestrator** — Ties it all together

**Key decisions:**
- Gmail MCP won't work for Outlook — use Chrome MCP + Outlook Web
- WhatsApp deferred for now
- No auto-send — Paul confirms every outreach
- Paul's corporate email: PAgusto@frontlineconstruction.com.au (Outlook/Exchange)
- SEEK sends CVs to Paul.Agusto@ExpressPros.com.AU (alias, same inbox)

### Pending for Monday
- [ ] Dashboard update: add "Accessed Profiles" tab with contact matrix
- [ ] Pipeline: Inbox Monitor (Chrome MCP + Outlook Web)
- [ ] Pipeline: CV Parser + Scoring Agent
- [ ] Pipeline: Outreach Agent (email templates + Twilio SMS)
- [ ] Implement Twilio SMS in `candidate-sourcing/outreach/sms_sender.py`
- [ ] HVAC Solutions NQ: deeper research (About/Services pages, Facebook reviews)

**Why:** Paul is building an autonomous recruitment pipeline to reduce manual work — scan inbox, parse CVs, score, and outreach with one confirmation click.

**How to apply:** On Monday, resume with pipeline implementation. Check the plan file for full architecture. 12 CV credits remain (of 30 max this round).
