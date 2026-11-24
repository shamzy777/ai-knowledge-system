#!/usr/bin/env python3
"""Validate TEACH-PATH-001 before or after the recorded human approval."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = ROOT / "teaching/paths/TEACH-PATH-001-proposal.md"
WIKI = ROOT / "wiki/concepts"
PRIMARY = {
    "tokenization", "embedding", "self-attention", "transformer",
    "language-model", "large-language-model", "softmax", "sampling",
}
SUPPORTING = {
    "neural-network", "distribution", "positional-encoding",
    "query-key-and-value", "multi-head-attention", "inference", "hallucination", "llm-evaluation",
}

def count_rows(segment: str, prefix: str) -> int:
    return sum(1 for line in segment.splitlines() if line.startswith(f"| {prefix}"))

def main() -> int:
    errors, warnings = [], []
    text = PROPOSAL.read_text(encoding="utf-8") if PROPOSAL.exists() else ""
    approved = "status: approved-for-html-implementation" in text and "html_authorized: true" in text
    state_markers = ["status: approved-for-html-implementation", "html_authorized: true"] if approved else ["status: awaiting-human-approval", "html_authorized: false"]
    for marker in [
        "teaching_path_id: TEACH-PATH-001", *state_markers,
        'knowledge_source: "published Week 10 Wiki only"', "planned_section_count: 11",
        "mastery_changed: false",
    ]:
        if marker not in text:
            errors.append(f"proposal metadata missing: {marker}")
    links = re.findall(r"\]\(\.\./\.\./wiki/concepts/([a-z0-9-]+)\.md\)", text)
    if not PRIMARY.issubset(set(links)):
        errors.append(f"primary concept evidence missing: {sorted(PRIMARY-set(links))}")
    for stem in set(links):
        if not (WIKI / f"{stem}.md").exists():
            errors.append(f"evidence link is not a published concept: {stem}")
    if re.search(r"https?://", text):
        errors.append("external URL present in Wiki-only proposal")
    narrative = text.split("## 4. Teaching narrative", 1)[1].split("## 5. Visual explanation plan", 1)[0]
    section_ids = re.findall(r"^### (T\d{2}) —", narrative, re.M)
    if section_ids != [f"T{i:02d}" for i in range(1, 12)]:
        errors.append(f"teaching sections invalid: {section_ids}")
    evidence = text.split("## 3. Wiki evidence map", 1)[1].split("## 4. Teaching narrative", 1)[0]
    evidence_ids = re.findall(r"^\| (T\d{2}) —", evidence, re.M)
    if evidence_ids != [f"T{i:02d}" for i in range(1, 12)]:
        errors.append(f"evidence map sections invalid: {evidence_ids}")
    interaction = text.split("## 6. Interaction plan", 1)[1].split("## 7. Quiz plan", 1)[0]
    interaction_rows = [line for line in interaction.splitlines() if line.startswith("| ") and not line.startswith("|---") and "Interaction |" not in line]
    if len(interaction_rows) != 3:
        errors.append(f"expected 3 learning-value interactions, found {len(interaction_rows)}")
    quiz = text.split("## 7. Quiz plan", 1)[1].split("## 8. Provenance plan", 1)[0]
    quiz_ids = re.findall(r"^\| (Q\d+) \|", quiz, re.M)
    if quiz_ids != [f"Q{i}" for i in range(1, 7)]:
        errors.append(f"quiz plan invalid: {quiz_ids}")
    for label in ["Course Material", "Research Paper", "Reliable Educational Reference"]:
        if label not in text:
            errors.append(f"provenance category missing: {label}")
    for gate in ["Wiki-only factual grounding", "Concept coverage", "Prerequisite order", "Citation mapping", "Quiz-answer support", "Content density", "Beginner comprehensibility"]:
        if gate not in text:
            errors.append(f"validation criterion missing: {gate}")
    routes = {
        "Insufficient evidence": "Wiki retrieval / evidence mapping",
        "Poor learning sequence": "Teaching outline",
        "Unsupported claim": "Corresponding teaching section",
        "Excessive content density": "Section draft",
    }
    for failure, destination in routes.items():
        if failure not in text or destination not in text:
            errors.append(f"graph return missing: {failure} -> {destination}")
    html_files = [path for path in (ROOT / "teaching").rglob("*") if path.is_file() and path.suffix.lower() in {".html", ".css", ".js", ".jsx", ".tsx"}]
    if html_files and not approved:
        errors.append(f"HTML/presentation implementation created early: {[str(path.relative_to(ROOT)) for path in html_files]}")
    if any("mastery_status: unconfirmed" not in path.read_text(encoding="utf-8") for path in WIKI.glob("*.md")):
        errors.append("published Wiki mastery status changed")
    print(f"TEACH-PATH-001 lint: {len(errors)} error(s), {len(warnings)} warning(s); sections={len(section_ids)}; evidence_rows={len(evidence_ids)}; interactions={len(interaction_rows)}; quiz_items={len(quiz_ids)}; wiki_links={len(set(links))}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
