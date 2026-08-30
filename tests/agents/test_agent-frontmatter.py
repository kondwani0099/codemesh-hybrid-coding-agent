#!/usr/bin/env python3
"""Test that every agent definition has valid frontmatter and required sections."""

import re
import sys
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent.parent / ".github" / "agents"

REQUIRED_SECTIONS = ["Role", "When to Use", "Rules"]


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


def test_all_agents_have_frontmatter():
    for path in AGENTS_DIR.rglob("*.agent.md"):
        front = parse_frontmatter(path.read_text(encoding="utf-8"))
        assert front.get("name"), f"{path} missing name"
        assert front.get("description"), f"{path} missing description"


def test_all_agents_have_required_sections():
    for path in AGENTS_DIR.rglob("*.agent.md"):
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            assert re.search(rf"^#+\s+{section}", text, re.MULTILINE), (
                f"{path} missing section {section}"
            )


if __name__ == "__main__":
    test_all_agents_have_frontmatter()
    test_all_agents_have_required_sections()
    print("All agent tests passed.")
    sys.exit(0)