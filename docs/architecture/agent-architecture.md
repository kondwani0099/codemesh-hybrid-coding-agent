# Agent Architecture

## Definition
Agents are defined in `.github/agents/` as `.agent.md` files with YAML frontmatter (`name`, `description`). They define **who** does a task.

## Categories
- **Core** — orchestration, planning, analysis, design, critique.
- **Frontend** — Vue/React specialists and reviewers.
- **Backend** — Python/FastAPI/Node specialists and reviewers.
- **Data** — database and API-contract.
- **Quality** — security, code review, QA, UAT.
- **Delivery** — devops, documentation, retrospective.

## Lifecycle
1. **Invoke** — the orchestrator routes to a specialist.
2. **Load skills** — the agent loads relevant `SKILL.md` files for knowledge.
3. **Produce artifact** — the agent outputs a template-based artifact.
4. **Hand off** — the artifact becomes the next agent's input.

## Design Principles
- Agents stay lightweight; knowledge lives in skills.
- Each agent has a clear, non-overlapping role.
- Handoffs follow the templates and handoff rules.

See `docs/agents/agent-overview.md`.