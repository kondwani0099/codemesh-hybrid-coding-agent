---
name: context-management
description: Defines the complete context strategy — how agents decide what context to load, summarize, and compress before escalation.
---

# Context Management Skill

## Purpose
Minimize token usage and cost by ensuring agents load and send only the context they actually need.

## Core Principle
> **Agents must answer: "What do I actually need to know to perform this task?" before requesting additional context.**

## Context Pipeline

```
Repository
 → File discovery
 → Relevance analysis
 → File summaries
 → Relevant code extraction
 → Context compression
 → Cloud model (only if needed)
```

## Rules
1. Never read the entire repository.
2. Identify relevant files before reading anything.
3. Prioritize existing summaries and cache (`.codemesh/`).
4. Use local models for summarization.
5. Compress context before any cloud escalation.
6. Preserve important technical decisions.
7. Never summarize away critical implementation details.
8. Redact secrets before any cloud request.

## Cost Optimization Priority
```
CACHE
 → LOCAL MODEL
 → SMALL LOCAL CODING MODEL
 → CLOUD MODEL
```

See `context-rules.md`, `summarization.md`, and `relevance-scoring.md` for details.

## Validation
- Context sent to a cloud model should be below the configured limit (`max_context_tokens`).
- Every file included must be traceable to the user request or plan.