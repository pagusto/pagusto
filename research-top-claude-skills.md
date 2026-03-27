# Resumen Ejecutivo: Top Skills de Claude Code 2026

**Fecha:** 2026-03-27
**Fuentes analizadas:** 15+ (GitHub repos, blogs, npm, artículos especializados)
**Método:** WebSearch multi-query, GitHub raw fetch, análisis cruzado de fuentes

---

## Hallazgos Principales

1. El ecosistema de skills de Claude Code ha explotado: de ~50 skills en mid-2025 a **1,300+ skills** en marzo 2026
2. Las skills funcionan cross-platform: Claude Code, Cursor, Codex, Gemini CLI, y 39+ agentes más
3. El método de instalación estándar es `npx skills add <org>/<repo>` (Vercel Labs)
4. Las skills más útiles suelen ser las que uno construye para su propio workflow

---

## TOP SKILLS RECOMENDADAS PARA INSTALAR

### TIER 1 — Esenciales (Instalar Primero)

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 1 | **Frontend Design** (Oficial Anthropic) | Guía React + Tailwind, evita "AI slop" | `npx skills add anthropics/claude-code --skill frontend-design` |
| 2 | **Web Artifacts Builder** (Oficial) | Crea artifacts HTML con React, Tailwind, shadcn/ui | `npx skills add anthropics/claude-code --skill web-artifacts-builder` |
| 3 | **MCP Builder** (Oficial) | Crea servidores MCP de alta calidad | `npx skills add anthropics/claude-code --skill mcp-builder` |
| 4 | **Webapp Testing** (Oficial) | Testing web con Playwright | `npx skills add anthropics/claude-code --skill webapp-testing` |
| 5 | **Skill Creator** (Oficial) | Crea tus propias skills interactivamente | `npx skills add anthropics/claude-code --skill skill-creator` |
| 6 | **Systematic Debugging** (Superpowers) | Debugging metódico: modelo mental → root cause → fix | Ya instalado via Superpowers |
| 7 | **TDD** (Superpowers) | Test-Driven Development con subagentes | Ya instalado via Superpowers |
| 8 | **Code Review** (Superpowers) | Review paralelo multi-agente | Ya instalado via Superpowers |

### TIER 2 — Productividad Avanzada

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 9 | **Antigravity Awesome Skills** | Librería de 1,326+ skills instalables | `npx antigravity-awesome-skills --claude` |
| 10 | **Everything Claude Code (ECC)** | Sistema de optimización: skills, memoria, seguridad | `git clone https://github.com/affaan-m/everything-claude-code` |
| 11 | **ECC AgentShield** | Auditor de seguridad para configs de agentes | `npx ecc-agentshield scan` |
| 12 | **Claude Starter** | Framework 40+ skills, TOON format (ahorra 30-60% tokens) | `npx create-claude-starter@latest` |
| 13 | **Valyu** (Research/Data) | Búsqueda web + 36 fuentes (SEC, PubMed, etc.) | `npx skills add valyuAI/skills` |
| 14 | **Shannon** (Security) | Pen testing autónomo, 96% éxito en exploits | `npx skills add unicodeveloper/shannon` |
| 15 | **Composio** | Integración con 850+ apps SaaS | `npx skills add composio/skills` |

### TIER 3 — Documentos y Creatividad

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 16 | **DOCX** (Oficial) | Crear/editar documentos Word | `npx skills add anthropics/claude-code --skill docx` |
| 17 | **PDF** (Oficial) | Manipulación de PDFs | `npx skills add anthropics/claude-code --skill pdf` |
| 18 | **PPTX** (Oficial) | Crear presentaciones PowerPoint | `npx skills add anthropics/claude-code --skill pptx` |
| 19 | **XLSX** (Oficial) | Operaciones con Excel | `npx skills add anthropics/claude-code --skill xlsx` |
| 20 | **Algorithmic Art** | Arte generativo con p5.js | `npx skills add anthropics/claude-code --skill algorithmic-art` |
| 21 | **Canvas Design** | Crear arte visual en PNG/PDF | `npx skills add anthropics/claude-code --skill canvas-design` |
| 22 | **D3.js Skill** | Visualizaciones con D3.js | `npx skills add chrisvoncsefalvay/claude-d3js-skill` |
| 23 | **Frontend Slides** | Presentaciones HTML animadas | `npx skills add zarazhangrui/frontend-slides` |

### TIER 4 — DevOps e Infraestructura

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 24 | **cc-devops-skills** | IaC para múltiples plataformas | `npx skills add akin-ozer/cc-devops-skills` |
| 25 | **CI/CD Pipeline Builder** | Detección de stack + generación de pipelines | Via alirezarezvani/claude-skills |
| 26 | **Incident Commander** | Playbooks de respuesta a incidentes | Via alirezarezvani/claude-skills |
| 27 | **Performance Profiler** | Profiling Node/Python/Go | Via alirezarezvani/claude-skills |
| 28 | **Database Designer** | Análisis de schemas, ERD, optimización de índices | Via alirezarezvani/claude-skills |

### TIER 5 — Marketing y Negocio

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 29 | **Marketing Skills** (43 skills) | Content, SEO, CRO, Growth, Sales | `npx skills add coreyhaines31/marketingskills` |
| 30 | **Product Manager** | Gestión de producto, PRDs, roadmaps | Via alirezarezvani/claude-skills |
| 31 | **C-Level Advisory** (28 skills) | Asesoría CEO, CFO, CTO, COO, CMO | Via alirezarezvani/claude-skills |
| 32 | **SaaS Metrics Coach** | ARR, MRR, churn, LTV, CAC | Via alirezarezvani/claude-skills |

