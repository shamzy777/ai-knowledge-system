#!/usr/bin/env python3
"""Validate RUN-002 concepts, provenance, isolation, and execution evidence."""

from __future__ import annotations

import hashlib
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONCEPT_DIR = ROOT / "staging" / "concepts"
SOURCE = ROOT / "sources" / "inbox" / "S03__Copy of 03AI為什麼每次都不一樣？.pdf"
MANIFEST = ROOT / "sources" / "manifests" / "S03.yaml"

NEW = {
    "generative-ai", "latent-vector", "generative-adversarial-network", "mode-collapse",
    "gan-variants", "distribution", "information", "entropy", "cross-entropy",
    "kl-divergence", "hard-and-soft-targets", "loss-function", "knowledge-distillation",
}
UPDATED = {"softmax", "sampling", "language-model", "one-hot-encoding", "hallucination"}
REQUIRED_HEADINGS = [
    "## One-sentence Definition / 一句話定義", "## Why It Matters / 為什麼重要",
    "## Prerequisites / 先備概念", "## Core Idea / 核心概念",
    "## Concept Relationships / 概念關係", "## Mastery Level / 掌握程度",
    "## Sources / 來源",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    paths = sorted(CONCEPT_DIR.glob("*.md"))
    ids = {path.stem for path in paths}
    if len(paths) != 30:
        errors.append(f"expected 30 total staging concepts after RUN-002; found {len(paths)}")
    if not NEW.issubset(ids) or not UPDATED.issubset(ids):
        errors.append("RUN-002 new/updated concept set is incomplete")

    titles: dict[str, str] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for link in re.findall(r"\[\[([^\]|#]+)", text):
            if link not in ids:
                errors.append(f"{path.name}: broken staging link [[{link}]]")
        match = re.search(r'^canonical_title:\s*"(.+)"$', text, re.MULTILINE)
        if not match:
            errors.append(f"{path.name}: canonical_title missing")
        else:
            key = normalize(match.group(1))
            if key in titles:
                errors.append(f"duplicate normalized title: {match.group(1)!r} and {titles[key]!r}")
            titles[key] = match.group(1)

        if path.stem in NEW:
            for marker in ["type: staging-concept", "run_id: RUN-002", "source_ids: [S03]",
                           "publication_status: staging", "mastery_status: unconfirmed"]:
                if marker not in text:
                    errors.append(f"{path.name}: missing marker {marker!r}")
            for heading in REQUIRED_HEADINGS:
                if heading not in text:
                    errors.append(f"{path.name}: missing required heading {heading!r}")
            if "Provenance: Course Material" not in text or "S03" not in text:
                errors.append(f"{path.name}: missing S03 course-material provenance")
            if "no model-knowledge supplement has been added" not in text.lower():
                errors.append(f"{path.name}: model-knowledge boundary missing")
            if "Unconfirmed. RUN-002 does not infer or change mastery." not in text:
                errors.append(f"{path.name}: mastery boundary missing")
        elif path.stem in UPDATED:
            for marker in ["source_ids: [S04, S03]", "updated_by_runs: [RUN-002]",
                           "## Source Perspectives / 來源觀點", "Provenance: Course Material"]:
                if marker not in text:
                    errors.append(f"{path.name}: multi-source update marker missing {marker!r}")
            if "S03" not in text:
                errors.append(f"{path.name}: missing S03 source perspective")

    title_values = list(titles.values())
    for index, left in enumerate(title_values):
        for right in title_values[index + 1:]:
            ratio = SequenceMatcher(None, normalize(left), normalize(right)).ratio()
            if ratio >= 0.92:
                warnings.append(f"near-duplicate title review: {left!r} vs {right!r} ({ratio:.2f})")

    sampling_strategies = (CONCEPT_DIR / "sampling-strategies.md").read_text(encoding="utf-8")
    if "S03" in sampling_strategies:
        errors.append("Sampling Strategies was updated from S03 despite absent strategy evidence")

    for path in [
        ROOT / "staging/ingests/RUN-002-S03-claims.md",
        ROOT / "staging/ingests/RUN-002-S03-canonical-decisions.md",
        ROOT / "staging/ingests/RUN-002-S03-conflicts.md",
        ROOT / "staging/relationships/RUN-002-S03-relationship-proposals.md",
        ROOT / "staging/relationships/RUN-002-S03-semantic-review.md",
        ROOT / "staging/relationships/RUN-001-S04-semantic-review.md",
    ]:
        if not path.exists():
            errors.append(f"required RUN-002 artifact missing: {path.relative_to(ROOT)}")

    if not MANIFEST.exists():
        errors.append("S03 manifest missing")
    else:
        manifest = MANIFEST.read_text(encoding="utf-8")
        for marker in ["source_id: S03", "run_id: RUN-002", "count_toward_5_plus: true",
                       'status: "validated-staging"', "permanent_ai_knowledge_system_modified: false",
                       "publication_authorized: false"]:
            if marker not in manifest:
                errors.append(f"manifest missing control {marker!r}")
    expected = "07c9ce92fde094f6f681b105a88be2fb379df9d361f38fade62eb67bf97cfd36"
    if not SOURCE.exists():
        errors.append("local S03 source copy missing")
    elif sha256(SOURCE) != expected:
        errors.append("S03 checksum mismatch")

    conflict = (ROOT / "staging/ingests/RUN-002-S03-conflicts.md").read_text(encoding="utf-8")
    if "requires_user_confirmation_before_publication: true" not in conflict or "CONFLICT-001" not in conflict:
        errors.append("existing Hallucination publication gate was not preserved")

    required_logs = [
        ROOT / "logs/ingest/RUN-002.md", ROOT / "logs/validation/RUN-002.md",
        ROOT / "logs/retries/RUN-002.md", ROOT / "logs/graph-return-routes/RUN-002.md",
        ROOT / "logs/decisions/RUN-002.md",
    ]
    for path in required_logs:
        if not path.exists():
            errors.append(f"required RUN-002 log missing: {path.relative_to(ROOT)}")

    for directory in (ROOT / "wiki", ROOT / "teaching"):
        if any(path.is_file() for path in directory.rglob("*")):
            errors.append(f"publication boundary violated: files found under {directory.name}/")

    print(f"RUN-002 lint: {len(errors)} error(s), {len(warnings)} warning(s)")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
