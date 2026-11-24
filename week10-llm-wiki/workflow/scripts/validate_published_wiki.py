#!/usr/bin/env python3
"""Full post-publication lint for PUB-RUN-001."""
from __future__ import annotations
from pathlib import Path
import importlib.util, re, sys

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
CONCEPTS = WIKI / "concepts"
CHAPTERS = WIKI / "chapters"

spec = importlib.util.spec_from_file_location("publisher", ROOT / "workflow/scripts/publish_week10_wiki.py")
publisher = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(publisher)

def main() -> int:
    errors, warnings = [], []
    published = publisher.CORE | publisher.SUPPORTING
    concept_paths = sorted(CONCEPTS.glob("*.md"))
    ids = {path.stem for path in concept_paths}
    if ids != published:
        errors.append(f"published set mismatch: missing={sorted(published-ids)}, extra={sorted(ids-published)}")
    if len(concept_paths) != 51:
        errors.append(f"expected 51 concepts, found {len(concept_paths)}")
    core_count = supporting_count = 0
    for path in concept_paths:
        text = path.read_text(encoding="utf-8")
        staging = (ROOT / "staging/concepts" / path.name).read_text(encoding="utf-8")
        for marker in ["type: wiki-concept", "publication_status: published-week10", "publication_gate: PUB-GATE-001", "publication_run: PUB-RUN-001", "mastery_status: unconfirmed", "## Sources / 來源", "Provenance:"]:
            if marker not in text:
                errors.append(f"{path.name}: missing {marker}")
        expected_class = "Core" if path.stem in publisher.CORE else "Supporting"
        if f"publication_class: {expected_class}" not in text:
            errors.append(f"{path.name}: wrong publication class")
        core_count += expected_class == "Core"
        supporting_count += expected_class == "Supporting"
        stage_sources = re.search(r"^source_ids:\s*\[([^\]]+)\]", staging, re.M)
        wiki_sources = re.search(r"^source_ids:\s*\[([^\]]+)\]", text, re.M)
        if not stage_sources or not wiki_sources or stage_sources.group(1) != wiki_sources.group(1):
            errors.append(f"{path.name}: source_ids changed during publication")
        for sid in re.findall(r"S\d{2}", wiki_sources.group(1) if wiki_sources else ""):
            if sid not in text:
                errors.append(f"{path.name}: source {sid} missing from content")
        for link in re.findall(r"\[\[([^\]|#]+)", text):
            if link not in ids:
                errors.append(f"{path.name}: broken/unpublished wikilink [[{link}]]")
        if "Unpublished" in text or "staging draft" in text or "staging shadow" in text:
            errors.append(f"{path.name}: stale staging publication language")
    if (core_count, supporting_count) != (33, 18):
        errors.append(f"classification count mismatch: Core={core_count}, Supporting={supporting_count}")
    for stem in publisher.DEFERRED:
        if not (ROOT / "staging/concepts" / f"{stem}.md").exists():
            errors.append(f"deferred concept missing from staging: {stem}")
        if (CONCEPTS / f"{stem}.md").exists():
            errors.append(f"deferred concept published: {stem}")

    chapter_paths = sorted(CHAPTERS.glob("*.md"))
    if len(chapter_paths) != 7:
        errors.append(f"expected 7 chapter pages, found {len(chapter_paths)}")
    chapter_members = []
    orders = []
    for path in chapter_paths:
        text = path.read_text(encoding="utf-8")
        for marker in ["type: wiki-chapter-navigation", "publication_status: published-week10", "navigation_only: true", "canonical_concept: false", "mastery_status: not-applicable"]:
            if marker not in text:
                errors.append(f"{path.name}: missing {marker}")
        order = re.search(r"^chapter_order:\s*(\d+)", text, re.M)
        if order:
            orders.append(int(order.group(1)))
        for relative in re.findall(r"\]\(\.\./concepts/([a-z0-9-]+)\.md\)", text):
            chapter_members.append(relative)
            if relative not in ids:
                errors.append(f"{path.name}: chapter link to unpublished concept {relative}")
    if sorted(orders) != list(range(1, 8)):
        errors.append(f"chapter order invalid: {orders}")
    if set(chapter_members) != ids:
        errors.append(f"chapter membership mismatch: missing={sorted(ids-set(chapter_members))}, extra={sorted(set(chapter_members)-ids)}")
    if len(chapter_members) != len(set(chapter_members)):
        warnings.append("one or more concepts appear in multiple chapter pages")

    registry = (WIKI / "relationship-registry.md").read_text(encoding="utf-8")
    rows = []
    for line in registry.splitlines():
        if line.startswith("| ["):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) == 5:
                rows.append(cells)
            else:
                errors.append(f"relationship row schema invalid: {line}")
    if len(rows) != 72 or "relationship_count: 72" not in registry:
        errors.append(f"expected 72 relationship rows, found {len(rows)}")
    allowed = set(publisher.VOCAB)
    for left, rel, right, proposal_ids, support in rows:
        left_link = re.search(r"\(concepts/([a-z0-9-]+)\.md\)", left)
        right_link = re.search(r"\(concepts/([a-z0-9-]+)\.md\)", right)
        relation = rel.strip("`")
        if not left_link or left_link.group(1) not in ids or not right_link or right_link.group(1) not in ids:
            errors.append(f"registry endpoint invalid: {left} -> {right}")
        if relation not in allowed:
            errors.append(f"registry relationship invalid: {relation}")
        if not re.search(r"R[1-4]-\d{3}", proposal_ids) or not re.search(r"S\d{2}", support):
            errors.append(f"registry provenance incomplete: {left} {relation} {right}")
    if any(row[1].strip("`") == "theory ↔ practice" for row in rows):
        errors.append("superseded theory ↔ practice edge published")

    if "canonical_title: \"Tokenization（詞元化）\"" not in (CONCEPTS / "tokenization.md").read_text(encoding="utf-8"):
        errors.append("Tokenization canonical bilingual term incorrect")
    hallucination = (CONCEPTS / "hallucination.md").read_text(encoding="utf-8")
    for marker in ["conflict_status: resolved-at-PUB-GATE-001", "fluent model output that is ungrounded or incorrect", "## Course Perspective / 課程觀點", "Provenance: Course Material", "Provenance: Reliable Educational Reference"]:
        if marker not in hallucination:
            errors.append(f"Hallucination conflict treatment missing: {marker}")
    teaching_implementation = [
        path for path in (ROOT / "teaching").rglob("*")
        if path.is_file() and path.suffix.lower() in {".html", ".css", ".js", ".jsx", ".tsx"}
    ]
    proposal = ROOT / "teaching/paths/TEACH-PATH-001-proposal.md"
    proposal_text = proposal.read_text(encoding="utf-8") if proposal.exists() else ""
    html_authorized = "status: approved-for-html-implementation" in proposal_text and "html_authorized: true" in proposal_text
    if teaching_implementation and not html_authorized:
        errors.append(f"teaching implementation created before HTML authorization: {teaching_implementation}")
    if (ROOT / "sources/manifests/S10.yaml").exists() or any((ROOT / "sources/inbox").glob("S10*")):
        errors.append("S10 was ingested")
    if not (WIKI / "README.md").exists():
        errors.append("Wiki index missing")
    print(f"PUB-RUN-001 Wiki lint: {len(errors)} error(s), {len(warnings)} warning(s); concepts={len(concept_paths)} (Core={core_count}, Supporting={supporting_count}); chapters={len(chapter_paths)}; relationships={len(rows)}; deferred={len(publisher.DEFERRED)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
