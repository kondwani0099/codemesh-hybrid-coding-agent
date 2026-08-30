

# CodeMesh — Hybrid Coding Agent Team

> A cost-optimized multi-agent workflow system for GitHub Copilot in VS Code.

## Quick Start

Bootstrap any project with the **reproducible one-liner installer** — it safely
copies the managed files, automatically backs up existing states, and validates
schema integrity:

### Linux / macOS / WSL
```bash
curl -fsSL https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.1/install.sh | bash
```

### Windows PowerShell
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iwr -useb https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.1/install.ps1 | iex
```

The installer downloads the CodeMesh framework at `v1.0.1`, snapshots any
existing CodeMesh files into `<project>/.codemesh/backups/<timestamp>/`, then
copies `.github/agents`, `.github/skills`, `.github/workflows`,
`.github/templates`, `.github/instructions` and a per-project `config/` into
your project — and finally validates the installed agent/skill schema.

> **Note**: Tune your per-project models and costs in
> `<project>/.codemesh/config/models.yaml` (and `costs.yaml`) after install.
> To overwrite existing CodeMesh files, re-run with `CODEMESH_FORCE=1`
> (PowerShell: `$env:CODEMESH_FORCE = "1"`).

### Install from a local clone (optional)

```bash
# 1. Install CodeMesh into a project (run from this repo)
python scripts/setup.py /path/to/your/project
python scripts/setup.py ../my-app --force    # overwrite existing CodeMesh files

# 2. Validate the framework (optional)
python scripts/validate-agents.py
python scripts/validate-skills.py
python scripts/check-links.py
```

Then open VS Code → Copilot Chat → select a CodeMesh agent (e.g. `codemesh`,
`planner`, `vue`, `python`, `qa`) and start a workflow. See
[`docs/getting-started/first-workflow.md`](docs/getting-started/first-workflow.md).

> **Version:** 1.0.1 — reproducible installer (`install.sh` / `install.ps1`).

## 1. Project Overview

**Project:** CodeMesh
**Repository:** `hybrid-coding-agent`

CodeMesh is a collection of specialized **VS Code GitHub Copilot custom agents** designed to work together as a structured software-development team.

The system is designed for real-world projects containing:

* Vue
* React
* Python
* FastAPI
* Node.js
* TypeScript
* JavaScript
* databases
* APIs
* DevOps infrastructure

The key difference is that CodeMesh introduces a **hybrid model strategy**.

Instead of forcing every agent operation through an expensive cloud model:

```text
VS Code Agent
     ↓
Cloud LLM
     ↓
Everything
```

CodeMesh encourages:

```text
VS Code Agent
      ↓
Local analysis
      ↓
Ollama
      ↓
Context / summaries
      ↓
Cloud model only when needed
```

The system therefore separates:

### Agent responsibility

Who should perform the work?

from:

### Model responsibility

Which model should provide the intelligence required for that work?

---

# 2. Core Philosophy

## Local First

Use local models whenever the task does not require expensive reasoning.

Examples:

* reading files
* summarizing files
* explaining existing code
* identifying relevant files
* extracting requirements
* reviewing simple changes
* summarizing test output
* maintaining agent context

## Cloud When Necessary

Use stronger API models for:

* complex architecture
* difficult debugging
* complicated implementation
* cross-domain reasoning
* major refactoring
* difficult security analysis
* ambiguous technical decisions

The system should never use a cloud model simply because it is available.

---

# 3. What CodeMesh Is NOT

CodeMesh is NOT:

* a replacement for VS Code
* a replacement for GitHub Copilot
* a standalone IDE
* a single autonomous coding agent
* a repository-wide AI that blindly reads every file
* an LLM hosting platform

CodeMesh is a **workflow and agent-definition system**.

The primary runtime is:

```text
VS Code
+
GitHub Copilot
+
Custom Agents
+
Agent Skills
+
Ollama
+
Optional Cloud APIs
```

---

# 4. Architecture

```text
                         CODEMESH
                            │
                    VS CODE + COPILOT
                            │
                 ┌──────────┴──────────┐
                 │                     │
          WORKFLOW AGENTS        SPECIALIST AGENTS
                 │                     │
                 │        ┌────────────┼────────────┐
                 │        │            │            │
                 │       Vue         React        Python
                 │      Agent        Agent        Agent
                 │        │            │            │
                 │        └────────────┼────────────┘
                 │                     │
                 ▼                     ▼
          Workflow Context       Domain Context
                 │                     │
                 └──────────┬──────────┘
                            │
                     LOCAL MODEL LAYER
                            │
                         Ollama
                            │
                     ┌──────┴──────┐
                     │             │
                  Gemma 4B      Qwen Coder
                     │             │
                  Summary       Code analysis
                  Context       Local fixes
                     │             │
                     └──────┬──────┘
                            │
                     CONTEXT PACKAGE
                            │
                            ▼
                     CLOUD MODEL
                            │
                  Complex reasoning
                            │
                            ▼
                   SPECIALIST AGENTS
                            │
                            ▼
                    Review / QA / UAT
