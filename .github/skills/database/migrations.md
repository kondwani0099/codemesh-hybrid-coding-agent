# Database Migrations

## Principles
1. One logical change per migration.
2. Migrations are ordered and idempotent where possible.
3. Forward and (where possible) reverse paths are defined.
4. Never edit an applied migration — create a new one.

## Template
```sql
-- up
ALTER TABLE invoices ADD COLUMN is_approved BOOLEAN NOT NULL DEFAULT FALSE;

-- down
ALTER TABLE invoices DROP COLUMN is_approved;
```

## Rules
- Test the down path.
- Handle NOT NULL additions with defaults or backfill.
- Coordinate with the `database` agent for schema review.

## Validation
- `up` then `down` then `up` applies cleanly.
- Existing rows remain valid.