# Security Audit Workflow

## Purpose
Review the codebase for security issues.

## Flow

```
Analyst
 → Security
 → Architect
 → Planner
 → Implementer
 → Security verification
```

## Steps

1. **Analyst** — map the attack surface (auth, data, external I/O).
2. **Security** — review against OWASP; produce `security-review.md`.
3. **Architect** — design remediation for structural findings.
4. **Planner** — sequence fixes.
5. **Implementer** — apply fixes.
6. **Security** — verify the fixes close the findings.

## Quality Gates
- Critical/high findings must be resolved or explicitly accepted.
- Secrets are never present in context or output.

## Artifacts
`security-review.md`, `plan.md`, `implementation.md`.