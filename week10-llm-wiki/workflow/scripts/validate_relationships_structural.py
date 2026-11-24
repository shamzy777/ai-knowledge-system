#!/usr/bin/env python3
"""Machine-verifiable structural validation for staged relationships."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONCEPT_DIR = ROOT / "staging" / "concepts"
RUN1 = ROOT / "staging" / "relationships" / "RUN-001-S04-relationships.md"
RUN2 = ROOT / "staging" / "relationships" / "RUN-002-S03-relationship-proposals.md"

ALLOWED = {
    "prerequisite", "part-of", "cause/effect", "evolution", "application",
    "contrast", "theory ↔ practice", "cross-domain analogy",
}


def concept_titles() -> set[str]:
    titles: set[str] = set()
    for path in CONCEPT_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r'^canonical_title:\s*"(.+)"$', text, re.MULTILINE)
        if match:
            full = match.group(1)
            titles.add(full)
            titles.add(full.split("（", 1)[0])
    return titles


def rows(path: Path) -> list[list[str]]:
    parsed: list[list[str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0] not in {"From", "ID"}:
            parsed.append(cells)
    return parsed


def main() -> int:
    errors: list[str] = []
    titles = concept_titles()

    if not RUN1.exists() or not RUN2.exists():
        errors.append("one or more relationship proposal registers are missing")
    else:
        for index, cells in enumerate(rows(RUN1), start=1):
            if len(cells) != 4:
                errors.append(f"RUN-001 row {index}: expected 4 cells, got {len(cells)}")
                continue
            source, relation, target, support = cells
            if relation not in ALLOWED:
                errors.append(f"RUN-001 row {index}: invalid vocabulary {relation!r}")
            if source not in titles or target not in titles:
                errors.append(f"RUN-001 row {index}: invalid endpoint {source!r} -> {target!r}")
            if not re.search(r"S04 pp?\.", support):
                errors.append(f"RUN-001 row {index}: missing S04 page citation")

        seen: set[str] = set()
        for cells in rows(RUN2):
            if len(cells) != 6:
                errors.append(f"RUN-002 malformed row: {cells}")
                continue
            rid, action, source, relation, target, support = cells
            if not re.fullmatch(r"R2-\d{3}", rid) or rid in seen:
                errors.append(f"RUN-002 invalid or duplicate ID {rid!r}")
            seen.add(rid)
            if action not in {"add", "add-source-support"} and not action.startswith("replacement-for-R2-"):
                errors.append(f"{rid}: invalid action {action!r}")
            if relation not in ALLOWED:
                errors.append(f"{rid}: invalid vocabulary {relation!r}")
            if source not in titles or target not in titles:
                errors.append(f"{rid}: invalid endpoint {source!r} -> {target!r}")
            if not re.search(r"S03 pp?\.", support):
                errors.append(f"{rid}: missing S03 page citation")

    print(f"Relationship structural lint: {len(errors)} error(s)")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
