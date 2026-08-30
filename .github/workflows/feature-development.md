# Feature Development Workflow

## Purpose
Implement a new feature end-to-end with quality gates.

## Flow

```
Product
 → Planner
 → Analyst
 → Architect
 → Critic
 → Implementer
 → Code Reviewer
 → QA
 → UAT
 → Documentation
```

## Steps

1. **Product** — clarify the business goal and acceptance criteria.
2. **Planner** — produce an implementation-ready `plan.md`.
3. **Analyst** — gather relevant repository context (local analysis).
4. **Architect** — validate structural fit; produce `architecture.md` if impactful.
5. **Critic** — challenge the plan; resolve concerns.
6. **Implementer** — execute the plan, file by file (safety protocol).
7. **Code Reviewer** — review the diff; fix issues.
8. **QA** — run tests; drive the fix loop until green.
9. **UAT** — confirm acceptance criteria are met.
10. **Documentation** — update docs.

## Quality Gates
- Plan approved by the user before implementation.
- Review must PASS before QA.
- Tests must pass before UAT.
- UAT sign-off required for completion.

## Artifacts
`plan.md`, `architecture.md`, `implementation.md`, `review.md`, `qa.md`, `uat.md`.