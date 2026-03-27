---
name: email-campaign
description: Designs complete email marketing campaigns with sequences, subject lines, segmentation, timing, and deliverability best practices
---

# Email Campaign Designer

## Overview

This skill designs complete email marketing campaigns from strategy to execution. It creates email sequences for various use cases (welcome, nurture, re-engagement, abandoned cart, post-purchase), writes compelling subject lines with A/B variants, structures email content with clear hierarchy and CTAs, defines segmentation rules and send triggers, plans timing and cadence, and follows deliverability best practices.

## When to Use This Skill

- When launching a new email marketing campaign or automation sequence
- When designing onboarding or nurture email flows
- When creating abandoned cart or re-engagement campaigns
- When optimizing subject lines and email content for higher open and click rates
- When setting up segmentation and trigger rules in an email platform
- When auditing existing email campaigns for performance improvements

## How It Works

1. Define the campaign objective and target audience
2. Map the email sequence with triggers and timing
3. Write each email with subject lines, preview text, body content, and CTAs
4. Create A/B test variants for key elements
5. Define segmentation rules and exit conditions
6. Plan send schedule and review deliverability requirements

## Instructions

### Step 1: Define Campaign Objectives

Clarify with the user:

- **Campaign type**: Welcome, nurture, re-engagement, abandoned cart, post-purchase, promotional, event-based
- **Primary goal**: Conversion, engagement, retention, education, feedback
- **Target audience**: New subscribers, active users, lapsed customers, specific segments
- **Success metrics**: Open rate, click rate, conversion rate, revenue per email
- **Email platform**: Mailchimp, Klaviyo, HubSpot, ActiveCampaign, SendGrid, etc.

### Step 2: Map the Email Sequence

Design the flow with triggers, delays, and conditions:

```
WELCOME SEQUENCE (5 emails, 14 days)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Trigger: New subscriber signs up

Email 1: Welcome + value proposition (immediately)
  |
  v  [Wait 2 days]
Email 2: Getting started guide (Day 2)
  |
  v  [Wait 2 days]
Email 3: Social proof / case study (Day 4)
  |
  v  [Check: Has user completed onboarding?]
  |       |
  YES     NO
  |       |
  v       v
Email 4a: Advanced tips (Day 7)
Email 4b: Need help? (Day 7)
  |
  v  [Wait 7 days]
Email 5: Offer / upgrade prompt (Day 14)

Exit conditions:
  - User unsubscribes
  - User converts to paid (move to post-purchase sequence)
  - User marks as spam
```

### Step 3: Write Email Content

For each email in the sequence, provide:

**Subject Line** (with 2 A/B variants):
```
Subject A: "Welcome to [Brand] -- here's your quick start guide"
Subject B: "[Name], your account is ready. Let's go."
Preview text: "Everything you need to get started in under 5 minutes"
```

Subject line best practices:
- Keep under 50 characters for mobile display
- Use personalization tokens when they add value
- Create curiosity or communicate clear benefit
- Avoid spam trigger words (free, act now, limited time, guaranteed)
- Use numbers when relevant ("3 steps", "5 minutes")
- Test emoji usage sparingly -- one emoji maximum, placed at the start or end

**Email Body Structure**:
```
[Header image or logo -- keep under 600px wide]

Hi {{first_name}},

[Opening hook -- 1-2 sentences that acknowledge the reader's situation]

[Value section -- 2-3 short paragraphs or bullet points delivering on
the subject line promise. Use subheadings for scanability.]

[Primary CTA button -- single, clear action]
  Button text: "Start your first project"
  Button color: Brand primary color
  Link: https://app.example.com/onboarding

[Secondary content -- optional social proof, PS line, or secondary link]

[Footer: Unsubscribe link, physical address, social links]
```

Content guidelines per email type:

| Email Type | Tone | Length | CTA Focus |
|-----------|------|--------|-----------|
| Welcome | Warm, enthusiastic | Short (100-150 words) | Get started |
| Nurture | Educational, helpful | Medium (150-250 words) | Learn more |
| Re-engagement | Direct, value-focused | Short (80-120 words) | Come back |
| Abandoned cart | Urgent but not pushy | Short (80-120 words) | Complete purchase |
| Post-purchase | Grateful, supportive | Medium (120-200 words) | Next step / review |

