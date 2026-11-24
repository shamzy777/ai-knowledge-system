#!/usr/bin/env python3
"""Validate RUN-003 concepts, provenance, source identity, logs, audit, and isolation."""
from __future__ import annotations
import hashlib, re, sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONCEPTS = ROOT / "staging/concepts"
SOURCES = {
 "S01": ("S01__AI程式設計 ~9_29 筆記.pdf", "a00dc3e98d48c0482ead6aa2fc07b2fa9b96477b626617a61072274648f967d8"),
 "S02": ("S02__02神經網路的概念.pdf", "2e57f2fe14f540e3280d82f762d3ddf8d06d5d8c99e468ff5175bf8ff50e530c"),
 "S05": ("S05__06 Concepts of Neural Networks.pdf", "0bbd493adcdb94c604c22d746974d7db619e98b254db93a76c4ea9070f9223a6"),
 "S06": ("S06__07 Implementation of Neural Networks.pdf", "0e9fd245a470cdcbd92441c68ae566bf7d44a910a0f2a0e970af08da0b8cb8fe"),
 "S07": ("S07__AI程式設計-筆記10-6.jpg", "2fe559964a9d56478860d1c3eccc1e6988a0259e545950b079bb22dddc4f6d3c"),
}
NEW = {"activation-function","backpropagation","classification","data-preprocessing","epoch-and-batch","evaluation-metric","feature-scaling","forward-propagation","gradient","hyperparameter","learning-rate","multilayer-perceptron","neural-network-training","optimizer","overfitting","perceptron","regression","tensor","tensorboard","training-validation-and-test-sets","weight-and-bias","weight-initialization"}
UPDATED = {"neural-network","loss-function","cross-entropy","softmax","distribution","one-hot-encoding"}
HEADINGS = ["## One-sentence Definition / 一句話定義","## Why It Matters / 為什麼重要","## Prerequisites / 先備概念","## Core Idea / 核心概念","## Concept Relationships / 概念關係","## Mastery Level / 掌握程度","## Sources / 來源"]

def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024), b""): h.update(block)
    return h.hexdigest()
def norm(s:str)->str: return re.sub(r"[^a-z0-9]+","",s.lower())

def main()->int:
    errors=[]; warnings=[]
    paths=sorted(CONCEPTS.glob("*.md")); ids={p.stem for p in paths}
    if len(paths)!=52: errors.append(f"expected 52 concepts, found {len(paths)}")
    if not (NEW|UPDATED).issubset(ids): errors.append("RUN-003 concept set incomplete")
    titles={}
    for p in paths:
        text=p.read_text(encoding="utf-8")
        for link in re.findall(r"\[\[([^\]|#]+)",text):
            if link not in ids: errors.append(f"{p.name}: broken link [[{link}]]")
        m=re.search(r'^canonical_title:\s*"(.+)"$',text,re.M)
        if not m: errors.append(f"{p.name}: canonical_title missing"); continue
        key=norm(m.group(1))
        if key in titles: errors.append(f"duplicate title {m.group(1)!r}/{titles[key]!r}")
        titles[key]=m.group(1)
        if p.stem in NEW:
            for marker in ["run_id: RUN-003","publication_status: staging","mastery_status: unconfirmed","Provenance: Course Material"]:
                if marker not in text: errors.append(f"{p.name}: missing {marker}")
            for heading in HEADINGS:
                if heading not in text: errors.append(f"{p.name}: missing heading {heading}")
            if "model-knowledge supplement added" not in text.lower(): errors.append(f"{p.name}: model-knowledge boundary missing")
        if p.stem in UPDATED:
            if "RUN-003" not in text or not re.search(r"source_ids: \[[^\]]*S0(?:1|2|5|6|7)",text): errors.append(f"{p.name}: batch update/provenance missing")
    values=list(titles.values())
    for i,left in enumerate(values):
        for right in values[i+1:]:
            ratio=SequenceMatcher(None,norm(left),norm(right)).ratio()
            if ratio>=.92: warnings.append(f"near-duplicate review: {left!r} vs {right!r} ({ratio:.2f})")
    for sid,(name,digest) in SOURCES.items():
        source=ROOT/"sources/inbox"/name; manifest=ROOT/"sources/manifests"/f"{sid}.yaml"
        if not source.exists() or sha(source)!=digest: errors.append(f"{sid}: source missing/checksum mismatch")
        if not manifest.exists(): errors.append(f"{sid}: manifest missing")
        else:
            mt=manifest.read_text(encoding="utf-8")
            for marker in [f"source_id: {sid}","run_id: RUN-003","count_toward_5_plus: true",'status: "validated-staging"',"permanent_ai_knowledge_system_modified: false","publication_authorized: false"]:
                if marker not in mt: errors.append(f"{sid} manifest missing {marker}")
        if not (ROOT/f"staging/ingests/RUN-003-{sid}-claims.md").exists(): errors.append(f"{sid}: claims missing")
    for rel in ["staging/ingests/RUN-003-canonical-decisions.md","staging/ingests/RUN-003-conflicts.md","staging/relationships/RUN-003-batch-relationship-proposals.md","staging/relationships/RUN-003-batch-semantic-review.md","docs/RUN-003-cross-source-staging-audit.md"]:
        if not (ROOT/rel).exists(): errors.append(f"required artifact missing: {rel}")
    for kind in ["ingest","validation","retries","decisions","graph-return-routes"]:
        if not (ROOT/f"logs/{kind}/RUN-003.md").exists(): errors.append(f"RUN-003 {kind} log missing")
    for directory in [ROOT/"wiki",ROOT/"teaching"]:
        if directory.exists() and any(x.is_file() for x in directory.rglob("*")): errors.append(f"isolation violated: files under {directory.name}")
    embedding=(CONCEPTS/"embedding.md").read_text(encoding="utf-8")
    if "RUN-003" in embedding or any(s in embedding for s in ["S01","S02","S05","S06","S07"]): errors.append("Embedding was improperly updated by RUN-003")
    print(f"RUN-003 lint: {len(errors)} error(s), {len(warnings)} warning(s); {len(paths)} concepts")
    for w in warnings: print(f"WARNING: {w}")
    for e in errors: print(f"ERROR: {e}")
    return 1 if errors else 0
if __name__=="__main__": sys.exit(main())
