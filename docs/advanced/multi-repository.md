# Multi-Repository

## Purpose
Work across multiple repositories in a single task.

## Approach
- Each repository gets its own context cache (`.codemesh/`).
- The orchestrator routes work per repository.
- Handoffs include the repository identity.

## Rules
- Never mix context between repositories.
- Keep repository-scoped memory separate.
- Track which repo each artifact belongs to.

See `docs/architecture/overview.md` for the base architecture.