#!/usr/bin/env python3
"""Publish the approved 51-concept Week 10 Wiki and relationship registry."""
from __future__ import annotations
from pathlib import Path
import re, shutil, sys

ROOT = Path(__file__).resolve().parents[2]
STAGING = ROOT / "staging/concepts"
WIKI = ROOT / "wiki"
OUT = WIKI / "concepts"

CORE = {
    "activation-function", "backpropagation", "cross-entropy", "distribution", "embedding",
    "forward-propagation", "gradient", "hallucination", "inference", "language-model",
    "large-language-model", "learning-rate", "llm-evaluation", "loss-function",
    "multi-head-attention", "neural-network-training", "neural-network", "optimizer",
    "overfitting", "positional-encoding", "post-training", "pretraining", "prompt-engineering",
    "query-key-and-value", "sampling-strategies", "sampling", "self-attention", "softmax",
    "tensor", "tokenization", "training-validation-and-test-sets", "transformer", "weight-and-bias",
}
SUPPORTING = {
    "byte-pair-encoding", "classification", "data-preprocessing", "entropy", "epoch-and-batch",
    "evaluation-metric", "feature-scaling", "generative-ai", "hyperparameter", "information",
    "kl-divergence", "multilayer-perceptron", "one-hot-encoding", "perceptron", "pretext-task",
    "recurrent-neural-network", "weight-initialization", "word2vec",
}
DEFERRED = {
    "gan-variants", "generative-adversarial-network", "hard-and-soft-targets",
    "knowledge-distillation", "latent-vector", "mode-collapse", "regression", "tensorboard",
}
VOCAB = ["theory ↔ practice", "cross-domain analogy", "cause/effect", "prerequisite", "application", "evolution", "contrast", "part-of"]

def cells(line: str) -> list[str]:
    return [item.strip() for item in line.strip("|").split("|")]

def title_map() -> tuple[dict[str, str], dict[str, str]]:
    title_to_stem, stem_to_title = {}, {}
    for path in STAGING.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r'^canonical_title:\s*"(.+)"$', text, re.M)
        if not match:
            raise ValueError(f"canonical title missing: {path}")
        full = match.group(1)
        short = re.sub(r"（.*?）", "", full).strip()
        title_to_stem[short] = path.stem
        stem_to_title[path.stem] = full
    return title_to_stem, stem_to_title

def semantic_outcomes(path: Path, prefix: str) -> dict[str, str]:
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if re.match(fr"\| {prefix}-\d{{3}} \|", line):
            row = cells(line)
            if prefix == "R1":
                result[row[0]] = row[2]
            else:
                result[row[0]] = row[1]
    return result

def current_relationships() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    r1_outcomes = semantic_outcomes(ROOT / "staging/relationships/RUN-001-S04-semantic-review.md", "R1")
    r1_rows = []
    for line in (ROOT / "staging/relationships/RUN-001-S04-relationships.md").read_text(encoding="utf-8").splitlines():
        row = cells(line)
        if len(row) == 4 and row[1] in VOCAB:
            r1_rows.append(row)
    for index, (left, rel, right, support) in enumerate(r1_rows, start=1):
        rid = f"R1-{index:03d}"
        if r1_outcomes.get(rid, "").startswith("accepted"):
            records.append({"from": left, "rel": rel, "to": right, "id": rid, "support": support})
    records.extend([
        {"from": "Sampling Strategies", "rel": "application", "to": "Language Model", "id": "R1-020", "support": "S04 pp. 53–64"},
        {"from": "Language Model", "rel": "cause/effect", "to": "Hallucination", "id": "R1-021", "support": "S04 pp. 38–41"},
    ])
    specs = [
        ("R2", "RUN-002-S03-relationship-proposals.md", "RUN-002-S03-semantic-review.md"),
        ("R3", "RUN-003-batch-relationship-proposals.md", "RUN-003-batch-semantic-review.md"),
        ("R4", "RUN-004-relationship-proposals.md", "RUN-004-semantic-review.md"),
    ]
    for prefix, proposal_name, review_name in specs:
        outcomes = semantic_outcomes(ROOT / "staging/relationships" / review_name, prefix)
        for line in (ROOT / "staging/relationships" / proposal_name).read_text(encoding="utf-8").splitlines():
            if not re.match(fr"\| {prefix}-\d{{3}} \|", line):
                continue
            row = cells(line)
            if len(row) != 6 or not outcomes.get(row[0], "").startswith("accepted"):
                continue
            rid, _, left, rel, right, support = row
            records.append({"from": left, "rel": rel, "to": right, "id": rid, "support": support})
    superseded = {"R3-018", "R3-023", "R3-026", "R3-027"}
    return [record for record in records if record["id"] not in superseded]

