# Example Workflow: React + Node

## Request
> "Add a customer approval workflow to orders."

## Agent Chain
```
Product → Analyst → Planner → Architect → Critic
 → React Agent (frontend) + Node Agent (backend)
 → Frontend Reviewer + Backend Reviewer
 → QA (Vitest + Jest) → UAT → Documentation
```

## API Contract
The `api-contract` agent ensures the new `POST /orders/{id}/approve` endpoint and the React API client stay in sync.

## Model Usage
- Local: analysis, summaries, review.
- Cloud: planning and complex implementation.