```

---

# 5. Agent Team

CodeMesh should initially contain these agents.

| Agent         | Responsibility                     |
| ------------- | ---------------------------------- |
| Workflow      | Coordinates the overall task       |
| Product       | Defines business requirements      |
| Planner       | Creates implementation plan        |
| Analyst       | Investigates technical questions   |
| Architect     | Designs system-level changes       |
| Vue           | Vue frontend development           |
| React         | React frontend development         |
| Python        | Python/FastAPI backend development |
| Database      | Database/schema/migration work     |
| API           | API contract and integration work  |
| Security      | Security analysis                  |
| Critic        | Challenges plans and assumptions   |
| Implementer   | Coordinates implementation         |
| Code Reviewer | Reviews implementation             |
| QA            | Testing and verification           |
| UAT           | Business acceptance                |
| DevOps        | Build/deployment/release           |
| Retrospective | Captures lessons                   |
| Documentation | Technical documentation            |

Agents should be specialized rather than attempting to do everything.

---

# 6. Agent Separation of Concerns

Each agent must have a clearly defined responsibility.

For example:

### Planner

CAN:

* understand requirements
* inspect relevant project context
* create implementation plans
* identify affected agents
* identify dependencies
* identify risks

CANNOT:

* implement code
* modify application files

---

### Architect

CAN:

* evaluate architecture
* propose patterns
* identify integration requirements
* identify architectural risks

CANNOT:

* arbitrarily rewrite the implementation

---

### Vue Agent

CAN:

* inspect Vue files
* modify Vue components
* modify Pinia stores
* modify frontend API clients
* create frontend tests

SHOULD NOT:

* modify Python backend unless explicitly delegated

---

### Python Agent

CAN:

* inspect Python code
* modify FastAPI services
* modify routes
* modify models
* create backend tests

SHOULD NOT:

* redesign Vue UI

---

### Database Agent

CAN:

* inspect schemas
* design migrations
* modify database-related code
* validate indexes and constraints

SHOULD NOT:

* modify unrelated frontend code

---

### Code Reviewer

CAN:

* inspect changes
* identify bugs
* identify architectural problems
* identify security issues
* recommend corrections

CANNOT:

* silently modify implementation

---

# 7. Workflow Agent

The Workflow Agent is the coordinator.

Example user request:

> Add customer approval to invoices.

Workflow Agent determines:

```text
Business requirement
       ↓
Planner
       ↓
Architect
       ↓
     ┌─┴─────────────┐
     ↓               ↓
 Python Agent     Vue Agent
     ↓               ↓
Database Agent    API Agent
     └───────┬───────┘
             ↓
        Code Reviewer
             ↓
             QA
             ↓
            UAT
```

The workflow agent should not perform all the coding itself.

It coordinates the specialists.

---

# 8. Agent Handoffs

Agents must produce structured handoffs.

Example:

```markdown
# Backend Implementation Handoff

## Task

Add invoice approval workflow.

## Relevant Files

- backend/invoices/models.py
- backend/invoices/service.py
- backend/invoices/routes.py

## Current Architecture

Invoices currently support:

draft
submitted

## Required Change

Add:

approved
rejected

## API Changes

POST /invoices/{id}/approve

## Frontend Dependency

Vue agent must expose the approval action.

## Risks

Existing clients may assume only draft/submitted states.
```

The next agent can consume this rather than rediscovering everything.

---

# 9. Local Ollama Intelligence Layer

Ollama is NOT the agent system.

Ollama provides models that agents can use for inexpensive intelligence.

Primary models:

```text
Gemma 4B
Qwen Coder
```

Models must be configurable.

Example:

```yaml
models:

  summarizer:
    provider: ollama
    model: gemma4:4b

  analyzer:
    provider: ollama
    model: gemma4:4b

  local-coder:
    provider: ollama
    model: qwen-coder

  cloud:
    provider: configurable
    model: configurable
