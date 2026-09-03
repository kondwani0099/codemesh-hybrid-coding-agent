# Security Audit Workflow

## Purpose
Review the codebase for security issues.

## Flow

```
Analyst
 → Security
 → Architect / Planner (if structural)
 → Security Patching (apply remediations)
 → QA
 → Security verification
```

## Steps

1. **Analyst** — map the attack surface (auth, data, external I/O).
2. **Security** — review against OWASP; produce `security-review.md`.
3. **Architect / Planner** — design architectural remediation for structural findings.
4. **Security Patching** — apply standard/advanced patching protocols and fix flaws; produce `security-patch.md`.
5. **QA** — run regression tests.
6. **Security** — verify the fixes close the findings.

## Quality Gates
- Critical/high findings must be resolved or explicitly accepted.
- Secrets are never present in context or output.

## Artifacts
`security-review.md`, `plan.md`, `implementation.md`.