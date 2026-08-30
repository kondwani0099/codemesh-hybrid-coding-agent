# Memory Strategy

## Layers
1. **User memory** — cross-workspace preferences.
2. **Repository memory** — codebase facts (conventions, commands, structure).
3. **Session memory** — task-specific state (cleared after session).

## Repository Cache
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

## Rules
- Prefer short, factual entries.
- Update memory when facts change.
- Never store secrets in memory.

## Workspace vs Project
- Workspace memory applies to the whole environment.
- Repository memory is committed to the repo (or kept local via `.gitignore` for cache).

See `docs/architecture/memory-architecture.md` and `docs/memory/context-vs-memory.md`.