# Example Workflow: Full-Stack Feature

## Request
> "Add a customer approval workflow to invoices, with a migration and API contract update."

## Agent Chain
```
Product      → requirements + acceptance criteria.
Analyst      → map invoices across backend, frontend, and database.
Database     → design is_approved migration.
API Contract → define the approve endpoint contract (breaking/non-breaking).
Planner      → coordinate backend + frontend + migration steps.
Architect    → verify structural fit.
Critic       → challenge the plan.
Implementer  → FastAPI endpoint + Vue store/button + migration.
Code Reviewer→ review diff.
QA           → run pytest + Vitest + migration checks.
UAT          → confirm the end-to-end flow.
```

## Quality Gates
- Migration reversible and tested.
- API contract updated on both sides.
- All tests pass before UAT.