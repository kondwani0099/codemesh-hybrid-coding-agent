# Emergency Fix Workflow

## Purpose
Handle a critical, time-sensitive issue with minimal ceremony but preserved safety.

## Flow

```
Analyst
 → Implementer
 → QA (focused)
 → User approval
```

## Steps

1. **Analyst** — quick root-cause triage.
2. **Implementer** — apply the minimal emergency fix.
3. **QA** — run focused tests on the affected path.
4. **User approval** — explicit approval before any deployment.

## Rules
- Skip non-essential gates, but never skip user approval for destructive or production actions.
- Document the emergency separately for a later retrospective.

## Artifacts
`analysis.md`, `implementation.md`, `qa.md`.