```

---

# 10. What Gemma 4B Does

Gemma 4B should primarily perform inexpensive context operations.

Examples:

```text
Read file
 ↓
Gemma
 ↓
Summary
```

```text
Test failure
 ↓
Gemma
 ↓
Error summary
```

```text
Large conversation
 ↓
Gemma
 ↓
Compact context
```

```text
Large source file
 ↓
Gemma
 ↓
Relevant implementation details
```

It should not automatically be treated as the primary implementation model.

---

# 11. Context Compression

This is a core CodeMesh feature.

Agents should avoid passing unnecessary context to cloud models.

Instead:

```text
50 files
 ↓
Local analysis
 ↓
10 relevant files
 ↓
Gemma summaries
 ↓
5 highly relevant files
 ↓
Compact context
 ↓
Cloud model
```

The cloud model receives only what it needs.

---

# 12. Context Package

Before invoking an expensive model, create a context package.

Example:

```markdown
# CodeMesh Context Package

## User Request

Add invoice approval.

## Project

FastAPI backend + Vue frontend.

## Backend Summary

...

## Frontend Summary

...

## Database Summary

...

## Relevant Files

### backend/invoices/service.py

...

### frontend/src/views/Invoice.vue

...

## Existing API Contract

...

## Constraints

...

## Open Questions

...
```

This is what gets passed to the stronger model.

---

# 13. Agent Skills

Create reusable skills separately from agents.

Structure:

```text
.github/
├── agents/
│   ├── workflow.agent.md
│   ├── planner.agent.md
│   ├── architect.agent.md
│   ├── vue.agent.md
│   ├── react.agent.md
│   ├── python.agent.md
│   ├── database.agent.md
│   ├── security.agent.md
│   ├── implementer.agent.md
│   ├── reviewer.agent.md
│   ├── qa.agent.md
│   └── uat.agent.md
│
└── skills/
    ├── context-management/
    ├── python/
    ├── fastapi/
    ├── vue/
    ├── react/
    ├── database/
    ├── api-contracts/
    ├── testing/
    ├── security/
    ├── git/
    └── documentation/
```

Skills should be loaded when relevant rather than duplicated into every agent.

---

# 14. Context Skill

Create a central `context-management` skill.

It should instruct agents to:

1. Determine what information is required.
2. Search only relevant files.
3. Use local models for summarization where possible.
4. Reuse existing summaries.
5. Avoid repeating expensive context.
6. Produce compact handoffs.
7. Escalate to cloud models only when justified.

---

# 15. Model Escalation

Agents should follow:

```text
Simple
 ↓
Local Ollama

Medium
 ↓
Local Ollama
 ↓
Escalate if confidence is low

Complex
 ↓
Cloud model

Critical
 ↓
Cloud model
 ↓
Human review
```

Do not automatically send everything to the cloud.

---

# 16. Confidence

Local analysis should include confidence.

Example:

```json
{
  "finding": "Invoice state is managed by InvoiceStatus enum",
  "confidence": 0.94,
  "source_files": [
    "models.py",
    "service.py"
  ]
}
```

If confidence is low:

```text
LOCAL MODEL
confidence < threshold
        ↓
additional analysis
        ↓
cloud escalation
```

---

# 17. Document-Driven Workflow

Agents should produce structured Markdown artifacts.

Example:

```text
agent-output/
├── analysis/
├── plans/
├── architecture/
├── reviews/
├── security/
├── qa/
├── uat/
└── retrospectives/
```

Example:

```text
agent-output/
└── 042/
    ├── analysis.md
    ├── plan.md
    ├── architecture.md
    ├── implementation.md
    ├── review.md
    ├── qa.md
    └── uat.md
```

All documents for one task share the same task ID.

---

# 18. Quality Gates

Recommended workflow:

```text
Planner
   ↓
Critic
   ↓
Architect
   ↓
Security
   ↓
Human approval
   ↓
Implementer
   ↓
Code Reviewer
   ↓
QA
   ↓
UAT
   ↓
