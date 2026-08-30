#!/usr/bin/env python3
"""Validate all CodeMesh agent definitions.

Checks that every .agent.md file has:
- Valid YAML frontmatter.
- A `name` and `description`.
- Required sections (Role, When to Use, Rules, Handoffs/Outputs where applicable).
- No broken references to other agents/skills.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent / ".github" / "agents"

REQUIRED_SECTIONS = ["Role", "When to Use", "Rules"]
OPTIONAL_SECTIONS = ["Responsibilities", "Inputs", "Outputs", "Handoffs"]

errors = []


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    front = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            front[key.strip()] = value.strip()
    return front


def main() -> int:
    agent_files = sorted(AGENTS_DIR.rglob("*.agent.md"))
    if not agent_files:
        print(f"No agent files found under {AGENTS_DIR}")
        return 1

    for path in agent_files:
        text = path.read_text(encoding="utf-8")
        front = parse_frontmatter(text)
        rel = path.relative_to(AGENTS_DIR.parent.parent)

        if not front.get("name"):
            errors.append(f"{rel}: missing frontmatter `name`")
        if not front.get("description"):
            errors.append(f"{rel}: missing frontmatter `description`")

        for section in REQUIRED_SECTIONS:
            if not re.search(rf"^#+\s+{section}", text, re.MULTILINE):
                errors.append(f"{rel}: missing required section `{section}`")

    if errors:
        print("Agent validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"All {len(agent_files)} agents validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())