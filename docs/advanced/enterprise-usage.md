# Enterprise Usage

## Considerations
- **Multi-repository** — manage context and memory per repo.
- **Security** — strict secret redaction, approval gates, dependency audits.
- **Compliance** — audit logs of all model requests and agent actions.
- **Cost control** — enforce cost policies and budgets per team/project.
- **Governance** — controlled model selection and routing policies.

## Recommended Setup
- Central configuration for models, costs, and security.
- Repository-level installs via `scripts/install.*`.
- CI validation of agent/skill structure.
- Logging of every agent action and model request (without secrets).

## Logging Format
```
2026-08-30 15:20:01
Agent: RepositoryAnalyzer
Model: gemma4:4b
Action: summarize_file
File: backend/invoices/service.py
Tokens: 824
```