---
name: webhook-automator
description: Designs webhook-based automation workflows with trigger-action mappings, payload schemas, and conditional routing
---

# Webhook Automator

## Overview

This skill designs webhook-based automation workflows that connect tools and services. It creates endpoint configurations, maps triggers to actions across platforms, generates payload schemas and transformation logic, and handles conditional routing and error recovery. The output includes workflow diagrams, configuration files, and implementation guides.

## When to Use This Skill

- When a user needs to connect two or more tools via webhooks (e.g., CRM to Slack)
- When designing event-driven automation pipelines
- When creating payload transformation logic between incompatible APIs
- When setting up conditional routing based on event data
- When documenting automation workflows for a team
- When troubleshooting or optimizing existing webhook integrations

## How It Works

1. **Requirement Gathering**: Identify the trigger event, source system, and target actions
2. **Workflow Design**: Map the complete flow from trigger to final action(s)
3. **Endpoint Configuration**: Define webhook URLs, methods, headers, and authentication
4. **Payload Mapping**: Create schemas and transformation logic between systems
5. **Conditional Logic**: Add branching, filtering, and routing rules
6. **Error Handling**: Define retry strategies, fallbacks, and alerting
7. **Documentation**: Output workflow diagrams and configuration files

## Instructions

### Workflow Design Process

For every automation request, define these components:

1. **Trigger**: The event that initiates the workflow
   - Source system (e.g., Stripe, Shopify, GitHub)
   - Event type (e.g., `payment.completed`, `order.created`, `push`)
   - Webhook URL and HTTP method

2. **Processing**: Transformation and logic applied to the payload
   - Data extraction and mapping
   - Conditional branching
   - Data enrichment (lookups to other systems)

3. **Action(s)**: The outcome(s) executed in target systems
   - Target system and API endpoint
   - Mapped payload
   - Expected response and success criteria

### Endpoint Configuration Template

```yaml
webhook:
  name: "[descriptive-name]"
  url: "https://your-domain.com/webhooks/[path]"
  method: POST
  headers:
    Content-Type: "application/json"
    Authorization: "Bearer ${WEBHOOK_SECRET}"
    X-Webhook-Source: "[source-system]"
  authentication:
    type: "hmac-sha256"
    secret_env: "WEBHOOK_SIGNING_SECRET"
    header: "X-Signature-256"
  rate_limit:
    max_requests: 100
    window_seconds: 60
  timeout_ms: 5000
```

### Payload Schema Design

Always define both the incoming and outgoing payload schemas:

```json
{
  "incoming": {
    "event_type": "string",
    "timestamp": "ISO 8601",
    "data": {
      "id": "string",
      "amount": "number",
      "currency": "string",
      "customer": {
        "email": "string",
        "name": "string"
      }
    }
  },
  "outgoing": {
    "channel": "#sales-notifications",
    "text": "New payment of {{data.currency}} {{data.amount}} from {{data.customer.name}}",
    "metadata": {
      "source_event_id": "{{data.id}}"
    }
  }
}
```

### Transformation Logic

When source and target schemas differ, provide explicit mapping:

```
Source Field              -> Target Field              Transform
----------------------------------------------------------------------
data.amount_cents         -> payment.amount            divide by 100
data.customer.full_name   -> contact.first_name        split on space, take [0]
data.customer.full_name   -> contact.last_name         split on space, take [1:]
data.created_at (unix)    -> event.timestamp            convert to ISO 8601
data.status               -> deal.stage                 map: "paid" -> "Won"
```

### Conditional Routing

Define routing rules clearly:

```yaml
routing:
  - condition: "data.amount >= 10000"
    action: "notify_sales_team"
    channel: "#high-value-deals"
  - condition: "data.amount >= 1000 AND data.amount < 10000"
    action: "notify_sales_channel"
    channel: "#sales"
  - condition: "data.customer.country NOT IN ['US', 'CA']"
    action: "notify_international_team"
    channel: "#international-sales"
  - default:
    action: "log_event"
    destination: "webhook_events_table"
```

### Error Handling Strategy

Every workflow must include error handling:

1. **Retry Policy**: Define retry count, backoff strategy, and intervals
   ```yaml
   retry:
     max_attempts: 3
     backoff: exponential
     initial_delay_ms: 1000
     max_delay_ms: 30000
   ```

2. **Dead Letter Queue**: Where failed events go after retries are exhausted
3. **Alerting**: Notify the team when failures occur (Slack, email, PagerDuty)
4. **Idempotency**: Use event IDs to prevent duplicate processing
5. **Validation**: Check payload structure before processing

### Common Integration Patterns

Provide platform-specific guidance for these common tools:

- **CRM** (HubSpot, Salesforce): Contact creation, deal updates, activity logging
- **Email** (SendGrid, Mailchimp): Triggered sends, list management, event tracking
- **Slack**: Channel messages, DMs, interactive messages with buttons
- **Project Management** (Asana, Jira, Linear): Task creation, status updates
- **Payment** (Stripe, PayPal): Payment events, subscription changes, refunds
- **E-commerce** (Shopify, WooCommerce): Order events, inventory updates

### Workflow Diagram Format

Present workflows as text-based diagrams:

```
[Stripe: payment.succeeded]
        |
        v
  [Validate Payload]
        |
        v
  [Extract Customer Data]
        |
        +---> [amount >= $10k] ---> [Slack: #high-value] + [CRM: Create VIP Deal]
        |
        +---> [amount < $10k]  ---> [Slack: #sales] + [CRM: Create Standard Deal]
        |
        v
  [Log to Analytics DB]
```

### Security Best Practices

- Always verify webhook signatures before processing payloads
- Use HTTPS endpoints exclusively
- Store secrets in environment variables, never in configuration files
- Implement IP allowlisting where the source platform supports it
- Set appropriate rate limits to prevent abuse
- Log all incoming webhooks for audit purposes
- Rotate signing secrets on a regular schedule
- Validate and sanitize all incoming data before use

### Best Practices

- Design workflows to be idempotent so replaying events is safe
- Include a unique event ID in every payload for deduplication
- Keep transformation logic simple; break complex workflows into stages
- Monitor webhook latency and set appropriate timeouts
- Document every workflow with a diagram, payload examples, and owner contact
- Test workflows with sample payloads before deploying to production
- Version your webhook endpoints (e.g., `/v1/webhooks/payments`) to support migrations
- Plan for the source system being unavailable (queue events for later processing)
