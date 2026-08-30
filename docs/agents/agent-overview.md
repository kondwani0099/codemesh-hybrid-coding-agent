# Agent Overview

## What Agents Are
Agents define **who** works on a task. Each is a lightweight `.agent.md` file with:
- YAML frontmatter (`name`, `description`).
- Role and responsibilities.
- Rules.
- Inputs, outputs, and handoffs.

## Where They Live
`.github/agents/` — organized by category:
- `frontend/`
- `backend/`
- `data/`
- `quality/`
- `delivery/`

## How They Work Together
```
Orchestrator routes → specialist produces artifact → handoff → next specialist
```

## How to Modify
See `CONTRIBUTING.md` and run `scripts/validate-agents.py` after changes.