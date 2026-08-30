---
name: api-contracts
description: Keeps backend API and frontend client in sync — schemas, compatibility, and versioning.
---

# API Contracts Skill

## Purpose
Ensure backend endpoints and frontend clients do not drift.

```
Backend endpoint
 → Request schema
 → Response schema
 → Frontend client
 → UI
```

## Rules
- Every endpoint has a documented request and response schema.
- Frontend DTOs mirror backend schemas.
- Detect and flag breaking changes.
- Prefer additive, backward-compatible changes.
- Version APIs when breaking changes are unavoidable.

## Compatibility
See `compatibility.md` for how to evaluate breaking changes.
See `versioning.md` for the versioning policy.

## Validation
- The frontend client compiles against the updated types.
- No documented endpoint changed without a contract update.