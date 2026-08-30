# Release Workflow

## Purpose
Prepare and validate a release.

## Steps
1. Run the full test suite and linting.
2. Run security and dependency audits.
3. Update changelog and documentation.
4. Build artifacts.
5. Prepare deployment notes.
6. Deploy with user approval.

## Agents Involved
- **QA** — full test suite.
- **Security** — security/dependency audit.
- **Documentation** — changelog and docs.
- **DevOps** — build and deployment.

## Quality Gates
- All tests pass.
- No critical security findings.
- Deployment requires explicit approval.