# API Versioning

## Strategy
- Prefer additive, backward-compatible changes.
- Use URL versioning (`/api/v1/...`) when breaking changes are required.
- Keep the previous version alive during a deprecation window.
- Document deprecation timelines.

## Rules
- Never silently change a released contract.
- Announce deprecations explicitly.
- Coordinate frontend migration with the backend version bump.
- Update the `api-contracts` documentation on every version change.

## Validation
- The API contract doc lists current and deprecated versions.
- No client references a removed field without a migration path.