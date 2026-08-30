# API Change Workflow

## Purpose
Change or add an API endpoint safely.

## Flow

```
Analyst
 → API Contract
 → Planner
 → Implementer
 → QA
 → API Contract verification
```

## Steps

1. **Analyst** — document current endpoint behavior.
2. **API Contract** — define request/response schemas; classify breaking vs non-breaking.
3. **Planner** — plan backend + frontend changes together.
4. **Implementer** — update backend, then the frontend client.
5. **QA** — test the contract on both sides.
6. **API Contract** — verify no drift.

## Quality Gates
- Breaking changes are approved and versioned.
- Frontend client compiles against new types.

## Artifacts
`analysis.md`, `plan.md`, `implementation.md`, `qa.md`.