# Standard & Advanced Security Patching Techniques

Actionable patterns, code recipes, and defensive remediation techniques for security vulnerabilities.

---

## 1. Injection Remediation Techniques

### SQL Injection Remediation
- **Rule**: Never interpolate, concatenate, or format strings into raw SQL queries.
- **Pattern (Python / SQLAlchemy)**:
  ```python
  # INSECURE:
  # db.execute(f"SELECT * FROM users WHERE username = '{username}'")

  # SECURE (Parameterized Query):
  from sqlalchemy import text
  stmt = text("SELECT id, username, email FROM users WHERE username = :username")
  result = db.execute(stmt, {"username": username})
  ```
- **Pattern (Node.js / pg)**:
  ```javascript
  // SECURE (Parameterized query):
  const query = 'SELECT id, username, email FROM users WHERE username = $1';
  const res = await pool.query(query, [username]);
  ```

### OS Command Injection Remediation
- **Rule**: Avoid invoking the system shell (`shell=True` in Python, or passing raw command strings to `exec()` in Node.js).
- **Pattern (Python)**:
  ```python
  # INSECURE:
  # os.system(f"ping -c 1 {user_host}")

  # SECURE (Direct argument array without shell interpreter):
  import subprocess
  import ipaddress

  # Validate input beforehand
  validated_ip = str(ipaddress.ip_address(user_host))
  result = subprocess.run(["ping", "-c", "1", validated_ip], capture_output=True, text=True, check=True)
  ```

---

## 2. Authorization & Access Control (IDOR / BOLA) Patching

### Multi-Tenant Ownership Verification
- **Rule**: Always include tenant / user ownership constraints in database queries, not just the resource ID.
- **Pattern**:
  ```python
  # INSECURE:
  # document = db.query(Document).filter(Document.id == doc_id).first()

  # SECURE:
  document = db.query(Document).filter(
      Document.id == doc_id,
      Document.organization_id == current_user.org_id
  ).first()
  if not document:
      raise HTTPException(status_code=404, detail="Resource not found")
  ```

### Declarative Authorization Decorators
```python
def require_permission(required_perm: str):
    def decorator(fn):
        @wraps(fn)
        async def wrapper(*args, current_user: User = Depends(get_current_user), **kwargs):
            if not current_user.has_permission(required_perm):
                raise HTTPException(status_code=403, detail="Forbidden")
            return await fn(*args, current_user=current_user, **kwargs)
        return wrapper
    return decorator
```

---

## 3. Cryptographic Hardening & Patching Techniques

### Secure Password Hashing
- Use **Argon2id** with memory-hard parameters.
```python
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)

# Hash password
hashed = ph.hash("user_secret_password")

# Verify password
try:
    ph.verify(hashed, "user_secret_password")
except VerifyMismatchError:
    # Invalid password
    pass
```

### Constant-Time String Comparison
- Prevent timing attacks when verifying HMAC signatures, tokens, or API keys.
```python
import hmac

# SECURE: Constant-time comparison
def verify_token(provided_token: str, expected_token: str) -> bool:
    return hmac.compare_digest(provided_token.encode("utf-8"), expected_token.encode("utf-8"))
```

### Authenticated Symmetric Encryption (AES-GCM)
```python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_data(plaintext: bytes, key: bytes) -> bytes:
    # 96-bit unique nonce per encryption
    nonce = os.urandom(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext

def decrypt_data(payload: bytes, key: bytes) -> bytes:
    nonce = payload[:12]
    ciphertext = payload[12:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)
```

---

## 4. SSRF & Egress Hardening Techniques

### IP/CIDR Egress Validator
- Prevent calls to internal addresses, loopback, link-local metadata (e.g. `169.254.169.254`), and private networks.
```python
import ipaddress
import socket
from urllib.parse import urlparse

BLOCKED_NETWORKS = [
    ipaddress.ip_network("127.0.0.0/8"),     # Loopback
    ipaddress.ip_network("10.0.0.0/8"),      # Private RFC 1918
    ipaddress.ip_network("172.16.0.0/12"),   # Private RFC 1918
    ipaddress.ip_network("192.168.0.0/16"),  # Private RFC 1918
    ipaddress.ip_network("169.254.0.0/16"),  # Link-Local / Metadata
    ipaddress.ip_network("::1/128"),         # IPv6 Loopback
    ipaddress.ip_network("fc00::/7"),        # IPv6 Unique Local
    ipaddress.ip_network("fe80::/10"),       # IPv6 Link-Local
]

def validate_safe_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("Invalid URL scheme; only HTTP/HTTPS allowed")
    
    hostname = parsed.hostname
    if not hostname:
        raise ValueError("Missing URL hostname")
    
    # Resolve all associated IPs
    addr_info = socket.getaddrinfo(hostname, None)
    for entry in addr_info:
        ip_str = entry[4][0]
        ip_obj = ipaddress.ip_address(ip_str)
        for blocked_net in BLOCKED_NETWORKS:
            if ip_obj in blocked_net:
                raise ValueError(f"Egress to prohibited network {ip_str} is blocked")
    return url
```

---

## 5. Safe Deserialization & Data Validation

### Safe Parsing
- **Prohibited**: `pickle.loads()`, `eval()`, `yaml.unsafe_load()`, `marshal.loads()`.
- **Recommended**: Typed validation using Pydantic / Zod / JSON Schema.
```python
from pydantic import BaseModel, Field, EmailStr

class UserProfilePatch(BaseModel):
    display_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    bio: str = Field("", max_length=500)
    
    class Config:
        extra = "forbid"  # Prevent mass-assignment / property injection
```

---

## 6. Dependency Patching & CVE Remediation

### Strategy
1. **Analyze Vulnerability Report**: Identify CVE ID, CVSS score, and affected package version range.
2. **Determine Minimal Non-Breaking Upgrade**: Pick the closest semantic version patch that resolves the CVE (e.g., `requests 2.31.0` -> `requests 2.32.0`).
3. **Verify Transitive Dependencies**: Ensure upstream/downstream lockfile constraints remain consistent.
4. **Execute Automated Regression Suite**: Run unit and integration tests to confirm zero functional breakage.
5. **Verify Security Resolution**: Re-scan using `pip-audit`, `npm audit`, or `osv-scanner` to confirm 0 known critical/high vulnerabilities remain.
