---
name: a-b-test-analyzer
description: Analyzes A/B test results with statistical significance calculations, confidence intervals, p-values, conversion rates, lift, sample size requirements, and clear winner/loser recommendations while warning about common pitfalls.
---

# A/B Test Analyzer

## Overview

This skill performs rigorous statistical analysis on A/B test results. It calculates key metrics including conversion rates, lift, confidence intervals, p-values, and statistical power. It provides a clear recommendation on whether a winner can be declared and warns about common mistakes that lead to incorrect conclusions.

## When to Use This Skill

- When an A/B test has completed and you need to determine if results are statistically significant
- When planning an A/B test and need to calculate the required sample size
- When stakeholders want a clear, understandable summary of test results
- When evaluating whether a test has run long enough to make a decision
- When comparing multiple test variants (A/B/n testing)
- When you need to check if observed differences are real or due to random chance

## How It Works

The skill applies frequentist hypothesis testing (two-proportion z-test for conversion metrics, t-test for continuous metrics) to determine whether the observed difference between control and variant groups is statistically significant. It calculates confidence intervals to show the range of plausible effect sizes and determines statistical power to assess whether the test had sufficient data to detect meaningful differences.

## Instructions

### Input Requirements

Provide the following data for each variant:

| Data Point        | Required | Description                                    |
|-------------------|----------|------------------------------------------------|
| Variant name      | Yes      | e.g., "Control (A)" and "Variant (B)"         |
| Sample size       | Yes      | Number of visitors/users in each group         |
| Conversions       | Yes      | Number of users who completed the goal action  |
| Metric type       | Yes      | CTR, conversion rate, revenue per visitor, etc.|
| Confidence level  | No       | Default: 95% (can use 90% or 99%)             |
| Test duration     | No       | How long the test has been running             |
| MDE               | No       | Minimum detectable effect (for power analysis) |

For continuous metrics (e.g., revenue per visitor, average order value), also provide:
- Mean value per variant
- Standard deviation per variant

### Calculations Performed

#### 1. Conversion Rate
```
Conversion Rate = Conversions / Sample Size
```

#### 2. Lift (Relative Improvement)
```
Lift = (Variant Rate - Control Rate) / Control Rate * 100%
```

#### 3. Standard Error
```
SE = sqrt(p_control * (1 - p_control) / n_control + p_variant * (1 - p_variant) / n_variant)
```

#### 4. Z-Score
```
Z = (p_variant - p_control) / SE
```

#### 5. P-Value
Derived from the z-score using the standard normal distribution. A two-tailed test is used by default.

#### 6. Confidence Interval
```
CI = (p_variant - p_control) +/- Z_alpha/2 * SE
```

#### 7. Statistical Power
The probability of detecting a true effect of the observed size, given the sample sizes.

#### 8. Minimum Sample Size (Pre-Test)
```
n = (Z_alpha/2 + Z_beta)^2 * (p1*(1-p1) + p2*(1-p2)) / (p2 - p1)^2
```

### Output Format

```
## A/B Test Results

### Test Summary
| Metric           | Control (A)     | Variant (B)     |
|------------------|-----------------|-----------------|
| Sample Size      | [n]             | [n]             |
| Conversions      | [count]         | [count]         |
| Conversion Rate  | [rate]%         | [rate]%         |

### Statistical Analysis
| Metric                  | Value           |
|-------------------------|-----------------|
| Absolute Difference     | [+/- X.XX pp]  |
| Relative Lift           | [+/- X.XX%]    |
| P-Value                 | [0.XXXX]       |
| Confidence Level        | [XX%]          |
| Statistically Significant | [Yes/No]     |
| Confidence Interval     | [lower, upper] |
| Statistical Power       | [XX%]          |

### Recommendation
**[WINNER: Variant B / NO CLEAR WINNER / INCONCLUSIVE - CONTINUE TESTING]**

[2-3 sentence explanation of the recommendation in plain language]

### Warnings and Caveats
[List any applicable warnings]
```

### Common Pitfalls to Check and Warn About

1. **Peeking Problem** - Checking results before reaching the planned sample size inflates false positive rates. If the test ended early, warn that significance may be overstated.
2. **Multiple Comparisons** - When testing more than 2 variants or multiple metrics, the chance of a false positive increases. Apply Bonferroni correction when necessary.
3. **Segment Bias** - Results may differ across segments (device, geo, new vs returning). Warn if the user is making decisions based on a segment that was not pre-defined.
4. **Insufficient Sample Size** - If statistical power is below 80%, warn that the test may not have been large enough to detect a meaningful difference.
5. **Duration Too Short** - Tests should run for at least 1-2 full business cycles (typically 1-2 weeks minimum) to account for day-of-week effects.
6. **Simpson's Paradox** - Aggregate results may mask opposite trends within segments.
7. **Novelty Effect** - Early results may be skewed by users reacting to something new, not necessarily better.
8. **Sample Ratio Mismatch** - If the split is not close to 50/50, there may be a technical issue with randomization. Flag if the ratio deviates by more than 1% from expected.

### Decision Framework

| Scenario                                         | Recommendation                        |
|--------------------------------------------------|---------------------------------------|
| p < 0.05 and power >= 80% and lift is meaningful | Declare winner, implement variant     |
| p < 0.05 but lift is very small (<1%)            | Statistically significant but not practically significant; consider cost of implementation |
| p > 0.05 and power >= 80%                        | No significant difference; keep control |
| p > 0.05 and power < 80%                         | Inconclusive; continue testing or increase traffic |
| p < 0.10 but > 0.05                              | Trending but not significant; extend the test |

### Best Practices

- Always determine sample size requirements before starting the test
- Define your primary metric and success criteria before launching
- Run tests for full weeks to capture weekly traffic patterns
- Do not stop a test early just because it looks like a winner (unless using sequential testing methods)
- Document every test with hypothesis, setup, results, and learnings
- For revenue metrics, use a t-test or Mann-Whitney U test instead of a z-test
- Consider Bayesian analysis as a complement for stakeholders who prefer probability-of-being-best framing

### Example Usage

**Input:** "Analyze this A/B test: Control had 15,000 visitors and 450 conversions. Variant had 14,800 visitors and 510 conversions. Use 95% confidence level."

**Output:** Full statistical analysis with conversion rates, lift, p-value, confidence interval, power, and a clear recommendation.
