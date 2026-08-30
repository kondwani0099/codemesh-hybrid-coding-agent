# Workflow System

## Purpose
Workflows define **how** agents work together. They are documents in `.github/workflows/` that sequence agents and enforce quality gates.

## Available Workflows
- `feature-development.md`
- `bug-fix.md`
- `refactoring.md`
- `security-audit.md`
- `performance-investigation.md`
- `api-change.md`
- `frontend-change.md`
- `backend-change.md`
- `database-change.md`
- `emergency-fix.md`

## Common Structure
Each workflow defines:
- **Purpose**
- **Flow** (ordered agent chain).
- **Steps**.
- **Quality gates**.
- **Artifacts**.

## Selecting a Workflow
The orchestrator selects a workflow based on the task type. See `.github/agents/codemesh.agent.md`.