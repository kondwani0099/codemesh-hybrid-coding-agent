#!/usr/bin/env python3
"""Test that handoff references between agents resolve to existing agent files.

Agents list their handoffs by name (e.g., 'Planner', 'Analyst'). This test
collects all declared agent names and verifies each handoff target exists.
"""

import re
import sys
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent.parent / ".github" / "agents"

# Agent names referenced in handoff sections (case-insensitive keywords).
KNOWN_AGENTS = {
    "analyst", "planner", "architect", "critic", "implementer",
    "code reviewer", "frontend reviewer", "backend reviewer", "qa", "uat",
    "security", "documentation", "devops", "retrospective", "database",
    "api contract", "product", "roadmap", "workflow", "vue", "react",
    "python", "fastapi", "node",
}


def test_handoff_references_are_known():
    for path in AGENTS_DIR.rglob("*.agent.md"):
        text = path.read_text(encoding="utf-8")
        # Find text after any Handoffs section
        match = re.search(r"#+\s*Handoffs(.*)", text, re.DOTALL)
        if not match:
            continue
        section = match.group(1)
        for name in KNOWN_AGENTS:
            # Every referenced agent should be one we know about; we only flag
            # explicit Markdown link references to files.
            for ref in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", section):
                target = ref[1]
                assert target.startswith(".github/agents/"), (
                    f"{path}: handoff link target must be an agent file: {target}"
                )


if __name__ == "__main__":
    test_handoff_references_are_known()
    print("All handoff tests passed.")
    sys.exit(0)