---
name: analytics-reporter
description: Generates structured marketing analytics reports from provided data with KPIs, trends, actionable insights, period-over-period comparisons, anomaly detection, and support for weekly, monthly, and quarterly formats.
---

# Analytics Reporter

## Overview

This skill transforms raw marketing data into structured, insight-driven analytics reports. It calculates key performance metrics, identifies trends and anomalies, creates comparison tables, and delivers actionable recommendations. Reports are formatted for stakeholder presentation with clear executive summaries and detailed breakdowns.

## When to Use This Skill

- When preparing weekly, monthly, or quarterly marketing performance reports
- When a client or executive needs a summary of campaign performance
- When comparing performance across channels, campaigns, or time periods
- When raw data from ad platforms or analytics tools needs to be interpreted
- When identifying underperforming campaigns or channels that need optimization
- When building a narrative around marketing results for stakeholder meetings

## How It Works

The skill takes provided marketing data (metrics from ad platforms, Google Analytics, CRM data, or spreadsheets), calculates derived KPIs, performs period-over-period comparisons, flags anomalies and opportunities, and assembles everything into a structured report with executive summary, detailed metrics, and actionable next steps.

## Instructions

### Input Requirements

Provide any combination of the following data:

- **Ad platform data**: Impressions, clicks, spend, conversions, revenue by campaign/channel
- **Website analytics**: Sessions, users, pageviews, bounce rate, session duration, conversion events
- **Email metrics**: Sends, opens, clicks, unsubscribes, conversions
- **Social media metrics**: Followers, engagement, reach, impressions, link clicks
- **Revenue/CRM data**: Leads, MQLs, SQLs, customers, revenue, deal size
- **Time period**: Current period and comparison period (previous period, same period last year)
- **Report type**: Weekly, monthly, or quarterly

### Key Metrics Calculated

| Metric | Formula | Description |
|--------|---------|-------------|
| **ROAS** | Revenue / Ad Spend | Return on ad spend |
| **CPA** | Ad Spend / Conversions | Cost per acquisition |
| **CPM** | (Ad Spend / Impressions) * 1000 | Cost per thousand impressions |
| **CTR** | (Clicks / Impressions) * 100 | Click-through rate |
| **CPC** | Ad Spend / Clicks | Cost per click |
| **Conversion Rate** | (Conversions / Clicks) * 100 | Percentage of clicks that convert |
| **LTV** | Avg Revenue Per Customer * Avg Lifespan | Customer lifetime value |
| **CAC** | Total Marketing Spend / New Customers | Customer acquisition cost |
| **LTV:CAC Ratio** | LTV / CAC | Efficiency of customer acquisition |
| **Bounce Rate** | Single-page Sessions / Total Sessions * 100 | Percentage leaving without interaction |
| **Email Open Rate** | Opens / Delivered * 100 | Percentage of emails opened |
| **Email CTR** | Clicks / Delivered * 100 | Percentage of emails clicked |

### Report Structure

#### Weekly Report Format

```
## Weekly Marketing Report: [Date Range]

### Executive Summary
[2-3 sentences highlighting the most important takeaway from the week]

### Key Metrics at a Glance
| Metric | This Week | Last Week | Change | Trend |
|--------|-----------|-----------|--------|-------|
| Spend  | $X,XXX    | $X,XXX    | +X%    | [up/down/flat] |
| Revenue| $X,XXX    | $X,XXX    | +X%    | [up/down/flat] |
| ROAS   | X.Xx      | X.Xx      | +X%    | [up/down/flat] |
| CPA    | $XX.XX    | $XX.XX    | +X%    | [up/down/flat] |
| Leads  | XXX       | XXX       | +X%    | [up/down/flat] |

### Channel Performance
| Channel | Spend | Revenue | ROAS | CPA | Conv | Notes |
|---------|-------|---------|------|-----|------|-------|
| ...     | ...   | ...     | ...  | ... | ...  | ...   |

### Top Performing Campaigns
[Top 3-5 campaigns by primary KPI]

### Underperforming Areas
[Campaigns or channels below target with root cause analysis]

### Action Items
- [ ] [Specific optimization recommendation 1]
- [ ] [Specific optimization recommendation 2]
- [ ] [Specific optimization recommendation 3]
```

#### Monthly Report Format

Includes everything in the weekly format plus:
- Month-over-month and year-over-year comparisons
- Budget pacing (actual spend vs planned spend)
- Funnel analysis (impressions to clicks to leads to customers)
- Channel mix analysis (pie chart representation of spend and revenue by channel)
- Cohort trends across the month (weekly breakdown within the month)

#### Quarterly Report Format

Includes everything in the monthly format plus:
- Quarter-over-quarter and year-over-year comparisons
- Strategic recommendations for next quarter
- Budget reallocation suggestions based on performance
- Customer acquisition trends and LTV analysis
- Market/competitive context if provided

### Anomaly Detection

Flag any metric that shows:
- **Spike**: More than 2 standard deviations above the rolling average
- **Drop**: More than 2 standard deviations below the rolling average
- **Sudden trend change**: Direction reversal sustained for 3+ data points
- **Budget pacing issues**: Spend more than 10% over or under the expected pace

For each anomaly, provide:
1. What happened (the metric and magnitude of change)
2. When it started
3. Possible causes (campaign changes, market events, technical issues)
4. Recommended action

### Comparison Tables

When comparing periods or channels, always include:
- Absolute values for both periods
- Absolute change (delta)
- Percentage change
- A directional indicator (arrow or +/- symbol)
- Color-coding guidance: green for improvements, red for declines (relative to goals, not just direction -- e.g., CPA going down is green)

### Best Practices

- Always lead with the most important insight, not just data
- Frame metrics in context of goals and targets when available
- Distinguish between correlation and causation in trend analysis
- Include both leading indicators (clicks, CTR) and lagging indicators (revenue, LTV)
- Normalize comparisons when periods have different lengths (use daily averages)
- Account for seasonality when comparing year-over-year data
- Segment data by device, geography, and audience when meaningful differences exist
- Round metrics appropriately: percentages to 2 decimal places, currency to 2 decimal places, large numbers with commas
- Always specify the date range and timezone for the data
- Note any data gaps, tracking issues, or attribution model changes that may affect comparisons

### Example Usage

**Input:** "Create a monthly report for March 2026. Google Ads: $12,500 spend, 350,000 impressions, 8,400 clicks, 210 conversions, $52,000 revenue. Meta Ads: $8,200 spend, 580,000 impressions, 6,100 clicks, 145 conversions, $31,500 revenue. Email: 45,000 sent, 38% open rate, 4.2% CTR, 85 conversions. Compare to February 2026 data: [data]."

**Output:** A complete monthly marketing report with KPIs, channel comparison, trends, anomalies, and action items.
