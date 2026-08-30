#!/usr/bin/env bash
# CodeMesh Installer (Linux/macOS)
# Delegates to the cross-platform setup.py so Linux and Windows behave identically.

set -euo pipefail

TARGET="${1:-.}"
FORCE_FLAG=""
if [ "${FORCE:-0}" = "1" ]; then
  FORCE_FLAG="--force"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SETUP="$SCRIPT_DIR/setup.py"

if [ ! -f "$SETUP" ]; then
  echo "Error: setup.py not found next to install.sh" >&2
  exit 1
fi

echo "Running CodeMesh Setup (cross-platform)..."
if command -v python3 >/dev/null 2>&1; then
  python3 "$SETUP" "$TARGET" $FORCE_FLAG
else
  python "$SETUP" "$TARGET" $FORCE_FLAG
fi