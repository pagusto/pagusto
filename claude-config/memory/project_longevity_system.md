---
name: Longevity Agent System
description: Multi-agent longevity optimization platform — 12 domain agents + orchestrator, Notion hub, Gmail notifications, Oura Ring + Samsung Watch
type: project
---

Multi-agent longevity optimization system at `longevity/` directory.

**Architecture**: 12 domain agents + 1 orchestrator in hierarchical-mesh topology.
- Agents: Sleep, Nutrition, Gym, Biometrics, Supplements, Grocery, Peptides, TRT, Hydration, Recovery, Mindfulness, Nootropics
- Event bus for inter-agent communication
- Notion as central data hub (13 databases, all in Spanish)
- Gmail for 3 daily notifications (8am, 2pm, 9pm)
- Oura Ring + Samsung Watch integration

**Why:** Paul wants automated health tracking and optimization with intelligent cross-agent coordination (e.g., low readiness → adjust workout, supplement interactions → safety alerts).

**How to apply:** When working on this project, all Notion content in Spanish, code in English. Agents communicate via events, never write to each other's DBs. Orchestrator resolves conflicts using priority matrix.
