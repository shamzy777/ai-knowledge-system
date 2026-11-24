#!/usr/bin/env python3
"""Validate RUN-004 staging, provenance, execution evidence, and isolation."""
from pathlib import Path
from difflib import SequenceMatcher
import hashlib, re, sys

ROOT = Path(__file__).resolve().parents[2]
CONCEPTS = ROOT / "staging/concepts"
SOURCES = {
    "S08": ("S08__Attention Is All You Need.pdf", "bdfaa68d8984f0dc02beaca527b76f207d99b666d31d1da728ee0728182df697", "Research Paper"),
    "S09": ("S09__Speech and Language Processing 3e 2026.pdf", "88d0362c3bcb62a0cd09403fb80fd15e778dd53566943912ab1047cda3ff5c79", "Reliable Educational Reference"),
}
NEW = {"tokenization", "byte-pair-encoding", "multi-head-attention", "positional-encoding", "pretraining", "post-training", "inference"}
UPDATED = {"transformer", "self-attention", "query-key-and-value", "embedding", "language-model", "large-language-model", "sampling", "sampling-strategies", "softmax", "cross-entropy", "word2vec", "prompt-engineering", "llm-evaluation", "hallucination", "neural-network-training", "recurrent-neural-network"}
HEADINGS = ["## One-sentence Definition / 一句話定義", "## Why It Matters / 為什麼重要", "## Prerequisites / 先備概念", "## Core Idea / 核心概念", "## Concept Relationships / 概念關係", "## Mastery Level / 掌握程度", "## Sources / 來源"]

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())

def main() -> int:
    errors, warnings = [], []
    paths = sorted(CONCEPTS.glob("*.md"))
    ids = {path.stem for path in paths}
    if len(paths) != 59:
        errors.append(f"expected 59 staging concepts, found {len(paths)}")
    titles = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for link in re.findall(r"\[\[([^\]|#]+)", text):
            if link not in ids:
                errors.append(f"{path.name}: broken link [[{link}]]")
        match = re.search(r'^canonical_title:\s*"(.+)"$', text, re.M)
        if not match:
            errors.append(f"{path.name}: canonical_title missing")
            continue
        key = norm(match.group(1))
        if key in titles:
            errors.append(f"duplicate canonical title: {match.group(1)} / {titles[key]}")
        titles[key] = match.group(1)
        if path.stem in NEW:
            for marker in ["run_id: RUN-004", "publication_status: staging", "mastery_status: unconfirmed"] + HEADINGS:
                if marker not in text:
                    errors.append(f"{path.name}: missing {marker}")
            if "Provenance:" not in text:
                errors.append(f"{path.name}: provenance missing")
        if path.stem in UPDATED:
            if "RUN-004" not in text or not re.search(r"source_ids: \[[^\]]*S0(?:8|9)", text):
                errors.append(f"{path.name}: RUN-004 update/provenance missing")
    values = list(titles.values())
    for index, left in enumerate(values):
        for right in values[index + 1:]:
            ratio = SequenceMatcher(None, norm(left), norm(right)).ratio()
            if ratio >= 0.92:
                warnings.append(f"near-duplicate review: {left!r} vs {right!r} ({ratio:.2f})")
    for sid, (filename, expected, category) in SOURCES.items():
        source = ROOT / "sources/inbox" / filename
        manifest = ROOT / "sources/manifests" / f"{sid}.yaml"
        if not source.exists() or digest(source) != expected:
            errors.append(f"{sid}: source missing/checksum mismatch")
        manifest_text = manifest.read_text(encoding="utf-8") if manifest.exists() else ""
        for marker in [f"source_id: {sid}", "run_id: RUN-004", f"source_type: {category}", 'status: "validated-staging"', "permanent_ai_knowledge_system_modified: false", "publication_authorized: false"]:
            if marker not in manifest_text:
                errors.append(f"{sid} manifest missing {marker}")
    required = [
        "staging/ingests/RUN-004-S08-claims.md", "staging/ingests/RUN-004-S09-claims.md",
        "staging/ingests/RUN-004-canonical-decisions.md", "staging/ingests/RUN-004-conflicts.md",
        "staging/relationships/RUN-004-relationship-proposals.md", "staging/relationships/RUN-004-semantic-review.md",
        "docs/RUN-004-graph-semantic-audit.md", "docs/RUN-004-final-coverage-audit.md",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            errors.append(f"missing artifact: {relative}")
    for kind in ["ingest", "validation", "retries", "decisions", "graph-return-routes"]:
        if not (ROOT / f"logs/{kind}/RUN-004.md").exists():
            errors.append(f"RUN-004 {kind} log missing")
    for directory in [ROOT / "wiki", ROOT / "teaching"]:
        if directory.exists() and any(path.is_file() for path in directory.rglob("*")):
            errors.append(f"isolation violated: files under {directory.name}")
    if any("theory ↔ practice" in path.read_text(encoding="utf-8") for path in paths):
        errors.append("current concept-page mirror still contains theory ↔ practice")
    if (ROOT / "sources/manifests/S10.yaml").exists() or any((ROOT / "sources/inbox").glob("S10*")):
        errors.append("S10 was ingested without authorization")
    print(f"RUN-004 overall lint: {len(errors)} error(s), {len(warnings)} warning(s); {len(paths)} concepts")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
