# Ollama

## Role in CodeMesh
Ollama is the local inference engine for analysis, summarization, coding, and review.

## Integration Surface
- `GET /api/tags`
- `POST /api/generate`
- `POST /api/chat`

## Recommended Models
- `gemma4:4b` — analyzer, summarizer, reviewer.
- `qwen-coder` — local coding model.

## Setup
See `.github/skills/ollama/setup.md`.

## Troubleshooting
See `.github/skills/ollama/troubleshooting.md`.

## Rules
- Model names are configurable (`config/models.yaml`).
- Detect availability and report clearly.
- Never auto-download models without user permission.