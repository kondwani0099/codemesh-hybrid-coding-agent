---
name: security
description: Reusable security knowledge — OWASP Top 10, standard and advanced security protocols, patching techniques, secrets management, and dependency security.
---

# Security Skill

## Purpose
Reusable security knowledge and defensive remediation standards for agents auditing, implementing, or patching code.

## Core Areas
- **OWASP Standards**: Web Application Top 10, API Security Top 10, and LLM Applications Top 10 (`owasp.md`).
- **Security Protocols**: Transport hardening (TLS 1.3), OAuth 2.1, OIDC, JWT hardening, zero-trust mTLS, and rate limiting (`protocols.md`).
- **Security Patching Techniques**: Parameterized queries, IDOR/BOLA fixes, cryptographic hardening (Argon2id, AES-GCM), SSRF egress filters, and safe deserialization (`patching-techniques.md`).
- **Secrets Management**: Redaction, environment variable isolation, and secret exclusion rules (`secrets.md`).
- **Dependency Security**: Software supply chain, CVE scanning, and minimal-version remediation (`dependency-security.md`).

## Rules
- Never send secrets, credentials, or tokens to cloud providers or unredacted logs.
- Exclude secret files from context:
  ```
  .env*
  *.pem
  *.key
  secrets/**
  credentials/**
  ```
- Redact secrets before any cloud model or logging request.
- Dangerous commands or destructive migrations require explicit approval.
- Follow the principle of least privilege and defense-in-depth across all code changes.
- Ensure all security patches include regression test coverage.

## Validation
- Security review passes for any change touching auth, data access, crypto, or external I/O.
- Zero known critical or high CVEs in active dependencies.
- All patches verified against OWASP standards without functional regression.