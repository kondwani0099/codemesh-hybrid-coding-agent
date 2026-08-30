# Using Agents

## Agent Definitions
Agents live in `.github/agents/` and are defined by `.agent.md` files with YAML frontmatter:

```yaml
---
name: planner
description: Produces an implementation-ready plan.
---
```

## Invoking an Agent
Mention the agent in a conversation, e.g.:

> "Planner, create a plan for invoice approval."

## Agent Categories

| Category | Agents |
|----------|--------|
| Core | codemesh, workflow, product, roadmap, analyst, planner, architect, critic |
| Frontend | vue, react, frontend-reviewer |
| Backend | python, fastapi, node, backend-reviewer |
| Data | database, api-contract |
| Quality | security, code-reviewer, qa, uat |
| Delivery | devops, documentation, retrospective |

## Agent Handoffs
Agents pass work via artifacts in `.github/templates/`. See `handoff-rules.md` in `.github/instructions/`.