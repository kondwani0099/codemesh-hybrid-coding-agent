#!/usr/bin/env python3
"""Check for broken relative links in Markdown files across the repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_PATTERNS = ("*.md",)

# Skip well-known external URL schemes and anchors.
SKIP_SCHEMES = ("http://", "https://", "mailto:", "#", "ftp://")

errors = []


def main() -> int:
    checked = 0
    for pattern in MARKDOWN_PATTERNS:
        for path in ROOT.rglob(pattern):
            # Skip generated/build dirs
            if any(part in {".git", "node_modules", ".venv", "dist"} for part in path.parts):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                if target.startswith(SKIP_SCHEMES):
                    continue
                # Strip anchor
                target_path = target.split("#")[0]
                if not target_path:
                    continue
                resolved = (path.parent / target_path).resolve()
                checked += 1
                if not resolved.exists():
                    errors.append(f"{path.relative_to(ROOT)}: broken link -> {target}")

    if errors:
        print("Link check FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"All {checked} relative links resolve correctly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())