DevOps
```

Agents may skip stages when appropriate, but the workflow must make the quality gates explicit.

---

# 19. Planner Rules

The planner produces:

```text
WHAT needs to change
WHY it needs to change
WHERE it needs to change
DEPENDENCIES
RISKS
TEST REQUIREMENTS
```

The planner should avoid prescribing low-level implementation unnecessarily.

---

# 20. Implementer Rules

The Implementer receives an approved plan.

It should:

1. Verify the plan.
2. Check relevant files.
3. Follow existing architecture.
4. Implement the required changes.
5. Write/update tests.
6. Review its own changes.
7. Report files modified.

It must not redesign the system simply because it prefers another architecture.

---

# 21. Code Review Gate

Code Reviewer checks:

```text
Correctness
Architecture
Maintainability
Security
Performance
Tests
API compatibility
Frontend/backend consistency
```

Output:

```text
PASS
```

or:

```text
CHANGES_REQUIRED
```

---

# 22. QA Agent

QA verifies:

* unit tests
* integration tests
* API behavior
* frontend behavior
* regression risk
* edge cases
* error handling

QA should not simply trust that tests pass.

---

# 23. UAT Agent

UAT asks:

> Did the implementation actually solve the business problem?

It validates the feature against the original requirement.

---

# 24. Security Agent

Security should review:

* authentication
* authorization
* input validation
* injection
* secrets
* API security
* dependency risks
* frontend security
* data exposure
* configuration

Security findings should be classified:

```text
CRITICAL
HIGH
MEDIUM
LOW
INFO
```

---

# 25. Cross-Agent Communication

Agents communicate through structured artifacts.

Example:

```text
Planner
 ↓
plan.md

Architect
 ↓
architecture.md

Security
 ↓
security.md

Implementer
 ↓
implementation.md

Reviewer
 ↓
review.md

QA
 ↓
qa.md

UAT
 ↓
uat.md
```

This creates an auditable chain.

---

# 26. Long-Term Memory

Memory should be treated as optional infrastructure.

CodeMesh should support a memory provider but should not make the entire project dependent on one proprietary memory service.

Possible memory:

```text
workspace decisions
architecture decisions
known constraints
previous implementation decisions
project conventions
known bugs
technical debt
```

The agent should distinguish:

```text
Current repository state
```

from:

```text
Historical memory
```

Repository state always has priority.

---

# 27. Repository Context

CodeMesh should not attempt to create a giant permanent repository summary.

Instead maintain targeted context:

```text
Frontend context
Backend context
Database context
API context
Infrastructure context
```

Each specialist agent owns its relevant context.

---

# 28. Example Vue + Python Workflow

User:

> Add approval functionality to Smart Invoice.

Workflow:

```text
Workflow Agent
       ↓
Planner
       ↓
Architect
       ↓
       ├──────────────┐
       ↓              ↓
 Python Agent      Vue Agent
       ↓              ↓
 Gemma analysis   Gemma analysis
       ↓              ↓
 Backend context  Frontend context
       └──────┬───────┘
              ↓
        Cloud Architect
              ↓
       Approved Plan
              ↓
       ┌──────┴──────┐
       ↓             ↓
 Python Agent     Vue Agent
       ↓             ↓
 Implementation Implementation
       └──────┬──────┘
              ↓
        Code Reviewer
              ↓
             QA
              ↓
             UAT
```

---

# 29. Agent Instructions

Every `.agent.md` must contain:

```text
---
name:
description:
tools:
handoffs:
---

# Role

# Responsibilities

# Constraints

# Workflow

# Context Requirements

# Model Strategy

# Output Format

# Handoff Rules
```

---

# 30. Agent Model Strategy

Agents should explicitly state which operations should use local models.

Example:

```markdown
## Model Strategy

Use local Ollama models for:

- file summarization
- simple code explanation
- context compression
- test output summarization

Escalate to a cloud model for:

- complex architectural decisions
- difficult debugging
- complex implementation
- ambiguous requirements
```

---

# 31. VS Code Native Integration

The repository must be designed around VS Code Custom Agents.

Users should be able to:

1. Clone the repository.
2. Copy `.github/agents` into their project.
3. Open VS Code.
4. Open GitHub Copilot Chat.
5. Select the desired agent.
6. Start the workflow.

No separate application should be required for the basic agent system.

---

# 32. User Experience

The experience should feel like having a software engineering team inside VS Code.

Example:

```text
You:
"Add customer approval to invoices."

Workflow Agent:

I'll coordinate this task.

