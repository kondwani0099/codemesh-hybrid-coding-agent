# OWASP Security Standards and Remediation

Comprehensive overview of OWASP standards across Web Applications, APIs, and LLMs/AI with defensive remediation patterns.

---

## 1. OWASP Top 10 Web Application Security Risks

### 1. A01:2021 - Broken Access Control
- **Risk**: Unauthorized users accessing sensitive resources, modifying data, or performing administrative functions (IDOR/BOLA, vertical privilege escalation).
- **Remediation**:
  - Implement server-side role-based or attribute-based access control (RBAC / ABAC) on every endpoint.
  - Enforce record-level ownership checks (e.g., `WHERE user_id = current_user.id`).
  - Disable directory listing and protect administrative routes with middleware guards.

### 2. A02:2021 - Cryptographic Failures
- **Risk**: Data transmission or storage in plaintext, weak encryption algorithms, predictable keys, or broken password hashing.
- **Remediation**:
  - Enforce TLS 1.3 with secure cipher suites for all network traffic.
  - Hash passwords using memory-hard functions: **Argon2id** (preferred) or **bcrypt** (cost factor $\ge 12$).
  - Encrypt data at rest using authenticated symmetric encryption: **AES-256-GCM** or **ChaCha20-Poly1305**.
  - Use cryptographically secure pseudorandom number generators (`secrets` in Python, `crypto.randomBytes` in Node.js).

### 3. A03:2021 - Injection (SQL, NoSQL, OS Command, Template, LDAP)
- **Risk**: Untrusted data sent to an interpreter as part of a command or query, hijacking execution flow.
- **Remediation**:
  - Use parameterized queries, prepared statements, and ORM abstractions with safe variable binding.
  - Avoid shell execution (`subprocess(..., shell=True)`, `eval()`, `exec()`). Use direct argument arrays.
  - Apply context-aware output encoding when rendering data into templates (HTML, JS, CSS).

### 4. A04:2021 - Insecure Design
- **Risk**: Missing security controls in system architecture, lack of threat modeling, or failure to establish trust boundaries.
- **Remediation**:
  - Threat-model applications during design phases.
  - Enforce defense-in-depth: tiered security controls, principle of least privilege, fail-safe defaults.
  - Establish clear trust boundaries between components and external services.

### 5. A05:2021 - Security Misconfiguration
- **Risk**: Default credentials, verbose error stack traces exposed to users, unneeded features/ports enabled, missing HTTP security headers.
- **Remediation**:
  - Set production security headers: `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`.
  - Disable debug/development modes in production environments.
  - Strip stack traces and sensitive error details from API error responses.

### 6. A06:2021 - Vulnerable and Outdated Components
- **Risk**: Using libraries or frameworks with known Common Vulnerabilities and Exposures (CVEs).
- **Remediation**:
  - Continuously scan dependencies using `pip-audit`, `npm audit`, `osv-scanner`, or Snyk.
  - Enforce minimal-version security patches for identified CVEs.
  - Pin versions and verify dependency hashes via lockfiles (`package-lock.json`, `poetry.lock`, `requirements.txt.hash`).

### 7. A07:2021 - Identification and Authentication Failures
- **Risk**: Credential stuffing, brute-force attacks, weak password policies, insecure session management, or missing MFA.
- **Remediation**:
  - Implement progressive rate limiting and account lockout/exponential backoff on authentication endpoints.
  - Use secure, HTTP-only, SameSite cookies for session identifiers with short expirations and server-side invalidation.
  - Support Multi-Factor Authentication (MFA/TOTP/FIDO2).

### 8. A08:2021 - Software and Data Integrity Failures
- **Risk**: Deserialization of untrusted data, unverified software updates, or untrusted CI/CD pipeline dependencies.
- **Remediation**:
  - Never deserialize untrusted data with unsafe parsers (`pickle.loads`, `yaml.unsafe_load`, `eval`).
  - Use strict data validation formats (JSON schemas, Pydantic models, Zod schemas).
  - Verify digital signatures and checksums for build artifacts and external packages.

### 9. A09:2021 - Security Logging and Monitoring Failures
- **Risk**: Failure to detect breaches, insufficient logging of auth events, or logging sensitive personal/credential data.
- **Remediation**:
  - Log all authentication, authorization, access control failures, and high-privilege operations.
  - Automatically redact passwords, tokens, API keys, and PII from log outputs.
  - Maintain centralized, tamper-evident audit trails with automated alerting for anomalous spikes.

