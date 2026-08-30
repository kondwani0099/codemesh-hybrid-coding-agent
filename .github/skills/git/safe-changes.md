# Safe Changes

## Before Editing a File
1. Read the current version.
2. Understand the surrounding code.
3. Make the smallest required change.
4. Preserve unrelated code.

## After Editing
5. Validate syntax.
6. Review the diff.
7. Never blindly replace an entire file unless necessary.

## Command Safety
- Dangerous commands require confirmation:
  ```
  rm -rf
  DROP DATABASE
  git reset --hard
  git push --force
  production deployment
  ```

## Rollback
- Prefer `git checkout <file>` for reverting uncommitted single-file changes.
- Use `git revert` for committed changes (never rewrite history).
- Confirm with the user before any destructive rollback.