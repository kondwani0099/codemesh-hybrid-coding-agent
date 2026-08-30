#!/usr/bin/env bash
# CodeMesh Uninstaller (Linux/macOS)
# Removes CodeMesh .github folders from a target project.

set -euo pipefail

TARGET="${1:-.}"

for folder in agents skills workflows templates instructions; do
  path="$TARGET/.github/$folder"
  if [ -d "$path" ]; then
    rm -rf "$path"
    echo "Removed $path"
  fi
done

echo "CodeMesh uninstalled."