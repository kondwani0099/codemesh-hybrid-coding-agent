# Feature Workflow

The standard feature workflow:

```
Product → Planner → Analyst → Architect → Critic
 → Implementer → Code Reviewer → QA → UAT → Documentation
```

## Quality Gates
1. Plan approved by the user before implementation.
2. Review PASS before QA.
3. Tests pass before UAT.
4. UAT sign-off for completion.

## Artifacts
`plan.md`, `architecture.md`, `implementation.md`, `review.md`, `qa.md`, `uat.md`.

See `.github/workflows/feature-development.md`.