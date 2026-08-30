# Safety Rules

## Destructive Commands (require approval)
Never execute automatically without explicit user approval:

```
rm -rf
DROP DATABASE
git reset --hard
git push --force
production deployment
```

## Secrets
- Never send to cloud providers:
  ```
  .env files
  private keys
  SSH keys
  credentials
  tokens
  passwords
  certificates
  database dumps
  ```
- Excluded by default:
  ```
  .env*
  *.pem
  *.key
  secrets/**
  credentials/**
  ```
- Redact secrets before any cloud request.

## File Modification
- Read the current version before editing.
- Make the smallest required change.
- Preserve unrelated code.
- Validate syntax after editing.
- Review the diff.
- Never blindly replace an entire file unless necessary.

## Human Approval
- Respect approval gates (plan approval, implementation approval).
- Do not allow unrestricted autonomous execution initially.