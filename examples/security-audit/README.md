# Security Audit Example

## Purpose
Demonstrates the security-audit workflow.

## Try It
> "Audit the authentication and authorization of the API."

## Workflow
1. **Analyst** — map the attack surface (auth, data, external I/O).
2. **Security** — review against OWASP; produce `security-review.md`.
3. **Architect** — design remediation for structural findings.
4. **Planner** — sequence fixes.
5. **Implementer** — apply fixes.
6. **Security** — verify fixes close the findings.

## Rules Applied
- Secrets are never sent to cloud models.
- Critical/high findings must be resolved or explicitly accepted.
- Dangerous commands require approval.

See `.github/workflows/security-audit.md`.