### Step 4: Create A/B Test Plan

Identify what to test for each email:

```
A/B Test Plan for Email 1 (Welcome):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Test 1: Subject line
  A: "Welcome to [Brand] -- here's your quick start guide"
  B: "[Name], your account is ready. Let's go."
  Metric: Open rate
  Split: 50/50
  Sample size: Minimum 1,000 per variant

Test 2: CTA button text
  A: "Start your first project"
  B: "Show me how it works"
  Metric: Click rate
  Split: 50/50

Rule: Test one variable at a time. Run for 48 hours or until
statistical significance (95% confidence) is reached.
```

### Step 5: Define Segmentation and Triggers

Specify the rules for each email:

**Trigger Rules**:
- Event-based: User performed action X (signed up, abandoned cart, purchased)
- Time-based: X days since last activity, subscription anniversary
- Behavioral: Opened previous email, clicked link, visited pricing page

**Segmentation Criteria**:
```
Segment: Active Trial Users
  Conditions:
    - Account created within last 14 days
    - Logged in at least 2 times
    - Has NOT converted to paid
    - Email status: subscribed
    - NOT in suppression list
```

**Exit and Suppression Rules**:
- Remove from sequence if user converts (avoid irrelevant emails)
- Suppress users who have not opened last 5 emails (protect sender reputation)
- Honor unsubscribe within 24 hours (legally required)
- Do not email addresses that have hard bounced

### Step 6: Plan Timing and Cadence

Recommended send times by audience type:

| Audience | Best Days | Best Times | Minimum Gap |
|----------|-----------|------------|-------------|
| B2B | Tuesday-Thursday | 9-11 AM recipient local time | 3 days |
| B2C | Tuesday, Thursday, Saturday | 10 AM or 7-8 PM | 2 days |
| E-commerce | Any day | 10 AM or 8 PM | 1-2 days |

Cadence guidelines:
- Welcome sequence: 5-7 emails over 14-21 days
- Nurture sequence: 1-2 emails per week
- Re-engagement: 3 emails over 10 days, then suppress
- Abandoned cart: 3 emails over 3 days (1hr, 24hr, 72hr)
- Post-purchase: 3-4 emails over 30 days
- Newsletter: Weekly or biweekly, consistent day and time

### Step 7: Deliverability Checklist

Ensure these technical and content requirements are met:

**Authentication**:
- SPF record configured for sending domain
- DKIM signing enabled and verified
- DMARC policy set (start with p=none, move to p=quarantine)
- Custom return-path domain configured

**List Hygiene**:
- Remove hard bounces immediately
- Suppress soft bounces after 3 consecutive failures
- Run email verification on imported lists before sending
- Implement double opt-in for new subscribers
- Clean inactive subscribers quarterly (no opens in 90+ days)

**Content Best Practices**:
- Maintain text-to-image ratio of at least 60:40
- Include a plain-text version of every email
- Keep HTML file size under 100KB
- Use alt text on all images
- Avoid URL shorteners (they trigger spam filters)
- Include a visible, easy-to-find unsubscribe link
- Add your physical mailing address (CAN-SPAM requirement)

**Sending Practices**:
- Warm up new sending domains gradually (start with engaged subscribers)
- Monitor bounce rate (keep under 2%), spam complaint rate (keep under 0.1%)
- Use a consistent "From" name and address
- Avoid sending to purchased or rented lists
- Throttle sends for large lists (spread over hours, not all at once)

## Best Practices

- Always preview emails on mobile before sending -- over 60% of opens are on mobile
- Write the subject line last, after you know the email's content
- One primary CTA per email -- do not split attention across multiple goals
- Use personalization beyond first name: reference user behavior, preferences, or account data
- Track revenue per email, not just opens and clicks, to measure true campaign value
- Set up a sunset policy for unengaged subscribers to protect deliverability
- Document every sequence with a visual flowchart for team alignment
- Review and refresh email content quarterly to prevent fatigue
- Respect time zones -- send at the recipient's local time when possible
- Test emails across clients (Gmail, Outlook, Apple Mail) before launch
