# Performance Investigation Workflow

## Purpose
Investigate and fix a performance problem.

## Flow

```
Analyst
 → (local profiling)
 → Architect
 → Planner
 → Implementer
 → QA
```

## Steps

1. **Analyst** — identify the bottleneck with profiling evidence.
2. **Architect** — propose the performance strategy.
3. **Planner** — define measurable targets.
4. **Implementer** — apply optimizations.
5. **QA** — benchmark before/after; verify targets.

## Rules
- Base changes on measurements, not guesses.
- Preserve correctness while optimizing.
- Document trade-offs.

## Artifacts
`analysis.md`, `architecture.md`, `plan.md`, `implementation.md`, `qa.md`.