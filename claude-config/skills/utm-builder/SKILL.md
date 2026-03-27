---
name: utm-builder
description: Generates UTM-tagged URLs for campaign tracking with consistent naming conventions, bulk generation for multi-channel campaigns, spreadsheet-friendly output, and URL validation.
---

# UTM Builder

## Overview

This skill generates properly formatted UTM-tagged URLs for marketing campaign tracking. It enforces consistent naming conventions, validates base URLs, supports bulk generation across multiple channels and campaigns, and outputs results in formats ready for spreadsheets or project management tools.

## When to Use This Skill

- When launching a new marketing campaign across multiple channels
- When setting up tracking for email newsletters or drip sequences
- When creating UTM-tagged links for social media posts
- When organizing paid media tracking across platforms
- When building a link tracking spreadsheet for a campaign plan
- When standardizing UTM conventions across a marketing team

## How It Works

The skill takes a base URL and campaign parameters, validates the URL, applies consistent formatting rules, appends UTM parameters, and returns the tagged URLs. For bulk requests, it generates a complete matrix of URLs across all specified channels, mediums, and content variants.

## Instructions

### UTM Parameter Reference

| Parameter       | Required | Description                                    | Example Values                                  |
|----------------|----------|------------------------------------------------|-------------------------------------------------|
| `utm_source`    | Yes      | The referrer or platform sending traffic       | google, facebook, linkedin, newsletter, twitter |
| `utm_medium`    | Yes      | The marketing medium or channel type           | cpc, social, email, display, affiliate, organic |
| `utm_campaign`  | Yes      | The campaign name or promotion identifier      | spring-sale-2026, product-launch, webinar-q1    |
| `utm_term`      | No       | Paid search keyword or targeting term          | project-management, best-crm-software           |
| `utm_content`   | No       | Differentiates similar content or links        | hero-banner, sidebar-cta, email-button-v2       |

### Naming Conventions

Always apply these formatting rules for consistency:

1. **Use lowercase only** - Never mix cases. Convert all values to lowercase.
2. **Use hyphens as separators** - Replace spaces and underscores with hyphens.
3. **No special characters** - Remove accents, ampersands, and other non-alphanumeric characters (except hyphens).
4. **Keep values concise** - Abbreviate where reasonable but maintain clarity.
5. **Use consistent source names** - Standardize platform names:
   - `facebook` (not fb, FB, Facebook)
   - `instagram` (not ig, IG, Insta)
   - `google` (not Google, goog)
   - `linkedin` (not LinkedIn, li)
   - `twitter` or `x` (pick one and be consistent)
   - `tiktok` (not TikTok, tt)
   - `youtube` (not YouTube, yt)
6. **Use consistent medium names** - Standardize medium types:
   - `cpc` for paid search
   - `paid-social` for paid social media
   - `organic-social` for unpaid social posts
   - `email` for email campaigns
   - `display` for display/banner ads
   - `affiliate` for affiliate links
   - `referral` for partner referrals
   - `video` for video ad placements

### Single URL Generation

**Input:** Provide the base URL and desired UTM parameters.

**Output:**
```
Base URL: https://example.com/landing-page
Tagged URL: https://example.com/landing-page?utm_source=facebook&utm_medium=paid-social&utm_campaign=spring-sale-2026&utm_content=carousel-ad-v1
```

### Bulk URL Generation

For multi-channel campaigns, provide the base URL(s) and the campaign details. The skill generates all necessary combinations.

**Output format (spreadsheet-friendly):**

```
| Base URL | Source | Medium | Campaign | Term | Content | Full Tagged URL |
|----------|--------|--------|----------|------|---------|-----------------|
| https://example.com/lp | google | cpc | spring-sale-2026 | project-tools | search-ad-v1 | https://example.com/lp?utm_source=google&utm_medium=cpc&utm_campaign=spring-sale-2026&utm_term=project-tools&utm_content=search-ad-v1 |
| https://example.com/lp | facebook | paid-social | spring-sale-2026 | | carousel-v1 | https://example.com/lp?utm_source=facebook&utm_medium=paid-social&utm_campaign=spring-sale-2026&utm_content=carousel-v1 |
| https://example.com/lp | linkedin | paid-social | spring-sale-2026 | | sponsored-post | https://example.com/lp?utm_source=linkedin&utm_medium=paid-social&utm_campaign=spring-sale-2026&utm_content=sponsored-post |
```

### URL Validation Rules

Before generating tagged URLs, validate the following:

1. **URL format** - Must start with `https://` or `http://`. Flag HTTP-only URLs with a warning.
2. **No existing UTM parameters** - If the base URL already contains UTM parameters, warn the user and strip them before applying new ones.
3. **No trailing slashes inconsistency** - Normalize trailing slashes (prefer no trailing slash unless it is a directory path).
4. **No fragments before parameters** - Ensure the `#fragment` comes after query parameters, not before.
5. **Proper encoding** - URL-encode any special characters in parameter values.
6. **No empty required fields** - utm_source, utm_medium, and utm_campaign must all be provided.

### Campaign Naming Suggestions

When the user does not provide a campaign name, suggest a structured format:

```
[initiative]-[descriptor]-[date-or-quarter]
```

Examples:
- `product-launch-march-2026`
- `webinar-ai-marketing-q1-2026`
- `black-friday-sale-2026`
- `brand-awareness-retargeting-q2`
- `email-nurture-trial-users`

### Best Practices

- Keep a master UTM tracking spreadsheet for the entire organization
- Never use UTMs on internal links (site-to-site navigation) as it breaks session attribution
- Use utm_content to differentiate A/B test variants of the same ad
- Use utm_term primarily for paid search keywords; for social, use utm_content instead
- Shorten tagged URLs with a branded link shortener (like Bitly or Rebrandly) for social media and print
- Document your naming conventions and share them with the team to prevent inconsistencies
- Review UTM data regularly in Google Analytics to catch typos or naming drift
- For email campaigns, use utm_content to identify which link in the email was clicked (e.g., `header-logo`, `cta-button`, `footer-link`)

### Example Usage

**Input:** "Generate UTM links for our Q2 product launch campaign. Base URL: https://acme.com/new-product. Channels: Google Search, Meta paid social, LinkedIn paid social, email newsletter, and organic Twitter posts. We have two ad variations for paid channels (v1 and v2)."

**Output:** A complete table with all URL combinations across the 5 channels, with v1/v2 content variants for paid channels, following all naming conventions.
