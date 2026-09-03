# Standard & Advanced Security Protocols

Comprehensive security protocols governing transport security, authentication, token lifecycle, zero-trust architecture, and abuse mitigation.

---

## 1. Transport & Edge Security Protocols

### TLS 1.3 & Transport Hardening
- **Protocol**: Enforce TLS 1.3 (with TLS 1.2 as minimum fallback where legacy clients require). Disable SSLv2, SSLv3, TLS 1.0, and TLS 1.1.
- **Cipher Suites**: Restrict to AEAD cipher suites:
  - `TLS_AES_256_GCM_SHA384`
  - `TLS_CHACHA20_POLY1305_SHA256`
  - `TLS_AES_128_GCM_SHA256`
- **HSTS (HTTP Strict Transport Security)**:
  ```http
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  ```

### HTTP Defense-in-Depth Headers
- **Content-Security-Policy (CSP Level 3)**:
  - Use cryptographic nonces for scripts (`'nonce-{random}'`) or strict-dynamic.
  - Disable `'unsafe-inline'` and `'unsafe-eval'`.
  ```http
  Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{RANDOM}' 'strict-dynamic'; object-src 'none'; base-uri 'none'; frame-ancestors 'none';
  ```
- **Clickjacking & MIME Protection**:
  ```http
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), camera=(), microphone=(), payment=()
  ```

### CORS Protocol
- Never use wildcard `Access-Control-Allow-Origin: *` in combination with `Access-Control-Allow-Credentials: true`.
- Validate the incoming `Origin` header against an explicit server-side allowlist.
- Restrict `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers` strictly to needed verbs and headers.
- Set conservative `Access-Control-Max-Age` (e.g. 600s).

---

## 2. Authentication & Token Lifecycle Protocols

### OAuth 2.1 & OpenID Connect (OIDC)
- **Flow**: Use Authorization Code Flow with mandatory **PKCE (Proof Key for Code Exchange)** using `S256` code challenge.
- **Deprecations**: Ban Implicit Grant and Resource Owner Password Credentials Grant flows.
- **Redirect URI**: Enforce strict exact-string match on registered redirect URIs (no wildcards or open regexes).
- **State & Nonce**: Generate cryptographically random `state` and `nonce` parameters to prevent CSRF and token replay.

### JWT Hardening Protocol
- **Algorithm Whitelist**: Explicitly allow only asymmetric signing algorithms (e.g., `RS256`, `ES256`, `EdDSA`). Explicitly reject `alg: "none"` and symmetric HMAC (`HS256`) when public keys are distributed.
- **Claims Verification**: Mandatory validation of standard claims:
  - `iss` (Issuer) matches expected authorization server.
  - `aud` (Audience) matches intended service client identifier.
  - `exp` (Expiration) enforced with minimal clock skew tolerance ($\le 60$ seconds).
  - `nbf` (Not Before) and `iat` (Issued At) checked.
- **Token Lifespans**:
  - Access Tokens: Short-lived (5 to 15 minutes).
  - Refresh Tokens: Long-lived with single-use rotation (RTR) and automatic reuse detection/revocation.
- **Revocation**: Maintain a revocation list or JTI (JWT ID) blacklist in fast key-value cache (Redis) with TTL matching token expiration.

### Secure Cookies & Session Management
- Attributes:
  ```http
  Set-Cookie: session_id=<RANDOM_UUID>; Secure; HttpOnly; SameSite=Strict; Path=/; Domain=example.com; Max-Age=3600
  ```
- Rotate session identifier immediately upon privilege changes (login, logout, elevation).

---

## 3. Zero-Trust & Inter-Service Security Protocols

### Mutual TLS (mTLS)
- Enforce bidirectional certificate validation for all service-to-service (east-west) communications.
- Validate client certificate CN/SAN against the service identity registry.
- Enforce short certificate validity windows with automated rotation (e.g. SPIFFE/SPIRE).

### Cryptographic Request Signing (HMAC-SHA256)
For webhook delivery and inter-service HTTP requests:
1. Canonicalize request parameters (Method, URI, Timestamp, Request Body Hash).
2. Generate signature: `HMAC-SHA256(secret_key, canonical_string)`.
3. Include timestamp in header (`X-Timestamp`) and reject requests older than 300 seconds to prevent replay attacks.
4. Verify signature using constant-time comparison.

---

## 4. Availability, Rate Limiting & DoS Mitigation Protocols

### Rate Limiting Protocols
- **Algorithms**:
  - **Token Bucket / Leaky Bucket**: For burst control and steady-state throttling.
  - **Sliding Window Counter**: For accurate sliding-window rate tracking across distributed nodes.
- **Tiered Limits**:
  - Public unauthenticated endpoints: Strict IP-based limits (e.g., 60 req/min).
  - Authentication endpoints (login, password reset): High-frequency throttle (e.g., 5 req/min per IP and per account).
  - Authenticated user endpoints: User/organization token-bucket limit.
- **Standard Rate Limit Headers**:
  ```http
  RateLimit-Limit: 100
  RateLimit-Remaining: 95
  RateLimit-Reset: 15
  ```

### Resource Guardrails
- Enforce maximum request body sizes (e.g., 1MB default, 10MB for specific file uploads).
- Enforce server-side execution timeouts on all database and external HTTP requests.
- Configure connection pool bounds to prevent thread/connection starvation.
