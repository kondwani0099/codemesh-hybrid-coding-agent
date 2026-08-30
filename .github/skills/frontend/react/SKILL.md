---
name: react
description: React conventions, hooks, state management, routing, component architecture, testing, and common mistakes.
---

# React Skill

## Purpose
Standard knowledge for building React frontends with CodeMesh.

## Rules
- Use existing component patterns.
- Prefer functional components with hooks.
- Avoid unnecessary global state.
- Use TypeScript where applicable.
- Preserve responsive design.
- Reuse components before creating new ones.
- Handle loading and error states.
- Validate API interactions.
- Avoid duplicated logic.

## Component Architecture
- Keep components focused and composable.
- Split containers from presentational components.
- Use Context/Redux/Zustand for shared state only when needed.
- Use React Router for navigation; lazy-load routes.

## API Integration
- Centralize API calls in a services layer.
- Use typed interfaces for API data.
- Handle errors consistently with error boundaries and async states.

## Testing
- Use Vitest/Jest + React Testing Library.
- Test behavior, not implementation details.
- Mock API calls.

## Common Mistakes
- Re-rendering too often (missing memoization).
- Over-using global state.
- Missing loading/error states.
- Unstable dependencies in effects.
- Not cleaning up subscriptions.

## Validation
- `npm run lint`
- `npm run build`
- `npm test`