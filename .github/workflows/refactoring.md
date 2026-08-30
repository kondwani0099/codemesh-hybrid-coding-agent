# Refactoring Workflow

## Purpose
Improve code structure without changing behavior.

## Flow

```
Analyst
 → Architect
 → Planner
 → Implementer
 → QA
 → Code Reviewer
```

## Steps

1. **Analyst** — map the current structure and behavior.
2. **Architect** — propose the target structure (`architecture.md`).
3. **Planner** — sequence the refactor into safe steps.
4. **Implementer** — apply each step; keep behavior identical.
5. **QA** — run the full test suite after each milestone.
6. **Code Reviewer** — review.

## Rules
- No behavior change without explicit approval.
- Tests must pass after every milestone.
- Keep refactors incremental and reversible.

## Artifacts
`architecture.md`, `plan.md`, `implementation.md`, `qa.md`, `review.md`.