#!/usr/bin/env python3
"""Validate RUN-001 staging artifacts with Python standard library only."""

from __future__ import annotations

import hashlib
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONCEPT_DIR = ROOT / "staging" / "concepts"
RELATION_FILE = ROOT / "staging" / "relationships" / "RUN-001-S04-relationships.md"
MANIFEST = ROOT / "sources" / "manifests" / "S04.yaml"
SOURCE = ROOT / "sources" / "inbox" / "S04__Copy of 04LLM只是在猜下一個字？.pdf"
CONFLICT_FILE = ROOT / "staging" / "ingests" / "RUN-001-S04-conflicts.md"

REQUIRED_HEADINGS = [
    "## One-sentence Definition / 一句話定義",
    "## Why It Matters / 為什麼重要",
    "## Prerequisites / 先備概念",
    "## Core Idea / 核心概念",
    "## Concept Relationships / 概念關係",
    "## Mastery Level / 掌握程度",
    "## Sources / 來源",
]

REQUIRED_FRONTMATTER = [
    "type: staging-concept",
    "run_id: RUN-001",
    "publication_status: staging",
    "mastery_status: unconfirmed",
]

ALLOWED_RELATIONSHIPS = {
    "prerequisite",
    "part-of",
    "cause/effect",
    "evolution",
    "application",
    "contrast",
    "theory ↔ practice",
    "cross-domain analogy",
}

TITLE_TO_ID = {
    "Neural Network": "neural-network",
    "Language Model": "language-model",
    "Large Language Model": "large-language-model",
    "Recurrent Neural Network": "recurrent-neural-network",
    "Transformer": "transformer",
    "Query, Key, and Value": "query-key-and-value",
    "Self-Attention": "self-attention",
    "Softmax": "softmax",
    "Sampling": "sampling",
    "Sampling Strategies": "sampling-strategies",
    "One-Hot Encoding": "one-hot-encoding",
    "Embedding": "embedding",
    "Pretext Task": "pretext-task",
    "Word2Vec": "word2vec",
    "Hallucination": "hallucination",
    "Prompt Engineering": "prompt-engineering",
    "LLM Evaluation": "llm-evaluation",
}


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    all_concept_files = sorted(CONCEPT_DIR.glob("*.md"))
    concept_files = [
        path for path in all_concept_files
        if "run_id: RUN-001" in path.read_text(encoding="utf-8")
    ]
    if len(concept_files) != 17:
        errors.append(f"expected 17 RUN-001 concept drafts; found {len(concept_files)}")

    ids = {path.stem for path in all_concept_files}
    titles: dict[str, str] = {}

    for path in concept_files:
        text = path.read_text(encoding="utf-8")
        for marker in REQUIRED_FRONTMATTER:
            if marker not in text:
                errors.append(f"{path.name}: missing frontmatter marker {marker!r}")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.name}: missing required heading {heading!r}")
        if "S04" not in text or "Provenance: Course Material" not in text:
            errors.append(f"{path.name}: missing S04 course-material provenance")
        if "No model-knowledge supplement has been added." not in text:
            errors.append(f"{path.name}: model-knowledge boundary not explicit")
        if "Unconfirmed. RUN-001 does not infer or change mastery." not in text:
            errors.append(f"{path.name}: mastery confirmation boundary missing")

        match = re.search(r'^canonical_title:\s*"(.+)"$', text, re.MULTILINE)
        if not match:
            errors.append(f"{path.name}: canonical_title missing")
        else:
            title = match.group(1)
            key = normalize(title)
            if key in titles:
                errors.append(f"duplicate normalized title: {title!r} and {titles[key]!r}")
            titles[key] = title

        for link in re.findall(r"\[\[([^\]|#]+)", text):
            if link not in ids:
                errors.append(f"{path.name}: broken staging link [[{link}]]")

    title_values = list(titles.values())
    for index, left in enumerate(title_values):
        for right in title_values[index + 1 :]:
            ratio = SequenceMatcher(None, normalize(left), normalize(right)).ratio()
            if ratio >= 0.92:
                warnings.append(f"near-duplicate title review: {left!r} vs {right!r} ({ratio:.2f})")

    if not RELATION_FILE.exists():
        errors.append("relationship register missing")
    else:
        rows = []
        for line in RELATION_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("|") and not line.startswith("|---"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if cells and cells[0] != "From":
                    rows.append(cells)
        if not rows:
            errors.append("relationship register has no data rows")
        for cells in rows:
            if len(cells) != 4:
                errors.append(f"malformed relationship row: {cells}")
                continue
            source_title, relationship, target_title, support = cells
            if relationship not in ALLOWED_RELATIONSHIPS:
                errors.append(f"unsupported relationship vocabulary: {relationship!r}")
            for title in (source_title, target_title):
                concept_id = TITLE_TO_ID.get(title)
                if not concept_id or concept_id not in ids:
                    errors.append(f"relationship endpoint has no staging concept: {title!r}")
            if "S04 pp." not in support and "S04 p." not in support:
                errors.append(f"relationship lacks page-level S04 support: {cells}")

    if not MANIFEST.exists():
        errors.append("S04 manifest missing")
    else:
        manifest_text = MANIFEST.read_text(encoding="utf-8")
        for marker in [
            "source_id: S04",
            "run_id: RUN-001",
            "count_toward_5_plus: true",
            'status: "validated-staging"',
            "permanent_ai_knowledge_system_modified: false",
            "publication_authorized: false",
        ]:
            if marker not in manifest_text:
                errors.append(f"manifest missing control {marker!r}")

    if not SOURCE.exists():
        errors.append("local S04 source copy missing")
    else:
        expected = "fd7ef7efa4281b6f356430a4c04715d81f7e870c8f76a1a7d2d73e381eed59d4"
        actual = sha256(SOURCE)
        if actual != expected:
            errors.append(f"S04 checksum mismatch: expected {expected}, got {actual}")

    if not CONFLICT_FILE.exists():
        errors.append("RUN-001 conflict register missing")
    else:
        conflict_text = CONFLICT_FILE.read_text(encoding="utf-8")
        for marker in [
            "requires_user_confirmation_before_publication: true",
            "CONFLICT-001",
            "Hallucination",
        ]:
            if marker not in conflict_text:
                errors.append(f"conflict register missing control {marker!r}")

    for directory in [ROOT / "wiki", ROOT / "teaching"]:
        unexpected = [path for path in directory.rglob("*") if path.is_file()]
        if unexpected:
            errors.append(f"publication boundary violated: files found under {directory.name}/")

    required_logs = [
        ROOT / "logs" / "ingest" / "RUN-001.md",
        ROOT / "logs" / "validation" / "RUN-001.md",
        ROOT / "logs" / "retries" / "RUN-001.md",
        ROOT / "logs" / "graph-return-routes" / "RUN-001.md",
        ROOT / "logs" / "decisions" / "RUN-001.md",
    ]
    for path in required_logs:
        if not path.exists():
            errors.append(f"required RUN-001 log missing: {path.relative_to(ROOT)}")

    print(f"RUN-001 lint: {len(errors)} error(s), {len(warnings)} warning(s)")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
