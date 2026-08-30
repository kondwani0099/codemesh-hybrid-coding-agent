---
name: database
description: Database conventions — schema design, indexes, migrations, and query optimization.
---

# Database Skill

## Purpose
Standard database knowledge for schema design, migrations, indexes, and queries.

## Rules
- Follow existing schema conventions.
- Pair every schema change with a migration.
- Consider existing data and backward compatibility.
- Add indexes for query patterns, not speculation.
- Use transactions for multi-step writes.
- Never run destructive commands without approval.

## Schema Design
- Use appropriate types and constraints.
- Normalize to a sensible degree; denormalize only for performance with justification.
- Use foreign keys for integrity.
- Name tables/columns consistently.

## Migrations
- One migration per logical change.
- Migrations must be reversible where possible.
- Test migrations against existing data.

## Indexes
- Index foreign keys and hot query columns.
- Use composite indexes for multi-column filters.
- Avoid redundant indexes.

## Query Optimization
- Profile slow queries.
- Avoid N+1 patterns.
- Use pagination for large result sets.

## Validation
- Migrations apply cleanly.
- Schema review passes (see `schema-review.md`).