# Quality Agents

## Security Agent
Performs security reviews and audits against OWASP standards. See `.github/agents/quality/security.agent.md`.

## Security Patching Agent
Formulates, applies, and verifies atomic, non-breaking security patches against OWASP flaws, CVEs, and insecure configurations using standard and advanced security protocols. See `.github/agents/quality/security-patching.agent.md`.

## Code Reviewer
Reviews implementation for code quality. See `.github/agents/quality/code-reviewer.agent.md`.

## Tester Agent
Proactively hunts for bugs, unhandled exceptions, runtime errors, and edge-case boundary failures. See `.github/agents/quality/tester.agent.md`.

## QA Agent
Validates functionality by running tests and driving the fix loop. See `.github/agents/quality/qa.agent.md`.

## UAT Agent
Confirms the implementation satisfies the business requirement. See `.github/agents/quality/uat.agent.md`.

## The Separation
```
Security          → "Where are the vulnerabilities and risks?"
Security Patching → "How do we remediate the flaws securely without regression?"
Code Reviewer     → "Is the code clean and well-structured?"
Tester            → "What edge cases, runtime errors, or hidden bugs break the system?"
QA                → "Does it pass the automated test suites and verify the fix loop?"
UAT               → "Does it solve the business problem?"
```