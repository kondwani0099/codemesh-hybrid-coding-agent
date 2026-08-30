# Custom Models

## Configuring Models
Model names and providers are set in `config/models.yaml`:

```yaml
models:
  analyzer:
    provider: ollama
    model: gemma4:4b
  planner:
    provider: cloud
    model: configurable
```

## Adding a Provider
Providers implement a common interface:

```python
class LLMProvider:
    async def generate(...)
    async def stream(...)
    async def count_tokens(...)
```

Add a new provider file under `providers/` and register it in the model router.

## Rules
- Never hardcode model names or API keys.
- Use environment variables for secrets.
- Update `config/costs.yaml` with rate cards for cost tracking.