→ Planner
→ Architect
→ Python Agent
→ Vue Agent
→ Security
→ Code Reviewer
→ QA
→ UAT
```

The user can invoke individual specialists when needed.

---

# 33. Individual Agent Usage

Users should be able to bypass the workflow.

Examples:

```text
@Vue
Fix the invoice table layout.

@Python
Investigate why invoice approval returns 403.

@Security
Audit the authentication middleware.

@Architect
Evaluate whether Redis should be introduced.

@QA
Create a test strategy for invoice approval.
```

The exact invocation mechanism must follow the current VS Code custom-agent behavior rather than inventing unsupported syntax.

---

# 34. Cost Transparency

When cloud models are used, record:

```text
model
provider
reason for escalation
input tokens
output tokens
estimated cost
```

Example:

```text
Cloud escalation

Reason:
Complex cross-stack implementation

Local analysis:
31,420 tokens

Cloud context:
7,820 tokens

Estimated cloud usage:
$0.06

Estimated full-cloud usage:
$0.31

Estimated savings:
80.6%
```

These figures should be estimates unless the provider supplies authoritative billing data.

---

# 35. Cost Optimization Principle

Never optimize merely by choosing the smallest model.

Optimize the entire workflow:

```text
Better context
      ↓
Fewer tokens
      ↓
Fewer requests
      ↓
Better model selection
      ↓
