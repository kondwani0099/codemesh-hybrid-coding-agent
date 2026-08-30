---
name: security
description: Reusable security knowledge — OWASP, authentication, authorization, secrets, dependency security, injection, and API security.
---

# Security Skill

## Purpose
Reusable security knowledge for agents reviewing or implementing code.

## Core Areas
- OWASP Top 10.
- Authentication and authorization.
- Secrets management.
- Dependency security.
- Injection defenses.
- API security.

See `owasp.md`, `secrets.md`, and `dependency-security.md`.

## Rules
- Never send secrets to cloud providers.
- Never log credentials or tokens.
- Exclude secret files from context:
  ```
  .env*
  *.pem
  *.key
  secrets/**
  credentials/**
  ```
- Redact secrets before any cloud request.
- Dangerous commands require approval.

## Validation
- Security review passes for any change touching auth, data, or external I/O.