# Relevance Scoring

## Purpose
Rank repository files by how relevant they are to a user request before loading them.

## Classification
Files are classified into four tiers:

| Tier | Meaning | Action |
|------|---------|--------|
| Critical | Directly referenced by the request | Load in full |
| Relevant | Strongly related | Load relevant sections |
| Possibly relevant | Weakly related | Summarize only |
| Irrelevant | Unrelated | Skip |

## Keyword Discovery
Given a request like *"Add invoice approval"*, search for:

- `invoice`, `approval`, `status`, `workflow`
- `routes`, `models`, `services`, `components`, `api`

## Scoring
```
score = weighted match of (name, path, symbols, imports, keywords)
```

Return a ranked list:

```json
[
  { "file": "backend/invoices/service.py", "score": 0.96 },
  { "file": "backend/invoices/models.py", "score": 0.94 },
  { "file": "frontend/src/views/Invoice.vue", "score": 0.91 }
]
```

## Rules
- Only forward files above the relevance threshold.
- Rank by score; include the score so downstream agents can prioritize.
- Re-evaluate when a plan is generated (the plan may surface new relevant files).