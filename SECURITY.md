# Security Policy

## Reporting a Vulnerability

CodeMesh handles repository context, code, and model APIs. If you discover a
security vulnerability, **do not** open a public issue. Instead, report it
privately to the maintainers.

Please include:

- The affected component and version.
- A description of the vulnerability.
- Steps to reproduce.
- Any potential impact.

## Security Principles

CodeMesh is designed around the following rules:

- **Never send secrets to cloud providers.** `.env` files, private keys, SSH
  keys, credentials, tokens, passwords, and certificates are excluded by
  default and must be redacted before any cloud request.
- **Never expose API keys.** All credentials are read from environment
  variables, never committed.
- **Controlled execution.** Dangerous commands require explicit user approval.
- **Agent permissions.** Agents operate with the minimum set of tools needed
  for their role.

## Excluded Patterns (default)

```
.env*
*.pem
*.key
secrets/**
credentials/**
```

## Model API Safety

- Do not hardcode model API keys.
- Use environment variables for all secrets.
- Redact sensitive repository content before it is sent to external models.

## Reporting Process

1. Reporter submits a private report.
2. Maintainers acknowledge within 5 business days.
3. Maintainers investigate and prepare a fix.
4. A security advisory is published after the fix is released.