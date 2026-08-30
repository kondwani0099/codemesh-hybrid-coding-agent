# OWASP

## Top Risks to Check
1. **Broken Access Control** — verify authorization on every route/action.
2. **Cryptographic Failures** — no plaintext secrets; TLS everywhere; strong hashing.
3. **Injection** — SQL, NoSQL, OS, and template injection; use parameterized queries.
4. **Insecure Design** — threat-model changes; validate trust boundaries.
5. **Security Misconfiguration** — no default creds; secure headers; minimal permissions.
6. **Vulnerable Components** — keep dependencies patched.
7. **Auth Failures** — implement MFA where appropriate; secure session handling.
8. **Data Integrity Failures** — validate deserialization; signed data.
9. **Logging Failures** — log security events without logging secrets.
10. **SSRF** — validate URLs and redirects.

## Review Checklist
- [ ] Authorization enforced server-side.
- [ ] Input validated and parameterized queries used.
- [ ] No secrets in code, logs, or responses.
- [ ] Dependencies current.
- [ ] Secure headers and TLS.
- [ ] Rate limiting on sensitive endpoints.