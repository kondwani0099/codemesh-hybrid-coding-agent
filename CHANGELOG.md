# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-09-03

### Added
- **Security Patching Agent** (`.github/agents/quality/security-patching.agent.md`): Specializes in analyzing vulnerability reports, CVE alerts, and OWASP audit findings to formulate, apply, and verify targeted, non-breaking security patches.
- **Tester Agent** (`.github/agents/quality/tester.agent.md`): Proactively discovers bugs, runtime errors, unhandled exceptions, and edge-case boundary failures with structured reproduction reporting.
- **OWASP Remediation Knowledge** (`.github/skills/security/owasp.md`): Comprehensive coverage of OWASP Top 10 Web Application risks, OWASP API Security Top 10, and OWASP LLM Applications Top 10.
- **Standard & Advanced Security Protocols** (`.github/skills/security/protocols.md`): TLS 1.3, CSP Level 3, HSTS, OAuth 2.1 with PKCE, JWT hardening, Zero-Trust mTLS, HMAC-SHA256 request signing, and rate limiting.
- **Advanced Security Patching Techniques** (`.github/skills/security/patching-techniques.md`): Parameterized queries, BOLA/IDOR authorization fixes, Argon2id/AES-GCM crypto hardening, SSRF egress validation, and safe deserialization.
- **Security Patching Workflow** (`.github/workflows/security-patching.md`): Structured flow from vulnerability triage to patching, QA regression testing, security verification, and release.

## [1.0.1] - 2026-08-30

### Fixed
- Re-tagged the installer as `v1.0.1`. The `v1.0.0` raw `install.ps1` was stuck on a
  stale GitHub raw-CDN cache (still serving the pre-fix script that assumed the
  archive folder was named `<repo>-v<tag>`).
- All one-liner URLs and default `CODEMESH_TAG` now point to `v1.0.1`, whose raw
  files are freshly cached and include the dynamic source-directory lookup.

## [1.0.0] - 2026-08-30

### Added
- Reproducible one-liner installer for bootstrapping any project:
  - Linux/macOS/WSL: `curl -fsSL https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.0/install.sh | bash`
  - Windows PowerShell: `Set-ExecutionPolicy Bypass -Scope Process -Force; iwr -useb https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.0/install.ps1 | iex`
- The installer safely copies managed files, **automatically backs up existing
  states** to `<project>/.codemesh/backups/<timestamp>/`, and **validates schema
  integrity** (agent frontmatter + skill structure) after installation.
- `scripts/setup.py` now supports `--no-backup` and performs post-install schema
  validation; local installs also back up existing states by default.
- Cross-platform setup script (`scripts/setup.py`) that automatically pulls the CodeMesh framework (agents, skills, workflows, templates, instructions) into a target project.
- Works identically on Windows, Linux, and macOS with a single command:
  `python scripts/setup.py <project-path>`.
- Per-project configuration is copied into `<project>/.codemesh/config/`.
- `--force` flag to overwrite existing CodeMesh files; safe default that never clobbers user files.
- `install.ps1` / `install.sh` now delegate to `setup.py` for a single source of truth.

## [Unreleased]

### Added
- Initial agent-team framework repository structure.
- Core workflow agents (planner, analyst, architect, critic, implementer).
- Frontend agents (Vue, React, frontend-reviewer).
- Backend agents (Python, FastAPI, Node, backend-reviewer).
- Data agents (database, api-contract).
- Quality agents (security, code-reviewer, qa, uat).
- Delivery agents (devops, documentation, retrospective).
- Reusable skill library (context-management, model-routing, ollama, testing, security, git, and stack skills).
- Workflow definitions (feature-development, bug-fix, refactoring, security-audit, etc.).
- Standardized output templates.
- Global agent instructions and safety rules.
- Configuration layer (codemesh.yaml, models.yaml, agents.yaml, workflows.yaml, costs.yaml).
- Installation scripts and validation tooling.
- Documentation and examples.