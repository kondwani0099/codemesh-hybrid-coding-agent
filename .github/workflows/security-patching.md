# Security Patching Workflow

## Purpose
Triage vulnerability findings, CVE alerts, and OWASP risks to formulate, apply, and verify targeted security patches without functional regression.

## Flow

```
Security / Analyst (Triage)
 → Security Patching (Remediation & Patching)
 → QA (Regression Testing)
 → Security (Verification & Re-audit)
 → Delivery / DevOps (Deployment)
```

## Steps

1. **Security / Analyst** — ingest vulnerability reports, SAST/DAST alerts, or CVE scans; assess severity and generate initial triage (`security-review.md`).
2. **Security Patching** — analyze root cause, formulate minimal non-breaking patch strategy, apply standard/advanced security protocols and patching recipes, generate regression tests, and write `security-patch.md`.
3. **QA** — execute full test suites and specialized regression tests to verify zero behavioral regression.
4. **Security** — verify the patch closes the vulnerability, complies with OWASP principles, and leaves no secondary exploit vectors.
5. **DevOps** — package and deploy patched code or updated dependencies.

## Quality Gates
- All critical and high findings resolved.
- Zero functional regression detected by QA suite.
- Security patch verified by Security Agent.
- Zero plaintext secrets committed or transmitted.

## Artifacts
`security-review.md`, `security-patch.md`, `qa.md`.
