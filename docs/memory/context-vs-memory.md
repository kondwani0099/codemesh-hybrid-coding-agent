# Context vs Memory

## Context
- Task-specific.
- Short-lived (per task).
- What the current agent needs to know right now.
- Managed by the context pipeline (relevance → summary → compression).

## Memory
- Persistent.
- Survives across sessions.
- What should be remembered about the user/repo/system.
- Organized by scope (user, repository, session).

## Rule of Thumb
- If it's needed only for this task → **context**.
- If it should be remembered next time → **memory**.

## Cost Impact
Context is a direct cost driver (tokens). Memory, when cached locally, is nearly free and reduces future context needs.