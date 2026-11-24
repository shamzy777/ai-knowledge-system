#!/usr/bin/env python3
"""Validate semantic-review completeness; semantic judgment remains evidence review."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REL = ROOT / "staging" / "relationships"
RUN2_PROPOSALS = REL / "RUN-002-S03-relationship-proposals.md"
RUN2_REVIEW = REL / "RUN-002-S03-semantic-review.md"
RUN1_REVIEW = REL / "RUN-001-S04-semantic-review.md"
ALLOWED_OUTCOMES = {"accepted", "rejected", "returned-to-staging"}


def rows(path: Path, header: str = "ID") -> list[list[str]]:
    result: list[list[str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0] != header:
            result.append(cells)
    return result


def main() -> int:
    errors: list[str] = []
    for path in (RUN2_PROPOSALS, RUN2_REVIEW, RUN1_REVIEW):
        if not path.exists():
            errors.append(f"missing semantic artifact: {path.relative_to(ROOT)}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    proposal_rows = rows(RUN2_PROPOSALS)
    proposal_ids = {cells[0] for cells in proposal_rows if len(cells) == 6}
    review_rows = rows(RUN2_REVIEW)
    reviewed: dict[str, str] = {}
    for cells in review_rows:
        if len(cells) != 3:
            errors.append(f"RUN-002 malformed semantic row: {cells}")
            continue
        rid, outcome, rationale = cells
        if outcome not in ALLOWED_OUTCOMES:
            errors.append(f"{rid}: invalid semantic outcome {outcome!r}")
        if len(rationale) < 40 or not re.search(r"S03 pp?\.", rationale):
            errors.append(f"{rid}: semantic rationale lacks page-grounded explanation")
        reviewed[rid] = outcome
    if set(reviewed) != proposal_ids:
        errors.append(
            f"RUN-002 review/proposal mismatch: missing={sorted(proposal_ids-set(reviewed))}, "
            f"extra={sorted(set(reviewed)-proposal_ids)}"
        )

    for cells in proposal_rows:
        if len(cells) != 6:
            continue
        rid, action = cells[0], cells[1]
        if action.startswith("replacement-for-"):
            original = action.removeprefix("replacement-for-")
            if reviewed.get(original) not in {"rejected", "returned-to-staging"}:
                errors.append(f"{rid}: replacement original {original} was not rejected/returned")
            if reviewed.get(rid) != "accepted":
                errors.append(f"{rid}: replacement is not semantically accepted")

    run1_rows = rows(RUN1_REVIEW)
    run1: dict[str, str] = {}
    for cells in run1_rows:
        if len(cells) != 4:
            errors.append(f"RUN-001 malformed semantic row: {cells}")
            continue
        rid, _edge, outcome, rationale = cells
        if outcome not in ALLOWED_OUTCOMES:
            errors.append(f"{rid}: invalid semantic outcome {outcome!r}")
        if len(rationale) < 35 or not re.search(r"S04 pp?\.", rationale):
            errors.append(f"{rid}: semantic rationale lacks page-grounded explanation")
        run1[rid] = outcome
    expected_run1 = {f"R1-{n:03d}" for n in range(1, 22)}
    if set(run1) != expected_run1:
        errors.append("RUN-001 retrospective semantic review does not cover R1-001 through R1-021")
    for original, replacement in (("R1-011", "R1-020"), ("R1-017", "R1-021")):
        if run1.get(original) != "rejected" or run1.get(replacement) != "accepted":
            errors.append(f"RUN-001 return route incomplete: {original} -> {replacement}")

    print(f"Relationship semantic-record lint: {len(errors)} error(s)")
    print(
        f"RUN-002 reviewed={len(reviewed)}, accepted={sum(v == 'accepted' for v in reviewed.values())}, "
        f"rejected={sum(v == 'rejected' for v in reviewed.values())}"
    )
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
