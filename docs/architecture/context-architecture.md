# Context Architecture

## Purpose
Minimize tokens sent to cloud models. The context pipeline:

```
Repository
 → File discovery
 → Relevance analysis
 → File summaries (local model)
 → Relevant code extraction
 → Context compression (local model)
 → Cloud model
```

## Key Components
- **File Relevance Engine** — ranks files by relevance to the request.
- **Summarizer** — compresses files with local models.
- **Compressor** — distills context to the essentials.
- **Cache** — `.codemesh/` stores summaries and indexes for reuse.

## Cost Priority
```
CACHE → LOCAL MODEL → SMALL LOCAL CODER → CLOUD MODEL
```

See `.github/skills/context-management/` for full rules.