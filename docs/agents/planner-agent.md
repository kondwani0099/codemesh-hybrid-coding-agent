# Planner Agent

## Purpose
Produces an implementation-ready plan.

## Inputs
- User request.
- Repository map.
- Compressed context (relevant files + summaries).

## Outputs
- A structured `plan.md` artifact.

## Rules
- Base the plan on actual repository context.
- Every step must be actionable without re-discovering the repository.
- Respect existing architecture and conventions.

See `.github/agents/planner.agent.md` and `.github/templates/plan.md`.