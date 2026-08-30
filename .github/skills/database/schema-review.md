# Database Schema Review

## What to Review
- Column types and constraints.
- Nullability and defaults.
- Foreign keys and referential integrity.
- Index coverage for known queries.
- Naming consistency.
- Migration reversibility.

## Checklist
- [ ] No `SELECT *` in application queries.
- [ ] No N+1 query patterns.
- [ ] Indexes exist for foreign keys and hot filters.
- [ ] Sensitive columns are protected (encryption at rest where required).
- [ ] Migrations are reversible and tested.
- [ ] Changes are backward compatible (or explicitly approved as breaking).

## Output
- PASS/FAIL with specific findings and recommendations.