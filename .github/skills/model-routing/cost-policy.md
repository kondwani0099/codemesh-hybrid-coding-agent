# Cost Policy

## Purpose
Minimize cloud API spend through caching, local models, and context compression.

## Priority
```
CACHE
 → LOCAL MODEL
 → SMALL LOCAL CODING MODEL
 → CLOUD MODEL
```

## Before Every Cloud Request
1. Check cached context.
2. Check existing summaries.
3. Retrieve only relevant files.
4. Compress context.
5. Remove duplicated/irrelevant information.
6. Estimate token cost.
7. Select the appropriate cloud model.

## Cost Tracking
Record for every request:

```json
{
  "provider": "example",
  "model": "example-model",
  "input_tokens": 12000,
  "output_tokens": 4000,
  "estimated_cost": 0.08
}
```

Report:
- Actual cloud cost.
- Estimated full-cloud cost (counterfactual).
- Estimated tokens saved.
- Percentage saved.