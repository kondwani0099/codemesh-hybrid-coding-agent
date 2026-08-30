# Installation

## Prerequisites
- Git
- VS Code with GitHub Copilot
- Python 3.10+ (for validation scripts)
- Ollama (for local models)

## Install CodeMesh into a Project

### Windows (PowerShell)
```powershell
.\scripts\install.ps1 -Target "C:\path\to\your\project"
```

### Linux/macOS
```bash
./scripts/install.sh /path/to/your/project
```

This copies the agent definitions, skills, workflows, templates, and
instructions into `.github/` in your project.

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