# Backend Change Workflow

## Purpose
Implement a backend-only change.

## Flow

```
Planner
 → Backend Agent (Python/FastAPI/Node)
 → Backend Reviewer
 → QA
```

## Steps

1. **Planner** — plan the backend change.
2. **Backend Agent** — implement following the stack skill.
3. **Backend Reviewer** — review architecture, logic, error handling, security.
4. **QA** — run backend tests and validations (pytest, ruff, mypy).

## Quality Gates
- Tests, lint, and type checks pass.
- Reviewer has no blocking issues.

## Artifacts
`plan.md`, `implementation.md`, `review.md`, `qa.md`.