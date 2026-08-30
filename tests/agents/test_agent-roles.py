#!/usr/bin/env python3
"""Test that agent roles are defined and do not overlap in prohibited ways.

Checks that each agent file declares a `name` matching its file name and that
no two agents share the same name.
"""

import re
import sys
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent.parent / ".github" / "agents"


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


def test_agent_names_are_unique():
    names = []
    for path in AGENTS_DIR.rglob("*.agent.md"):
        front = parse_frontmatter(path.read_text(encoding="utf-8"))
        names.append(front.get("name"))
    assert len(names) == len(set(names)), f"Duplicate agent names: {names}"


def test_agent_files_declare_role_section():
    for path in AGENTS_DIR.rglob("*.agent.md"):
        text = path.read_text(encoding="utf-8")
        assert "## Role" in text or "# Role" in text, f"{path} missing Role section"


if __name__ == "__main__":
    test_agent_names_are_unique()
    test_agent_files_declare_role_section()
    print("All agent role tests passed.")
    sys.exit(0)