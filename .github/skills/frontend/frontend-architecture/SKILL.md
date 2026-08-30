---
name: frontend-architecture
description: Frontend architecture principles — layering, state management, API clients, and performance.
---

# Frontend Architecture Skill

## Purpose
Standard frontend architecture principles that apply across Vue and React.

## Layering
```
Views/Pages
 → Containers
 → Components
 → Services (API client)
 → Backend
```

## Rules
- Views own routing and page-level state.
- Containers fetch data; presentational components render it.
- Services own all HTTP communication and DTO mapping.
- Keep business logic out of components where possible.

## State Management
- Server state (API data) should be cached and synchronized.
- Shared client state belongs in a store (Pinia/Redux/Zustand).
- Component state stays local.
- Avoid prop drilling with too many levels.

## API Client
- Single base URL configuration.
- Centralized error handling and auth tokens.
- Typed request/response DTOs.
- Align with `api-contracts` skill.

## Performance
- Lazy-load routes and heavy components.
- Memoize expensive computations.
- Virtualize long lists.
- Code-split large dependencies.

## Validation
- Lint, build, and unit tests pass.
- No unnecessary re-renders in profiler.