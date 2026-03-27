---
name: seo-audit
description: Analyzes web pages and sites for SEO issues, checking meta tags, headings, content structure, keyword density, links, image alt text, schema markup, page speed factors, and mobile-friendliness. Outputs prioritized recommendations with severity levels.
---

# SEO Audit

## Overview

This skill performs a comprehensive SEO audit on a given web page URL or HTML file. It evaluates on-page SEO factors, technical SEO elements, content quality signals, and provides a prioritized list of actionable recommendations ranked by severity and potential impact on search rankings.

## When to Use This Skill

- When a client or stakeholder wants to understand why a page is not ranking well
- Before launching a new page or site to catch SEO issues early
- During periodic SEO health checks (monthly or quarterly)
- When migrating content to a new domain or CMS
- To benchmark a page against SEO best practices before a redesign
- When comparing your page against a competitor's page for the same target keyword

## How It Works

The audit inspects the following categories:

1. **Meta Tags** - Title tag length and keyword placement, meta description length and relevance, canonical tags, robots directives, Open Graph and Twitter Card tags
2. **Heading Structure** - H1 presence and uniqueness, heading hierarchy (H1 through H6), keyword usage in headings
3. **Content Quality** - Word count assessment, keyword density analysis, readability score estimation, thin content detection, duplicate content indicators
4. **Internal and External Links** - Broken link identification, anchor text optimization, internal linking depth, external link quality and nofollow usage, orphan page detection
5. **Image Optimization** - Alt text presence and quality, image file size concerns, lazy loading implementation, next-gen format usage (WebP, AVIF)
6. **Schema Markup** - Structured data presence and validity, recommended schema types for the page, JSON-LD vs microdata assessment
7. **Technical SEO** - URL structure and length, HTTPS usage, mobile-friendliness signals, Core Web Vitals indicators, page speed factors (render-blocking resources, compression, caching headers)
8. **Indexability** - Robots.txt compliance, sitemap presence, canonical consistency, hreflang for multilingual sites

## Instructions

### Input Requirements

Provide one of the following:
- A live URL to audit (e.g., `https://example.com/page`)
- Raw HTML content pasted or provided as a file
- Optionally, a target keyword or set of keywords to evaluate against

### Performing the Audit

1. **Fetch or receive the page content.** If given a URL, use web fetch to retrieve the HTML. If given an HTML file, read it directly.
2. **Parse the HTML** and extract all relevant elements: meta tags, headings, links, images, structured data, text content.
3. **Evaluate each SEO category** against current best practices (as of 2025-2026 standards).
4. **Score each finding** with a severity level:
   - **Critical** - Issues that severely harm rankings or prevent indexing (e.g., noindex on a page that should be indexed, missing title tag, blocked by robots.txt)
   - **High** - Issues with significant ranking impact (e.g., duplicate title tags, missing H1, very thin content, slow page speed)
   - **Medium** - Issues that affect ranking but are not urgent (e.g., missing alt text on some images, suboptimal meta description, weak internal linking)
   - **Low** - Minor improvements and nice-to-haves (e.g., Open Graph tags missing, schema markup could be enhanced, URL slightly long)

### Output Format

Structure the audit report as follows:

```
## SEO Audit Report: [Page Title or URL]

### Audit Summary
- Overall Score: [X/100]
- Critical Issues: [count]
- High Issues: [count]
- Medium Issues: [count]
- Low Issues: [count]

### Critical Issues
| # | Issue | Description | Recommendation |
|---|-------|-------------|----------------|
| 1 | ...   | ...         | ...            |

### High Priority Issues
| # | Issue | Description | Recommendation |
|---|-------|-------------|----------------|

### Medium Priority Issues
...

### Low Priority Issues
...

### Category Breakdown
| Category          | Status | Score |
|-------------------|--------|-------|
| Meta Tags         | ...    | X/10  |
| Heading Structure | ...    | X/10  |
| Content Quality   | ...    | X/10  |
| Links             | ...    | X/10  |
| Images            | ...    | X/10  |
| Schema Markup     | ...    | X/10  |
| Technical SEO     | ...    | X/10  |
| Indexability       | ...    | X/10  |

### Quick Wins
[List the top 3-5 easiest fixes with highest impact]

### Detailed Recommendations
[Expanded guidance for each critical and high issue]
```

### Best Practices

- Always check the page from both desktop and mobile user-agent perspectives when possible
- Compare title tag and meta description against SERP display limits (title: ~55-60 chars, description: ~155-160 chars)
- Flag keyword stuffing if density exceeds 2.5% for any single keyword
- Recommend a minimum word count of 300 for standard pages, 1000+ for pillar content
- Check for multiple H1 tags (there should be exactly one)
- Verify that the canonical URL matches the actual URL being served
- Look for redirect chains (more than one redirect hop)
- Flag mixed content issues (HTTP resources on HTTPS pages)
- Note any render-blocking JavaScript or CSS in the document head
- Check that the page has a logical, crawlable URL structure with hyphens separating words

### Example Usage

**Input:** "Audit https://example.com/blog/seo-tips-2026 for the keyword 'seo tips'"

**Output:** A full audit report following the format above, with specific findings tied to the provided URL and keyword, severity ratings, and actionable next steps.
