# Ollama Models

## Model Profiles

| Role | Recommended | Notes |
|------|-------------|-------|
| analyzer | gemma4:4b | Repository analysis, file identification |
| summarizer | gemma4:4b | Summarization, context compression |
| coder | qwen-coder | Local coding, small fixes, refactoring |
| reviewer | gemma4:4b | Simple code review, test-output summarization |

## Model Responsibilities

### Gemma 4B (inexpensive operations)
- File summaries.
- Repository summaries.
- Code explanations.
- Context compression.
- Identifying relevant files.
- Simple code review.
- Test-output summarization.
- Documentation summaries.
- Dependency explanations.

Do **not** automatically use Gemma 4B for complex architectural decisions when a stronger model is available.

### Qwen Coder (local coding)
- Code search.
- Implementation inspection.
- Identifying existing patterns.
- Generating small fixes.
- Local refactoring.
- Local debugging.
- Code review.

## Configuration
Model names are configured in `config/models.yaml` and are not hardcoded.