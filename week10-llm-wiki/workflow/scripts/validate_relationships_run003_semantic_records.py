#!/usr/bin/env python3
"""Validate RUN-003 semantic-review coverage without judging semantics mechanically."""
from __future__ import annotations
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROPOSALS = ROOT / "staging/relationships/RUN-003-batch-relationship-proposals.md"
REVIEW = ROOT / "staging/relationships/RUN-003-batch-semantic-review.md"

def ids(path: Path) -> list[str]:
    return re.findall(r"^\| (R3-\d{3}) \|", path.read_text(encoding="utf-8"), re.M)

def main() -> int:
    errors: list[str] = []
    if not PROPOSALS.exists() or not REVIEW.exists():
        errors.append("proposal or semantic-review artifact missing")
    else:
        pids, rids = ids(PROPOSALS), ids(REVIEW)
        if sorted(pids) != sorted(rids): errors.append("semantic review does not cover every proposal exactly once")
        text = REVIEW.read_text(encoding="utf-8")
        rejected = set(re.findall(r"^\| (R3-\d{3}) \| rejected-returned-to-staging \|", text, re.M))
        if rejected != {"R3-035", "R3-036", "R3-037"}: errors.append(f"unexpected rejected set: {sorted(rejected)}")
        accepted = re.findall(r"^\| R3-\d{3} \| accepted(?:-with-scope)? \|", text, re.M)
        if len(accepted) != 34: errors.append(f"expected 34 accepted records, found {len(accepted)}")
        for rid in rejected:
            if "returned-to-staging" not in next(line for line in text.splitlines() if line.startswith(f"| {rid} |")):
                errors.append(f"{rid}: return route missing")
    print(f"RUN-003 semantic-record lint: {len(errors)} error(s)")
    for e in errors: print(f"ERROR: {e}")
    return 1 if errors else 0

if __name__ == "__main__": sys.exit(main())
