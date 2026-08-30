#!/usr/bin/env python3
"""Generate index files for agents, skills, and workflows.

Writes:
- agent-output/agent-index.md (or prints to stdout by default)
- agent-output/skill-index.md
- agent-output/workflow-index.md
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "agent-output"

DIRS = {
    "agents": ROOT / ".github" / "agents",
    "skills": ROOT / ".github" / "skills",
    "workflows": ROOT / ".github" / "workflows",
}

HEADERS = {
    "agents": "# Agent Index",
    "skills": "# Skill Index",
    "workflows": "# Workflow Index",
}


def generate_index(kind: str) -> str:
    base_dir = DIRS[kind]
    lines = [HEADERS[kind], ""]
    if not base_dir.exists():
        lines.append("_(empty)_")
        return "\n".join(lines) + "\n"

    for path in sorted(base_dir.rglob("*")):
        if path.is_file():
            rel = path.relative_to(ROOT)
            lines.append(f"- [{path.name}](../{rel.as_posix()})")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    write = "--write" in sys.argv
    for kind in DIRS:
        index = generate_index(kind)
        if write:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            dest = OUT_DIR / f"{kind}-index.md"
            dest.write_text(index, encoding="utf-8")
            print(f"Wrote {dest.relative_to(ROOT)}")
        else:
            print(index)
    return 0


if __name__ == "__main__":
    main()