# Skill System

## Purpose
Skills define reusable knowledge and processes. Agents define **who**; skills define **how** and **what they know**.

## Structure
Each skill is a directory under `.github/skills/` with a `SKILL.md` and optional supporting docs:

```
skills/
├── context-management/
│   ├── SKILL.md
│   ├── context-rules.md
│   ├── summarization.md
│   └── relevance-scoring.md
```

## Skill Categories
- **Context & Model** — context-management, model-routing, ollama.
- **Stack** — frontend (vue/react), backend (python/fastapi/node).
- **Cross-cutting** — database, api-contracts, testing, security, git, documentation.

## Loading
Agents load relevant skills based on their role and the task. See `docs/skills/creating-skills.md` for authoring.