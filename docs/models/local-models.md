# Local Models

## Profiles

| Role | Model | Use |
|------|-------|-----|
| analyzer | gemma4:4b | Repository analysis, file identification |
| summarizer | gemma4:4b | Summaries, context compression |
| coder | qwen-coder | Local coding, small fixes |
| reviewer | gemma4:4b | Simple review, test-output summarization |

## Gemma 4B — Inexpensive Operations
- File/repository summaries.
- Code explanations.
- Context compression.
- Relevant file identification.
- Simple review.
- Documentation summaries.

Do not use Gemma 4B for complex architectural decisions when a stronger model is available.

## Qwen Coder — Local Coding
- Code search and inspection.
- Pattern identification.
- Small fixes and local refactoring.
- Local debugging and review.

## Configuration
Model names are not hardcoded; configure in `config/models.yaml`.