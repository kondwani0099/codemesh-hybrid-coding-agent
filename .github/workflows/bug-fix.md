# Bug Fix Workflow

## Purpose
Diagnose and fix a reported bug.

## Flow

```
Analyst
 → Root cause
 → Planner
 → Implementer
 → QA
 → Code Reviewer
```

## Steps

1. **Analyst** — reproduce and diagnose the root cause using local analysis.
2. **Planner** — produce a focused fix plan (`plan.md`).
3. **Implementer** — apply the smallest fix.
4. **QA** — add a regression test and verify the fix.
5. **Code Reviewer** — review the change.

## Quality Gates
- Root cause is documented before fixing.
- A regression test covers the bug.
- Tests pass.

## Artifacts
`analysis.md`, `plan.md`, `implementation.md`, `qa.md`, `review.md`.