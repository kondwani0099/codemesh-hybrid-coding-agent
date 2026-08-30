# Example Workflow: Vue + Python

## Request
> "Add an approval workflow to invoices."

## Agent Chain
```
Product      → clarify "approval" requirements and acceptance criteria.
Analyst      → find invoice model, service, route, and Vue view (local analysis).
Planner      → produce plan.md (approval status field, migration, endpoint, UI button).
Architect    → verify structural fit.
Critic       → challenge the plan (status transitions, permissions).
Implementer  → add is_approved field, migration, approve endpoint, Vue button + store.
Code Reviewer→ review diff (naming, API consistency, unused imports).
QA           → run pytest + Vitest; fix loop until green.
UAT          → confirm the invoice approval flow meets the request.
Documentation→ update API docs.
```

## Artifacts Produced
`analysis.md`, `plan.md`, `architecture.md`, `implementation.md`, `review.md`, `qa.md`, `uat.md`.

## Model Usage
- Local (Gemma 4B): file identification, summaries, review.
- Local (Qwen): small code inspection.
- Cloud: plan + implementation.