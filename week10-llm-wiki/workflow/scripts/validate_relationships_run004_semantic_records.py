#!/usr/bin/env python3
"""Validate one independent semantic-review record per RUN-004 proposal."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[2]
PROPOSALS = ROOT / "staging/relationships/RUN-004-relationship-proposals.md"
REVIEW = ROOT / "staging/relationships/RUN-004-semantic-review.md"

def ids(path: Path) -> list[str]:
    return re.findall(r"^\| (R4-\d{3}) \|", path.read_text(encoding="utf-8"), re.M)

def main() -> int:
    errors = []
    proposed = ids(PROPOSALS)
    reviewed = ids(REVIEW)
    if set(proposed) != set(reviewed):
        errors.append(f"proposal/review mismatch: missing={sorted(set(proposed)-set(reviewed))}, extra={sorted(set(reviewed)-set(proposed))}")
    if len(reviewed) != len(set(reviewed)):
        errors.append("duplicate semantic review record")
    text = REVIEW.read_text(encoding="utf-8")
    for line in text.splitlines():
        if re.match(r"\| R4-\d{3} \|", line):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) != 3 or not cells[1].startswith("accepted") or len(cells[2]) < 30:
                errors.append(f"incomplete semantic record: {line}")
    if "No proposal was silently reversed or relabelled" not in text:
        errors.append("no-silent-rewrite statement missing")
    print(f"RUN-004 semantic-record lint: {len(errors)} error(s); {len(reviewed)} reviews")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
