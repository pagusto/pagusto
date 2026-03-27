---
name: roi-calculator
description: Calculates marketing ROI, ROAS, CPA, LTV, CAC and provides budget allocation recommendations across channels
---

# ROI Calculator

## Overview

This skill calculates and analyzes marketing return on investment across campaigns, channels, and time periods. It computes key financial metrics, projects future performance based on historical data, and delivers actionable budget allocation recommendations in formatted tables.

## When to Use This Skill

- When a user asks to calculate ROI, ROAS, CPA, LTV, or CAC for marketing campaigns
- When comparing performance across multiple advertising channels
- When projecting future campaign returns based on historical data
- When determining break-even points for marketing investments
- When deciding how to allocate or reallocate marketing budgets
- When building a business case for increasing or decreasing spend on a channel

## How It Works

1. **Data Collection**: Gather campaign spend, revenue, conversions, and customer data from the user
2. **Metric Calculation**: Compute all relevant financial metrics using standard formulas
3. **Cross-Channel Comparison**: Normalize metrics across channels for fair comparison
4. **Projection Modeling**: Use historical trends to forecast future performance
5. **Break-Even Analysis**: Determine the point at which investment recovers cost
6. **Recommendation Generation**: Produce budget allocation advice based on the analysis

## Instructions

### Core Metrics and Formulas

Always calculate these metrics when sufficient data is provided:

- **ROI** = ((Revenue - Cost) / Cost) x 100
- **ROAS** = Revenue / Ad Spend
- **CPA** = Total Campaign Cost / Number of Conversions
- **LTV** = Average Purchase Value x Purchase Frequency x Average Customer Lifespan
- **CAC** = Total Sales and Marketing Cost / Number of New Customers Acquired
- **LTV:CAC Ratio** = Customer Lifetime Value / Customer Acquisition Cost

### Input Requirements

Ask the user for the following data points (at minimum):

- Campaign name or channel identifier
- Total spend (broken down by channel if comparing)
- Revenue generated or number of conversions
- Time period covered
- Conversion value (if not revenue-based)
- For LTV calculations: average order value, purchase frequency, retention period

### Output Format

Always present results in structured tables. Example format:

```
| Channel        | Spend     | Revenue   | ROI    | ROAS  | CPA    |
|----------------|-----------|-----------|--------|-------|--------|
| Google Ads     | $10,000   | $35,000   | 250%   | 3.5x  | $28.57 |
| Meta Ads       | $8,000    | $22,400   | 180%   | 2.8x  | $35.56 |
| LinkedIn Ads   | $5,000    | $11,000   | 120%   | 2.2x  | $62.50 |
```

### Break-Even Analysis

When performing break-even analysis:

1. Calculate the break-even point: Spend / Average Revenue Per Conversion
2. Determine time to break-even based on current conversion rates
3. Factor in fixed costs vs. variable costs where applicable
4. Present a clear statement: "At the current CPA of $X and average deal value of $Y, the campaign breaks even after Z conversions (approximately N days at current pace)"

### Projection Guidelines

When projecting ROI:

- Use at least 3 data points (ideally monthly or weekly) for trend analysis
- Apply diminishing returns curves for scaling projections (do not assume linear growth)
- State all assumptions explicitly (e.g., "Assuming consistent conversion rates and no seasonality adjustments")
- Provide conservative, moderate, and aggressive scenarios
- Flag any data quality concerns or insufficient sample sizes

### Budget Allocation Recommendations

Structure recommendations as follows:

1. **Current allocation** vs. **recommended allocation** side by side
2. **Rationale** for each reallocation tied to specific metrics
3. **Expected impact** of the reallocation in concrete numbers
4. **Risk factors** that could affect the recommendation
5. **Suggested test**: recommend a phased approach rather than abrupt shifts

### Best Practices

- Always clarify whether figures are gross or net revenue
- Account for attribution models (last-click, first-click, multi-touch) and note which is being used
- Distinguish between blended and channel-specific CAC
- For LTV:CAC ratio, flag if it falls below 3:1 (unhealthy) or above 5:1 (potential underinvestment)
- Include confidence intervals or ranges rather than single-point estimates when projecting
- Consider seasonality, market changes, and competitive dynamics in projections
- Round financial figures to two decimal places; round percentages to one decimal place
- When data is incomplete, state what additional data would improve the analysis
- Never present projections as guarantees; always frame them as estimates based on stated assumptions

### Example Interaction

User provides: "We spent $15,000 on Google Ads and $10,000 on Meta last month. Google generated $52,500 in revenue from 150 conversions. Meta generated $28,000 from 200 conversions."

Response should include:
1. A comparison table with ROI, ROAS, CPA for both channels
2. Observation that Meta has lower CPA but Google has higher ROAS
3. Note about different conversion values ($350 Google vs $140 Meta)
4. Recommendation to investigate conversion quality differences
5. Suggestion for budget reallocation with expected outcomes
