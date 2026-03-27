---
name: brand-voice
description: Defines, maintains, and applies consistent brand voice across all content types with multi-persona support
---

# Brand Voice

## Overview

This skill helps define, document, and enforce a consistent brand voice across all content. It can analyze existing content to extract voice characteristics, create comprehensive brand voice guidelines, adapt content to match a target voice, and support multiple brand personas tailored to different audience segments.

## When to Use This Skill

- When a user needs to establish brand voice guidelines from scratch
- When analyzing existing content for voice consistency
- When rewriting or adapting content to match a specific brand personality
- When creating voice variations for different audience segments
- When reviewing content drafts for brand alignment
- When onboarding new content creators who need to understand the brand voice

## How It Works

1. **Voice Discovery**: Analyze sample content or user descriptions to identify voice attributes
2. **Guideline Creation**: Document the voice across multiple dimensions with concrete examples
3. **Content Analysis**: Score existing content against the defined voice profile
4. **Voice Adaptation**: Rewrite or adjust content to align with the brand voice
5. **Persona Management**: Maintain distinct voice profiles for different audiences or sub-brands

## Instructions

### Voice Dimensions

Define brand voice across these five core dimensions, each on a spectrum:

1. **Tone**: Formal <---> Casual
2. **Emotion**: Reserved <---> Enthusiastic
3. **Complexity**: Simple <---> Technical
4. **Authority**: Peer-level <---> Expert
5. **Humor**: Serious <---> Playful

Rate each dimension on a 1-10 scale and provide descriptive anchors.

### Creating Voice Guidelines from Examples

When the user provides sample content:

1. Analyze at least 3-5 content samples for patterns
2. Identify recurring vocabulary, sentence structures, and rhetorical devices
3. Note what the voice avoids (jargon, slang, passive voice, etc.)
4. Extract the implied relationship with the reader
5. Document findings in a structured voice profile

Output format for a voice profile:

```
## Brand Voice Profile: [Brand Name]

### Voice Summary
[2-3 sentence elevator pitch of the brand voice]

### Dimension Scores
- Tone: [score]/10 — [description]
- Emotion: [score]/10 — [description]
- Complexity: [score]/10 — [description]
- Authority: [score]/10 — [description]
- Humor: [score]/10 — [description]

### Vocabulary Guidelines
- Preferred words: [list]
- Avoid these words: [list]
- Industry terms to use: [list]
- Industry terms to avoid: [list]

### Sentence Structure
- Average sentence length: [short/medium/long]
- Preferred structures: [examples]
- Paragraph length: [guideline]

### Do's and Don'ts
| Do                              | Don't                           |
|---------------------------------|---------------------------------|
| [specific positive example]     | [specific negative example]     |
```

### Analyzing Content for Consistency

When reviewing content against a voice profile:

1. Score the content on each of the five dimensions
2. Compare scores to the target profile
3. Highlight specific passages that deviate from the voice
4. Calculate an overall consistency score (percentage alignment)
5. Provide specific, actionable revision suggestions

Format the analysis as:

```
### Voice Consistency Report

**Overall Score**: [X]% aligned with [Brand Name] voice

| Dimension   | Target | Actual | Gap | Status |
|-------------|--------|--------|-----|--------|
| Tone        | 7      | 5      | -2  | Needs adjustment |
| Emotion     | 6      | 7      | +1  | Acceptable |

**Flagged Passages**:
1. "[quoted text]" — Issue: [description] — Suggestion: [revision]
```

### Adapting Content to Brand Voice

When rewriting content to match a voice profile:

1. Preserve the original meaning and key information
2. Adjust vocabulary to match preferred word lists
3. Restructure sentences to match target length and complexity
4. Modify tone markers (greetings, sign-offs, transitions)
5. Present before/after comparisons for transparency

Always show the transformation:

```
**Before**: "We are pleased to inform you that our new product has been released."
**After**: "Big news — our latest product just dropped, and we think you'll love it."
**Changes**: Reduced formality (7 to 4), increased enthusiasm (3 to 7), shortened sentence, added direct address
```

### Multi-Persona Support

When managing multiple personas:

- Create a base voice profile that all personas share (brand DNA)
- Define persona-specific adjustments as deltas from the base
- Name each persona clearly (e.g., "Enterprise Persona," "Creator Persona")
- Specify which channels or audiences each persona serves
- Ensure personas are distinct but recognizably part of the same brand family

### Content Types and Adjustments

Recognize that voice naturally shifts across content types. Provide guidance for:

- **Website copy**: Core voice, most polished
- **Social media**: More casual, shorter, higher energy
- **Email marketing**: Warm, direct, action-oriented
- **Technical docs**: More precise, less personality, clarity-first
- **Customer support**: Empathetic, solution-focused, patient
- **Ad copy**: Punchy, benefit-driven, high-impact

### Best Practices

- Voice is not the same as tone; voice is consistent, tone adapts to context
- Always ground guidelines in concrete examples rather than abstract descriptions
- Update voice guidelines quarterly or when brand positioning shifts
- Test voice guidelines with multiple content creators to ensure they are actionable
- When in doubt, prioritize clarity over personality
- Avoid over-prescribing; leave room for natural variation within guardrails
- Consider cultural sensitivity when the brand operates across regions
- Document exceptions explicitly (e.g., "Legal disclaimers use formal tone regardless of persona")
