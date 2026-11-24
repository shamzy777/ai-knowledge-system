#!/usr/bin/env python3
"""Validate PUB-GATE-001 coverage, classifications, source identity, and isolation."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[2]
REVIEW = ROOT / "docs/PUB-GATE-001-publication-review.md"
CONCEPTS = ROOT / "staging/concepts"

def main() -> int:
    errors = []
    text = REVIEW.read_text(encoding="utf-8")
    segment = text.split("## Complete 59-concept review", 1)[1].split("## Proposed chapter membership", 1)[0]
    rows = []
    for line in segment.splitlines():
        if re.match(r"^\| .+ \| \*\*(Core|Supporting|Deferred)\*\* \|", line):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) != 7:
                errors.append(f"bad review row schema: {line}")
            else:
                rows.append(cells)
    if len(rows) != 59:
        errors.append(f"expected 59 review rows, found {len(rows)}")
    review_by_title = {row[0]: row for row in rows}
    if len(review_by_title) != len(rows):
        errors.append("duplicate concept in review")
    staging = {}
    for path in CONCEPTS.glob("*.md"):
        page = path.read_text(encoding="utf-8")
        title = re.search(r'^canonical_title:\s*"(.+)"$', page, re.M)
        sources = re.search(r'^source_ids:\s*\[([^\]]+)\]$', page, re.M)
        if not title or not sources:
            errors.append(f"{path.name}: title/source_ids missing")
            continue
        staging[title.group(1)] = {item.strip() for item in sources.group(1).split(",")}
        if "mastery_status: unconfirmed" not in page:
            errors.append(f"{path.name}: mastery changed or unconfirmed marker missing")
    if set(staging) != set(review_by_title):
        errors.append(f"review/staging title mismatch: missing={sorted(set(staging)-set(review_by_title))}; extra={sorted(set(review_by_title)-set(staging))}")
    counts = {"Core": 0, "Supporting": 0, "Deferred": 0}
    for title, row in review_by_title.items():
        status = row[1].strip("*")
        counts[status] += 1
        listed_sources = {item.strip() for item in row[3].split(",")}
        if listed_sources != staging.get(title, set()):
            errors.append(f"{title}: source mismatch {sorted(listed_sources)} vs {sorted(staging.get(title, set()))}")
        if status == "Deferred" and row[4] != "—":
            errors.append(f"{title}: deferred concept has publication chapter")
        if status != "Deferred" and not re.match(r"^[1-7]\. ", row[4]):
            errors.append(f"{title}: publishable concept lacks chapter")
        if any(not cell for cell in [row[2], row[5], row[6]]):
            errors.append(f"{title}: reason/prerequisite/issue field empty")
    if counts != {"Core": 33, "Supporting": 18, "Deferred": 8}:
        errors.append(f"incorrect classification counts: {counts}")
    required_decisions = [
        "Backpropagation computes gradients", "single-label multiclass classification",
        "narrower S09 technical definition", "different task/teaching contexts",
        "architectural/evolutionary scope differences", "variants, not contradictions",
    ]
    for phrase in required_decisions:
        if phrase not in text:
            errors.append(f"human conflict decision missing: {phrase}")
    if "publication_authorized: false" in text:
        for directory in [ROOT / "wiki", ROOT / "teaching"]:
            if directory.exists() and any(path.is_file() for path in directory.rglob("*")):
                errors.append(f"publication isolation violated before approval: file under {directory.name}")
    elif any(path.is_file() for path in (ROOT / "teaching").rglob("*")):
        errors.append("teaching artifact created before teaching-path approval")
    if not re.search(r"publication_authorized: (?:false|true)", text) or "mastery_changed: false" not in text:
        errors.append("gate authorization/mastery safeguards missing")
    print(f"PUB-GATE-001 lint: {len(errors)} error(s); {len(rows)} concepts; Core={counts['Core']}, Supporting={counts['Supporting']}, Deferred={counts['Deferred']}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
