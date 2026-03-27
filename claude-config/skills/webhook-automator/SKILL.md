---
name: webhook-automator
description: Designs webhook-based automation workflows with trigger-action mappings, payload schemas, and conditional routing
---

# Webhook Automator

## Overview

This skill designs webhook-based automation workflows that connect tools and services. It creates endpoint configurations, maps triggers to actions across platforms (CRM, email, Slack, project management), generates payload schemas and transformation logic, and supports conditional routing with error handling. The output includes workflow diagrams and ready-to-use configuration files.

## When to Use This Skill

- When connecting two or more tools that support webhooks
- When automating repetitive tasks triggered by events (form submission, purchase, status change)
- When building notification pipelines across Slack, email, and project management tools
- When designing data sync workflows between CRM, marketing, and sales platforms
- When creating event-driven workflows that require conditional logic or branching
- When documenting existing automation flows or planning new integrations

## How It Works

1. Identify the trigger event and source system
2. Define the desired action(s) and destination system(s)
3. Map the data fields from trigger payload to action payload
4. Add conditional routing, filters, and transformation logic
5. Configure error handling and retry strategies
6. Output the complete workflow as a diagram and configuration

## Instructions

### Step 1: Define the Trigger

Gather the following from the user:

- **Source system**: The platform generating the event (e.g., Stripe, Shopify, HubSpot, Typeform)
- **Trigger event**: The specific event (e.g., "payment.completed", "form.submitted", "deal.stage.changed")
- **Payload structure**: The data sent with the webhook (or ask the user to provide a sample payload)
- **Frequency**: Expected volume (events per hour/day) for rate limiting considerations

Document the trigger as:

```
Trigger:
  Source: Stripe
  Event: payment_intent.succeeded
  Payload fields: id, amount, currency, customer_email, metadata
  Expected volume: ~200 events/day
```

### Step 2: Define the Action(s)

For each action in the workflow:

- **Destination system**: Where the data should go
- **Action type**: Create record, update record, send message, trigger workflow
- **Required fields**: What the destination API needs
- **Authentication**: API key, OAuth, bearer token

Common action patterns:

| Trigger | Action | Use Case |
|---------|--------|----------|
| Form submitted | Create CRM contact | Lead capture |
| Payment received | Send Slack notification | Sales alerts |
| Deal stage changed | Update project board | Pipeline sync |
| Customer created | Add to email sequence | Onboarding automation |
| Support ticket closed | Send survey email | Feedback collection |

### Step 3: Map and Transform Data

Create a field mapping table:

```
Field Mapping:
  Source (Stripe)          -> Destination (HubSpot)
  ─────────────────────────────────────────────────
  customer_email           -> email
  amount / 100             -> deal_amount (transform: cents to dollars)
  metadata.plan_name       -> plan_type (nested field extraction)
  created (unix timestamp) -> close_date (transform: to ISO 8601)
  "Won"                    -> deal_stage (static value)
```

Document any transformations:
- Data type conversions (timestamp formats, currency units)
- String manipulations (concatenation, case changes)
- Conditional value mapping (if status = X, set field = Y)
- Default values for missing fields

### Step 4: Add Conditional Routing

Define branching logic when the workflow has multiple paths:

```
Routing Rules:
  IF amount >= 10000:
    -> Send to #high-value-deals Slack channel
    -> Assign to senior sales rep in CRM
    -> Create task in project management tool
  ELSE IF amount >= 1000:
    -> Send to #deals Slack channel
    -> Assign to sales team round-robin
  ELSE:
    -> Log to spreadsheet only
    -> Add to automated nurture sequence
```

### Step 5: Configure Error Handling

Define what happens when things go wrong:

- **Retry strategy**: Number of retries, backoff interval (e.g., 3 retries with exponential backoff: 1s, 4s, 16s)
- **Timeout**: Maximum wait time for destination response (recommend 30 seconds)
- **Dead letter queue**: Where to store failed events for manual review
- **Alerting**: Who gets notified on persistent failures and how
- **Idempotency**: How to handle duplicate webhook deliveries (use event ID for deduplication)

```
Error Handling:
  Retries: 3 (exponential backoff: 1s, 4s, 16s)
  Timeout: 30 seconds
  On failure after retries:
    -> Log to error tracking (Sentry/Datadog)
    -> Send alert to #ops-alerts Slack channel
    -> Store payload in dead letter queue for manual retry
  Deduplication: Use event.id field, ignore duplicates within 24h window
```

### Step 6: Generate Workflow Diagram

Present the workflow visually using ASCII or text-based diagrams:

```
[Stripe: payment.succeeded]
        |
        v
  {Amount >= $100?}
      /        \
    YES         NO
     |           |
     v           v
[Slack: #deals] [Log only]
     |
     v
[HubSpot: Create/Update Deal]
     |
     v
[Email: Send receipt]
```

### Step 7: Output Configuration

Provide the webhook endpoint configuration:

```json
{
  "webhook": {
    "endpoint": "/webhooks/stripe/payment-succeeded",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "X-Webhook-Secret": "${STRIPE_WEBHOOK_SECRET}"
    },
    "signature_verification": {
      "header": "Stripe-Signature",
      "algorithm": "HMAC-SHA256"
    }
  },
  "actions": [
    {
      "name": "notify_slack",
      "type": "http_post",
      "url": "${SLACK_WEBHOOK_URL}",
      "condition": "payload.amount >= 10000",
      "body_template": {
        "text": "New payment: ${{amount/100}} from {{customer_email}}"
      }
    }
  ]
}
```

## Best Practices

- Always verify webhook signatures to prevent spoofed requests
- Use HTTPS endpoints exclusively for webhook receivers
- Respond to webhooks with a 200 status quickly, then process asynchronously
- Log all incoming webhook payloads for debugging (redact sensitive data)
- Implement idempotency to handle duplicate deliveries gracefully
- Set up monitoring for webhook delivery failures and latency
- Document rate limits for both source and destination APIs
- Use environment variables for secrets, never hardcode API keys
- Test workflows with sample payloads before connecting to production events
- Version your webhook endpoints to allow non-breaking changes
- Consider webhook ordering -- events may not arrive in chronological order
