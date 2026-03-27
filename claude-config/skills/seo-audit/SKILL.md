---
name: seo-audit
description: Analyzes web pages and sites for SEO issues, checking meta tags, headings, content structure, keyword density, links, image alt text, schema markup, page speed factors, and mobile-friendliness. Outputs prioritized recommendations with severity levels.
---

# SEO Audit

## Overview

This skill performs a comprehensive SEO audit on a web page or HTML file. It evaluates on-page SEO factors, technical SEO elements, content quality signals, and structural issues that affect search engine rankings. The audit produces a prioritized list of findings with severity levels (Critical, High, Medium, Low) and actionable recommendations.

## When to Use This Skill

- When a user provides a URL or HTML file and asks for an SEO review
- When someone wants to understand why a page is not ranking well
- When preparing a page for launch and need to verify SEO readiness
- When conducting a competitive SEO analysis
- When migrating a site and need to ensure SEO parity

## How It Works

The audit examines the following categories:

1. **Meta Tags**: Title tag length and uniqueness, meta description quality, canonical tags, robots directives, Open Graph and Twitter Card tags
2. **Heading Structure**: H1 presence and uniqueness, heading hierarchy (H1-H6), keyword usage in headings
3. **Content Quality**: Word count, keyword density, readability, duplicate content signals, thin content detection
4. **Internal/External Links**: Link count, anchor text diversity, broken link indicators, nofollow usage, orphan page risk
5. **Image Optimization**: Alt text presence and quality, file size indicators, lazy loading, WebP/modern format usage
6. **Schema Markup**: Structured data presence, schema type validation, required property coverage
7. **Page Speed Factors**: Render-blocking resources, image compression, minification status, critical CSS, font loading
8. **Mobile-Friendliness**: Viewport meta tag, tap target sizes, font size readability, responsive design indicators
9. **URL Structure**: URL length, keyword presence, special characters, trailing slashes, HTTPS usage
10. **Indexability**: Robots.txt compliance, sitemap reference, canonical consistency, redirect chains

## Instructions

### Input Formats

Accept any of the following:
- A URL (fetch and analyze the page)
- Raw HTML content pasted by the user
- A path to a local HTML file

### Audit Process

1. **Parse the page** and extract all relevant elements (meta tags, headings, links, images, scripts, stylesheets, structured data).

2. **Evaluate each SEO category** using these specific checks:

   **Title Tag**
   - Present: yes/no
   - Length: 50-60 characters ideal; flag if <30 or >60
   - Contains primary keyword: yes/no
   - Unique across site (if multiple pages provided)

   **Meta Description**
   - Present: yes/no
   - Length: 150-160 characters ideal; flag if <70 or >160
   - Contains call-to-action or compelling copy
   - Contains primary keyword

   **Headings**
   - Exactly one H1: flag if zero or multiple
   - H1 contains primary keyword
   - Logical hierarchy: no skipped levels (e.g., H1 -> H3 with no H2)
   - Headings are descriptive, not generic

   **Content**
   - Word count: flag if <300 words (thin content)
   - Keyword density: ideal 1-2%; flag if >3% (keyword stuffing) or 0%
   - Readability: estimate reading level, flag if too complex for target audience
   - Content uniqueness signals

   **Links**
   - Internal links present: flag if <2
   - External links to authoritative sources
   - All links have descriptive anchor text (flag "click here", "read more")
   - No excessive links (flag if >100 on a single page)

   **Images**
   - All images have alt attributes: list those missing
   - Alt text is descriptive (flag empty alt="" on non-decorative images)
   - Image file names are descriptive (flag random strings)

   **Schema Markup**
   - Structured data present: yes/no
   - Valid JSON-LD format preferred over microdata
   - Appropriate schema type for page content (Article, Product, FAQ, LocalBusiness, etc.)
   - Required properties populated

   **Technical**
   - Viewport meta tag present
   - HTTPS usage
   - Canonical tag present and self-referencing
   - Language attribute on HTML tag
   - Favicon present

3. **Score and prioritize findings** using severity levels:
   - **Critical**: Issues that actively prevent indexing or cause major ranking loss (missing title, noindex on important page, broken canonical)
   - **High**: Issues with significant ranking impact (missing H1, no meta description, thin content, missing alt text on key images)
   - **Medium**: Issues that affect optimization but are not blocking (suboptimal title length, missing schema, poor heading hierarchy)
   - **Low**: Minor improvements and best practices (image file names, Open Graph tags, minor link text improvements)

### Output Format

Structure the audit report as follows:

```
## SEO Audit Report: [Page Title or URL]

### Overall Score: [X/100]

### Summary
[2-3 sentence overview of the page's SEO health]

### Critical Issues (Fix Immediately)
- [ ] Issue description — **Impact**: explanation — **Fix**: specific recommendation

### High Priority Issues
- [ ] Issue description — **Impact**: explanation — **Fix**: specific recommendation

### Medium Priority Issues
- [ ] Issue description — **Impact**: explanation — **Fix**: specific recommendation

### Low Priority / Best Practices
- [ ] Issue description — **Fix**: specific recommendation

### Category Breakdown
| Category         | Status | Score |
|-----------------|--------|-------|
| Meta Tags        | ...    | X/10  |
| Headings         | ...    | X/10  |
| Content          | ...    | X/10  |
| Links            | ...    | X/10  |
| Images           | ...    | X/10  |
| Schema           | ...    | X/10  |
| Technical        | ...    | X/10  |
| Mobile           | ...    | X/10  |

### Detailed Findings
[Expanded analysis per category]
```

### Best Practices

- Always explain WHY an issue matters, not just what is wrong
- Provide specific, actionable fix instructions (e.g., "Change title from 'Home' to 'Affordable Running Shoes | BrandName' to include target keyword")
- If the user provides a target keyword, evaluate all elements against that keyword
- When auditing multiple pages, note site-wide patterns (e.g., all pages missing schema)
- Compare against current Google Search guidelines and core web vitals recommendations
- Flag any black-hat SEO techniques (hidden text, cloaking, keyword stuffing) as critical issues
- Consider search intent alignment: does the content match what a searcher would expect?
