---
name: vue
description: Vue conventions, component architecture, Composition API, state management, testing, and common mistakes.
---

# Vue Skill

## Purpose
Standard knowledge for building Vue frontends with CodeMesh.

## Rules
- Use existing component patterns.
- Prefer Composition API with `<script setup>` unless the project uses Options API.
- Avoid unnecessary global state.
- Use TypeScript where applicable.
- Preserve responsive design.
- Reuse components before creating new ones.
- Handle loading and error states on all async interactions.
- Validate API interactions.
- Avoid duplicated logic.

## Component Architecture
- Keep components focused and single-purpose.
- Split containers (data) from presentational components.
- Use Pinia for shared state; component-local state otherwise.
- Use Vue Router for navigation; lazy-load routes.

## API Integration
- Centralize API calls in a services layer.
- Map backend DTOs to typed interfaces.
- Handle API errors consistently.

## Testing
- Use Vitest + Vue Test Utils.
- Test component behavior, not implementation details.
- Mock API calls.

## Common Mistakes
- Over-using global state.
- Missing loading/error states.
- Ignoring TypeScript types for API data.
- Duplicating logic across components.
- Not cleaning up watchers/subscriptions.

## Validation
- `npm run lint`
- `npm run build`
- `npm test` (Vitest)