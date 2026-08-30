# Secrets

## Rules
- Secrets live in environment variables, never in source.
- Use a `.env` file (git-ignored) or a secret manager.
- Never commit `.env`, keys, tokens, or passwords.
- Redact secrets before any cloud request.
- Exclude by default:
  ```
  .env*
  *.pem
  *.key
  secrets/**
  credentials/**
  ```

## Handling
- Rotate secrets if they are ever exposed.
- Use least-privilege keys.
- Prefer short-lived credentials.

## Audit
- Search for hardcoded secrets in diffs before merging.
- Log secret access events without logging the secret values.