---
name: git
description: Safe Git behavior — status, diff, branching, commits, and rollback. Never force push or destroy user work.
---

# Git Skill

## Purpose
Define safe Git behavior for agents operating inside real repositories.

## Rules
- Check `git status` before making changes.
- Review `git diff` after changes.
- Never `force push`.
- Never `git reset --hard` without explicit approval.
- Never destroy user work.
- Do not auto-commit unless explicitly configured.

## Before Implementation
```
git status
```
Ensure a clean base or a documented starting point.

## After Implementation
```
git diff
```
Show:
- files added
- files modified
- files deleted
- lines added
- lines removed

## Branching
See `branching.md`.
## Safe Changes
See `safe-changes.md`.

## Dangerous Commands (require approval)
- `rm -rf`
- `git reset --hard`
- `git push --force`
- production deployment

## Validation
- Diff is reviewed before any commit.
- No unrelated changes in the diff.