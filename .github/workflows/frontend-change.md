# Frontend Change Workflow

## Purpose
Implement a frontend-only change.

## Flow

```
Planner
 → Frontend Agent (Vue/React)
 → Frontend Reviewer
 → QA
 → UAT
```

## Steps

1. **Planner** — plan the UI change.
2. **Frontend Agent** — implement components/state following the stack skill.
3. **Frontend Reviewer** — review UX, architecture, performance, accessibility.
4. **QA** — run frontend tests and build.
5. **UAT** — confirm the UI matches the request.

## Quality Gates
- Lint, build, and tests pass.
- Reviewer has no blocking issues.

## Artifacts
`plan.md`, `implementation.md`, `review.md`, `qa.md`, `uat.md`.