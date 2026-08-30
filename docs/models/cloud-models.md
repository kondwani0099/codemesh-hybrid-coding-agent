# Cloud Models

## Purpose
Reserved for expensive reasoning and implementation.

## Provider Abstraction
The system supports multiple providers via a common interface:

```
providers/
    ollama.py
    openai.py
    anthropic.py
    google.py
    openrouter.py
```

The application never depends directly on one provider.

## When to Use
- Complex planning.
- Complex implementation.
- Complex debugging.
- Architecture decisions.
- Security-sensitive reasoning.

## Configuration
Providers and models are configured in `config/models.yaml` and `config/costs.yaml`. Secrets come from environment variables — never hardcoded.

## Failure Handling
Retry → provider fallback → notify user. Never lose task state.