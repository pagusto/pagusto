---
name: roi-calculator
description: Calculates marketing ROI, ROAS, CPA, LTV, CAC and provides budget allocation recommendations with break-even analysis
---

# Marketing ROI Calculator

## Overview

This skill calculates key marketing performance metrics across campaigns and channels. It computes ROI, ROAS, CPA, LTV, and CAC, then projects future performance based on historical data. The output includes formatted comparison tables with actionable budget allocation recommendations.

## When to Use This Skill

- When evaluating the financial performance of marketing campaigns
- When comparing ROI across multiple channels (paid search, social, email, display, etc.)
- When deciding how to allocate or reallocate marketing budget
- When projecting future returns based on historical campaign data
- When performing break-even analysis on new campaigns or channels
- When calculating customer lifetime value relative to acquisition cost

## How It Works

1. Collect campaign data: spend, revenue, conversions, time period, and channel
2. Calculate core metrics for each campaign and channel
3. Compare performance across channels using normalized metrics
4. Project future ROI based on historical trends and stated assumptions
5. Run break-even analysis to determine minimum performance thresholds
6. Output formatted tables with clear recommendations

## Key Metrics and Formulas

- **ROI** = ((Revenue - Cost) / Cost) x 100
- **ROAS** = Revenue / Ad Spend
- **CPA** = Total Cost / Number of Conversions
- **LTV** = Average Purchase Value x Purchase Frequency x Customer Lifespan
- **CAC** = Total Sales & Marketing Cost / Number of New Customers Acquired
- **Break-even ROAS** = 1 / Profit Margin (as a decimal)

## Instructions

### Step 1: Gather Input Data

Ask the user for the following information per campaign or channel:

- Campaign/channel name
- Total spend (ad spend + associated costs)
- Revenue generated (or conversion value)
- Number of conversions or customers acquired
- Time period (start and end dates)
- Average order value (if available)
- Customer retention rate and repeat purchase data (for LTV)
- Profit margin on products/services (for break-even analysis)

If the user provides partial data, calculate what is possible and note which metrics require additional inputs.

### Step 2: Calculate Core Metrics

For each campaign or channel, compute:

| Metric | Formula | Good Benchmark |
|--------|---------|----------------|
| ROI | ((Revenue - Cost) / Cost) x 100 | > 100% |
| ROAS | Revenue / Ad Spend | > 3.0x |
| CPA | Total Cost / Conversions | Varies by industry |
| LTV | Avg Value x Frequency x Lifespan | > 3x CAC |
| CAC | Total Cost / New Customers | < 1/3 of LTV |

### Step 3: Build the Comparison Table

Present results in a clear markdown table:

```
| Channel       | Spend    | Revenue  | ROI    | ROAS  | CPA    | LTV:CAC |
|---------------|----------|----------|--------|-------|--------|---------|
| Google Ads    | $10,000  | $35,000  | 250%   | 3.5x  | $25.00 | 4.2:1   |
| Meta Ads      | $8,000   | $20,000  | 150%   | 2.5x  | $32.00 | 3.1:1   |
| Email         | $2,000   | $15,000  | 650%   | 7.5x  | $8.00  | 6.8:1   |
```

### Step 4: Project Future ROI

When projecting, clearly state assumptions:

- Historical growth rate or trend direction
- Diminishing returns at higher spend levels (assume 10-20% efficiency loss per 50% budget increase unless told otherwise)
- Seasonal adjustments if applicable
- Market saturation considerations

### Step 5: Break-Even Analysis

Calculate the break-even point for each channel:

- Break-even ROAS = 1 / Profit Margin
- Break-even CPA = Average Order Value x Profit Margin
- Months to break even = CAC / (Monthly Revenue per Customer x Profit Margin)

### Step 6: Provide Recommendations

Always conclude with:

1. **Top performing channel** by ROI and by ROAS
2. **Recommended budget reallocation** with specific percentages
3. **Channels to scale** (high ROI with room to grow)
4. **Channels to optimize** (moderate ROI, potential for improvement)
5. **Channels to reconsider** (below break-even or negative ROI)
6. **Projected impact** of the recommended reallocation

## Best Practices

- Always distinguish between blended ROI and channel-specific ROI
- Account for attribution models when comparing channels (last-click vs. multi-touch)
- Flag when data samples are too small for reliable conclusions (fewer than 100 conversions)
- Include confidence intervals on projections when possible
- Remind users that correlation between spend and revenue does not imply direct causation
- Consider the full funnel impact -- some channels drive awareness that converts elsewhere
- When LTV data is unavailable, note that CPA-only analysis may undervalue channels that attract high-retention customers
- Use consistent time periods when comparing across channels
- Round currency to two decimal places and percentages to one decimal place
