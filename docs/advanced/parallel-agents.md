# Parallel Agents

## Purpose
Run independent agent work concurrently to save time.

## When to Parallelize
- Independent file changes.
- Separate backend/frontend tasks with a stable contract.
- Independent investigations.

## Rules
- Never parallelize agents that depend on each other's output.
- Coordinate through artifacts.
- Merge results and run integration tests afterward.
- Keep shared state consistent (avoid concurrent edits to the same file).

## Caution
- Parallel edits to the same file cause conflicts.
- Prefer sequential handoffs unless independence is clear.