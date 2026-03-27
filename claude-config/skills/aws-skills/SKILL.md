---
name: aws-skills
description: "AWS development skills for Claude Code. Provides expert guidance on AWS CDK infrastructure as code, serverless and event-driven architecture, cost optimization and monitoring, Bedrock AgentCore for AI agents, and MCP server integrations. Triggers on: AWS, CDK, Lambda, serverless, CloudWatch, cost optimization, Bedrock, AgentCore, infrastructure as code, Step Functions, EventBridge, S3, DynamoDB, IAM."
argument-hint: "<aws task description>"
license: MIT
---

# aws-skills -- AWS Development Skills

A collection of Claude Code plugins for AWS development with specialized knowledge and MCP server integrations. Covers CDK, serverless architecture, cost optimization, monitoring, and Bedrock AgentCore for AI agent deployment.

## Plugins Available

This skill contains 5 plugins located in `plugins/`:

| Plugin | Directory | Purpose |
|--------|-----------|---------|
| aws-common | `plugins/aws-common/` | Shared AWS MCP configuration (dependency for all others) |
| aws-cdk | `plugins/aws-cdk/` | CDK infrastructure as code best practices and patterns |
| aws-cost-ops | `plugins/aws-cost-ops/` | Cost optimization, CloudWatch monitoring, operational excellence |
| serverless-eda | `plugins/serverless-eda/` | Serverless and event-driven architecture patterns |
| aws-agentic-ai | `plugins/aws-agentic-ai/` | Bedrock AgentCore for deploying and managing AI agents |

## Usage

Each plugin has its own SKILL.md with detailed instructions. Load the relevant plugin skill for the task:

```bash
# CDK development
cat plugins/aws-cdk/skills/aws-cdk-development/SKILL.md

# Cost and operations
cat plugins/aws-cost-ops/skills/aws-cost-operations/SKILL.md

# Serverless / event-driven
cat plugins/serverless-eda/skills/aws-serverless-eda/SKILL.md

# Bedrock AgentCore
cat plugins/aws-agentic-ai/skills/aws-agentic-ai/SKILL.md

# Shared MCP setup
cat plugins/aws-common/skills/aws-mcp-setup/SKILL.md
```

## Key Principles

- **Do NOT explicitly specify resource names** in CDK constructs when optional -- let CDK generate unique names
- Use `NodejsFunction` for TypeScript/JS Lambda, `PythonFunction` for Python Lambda
- Always run `cdk synth` and validation before deploying
- MCP server names use short identifiers (e.g., `cdk`, `cw`, `pricing`) due to Bedrock's 64-char tool name limit

## Important

- If the user asks about AWS CDK, load the `aws-cdk` plugin skill
- If the user asks about costs or monitoring, load the `aws-cost-ops` plugin skill
- If the user asks about serverless or event-driven patterns, load the `serverless-eda` plugin skill
- If the user asks about AI agents or Bedrock, load the `aws-agentic-ai` plugin skill
