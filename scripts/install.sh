#!/usr/bin/env bash
# CodeMesh Installer (Linux/macOS)
# Copies .github/agents, .github/skills, .github/workflows into the target project.

set -euo pipefail

TARGET="${1:-.}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

copy_dir() {
  local src="$1" dst="$2"
  if [ -d "$dst" ] && [ "${FORCE:-0}" != "1" ]; then
    echo "Destination exists: $dst (set FORCE=1 to overwrite)" >&2
    return
  fi
  mkdir -p "$dst"
  cp -R "$src/." "$dst/"
  echo "Copied $src -> $dst"
}

echo "Installing CodeMesh into $TARGET"
copy_dir "$REPO_ROOT/.github/agents" "$TARGET/.github/agents"
copy_dir "$REPO_ROOT/.github/skills" "$TARGET/.github/skills"
copy_dir "$REPO_ROOT/.github/workflows" "$TARGET/.github/workflows"
copy_dir "$REPO_ROOT/.github/templates" "$TARGET/.github/templates"
copy_dir "$REPO_ROOT/.github/instructions" "$TARGET/.github/instructions"

echo "CodeMesh installed successfully."