Lower cost
```

The objective is:

> **Maximum useful reasoning per cloud token.**

---

# 36. Git Safety

Agents must inspect:

```text
git status
git diff
```

before and after implementation.

Never automatically:

```text
git push
git reset --hard
delete branches
force push
deploy production
```

without explicit permission.

---

# 37. Secrets

Never include:

```text
.env
API keys
passwords
private keys
tokens
certificates
database credentials
```

in cloud context.

Use redaction.

---

# 38. Repository Installation

Provide an installation script that copies the CodeMesh agents and skills into:

```text
.github/agents/
.github/skills/
.github/workflows/
.github/templates/
.github/instructions/
```

Do not overwrite user-created agents without confirmation.

Installation scripts:
- Windows: `scripts/install.ps1 -Target <project>`
- Linux/macOS: `scripts/install.sh <project>`

Uninstall:
- Windows: `scripts/uninstall.ps1 -Target <project>`
- Linux/macOS: `scripts/uninstall.sh <project>`

---

# 39. Example Repository

The CodeMesh repository itself should look like:

```text
hybrid-coding-agent/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── .gitignore
├── .editorconfig
├── .markdownlint.json
│
├── .github/
│   ├── agents/
│   │   ├── codemesh.agent.md
│   │   ├── workflow.agent.md
│   │   ├── product.agent.md
│   │   ├── roadmap.agent.md
│   │   ├── analyst.agent.md
│   │   ├── planner.agent.md
│   │   ├── architect.agent.md
│   │   ├── critic.agent.md
│   │   ├── frontend/
│   │   │   ├── vue.agent.md
│   │   │   ├── react.agent.md
│   │   │   └── frontend-reviewer.agent.md
│   │   ├── backend/
│   │   │   ├── python.agent.md
│   │   │   ├── fastapi.agent.md
│   │   │   ├── node.agent.md
│   │   │   └── backend-reviewer.agent.md
│   │   ├── data/
│   │   │   ├── database.agent.md
│   │   │   └── api-contract.agent.md
│   │   ├── quality/
│   │   │   ├── security.agent.md
│   │   │   ├── code-reviewer.agent.md
│   │   │   ├── qa.agent.md
│   │   │   └── uat.agent.md
│   │   └── delivery/
│   │       ├── devops.agent.md
│   │       ├── documentation.agent.md
│   │       └── retrospective.agent.md
│   │
│   ├── skills/
│   │   ├── context-management/
│   │   ├── model-routing/
│   │   ├── ollama/
│   │   ├── frontend/
│   │   │   ├── vue/
│   │   │   ├── react/
│   │   │   └── frontend-architecture/
│   │   ├── backend/
│   │   │   ├── python/
│   │   │   ├── fastapi/
│   │   │   └── node/
│   │   ├── database/
│   │   ├── api-contracts/
│   │   ├── testing/
│   │   ├── security/
│   │   ├── git/
│   │   └── documentation/
│   │
│   ├── workflows/
│   │   ├── feature-development.md
│   │   ├── bug-fix.md
│   │   ├── refactoring.md
│   │   ├── security-audit.md
│   │   ├── api-change.md
│   │   └── ...
│   │
│   ├── templates/
│   │   ├── analysis.md
│   │   ├── plan.md
│   │   ├── architecture.md
│   │   ├── implementation.md
│   │   ├── code-review.md
│   │   ├── qa.md
│   │   ├── uat.md
│   │   └── context-package.md
│   │
│   └── instructions/
│       ├── global.md
│       ├── agent-rules.md
│       ├── safety-rules.md
│       ├── coding-rules.md
│       └── handoff-rules.md
│
├── config/
│   ├── codemesh.yaml
│   ├── models.yaml
│   ├── agents.yaml
│   ├── workflows.yaml
│   └── costs.yaml
│
├── scripts/
│   ├── install.ps1
│   ├── install.sh
│   ├── uninstall.ps1
│   ├── uninstall.sh
│   ├── validate-agents.py
│   ├── validate-skills.py
│   ├── check-links.py
│   └── generate-index.py
│
├── docs/
│   ├── getting-started/
│   ├── architecture/
│   ├── agents/
│   ├── models/
│   ├── workflows/
│   ├── skills/
│   ├── memory/
│   └── advanced/
│
├── examples/
│   ├── vue-python/
│   ├── react-node/
│   ├── full-stack/
│   └── security-audit/
│
├── tests/
│   ├── agents/
│   ├── skills/
│   ├── workflows/
│   └── fixtures/
│
├── agent-output/
└── .vscode/
```

---

# 40. MVP

Do not build a separate Python application first.

The MVP is the **agent repository itself**.

First implement:

```text
1. Workflow Agent
2. Planner
3. Architect
4. Vue Agent
5. React Agent
6. Python Agent
7. Database Agent
8. Implementer
9. Code Reviewer
10. QA
11. Security
12. UAT
```

Then add:

```text
13. Context Management Skill
14. Model Routing Skill
15. Ollama integration instructions
16. Cost optimization
17. Memory integration
```

---

# 41. Phase 2

Add specialized agents:

```text
API
DevOps
Documentation
Performance
Mobile
Flutter
Node
PHP
C/C++
```

---

# 42. Phase 3

Add advanced orchestration:

```text
parallel agents
automatic handoffs
agent delegation
dynamic workflow selection
local/cloud escalation
confidence scoring
context caching
```

---

# 43. Phase 4

Add optional external orchestration tooling if required.

The core system must remain usable directly inside VS Code.

---

# 44. Design Principle

The most important distinction in CodeMesh is:

```text
AGENT ≠ MODEL
```

An agent defines:

```text
role
responsibility
constraints
workflow
tools
handoffs
output
```

A model provides:

```text
reasoning
generation
analysis
summarization
coding ability
```

Therefore:

```text
Python Agent
    │
    ├── Gemma 4B for summarization
    │
    ├── Qwen Coder locally for code analysis
    │
    └── Cloud model for complex implementation
```

The agent remains the same even when the model changes.

---

# 45. Final Goal

CodeMesh should make AI-assisted development feel like working with an engineering organization rather than one giant chatbot.

```text
                    CODEMESH

                      USER
                       │
                       ▼
                WORKFLOW AGENT
                       │
          ┌────────────┼────────────┐
          │            │            │
       PLANNER      ANALYST     ARCHITECT
          │            │            │
          └────────────┼────────────┘
                       │
               SPECIALIST AGENTS
                       │
       ┌───────────────┼───────────────┐
       │               │               │
      VUE            REACT           PYTHON
       │               │               │
       └───────────────┼───────────────┘
                       │
                 LOCAL MODELS
                       │
                 Ollama/Gemma
                       │
                Context reduction
                       │
                       ▼
                 CLOUD MODEL
                       │
               Complex reasoning
                       │
                       ▼
                 IMPLEMENTATION
                       │
                       ▼
                 CODE REVIEW
                       │
                       ▼
                      QA
                       │
                       ▼
                      UAT
                       │
                       ▼
                    RELEASE
```

## Core proposition

**CodeMesh = Specialized VS Code agents + structured handoffs + local model intelligence + selective cloud escalation.**

The purpose is not simply to make AI coding more autonomous.

The purpose is to make it:

**more structured, more auditable, more specialized, and significantly more cost-efficient.**
