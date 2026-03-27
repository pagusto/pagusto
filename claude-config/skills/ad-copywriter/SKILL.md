---
name: ad-copywriter
description: Generates ad copy optimized for specific platforms (Meta, Google, TikTok, LinkedIn, YouTube, Microsoft Ads) with correct character limits, multiple A/B variations, and tone adaptation based on brand voice and target audience.
---

# Ad Copywriter

## Overview

This skill generates high-converting ad copy tailored to specific advertising platforms. It understands the character limits, formatting rules, and best practices for each platform and ad format. It produces multiple variations suitable for A/B testing and adapts tone, hooks, and messaging based on the brand voice, target audience, and campaign objective.

## When to Use This Skill

- When a user needs ad copy for a specific platform (Meta, Google, TikTok, LinkedIn, YouTube, Microsoft Ads)
- When launching a new campaign and need multiple creative variations
- When refreshing existing ad copy to combat creative fatigue
- When adapting copy from one platform to another
- When the user wants A/B test variations of headlines, descriptions, or CTAs

## How It Works

The skill uses platform-specific knowledge of character limits, ad formats, audience behavior, and algorithmic preferences to generate copy that maximizes engagement and conversions within each platform's constraints.

## Instructions

### Step 1: Gather Input

Before writing, collect or infer the following:
- **Platform**: Meta (Facebook/Instagram), Google Ads, TikTok, LinkedIn, YouTube, Microsoft Ads
- **Ad Format**: Search ad, display ad, video ad, carousel, story, feed post, etc.
- **Campaign Objective**: Awareness, traffic, engagement, leads, conversions, app installs
- **Target Audience**: Demographics, interests, pain points, sophistication level
- **Product/Service**: What is being advertised, key features, unique selling propositions
- **Brand Voice**: Professional, casual, playful, authoritative, empathetic, bold
- **CTA Goal**: What action should the viewer take (buy, sign up, learn more, download, book)
- **Key Offer**: Discount, free trial, limited time, exclusive access, etc.

### Step 2: Apply Platform-Specific Rules

**Google Ads (Search)**
- Headline 1-15: max 30 characters each (provide at least 5)
- Description 1-4: max 90 characters each (provide at least 2)
- Display URL path: 2 fields, 15 characters each
- Tips: Include keywords in headlines, use numbers, include CTA in descriptions

**Meta Ads (Facebook/Instagram)**
- Primary Text: 125 characters recommended (up to 1,000 visible with "See More")
- Headline: 40 characters recommended (max 255)
- Description: 30 characters recommended (max 255)
- Tips: Lead with hook in first line, use emojis strategically, ask questions, use social proof

**TikTok Ads**
- Ad Description: max 100 characters
- Display Name: max 40 characters
- Video text overlays: keep to 2-3 words per frame
- Tips: Native feel is critical, start with a hook in first 1-2 seconds, use trending language, avoid looking like an ad

**LinkedIn Ads**
- Single Image Ad Headline: max 70 characters (recommended)
- Introductory Text: max 150 characters for visibility (up to 600 total)
- Description: max 100 characters
- Tips: Professional tone, use industry jargon appropriately, lead with value/ROI, cite data

**YouTube Ads**
- Video ad companion headline: max 15 characters
- Companion description: max 15 characters
- In-feed headline: max 100 characters
- In-feed description 1-2: max 35 characters each
- Tips: Hook in first 5 seconds (before skip), address viewer directly, strong CTA at end

**Microsoft Ads**
- Headlines: max 30 characters (up to 15 headlines)
- Descriptions: max 90 characters (up to 4)
- Similar to Google Ads but audience skews older and more B2B

### Step 3: Write Compelling Copy

Apply these copywriting principles:

**Hooks (first line must stop the scroll)**
- Question hook: "Still paying too much for [X]?"
- Statistic hook: "87% of marketers are making this mistake"
- Pain point hook: "Tired of [common frustration]?"
- Curiosity hook: "The one thing top performers do differently"
- Contrarian hook: "Stop doing [common advice] — here is why"

**Emotional Triggers**
- Fear of missing out (FOMO): limited time, exclusive, ending soon
- Social proof: join 10,000+ customers, as seen in, rated #1
- Authority: backed by research, expert-approved, industry-leading
- Urgency: today only, last chance, while supplies last
- Aspiration: imagine, transform, achieve, unlock

**Structure**
- Hook -> Problem -> Solution -> Proof -> CTA
- Keep sentences short and punchy
- Use power words: free, new, proven, guaranteed, instant, exclusive
- One clear message per ad (do not overload)

### Step 4: Generate Variations

For each ad request, provide:
- **3-5 headline variations** (testing different hooks and angles)
- **2-3 description variations** (testing different value propositions)
- **2-3 CTA variations** (testing different action words)

Label each variation with its angle:
- Variation A: Pain point angle
- Variation B: Benefit/aspiration angle
- Variation C: Social proof angle
- Variation D: Urgency/FOMO angle
- Variation E: Curiosity/question angle

### Output Format

```
## Ad Copy: [Campaign Name]
**Platform**: [Platform] | **Format**: [Format] | **Objective**: [Objective]

### Variation A — [Angle Name]
- **Headline**: [copy] (X/Y chars)
- **Description**: [copy] (X/Y chars)
- **Primary Text**: [copy] (X/Y chars)
- **CTA Button**: [CTA]

### Variation B — [Angle Name]
...

### A/B Testing Recommendations
- Test [X] vs [Y] to determine whether [hypothesis]
- Start with [recommended variation] based on [reasoning]
- Run for minimum [timeframe] or [sample size] before declaring winner

### Platform-Specific Notes
- [Any platform-specific tips or warnings]
```

### Best Practices

- Always show character counts next to each copy element: "(23/30 chars)"
- Never exceed hard character limits — truncated ads waste budget
- Match the ad copy tone to the landing page tone for consistency
- When the user provides existing copy, offer improvements rather than starting from scratch
- Suggest complementary ad formats when relevant (e.g., "This would also work well as a carousel")
- Flag any policy risks (restricted categories, prohibited claims, required disclaimers)
- For remarketing/retargeting copy, acknowledge familiarity ("Come back and finish your order")
- Consider the full funnel: awareness ads should not hard-sell, conversion ads should be direct
