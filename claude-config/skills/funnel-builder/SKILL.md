---
name: funnel-builder
description: Designs complete marketing funnels (TOFU, MOFU, BOFU) with customer journey mapping, content and ad strategies per stage, email sequences, retargeting strategies, conversion rate estimates, and ASCII/markdown funnel diagrams.
---

# Funnel Builder

## Overview

This skill designs complete marketing funnels from top to bottom. It maps the customer journey through awareness, consideration, and conversion stages, defines the content, ads, and touchpoints for each stage, includes email nurture sequences and retargeting strategies, estimates conversion rates between stages, and outputs visual funnel diagrams in ASCII or markdown format.

## When to Use This Skill

- When launching a new product or service and need a go-to-market funnel
- When an existing funnel has leaks and needs to be redesigned
- When planning a multi-channel campaign with a clear conversion path
- When mapping out the customer journey for a new audience segment
- When building an automated marketing system with email sequences and retargeting
- When presenting a funnel strategy to stakeholders or clients

## How It Works

The skill takes business information (product, audience, goals, channels, budget range) and designs a complete funnel architecture. It specifies what happens at each stage, what content and ads are served, how users move between stages, and what conversion rates to expect. The output includes both a visual diagram and detailed stage-by-stage breakdowns.

## Instructions

### Input Requirements

Provide as many of the following as possible:

- **Product/Service**: What you are selling
- **Price Point**: Helps determine funnel complexity (higher price = more nurturing stages)
- **Target Audience**: Who the ideal customer is
- **Current Channels**: Where you currently advertise or publish content
- **Sales Model**: Self-serve, sales-assisted, enterprise, e-commerce
- **Goal**: Lead generation, direct sales, app installs, subscriptions, bookings
- **Budget Range**: Helps calibrate channel recommendations
- **Existing Assets**: Landing pages, email lists, content library, ad accounts

### Funnel Stages

#### TOFU - Top of Funnel (Awareness)
**Objective:** Attract attention and introduce the brand to cold audiences.

| Element | Details |
|---------|---------|
| **Audience** | Cold - no prior interaction with the brand |
| **Channels** | Paid social (broad targeting), search ads (informational keywords), SEO content, YouTube pre-roll, TikTok, podcast ads, PR |
| **Content Types** | Blog posts, educational videos, infographics, social media posts, podcasts, free tools |
| **Ad Formats** | Video ads (15-30s), carousel ads, display banners, native ads |
| **Key Metrics** | Impressions, reach, CPM, video views, website visits, social engagement |
| **CTA** | Learn more, watch video, read article, follow us |
| **Expected CPM** | $5-$25 depending on channel and audience |

#### MOFU - Middle of Funnel (Consideration)
**Objective:** Nurture warm audiences and build trust, preference, and intent.

| Element | Details |
|---------|---------|
| **Audience** | Warm - visited site, engaged with content, on email list |
| **Channels** | Retargeting ads, email nurture, webinars, social proof content, comparison content |
| **Content Types** | Case studies, whitepapers, webinars, product demos, comparison guides, testimonials, email sequences |
| **Ad Formats** | Retargeting display, social retargeting, sponsored content, lead gen forms |
| **Key Metrics** | Email open/click rates, webinar registrations, content downloads, return visits, time on site |
| **CTA** | Download guide, register for webinar, start free trial, request demo |
| **Lead Magnet Ideas** | Ebooks, templates, checklists, free tools, assessments, mini-courses |

#### BOFU - Bottom of Funnel (Conversion)
**Objective:** Convert high-intent prospects into customers.

| Element | Details |
|---------|---------|
| **Audience** | Hot - demonstrated purchase intent (pricing page, cart, demo request) |
| **Channels** | Retargeting, email, search ads (high-intent keywords), direct sales outreach |
| **Content Types** | Free trials, product demos, pricing pages, customer reviews, ROI calculators, limited-time offers |
| **Ad Formats** | Dynamic retargeting, search ads (branded + high-intent), email sequences with urgency |
| **Key Metrics** | Conversion rate, CPA, ROAS, close rate, average deal size |
| **CTA** | Buy now, start trial, schedule call, claim offer |
| **Conversion Triggers** | Scarcity, social proof, risk reversal (guarantees), time-limited discounts |

#### Post-Purchase (Retention and Advocacy)
**Objective:** Retain customers, increase LTV, and generate referrals.

| Element | Details |
|---------|---------|
| **Content Types** | Onboarding emails, product education, loyalty programs, referral programs, upsell/cross-sell campaigns |
| **Key Metrics** | Retention rate, NPS, repeat purchase rate, referral rate, LTV |

### Email Sequence Templates

#### Welcome/Nurture Sequence (MOFU)
```
Day 0: Welcome + deliver lead magnet
Day 2: Educational content related to their interest
Day 4: Case study or social proof
Day 7: Product introduction (soft sell)
Day 10: Objection handling / FAQ
Day 14: Offer or trial invitation (CTA)
```

