# Database Change Workflow

## Purpose
Change the database schema safely.

## Flow

```
Analyst
 → Database Agent
 → Planner
 → Implementer
 → QA
 → Schema review
```

## Steps

1. **Analyst** — document current schema and data usage.
2. **Database Agent** — design the change and migration (`migrations.md`).
3. **Planner** — coordinate code changes that use the new schema.
4. **Implementer** — apply migration and code changes.
5. **QA** — verify migrations and affected flows.
6. **Schema review** — review the final schema.

## Quality Gates
- Migrations are reversible and tested.
- Existing data remains valid.
- No destructive commands without approval.

## Artifacts
`plan.md`, `implementation.md`, `qa.md`, `schema-review.md`.