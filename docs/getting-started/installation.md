# Installation

## Prerequisites
- Git
- VS Code with GitHub Copilot
- Python 3.10+ (for validation scripts)
- Ollama (for local models)

## Install CodeMesh into a Project

### One-liner reproducible installer (recommended)

Runs anywhere — Linux, macOS, WSL, and Windows — fetches the framework at the
version tag, backs up existing states, copies the managed files, and validates
the install.

#### Linux / macOS / WSL
```bash
curl -fsSL https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.1/install.sh | bash
```

#### Windows PowerShell
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iwr -useb https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.1/install.ps1 | iex
```

Environment options:

| Variable | Purpose | Default |
|----------|---------|---------|
| `CODEMESH_TARGET` | Project directory to install into | current dir |
| `CODEMESH_TAG` | Version tag to install | `v1.0.1` |
| `CODEMESH_FORCE=1` | Overwrite existing CodeMesh files | off |
| `CODEMESH_NO_BACKUP=1` | Skip backing up existing states | off |

### From a local clone

Use the cross-platform setup script (works on Windows, Linux, and macOS):

```bash
python scripts/setup.py /path/to/your/project
python scripts/setup.py            # install into the current directory
python scripts/setup.py ../my-app --force
```

This copies the agent definitions, skills, workflows, templates, and
instructions into `.github/` in your project, and drops a per-project
`config/` under `<project>/.codemesh/config/` for you to tune.

## Install Ollama
See `.github/skills/ollama/setup.md`.

## Verify
```bash
python scripts/validate-agents.py
python scripts/validate-skills.py
```

## Uninstall
```powershell
.\scripts\uninstall.ps1 -Target "C:\path\to\your\project"
```
or
```bash
./scripts/uninstall.sh /path/to/your/project
```