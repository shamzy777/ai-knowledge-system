#!/usr/bin/env python3
"""Structural-only relationship gate for RUN-004."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "staging/relationships/RUN-004-relationship-proposals.md"
VOCAB = {"prerequisite", "part-of", "cause/effect", "evolution", "application", "contrast", "theory ↔ practice", "cross-domain analogy"}

def main() -> int:
    errors = []
    text = REGISTER.read_text(encoding="utf-8")
    titles = set()
    for path in (ROOT / "staging/concepts").glob("*.md"):
        match = re.search(r'^canonical_title:\s*"(.+?)"$', path.read_text(encoding="utf-8"), re.M)
        if match:
            titles.add(re.sub(r"（.*?）", "", match.group(1)).strip())
    rows = []
    for line in text.splitlines():
        if re.match(r"\| R4-\d{3} \|", line):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) != 6:
                errors.append(f"bad schema: {line}")
                continue
            rows.append(cells)
    ids = [row[0] for row in rows]
    if len(rows) != 30:
        errors.append(f"expected 30 proposals, found {len(rows)}")
    if len(ids) != len(set(ids)):
        errors.append("duplicate proposal ID")
    for pid, action, left, rel, right, support in rows:
        if rel not in VOCAB:
            errors.append(f"{pid}: invalid relationship {rel}")
        if left not in titles or right not in titles:
            errors.append(f"{pid}: invalid endpoint {left!r} -> {right!r}")
        if action not in {"add", "add-source-support"} and not action.startswith("replacement-for-"):
            errors.append(f"{pid}: invalid action {action}")
        if not re.search(r"S\d{2}", support) or not re.search(r"p\.?|pp\.?|book", support, re.I):
            errors.append(f"{pid}: missing source locator")
    print(f"RUN-004 structural relationship lint: {len(errors)} error(s); {len(rows)} proposals")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
