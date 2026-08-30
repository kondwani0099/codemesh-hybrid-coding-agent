---
name: ollama
description: How and when to use local Ollama models — setup, model profiles, and troubleshooting.
---

# Ollama Skill

## Purpose
Everything needed to use local Ollama models as the primary inference engine for analysis, summarization, coding, and review.

## API Surface
The system integrates with Ollama through an abstraction:

- `GET /api/tags` — list installed models.
- `POST /api/generate` — non-streaming generation.
- `POST /api/chat` — chat-style generation (supports streaming).

## Availability Detection
Check and report:
- Ollama server available/unavailable.
- Model available/unavailable.
- If a model is not installed, show:
  ```
  Model gemma4:4b is not installed.
  Install with:
  ollama pull gemma4:4b
  ```
- Never auto-download models without user permission.

## Recommended Profiles
See `models.md` for the analyzer, summarizer, coder, and reviewer profiles.
See `setup.md` for installation steps.
See `troubleshooting.md` for common issues.

## Rules
- Do not hardcode one model forever — models are configurable.
- Prefer local models for inexpensive operations (see `model-routing`).
- Report model availability clearly to the user.

## Validation
- `GET /api/tags` returns the configured model before use.
- All model names resolve to installed models.