### 10. A10:2021 - Server-Side Request Forgery (SSRF)
- **Risk**: Web application fetches a remote resource without validating the user-supplied URL, exposing internal services or cloud metadata.
- **Remediation**:
  - Validate and sanitize all user-supplied destination URLs against a strict protocol (HTTPS only) and hostname whitelist.
  - Block egress requests to loopback (`127.0.0.0/8`, `::1`), link-local (`169.254.0.0/16`), and private network ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
  - Resolve DNS prior to connection and enforce IP range checks to prevent DNS rebinding attacks.

---

## 2. OWASP API Security Top 10

1. **API1: Broken Object Level Authorization (BOLA / IDOR)**: Enforce user/tenant ownership validation at the data layer for every resource identifier.
2. **API2: Broken Authentication**: Secure token generation, validate signatures on every request, mandate short token lifespans.
3. **API3: Broken Object Property Level Authorization**: Prevent mass assignment by validating allowed request payloads against strict DTOs (Data Transfer Objects).
4. **API4: Unrestricted Resource Consumption**: Enforce per-client rate limits, memory/CPU bounds, execution timeouts, and pagination query limits (`limit`, `max_limit`).
5. **API5: Broken Function Level Authorization**: Validate administrative and privileged endpoints against user capabilities and roles, not just UI visibility.
6. **API6: Unrestricted Access to Sensitive Business Flows**: Protect high-impact endpoints (checkout, credential reset, bulk exports) with CAPTCHA, bot mitigation, and behavioral rate limiting.
7. **API7: Server-Side Request Forgery (SSRF)**: Validate egress URLs, block internal metadata access (e.g. AWS/GCP instance metadata services).
8. **API8: Security Misconfiguration**: Harden CORS policies, restrict HTTP methods (e.g. disable `TRACE`, `OPTIONS` details), disable unneeded debug endpoints.
9. **API9: Improper Inventory Management**: Document all API versions (OpenAPI/Swagger), decommission deprecated endpoints, protect sandbox/staging APIs with production-grade auth.
10. **API10: Unsafe Consumption of APIs**: Treat third-party and upstream API responses as untrusted input; validate schemas and apply timeouts.

---

## 3. OWASP Top 10 for LLM & AI Applications

1. **LLM01: Prompt Injection**: Separate user input from system instructions using structural delimiters; validate and sanitize untrusted text inputs.
2. **LLM02: Sensitive Information Disclosure**: Filter model prompts and completions for credentials, PII, and proprietary data using regex/DLP scanners.
3. **LLM03: Supply Chain Vulnerabilities**: Verify source integrity of pre-trained models, fine-tuning datasets, plugins, and third-party AI libraries.
4. **LLM04: Data and Model Poisoning**: Validate data provenance and implement anomaly detection across training/fine-tuning datasets.
5. **LLM05: Improper Output Handling**: Treat LLM outputs as untrusted user input before passing into interpreters, HTML renderers, or SQL queries.
6. **LLM06: Excessive Agency**: Enforce human-in-the-loop approvals for destructive actions; limit tool execution capabilities with least-privilege boundaries.
7. **LLM07: System Prompt Leakage**: Prevent system prompts containing internal secrets or instructions from being revealed to users.
8. **LLM08: Vector and Embedding Weaknesses**: Isolate tenant vectors in RAG stores; enforce authorization filters before retrieving embedding context.
9. **LLM09: Misinformation**: Ground model answers with verified citations and structured validation schemas.
10. **LLM10: Unbounded Consumption**: Implement token limits, request timeouts, and cost budgets per user/session.

---

## 4. Remediation Checklist

- [ ] **Access Control**: Every endpoint verifies server-side identity and tenant ownership.
- [ ] **Injection Defenses**: Parameterized database queries, safe subprocess invocation, context-aware encoding.
- [ ] **Cryptography**: Argon2id/bcrypt for passwords, AES-256-GCM/ChaCha20-Poly1305 for data, TLS 1.3 in transit.
- [ ] **Network Defense**: SSRF protections blocking private CIDRs and cloud metadata endpoints.
- [ ] **Data Sanitization**: Mass-assignment prevented via strict DTOs / Pydantic / Zod models.
- [ ] **Logging & Redaction**: Zero secrets, tokens, or PII written to logs; full audit trail for auth/privilege events.