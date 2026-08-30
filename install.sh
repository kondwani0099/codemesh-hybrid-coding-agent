#!/usr/bin/env bash
# CodeMesh — Reproducible Installer (Linux / macOS / WSL)
#
# One-liner usage:
#   curl -fsSL https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.0/install.sh | bash
#
# Optional environment variables:
#   CODEMESH_TARGET   Project directory to install into  (default: current dir)
#   CODEMESH_TAG      Version tag to install             (default: v1.0.0)
#   CODEMESH_FORCE=1  Overwrite existing CodeMesh files
#   CODEMESH_NO_BACKUP=1  Do not back up existing states
#
# What it does:
#   1. Downloads the CodeMesh framework archive at the version tag.
#   2. Automatically backs up any existing CodeMesh files in the target
#      (<target>/.codemesh/backups/<timestamp>/).
#   3. Safely copies the managed files (.github/agents, skills, workflows,
#      templates, instructions) and per-project config into the target.
#   4. Validates schema integrity of the installed files.

set -euo pipefail

CODEMESH_OWNER="${CODEMESH_OWNER:-kondwani0099}"
CODEMESH_REPO="${CODEMESH_REPO:-codemesh-hybrid-coding-agent}"
CODEMESH_TAG="${CODEMESH_TAG:-v1.0.0}"
CODEMESH_TARGET="${CODEMESH_TARGET:-$PWD}"

ARCHIVE_URL="https://github.com/${CODEMESH_OWNER}/${CODEMESH_REPO}/archive/refs/tags/${CODEMESH_TAG}.tar.gz"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

echo "CodeMesh Reproducible Installer v${CODEMESH_TAG}"
echo "Downloading CodeMesh ${CODEMESH_TAG} from ${CODEMESH_OWNER}/${CODEMESH_REPO} ..."

if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$ARCHIVE_URL" -o "$TMP_DIR/codemesh.tar.gz"
elif command -v wget >/dev/null 2>&1; then
  wget -q "$ARCHIVE_URL" -O "$TMP_DIR/codemesh.tar.gz"
else
  echo "Error: need curl or wget to download CodeMesh." >&2
  exit 1
fi

echo "Extracting..."
tar -xzf "$TMP_DIR/codemesh.tar.gz" -C "$TMP_DIR"
SRC="$TMP_DIR/${CODEMESH_REPO}-${CODEMESH_TAG}"

if [ ! -d "$SRC/.github" ]; then
  echo "Error: downloaded archive does not contain the CodeMesh framework." >&2
  exit 1
fi

# Build arguments for setup.py (the single source of truth).
ARGS=("$CODEMESH_TARGET")
if [ "${CODEMESH_FORCE:-0}" = "1" ]; then
  ARGS+=("--force")
fi
if [ "${CODEMESH_NO_BACKUP:-0}" = "1" ]; then
  ARGS+=("--no-backup")
fi

echo "Installing into: ${CODEMESH_TARGET}"
if command -v python3 >/dev/null 2>&1; then
  python3 "$SRC/scripts/setup.py" "${ARGS[@]}"
else
  python "$SRC/scripts/setup.py" "${ARGS[@]}"
fi
