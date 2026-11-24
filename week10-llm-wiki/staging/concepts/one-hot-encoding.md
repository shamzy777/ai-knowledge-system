---
type: staging-concept
concept_id: one-hot-encoding
canonical_title: "One-Hot Encoding（獨熱編碼）"
run_id: RUN-001
source_ids: [S04, S03, S01, S02, S06]
updated_by_runs: [RUN-002, RUN-003]
decision: create-new-week10-candidate
parent_match: null
publication_status: staging
mastery_status: unconfirmed
---

# One-Hot Encoding（獨熱編碼）

## One-sentence Definition / 一句話定義

One-Hot Encoding（獨熱編碼） represents one identity with a vector containing one `1` and zeros elsewhere.

Source: S04, pp. 67–75.

## Source Perspectives / 來源觀點

S03 uses one-hot encoding as a hard target in cross entropy: all target mass is assigned to the correct class. It then contrasts this with a teacher's soft target distribution.

Source: S03, pp. 76–81, 88–92.

S02 uses one-hot output labels in supervised classification and MNIST; S06 applies one-hot encoding in the ten-class implementation. S01 contains a handwritten preprocessing example.

Source: S02, pp. 7–13, 109–123; S06, pp. 59–89; S01, p. 4.

## Why It Matters / 為什麼重要

It gives categorical items distinct numeric identities but does not by itself express semantic similarity.

Source: S04, pp. 67–75.

## Prerequisites / 先備概念

- Categorical identity（類別識別）
- Vector representation（向量表示）

Source basis: S04, pp. 67–75.

## Core Idea / 核心概念

S04 uses one-hot vectors for vocabulary identities and contrasts them with learned embeddings that can carry relational features.

Source: S04, pp. 67–75.

## Concept Relationships / 概念關係

- contrast: [[embedding]] — sparse identity code versus learned feature representation (S04 pp. 67–75).
- part-of: [[hard-and-soft-targets]] — one-hot labels are hard targets (S03 pp. 88–92).
- part-of: [[cross-entropy]] — one-hot targets simplify the loss to the correct-class term (S03 pp. 76–81).
- part-of: [[classification]] — categorical target representation in the taught multiclass route (S02 pp. 7–13, 109–123; S06 pp. 59–89).

## Mastery Level / 掌握程度

Unconfirmed. RUN-001 does not infer or change mastery.

## Sources / 來源

- S04 — *Copy of 04LLM只是在猜下一個字？.pdf*, pp. 67–75. Provenance: Course Material.
- S03 — *Copy of 03AI為什麼每次都不一樣？.pdf*, pp. 76–81, 88–92. Provenance: Course Material.
- S01 — *AI程式設計 ~9_29 筆記.pdf*, p. 4. Provenance: Course Material; handwriting uncertainty.
- S02 — *02神經網路的概念.pdf*, pp. 7–13, 109–123. Provenance: Course Material.
- S06 — *07 Implementation of Neural Networks.pdf*, pp. 59–89. Provenance: Course Material.
- Read-only permanent match, when listed in frontmatter, was used for identity comparison only and is not counted as an ingested source.

## Staging Notes / 暫存說明

- Unpublished Week 10 staging draft.
- No model-knowledge supplement has been added.

