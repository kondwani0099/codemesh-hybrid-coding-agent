# Dependency Security

## Rules
- Keep dependencies up to date.
- Pin versions for reproducibility where required.
- Run dependency vulnerability scans (`pip-audit`, `npm audit`, `osv-scanner`).
- Review license compatibility.
- Avoid adding dependencies for trivial functionality.

## Checklist
- [ ] No known critical vulnerabilities in direct dependencies.
- [ ] Transitive dependencies are scanned.
- [ ] New dependencies are justified.
- [ ] Lockfiles are committed where the project uses them.

## Validation
- `npm audit` / `pip-audit` report no critical issues.
- Dependency changes are reviewed.