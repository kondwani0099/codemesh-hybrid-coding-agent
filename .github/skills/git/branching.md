# Git Branching

## Principles
- One branch per feature/bugfix.
- Branch names are descriptive: `feature/invoice-approval`, `fix/approval-status`.
- Keep branches short-lived.
- Rebase or merge strategies follow the project's convention.

## Rules
- Never commit directly to a protected branch.
- Pull latest before branching.
- Keep the branch focused; no unrelated commits.

## Validation
- Branch contains only the intended changes.
- `git status` is clean before branch operations.