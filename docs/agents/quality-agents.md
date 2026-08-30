# Quality Agents

## Security Agent
Performs security reviews against OWASP. See `.github/agents/quality/security.agent.md`.

## Code Reviewer
Reviews implementation for code quality. See `.github/agents/quality/code-reviewer.agent.md`.

## QA Agent
Validates functionality by running tests and driving the fix loop. See `.github/agents/quality/qa.agent.md`.

## UAT Agent
Confirms the implementation satisfies the business requirement. See `.github/agents/quality/uat.agent.md`.

## The Separation
```
Code Reviewer → "Is the code good?"
QA           → "Does it work?"
UAT          → "Does it solve the business problem?"
```