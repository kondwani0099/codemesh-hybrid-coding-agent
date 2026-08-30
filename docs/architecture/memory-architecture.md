# Memory Architecture

## Purpose
What should survive across sessions vs what is temporary context.

## Distinction
- **Context** — task-specific, short-lived (per task).
- **Memory** — persistent knowledge reused across sessions.

## Memory Layers
1. **User memory** — preferences and patterns that apply everywhere.
2. **Repository memory** — facts about a specific codebase (conventions, commands, structure).
3. **Session memory** — task-specific working state (cleared after the session).

## Workspace Memory
Stored in `.codemesh/`:
```
.codemesh/
├── repository.json
├── architecture.json
├── files.json
├── summaries/
├── index/
├── tasks/
├── logs/
└── metrics/
```

See `docs/memory/memory-strategy.md` and `docs/memory/context-vs-memory.md`.