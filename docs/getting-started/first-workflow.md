# First Workflow

This guide walks through your first CodeMesh workflow: a simple feature.

## 1. Open Your Repository
Open the target project in VS Code with the CodeMesh `.github/` folders installed.

## 2. Invoke the CodeMesh Agent
Start a conversation with the `codemesh` agent and state your request:

> "Add an approval workflow to invoices."

## 3. Routing
The orchestrator classifies the request (feature, high complexity) and routes it:

```
Feature → planner → analyst → implementer → qa → uat
```

## 4. What Happens
1. **Analyst** runs local analysis to find relevant files.
2. **Planner** produces a `plan.md` (requires your approval).
3. **Implementer** executes the plan.
4. **QA** runs tests.
5. **UAT** confirms the feature meets the request.

## 5. Approve the Plan
The workflow pauses at the approval gate. Review `plan.md` and approve.

## 6. Review the Result
After completion, review the artifacts in `agent-output/`:
- `plan.md`
- `implementation.md`
- `review.md`
- `qa.md`
- `uat.md`