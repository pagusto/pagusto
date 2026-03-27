---
name: vibe-prospecting
description: B2B prospecting powered by Explorium's Vibe Prospecting MCP. Find companies, discover contacts, enrich data, and export lead lists using natural language — backed by 150M+ companies and 800M+ professionals from 50+ data sources.
---

# Vibe Prospecting

B2B intelligence and prospecting powered by [Vibe Prospecting](https://www.vibeprospecting.ai/) (by Explorium). Describe who you're looking for in natural language and get enriched company and contact data instantly.

## MCP Server Setup

Add the following to your Claude Code MCP configuration:

```json
{
  "mcpServers": {
    "vibeprospecting": {
      "type": "streamable-http",
      "url": "https://vibeprospecting.explorium.ai/mcp"
    }
  }
}
```

Authentication is handled via OAuth — on first use you'll be prompted to authorize in your browser.

## Available Tools

| Tool | Description |
|------|-------------|
| `autocomplete` | Autocomplete search queries for companies and prospects |
| `match-business` | Find companies by name, domain, industry, size, tech stack, location, or intent signals |
| `match-prospects` | Find contacts by job title, department, company, or location |
| `enrich-business` | Enrich companies with firmographics, technographics, funding, and events |
| `enrich-prospects` | Enrich contacts with verified emails, phone numbers, and professional details |
| `fetch-entities` | Retrieve full entity data from a dataset |
| `fetch-entities-statistics` | Get aggregate statistics on matched entities |
| `fetch-businesses-events` | Get recent business events (funding, hiring, product launches) |
| `fetch-prospects-events` | Get recent prospect activity and career events |
| `get-dataset` | Retrieve a previously created dataset |
| `estimate-cost` | Estimate credit cost before running a query |
| `export-to-csv` | Export results to CSV file |

## When to Use This Skill

- **Lead list building** — Find companies matching your ICP by industry, size, tech stack, location, or buying intent
- **Contact discovery** — Find decision-makers by title, department, or seniority
- **Account research** — Enrich company profiles with firmographics, technographics, and recent events
- **Meeting prep** — Get the latest business and contact insights before a call
- **Outreach personalization** — Gather context like recent posts, product changes, or industry trends
- **Recruiting** — Find candidates by skills, experience, and background

## Data Coverage

- **150M+ companies** worldwide
- **800M+ professionals** with verified contact info
- **50+ data sources** including firmographics, technographics, hiring trends, intent signals, and funding events
- Up to **1,000 entities per query** for bulk operations

## How It Works

Vibe Prospecting uses **lazy evaluation**:

1. **Sample first** — Shows 5-10 sample results immediately
2. **Review** — You inspect and refine the results
3. **Export on confirm** — Full dataset is only processed when you explicitly request export

This keeps costs low and lets you iterate quickly.

## Examples

### Find Companies

```
Find SaaS companies in the US with 50-200 employees that use Kubernetes and raised Series A in the last 12 months
```

### Find Decision Makers

```
Find VP of Engineering or CTO contacts at fintech companies in New York with 100+ employees
```

### Enrich a Company

```
Enrich acme.com — I need firmographics, tech stack, recent funding, and key contacts
```

### Meeting Prep

```
I have a meeting with the CEO of Stripe tomorrow. Get me the latest company info, recent events, and leadership team
```

### Export Leads

```
Export all matched companies to CSV with company name, domain, employee count, industry, and primary contact email
```

## Tips

- **Be specific** with your criteria for better matches
- **Use `estimate-cost`** before large queries to check credit usage
- **Start with samples** then refine before exporting the full dataset
- **Combine filters** — industry + size + tech stack + location for precise targeting

## Resources

- [Vibe Prospecting](https://www.vibeprospecting.ai/)
- [Developer Docs](https://developers.explorium.ai/mcp-docs/vibeprospecting)
- [GitHub - MCP Server](https://github.com/explorium-ai/vibeprospecting-mcp)
- Support: support@vibeprospecting.ai
