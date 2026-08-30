# API Contract Compatibility

## Breaking vs Non-Breaking

### Non-Breaking (safe)
- Adding a new optional field to a response.
- Adding a new endpoint.
- Adding a new optional request parameter.
- Relaxing validation (widening accepted input).

### Breaking (requires approval/versioning)
- Removing or renaming a field.
- Changing a field's type.
- Making an optional field required.
- Changing status codes or error shapes.
- Changing auth requirements.

## Evaluation Flow
1. Compare old and new schemas.
2. Classify each change as breaking or non-breaking.
3. Flag breaking changes to the API Contract agent and the user.
4. Coordinate versioning or a coordinated frontend/backend update.

## Validation
- The compatibility report lists every change and its classification.