### TIER 6 — Seguridad

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 33 | **Trail of Bits Security** | Auditoría de código, CodeQL, Semgrep | `npx skills add trailofbits/skills` |
| 34 | **OWASP Security** | OWASP Top 10:2025, ASVS 5.0 | Via BehiSecc/awesome-claude-skills |
| 35 | **Security Auditor** | Detección de código malicioso pre-instalación | Via alirezarezvani/claude-skills |

### TIER 7 — Investigación y Ciencia

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 36 | **Scientific Skills** | Workflows científicos y de investigación | `npx skills add K-Dense-AI/claude-scientific-skills` |
| 37 | **RAG Architect** | Pipelines RAG, chunking, retrieval | Via alirezarezvani/claude-skills |
| 38 | **NotebookLM** | Análisis profundo multi-fuente (ya instalado) | Ya instalado |
| 39 | **yt-research** | Búsqueda en YouTube (ya instalado) | Ya instalado |

### TIER 8 — Orquestación y Plugins

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 40 | **Superpowers** | Subagentes paralelos, TDD, debugging | Ya instalado |
| 41 | **GSD** | Get Shit Done — proyecto de cero a deploy | Ya instalado |
| 42 | **Claude Squad** | Múltiples instancias Claude en terminal | `npm install -g claude-squad` |
| 43 | **Claude Swarm** | Sesión conectada a swarm de agentes | `git clone https://github.com/parruda/claude-swarm` |
| 44 | **Auto-Claude** | Multi-agente autónomo con kanban UI | `git clone https://github.com/AndyMik90/Auto-Claude` |

### TIER 9 — Herramientas de Productividad

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 45 | **OpenPaw** | 38 skills: git, Telegram, Discord, Obsidian, etc. | `npx pawmode` |
| 46 | **Fullstack Dev Skills** | 65 skills para desarrollo fullstack | `git clone https://github.com/jeffallan/claude-skills` |
| 47 | **Context Engineering Kit** | Técnicas de context engineering | `git clone https://github.com/NeoLabHQ/context-engineering-kit` |
| 48 | **Expo Skills** (Oficial) | Desarrollo de apps con Expo | `npx skills add expo/skills` |
| 49 | **shadcn/ui** | Componentes y patrones shadcn | Via ui.shadcn.com/docs/skills |
| 50 | **Playwright Skill** | Automatización de browser | `npx skills add lackeyjb/playwright-skill` |

### TIER 10 — Utilidades y Calidad de Vida

| # | Skill | Qué hace | Comando de instalación |
|---|-------|----------|----------------------|
| 51 | **Internal Comms** (Oficial) | Reportes de estado, newsletters | `npx skills add anthropics/claude-code --skill internal-comms` |
| 52 | **Brand Guidelines** (Oficial) | Colores y tipografía Anthropic | `npx skills add anthropics/claude-code --skill brand-guidelines` |
| 53 | **Slack GIF Creator** (Oficial) | GIFs animados para Slack | `npx skills add anthropics/claude-code --skill slack-gif-creator` |
| 54 | **Web Asset Generator** | Favicons, app icons, social media | `npx skills add alonw0/web-asset-generator` |
| 55 | **iOS Simulator** | Build y test de apps iOS | `npx skills add conorluddy/ios-simulator-skill` |

---

## Paquetes Completos (Instalan Múltiples Skills de Una Vez)

| Paquete | Skills incluidas | Comando |
|---------|-----------------|---------|
| **Antigravity Essentials** | Bundle esencial multi-categoría | `npx antigravity-awesome-skills --claude` |
| **alirezarezvani/claude-skills** | 205 skills en 9 dominios | `/plugin marketplace add alirezarezvani/claude-code-skills` |
| **Everything Claude Code** | Skills + memoria + seguridad | `git clone https://github.com/affaan-m/everything-claude-code` |
| **Claude Starter** | 40+ skills + TOON format | `npx create-claude-starter@latest` |
| **Superpowers** | 10+ skills dev (TDD, debug, review) | Ya instalado |
| **GSD** | 55+ comandos proyecto | Ya instalado |

---

## Tendencias Identificadas

1. **Cross-platform**: Las skills ya no son solo para Claude — funcionan en 39+ agentes
2. **Seguridad primero**: AgentShield y similares auditan configs antes de usarlas
3. **Subagentes paralelos**: La tendencia es dividir trabajo en múltiples agentes simultáneos
4. **Progressive disclosure**: Skills inteligentes que solo cargan cuando son relevantes (~100 tokens de overhead)
5. **Bundles**: Se empaquetan múltiples skills en instaladores únicos

## Recomendaciones

### Para instalar YA (mayor impacto inmediato):
1. Skills oficiales de Anthropic (frontend-design, docx, pdf, pptx, xlsx, mcp-builder)
2. ECC AgentShield (seguridad)
3. Valyu (research)
4. Antigravity Essentials (bundle completo)

### Ya tienes instalado:
- Superpowers (10+ skills de desarrollo)
- GSD (55+ comandos de proyecto)
- yt-research (YouTube research)
- NotebookLM (análisis profundo)
- Pensador (orquestador de research)

---

## Fuentes

- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
- [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [vercel-labs/skills](https://github.com/vercel-labs/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills)
- [raintree-technology/claude-starter](https://github.com/raintree-technology/claude-starter)
- [Anthropic Claude Code Docs](https://code.claude.com/docs/en/skills)
- [Composio - Top Claude Skills](https://composio.dev/content/top-claude-skills)
- [Firecrawl - Best Claude Code Skills](https://www.firecrawl.dev/blog/best-claude-code-skills)
- [OpenAIToolsHub - 349 Skills Ranked](https://www.openaitoolshub.org/en/blog/best-claude-code-skills-2026)
- [Pulumi - Top 8 DevOps Skills](https://www.pulumi.com/blog/top-8-claude-skills-devops-2026/)