#### Cart Abandonment Sequence (BOFU)
```
Hour 1: Reminder email ("You left something behind")
Hour 24: Social proof email (reviews, testimonials)
Hour 48: Urgency email (limited stock or time-limited discount)
Hour 72: Final reminder with incentive (free shipping, bonus)
```

#### Post-Purchase Sequence
```
Day 0: Order confirmation + what to expect
Day 3: Product tips / getting started guide
Day 7: Check-in + request for feedback
Day 14: Related product recommendation
Day 30: Loyalty program or referral invitation
```

### Retargeting Strategy

Define retargeting audiences based on funnel behavior:

| Audience Segment | Behavior | Retargeting Ad | Duration |
|-----------------|----------|----------------|----------|
| Site visitors (no action) | Visited any page but did not convert | Educational content, social proof | 30 days |
| Content engagers | Downloaded guide, watched video | Product benefits, case studies | 21 days |
| Product page viewers | Viewed product/pricing page | Testimonials, limited offer | 14 days |
| Cart/form abandoners | Started checkout or form | Reminder with incentive | 7 days |
| Past customers | Purchased before | Upsell, cross-sell, loyalty | 90 days |

### Expected Conversion Rates Between Stages

| Transition | Low Benchmark | Average | High Benchmark |
|------------|--------------|---------|----------------|
| TOFU to MOFU (visitor to lead) | 1-2% | 3-5% | 8-15% |
| MOFU to BOFU (lead to opportunity) | 5-10% | 15-25% | 30-50% |
| BOFU to Customer (opportunity to sale) | 10-15% | 20-35% | 40-60% |
| Overall (visitor to customer) | 0.5-1% | 1-3% | 3-8% |

These vary significantly by industry, price point, and sales model. Use them as starting estimates and adjust based on actual data.

### Funnel Diagram Output

Include an ASCII funnel diagram in the output:

```
                    AWARENESS (TOFU)
    ================================================
    |  Paid Social  |  SEO/Content  |  YouTube Ads  |
    |  100,000 visitors/month                       |
    ================================================
                          |
                     3% convert
                          |
                  CONSIDERATION (MOFU)
        ======================================
        |  Email Nurture  |  Retargeting Ads  |
        |  3,000 leads/month                  |
        ======================================
                          |
                    20% convert
                          |
                   CONVERSION (BOFU)
            ============================
            |  Free Trial  |  Demo Call  |
            |  600 opportunities/month   |
            ============================
                          |
                    30% convert
                          |
                     CUSTOMER
                ==================
                | 180 customers  |
                |   /month       |
                ==================
                          |
                   RETENTION
              ======================
              | Onboarding, Upsell |
              | Referral Program   |
              ======================
```

### Output Format

```
## Marketing Funnel: [Product/Campaign Name]

### Funnel Overview
[2-3 sentence summary of the funnel strategy]

### Funnel Diagram
[ASCII diagram as shown above, with actual numbers]

### Stage 1: Awareness (TOFU)
- **Channels:** [list]
- **Content:** [list with descriptions]
- **Ads:** [ad types and targeting]
- **Budget Allocation:** [% of total budget]
- **KPIs:** [metrics and targets]

### Stage 2: Consideration (MOFU)
- **Channels:** [list]
- **Content:** [list with descriptions]
- **Email Sequence:** [outline]
- **Retargeting:** [strategy]
- **Budget Allocation:** [% of total budget]
- **KPIs:** [metrics and targets]

### Stage 3: Conversion (BOFU)
- **Channels:** [list]
- **Offers:** [conversion offers]
- **Email Sequence:** [outline]
- **Retargeting:** [strategy]
- **Budget Allocation:** [% of total budget]
- **KPIs:** [metrics and targets]

### Stage 4: Retention
- **Onboarding:** [plan]
- **Upsell/Cross-sell:** [strategy]
- **Referral Program:** [outline]

### Conversion Math
[Table showing expected numbers at each stage]

### Implementation Timeline
[Phased rollout plan: what to build first, second, third]
```

### Best Practices

- Start with the bottom of the funnel first; it is easier to convert warm leads than to build awareness
- Allocate 60% of budget to the funnel stages that are closest to revenue
- Every funnel stage must have a clear next action that moves the user to the next stage
- Use different messaging at each stage; do not serve BOFU ads to TOFU audiences
- Build measurement and attribution into the funnel from day one
- Test one stage at a time; do not try to optimize the entire funnel simultaneously
- Audit funnel leaks monthly by checking drop-off rates between stages
- For high-ticket items ($1000+), expect a longer funnel with more MOFU touchpoints
- For low-ticket items (<$50), the funnel can be compressed to TOFU directly to BOFU

### Example Usage

**Input:** "Build a marketing funnel for a B2B SaaS product ($99/month) targeting marketing managers at mid-size companies. We have $15K/month ad budget. Channels: Google Ads, LinkedIn, Meta. Goal: 50 new customers per month."

**Output:** A complete funnel with diagram, stage-by-stage breakdown, email sequences, retargeting strategy, conversion math showing how to reach the 50-customer target, and a phased implementation timeline.