def publish_concepts() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if any(OUT.glob("*.md")):
        raise RuntimeError("wiki/concepts is not empty; refusing to overwrite")
    for stem in sorted(CORE | SUPPORTING):
        source = STAGING / f"{stem}.md"
        text = source.read_text(encoding="utf-8")
        classification = "Core" if stem in CORE else "Supporting"
        text = text.replace("type: staging-concept", "type: wiki-concept", 1)
        text = text.replace(
            "publication_status: staging",
            f"publication_status: published-week10\npublication_gate: PUB-GATE-001\npublication_run: PUB-RUN-001\npublication_class: {classification}",
            1,
        )
        text = text.replace("## Staging Notes / 暫存說明", "## Publication Notes / 發布說明")
        text = text.replace("Unpublished Week 10 staging draft", "Published in the isolated Week 10 Wiki under PUB-GATE-001")
        text = text.replace("Unpublished Week 10 staging shadow", "Published in the isolated Week 10 Wiki under PUB-GATE-001")
        text = text.replace("Unpublished", "Published in the isolated Week 10 Wiki under PUB-GATE-001")
        (OUT / source.name).write_text(text, encoding="utf-8")

def publish_relationship_registry(title_to_stem: dict[str, str], stem_to_title: dict[str, str]) -> int:
    published = CORE | SUPPORTING
    aggregate: dict[tuple[str, str, str], dict[str, set[str]]] = {}
    for record in current_relationships():
        left_stem = title_to_stem.get(record["from"])
        right_stem = title_to_stem.get(record["to"])
        if left_stem not in published or right_stem not in published:
            continue
        key = (record["from"], record["rel"], record["to"])
        item = aggregate.setdefault(key, {"ids": set(), "support": set()})
        item["ids"].add(record["id"])
        item["support"].add(record["support"])
    if len(aggregate) != 72:
        raise RuntimeError(f"expected 72 published relationships, found {len(aggregate)}")
    lines = [
        "---", "type: wiki-relationship-registry", "publication_gate: PUB-GATE-001",
        "publication_run: PUB-RUN-001", "publication_status: published-week10",
        f"relationship_count: {len(aggregate)}", "---", "", "# Week 10 Wiki Relationship Registry", "",
        "Only relationships whose two endpoints are published are included. Historical rejected/superseded proposals remain in staging logs and are not active Wiki edges.", "",
        "| From | Relationship | To | Validated proposal IDs | Source support |", "|---|---|---|---|---|",
    ]
    for (left, rel, right), evidence in sorted(aggregate.items()):
        left_stem, right_stem = title_to_stem[left], title_to_stem[right]
        left_label, right_label = stem_to_title[left_stem], stem_to_title[right_stem]
        ids = ", ".join(sorted(evidence["ids"]))
        support = "; ".join(sorted(evidence["support"]))
        lines.append(f"| [{left_label}](concepts/{left_stem}.md) | `{rel}` | [{right_label}](concepts/{right_stem}.md) | {ids} | {support} |")
    lines.extend(["", "## Scope notes", "", "- Relationships involving any of the eight Deferred concepts remain in staging and are not published in this registry.", "- Replacements from RUN-004 are active; superseded `theory ↔ practice` edges are excluded.", "- Relationship type and direction are copied from the final validated semantic state; no new edge is inferred during publication.", ""])
    (WIKI / "relationship-registry.md").write_text("\n".join(lines), encoding="utf-8")
    return len(aggregate)

def main() -> int:
    all_stems = {path.stem for path in STAGING.glob("*.md")}
    if len(all_stems) != 59 or CORE | SUPPORTING | DEFERRED != all_stems:
        raise RuntimeError("approved classification does not partition all 59 staging concepts")
    if len(CORE) != 33 or len(SUPPORTING) != 18 or len(DEFERRED) != 8:
        raise RuntimeError("approved classification counts changed")
    publish_concepts()
    title_to_stem, stem_to_title = title_map()
    relation_count = publish_relationship_registry(title_to_stem, stem_to_title)
    print(f"Published {len(CORE)} Core + {len(SUPPORTING)} Supporting concepts; {len(DEFERRED)} Deferred retained; {relation_count} relationships.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
