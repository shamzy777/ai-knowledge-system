# Source Audit

Date: 2026-11-23 (Asia/Taipei)

## Scope

This is a read-only audit of the existing permanent AI Knowledge System at:

`/Users/shamzylee/Documents/Obsidian Vault/Ai knowledge system/`

No parent-system file was modified. S01-S07 have validated course-first staging outputs. S08-S09 now have official project-local copies, manifests, ingest evidence, and validated gap-fill staging outputs.

## Audit criteria

A source is **ready** when it has a distinct identity, a stable local path or URL, enough provenance to identify the original material, and relevance to the LLM Wiki.

A source is **conditional** when a useful processed course note exists but the original material lacks a stable locator, accessible artifact, version, or clear separation from other sources.

A record is **excluded from the 5+ count** when it is an internal canonical note, index, prototype presentation, model knowledge, or an aggregate that cannot yet be traced to its underlying materials.

## Inventory summary

- 80 root-level Markdown knowledge records were found. These are primarily canonical concepts or system pages, not independent source ingests.
- 10 Markdown course records were found under `Courses/`.
- The original S01-S07 artifacts have now been resolved and verified in Google Drive by exact filename, file ID, MIME type, size, and parent folder.
- S01-S06 are PDF files. S07 is a JPEG image and must use image/OCR-aware ingestion rather than a PDF path.
- The AI Programming MLP/training note remains an aggregate synthesis, but its four underlying source artifacts are now independently identifiable as S01 and S05-S07.
- S04 has been copied into this project for RUN-001 and verified as a 115-page, unencrypted Keynote-generated PDF with SHA-256 `fd7ef7efa4281b6f356430a4c04715d81f7e870c8f76a1a7d2d73e381eed59d4`.

## Verified course-first artifact register

| ID | Exact Drive title | MIME type | Size (bytes) | Drive file ID | Status |
|---|---|---:|---:|---|---|
| S01 | `AI程式設計 ~9_29 筆記.pdf` | `application/pdf` | 3,301,123 | `1IZ2FHaaF0YmaWgGLq1aFd0X3rBfmZQhc` | RUN-003 validated staging; handwriting uncertainty retained |
| S02 | `02神經網路的概念.pdf` | `application/pdf` | 90,486,096 | `15wzeEhfpLPqpKxSiZj5Io3Y3nuPpEnzW` | RUN-003 validated staging; conflict recorded |
| S03 | `Copy of 03AI為什麼每次都不一樣？.pdf` | `application/pdf` | 64,720,520 | `1MpZP76_KNYfTGth9q9JKDFh-KsRUHDGP` | RUN-002 validated staging |
| S04 | `Copy of 04LLM只是在猜下一個字？.pdf` | `application/pdf` | 72,272,634 | `1p4IRG-HcuxF37nkdJcJ3LVJZbLV06JRt` | RUN-001 validated staging |
| S05 | `06 Concepts of Neural Networks.pdf` | `application/pdf` | 3,853,651 | `1ykFcPTuivt9lSC5uWBZiqIIL9fzk-0mx` | RUN-003 validated staging |
| S06 | `07 Implementation of Neural Networks.pdf` | `application/pdf` | 6,417,628 | `1m0Up92dVKIi4tqrtkZjgALPIvv56-tNZ` | RUN-003 validated staging; terminology conflict recorded |
| S07 | `AI程式設計-筆記10/6.jpg` | `image/jpeg` | 500,842 | `1TVWDShdxjapq48WR24BvJO4V9Jz_CNO-` | RUN-003 validated staging; handwriting uncertainty retained |

## Relevant existing materials

| Existing record | Relevance | Traceability | Audit status | Required action before counting |
|---|---|---|---|---|
| `Courses/人工智慧程式設計/2026-09-29 手寫筆記整理.md` | Data, neural networks, training foundations | Now matched to S01 by exact title and Drive file ID | Ready with OCR caution | Preserve the original note's OCR warnings during later ingest |
| `Courses/TAICA 生成式 AI/Week 2 神經網路.md` | Neural-network foundations and training mechanism | Now matched to S02 | Ready; not ingested | Create a manifest only when its run is authorized |
| `Courses/TAICA 生成式 AI/Week 3 GAN to LLM.md` | Probability distributions, sampling, and transition toward language models | Now matched to S03 | Ready; not ingested | Create a manifest only when its run is authorized |
| `Courses/TAICA 生成式 AI/Week 4 LLM and Transformer.md` | Language models, attention, sampling, embeddings, and use | Now matched to S04 | RUN-001 pilot | See `sources/manifests/S04.yaml` |
| `Courses/人工智慧程式設計/多層感知器的學習、訓練與驗證流程.md` | Keras implementation, training, validation | Underlying artifacts resolved as S01 and S05-S07 | Aggregate excluded; underlying artifacts ready | Count each original artifact only after its own manifest and ingest |
| `Courses/TAICA 生成式 AI/TAICA 生成式 AI.md` | Course map | General course title only | Excluded as independent ingest | Use as navigation metadata only |
| `Courses/人工智慧程式設計/人工智慧程式設計.md` | Course map | General label `AI Programming` only | Excluded as independent ingest | Use as navigation metadata only |
| Social Network Analysis and image-generation course notes | Outside current LLM scope | Mixed | Excluded for this assignment scope | None unless the Wiki scope later expands |

## Parent records that must not count as independent ingests

- Root canonical concept pages such as `Transformer.md`, `Softmax.md`, and `Large Language Model.md`.
- Maps of content and course indexes.
- Week 9 prototype Markdown, HTML, specifications, and presentation-layer content.
- Model-generated supplementary explanations.

These materials are useful read-only references for canonical matching and inherited rules, but counting them as independent sources would confuse prior synthesis with source evidence.

## Provenance risks

1. Processed permanent-system notes remain syntheses and cannot substitute for the original artifacts.
2. S01 and S07 are handwritten/image sources and will need OCR plus visual verification.
3. S04 text extraction loses mathematical layout; RUN-001 required a visual retry for the attention scaling term.
4. S04 includes time-sensitive model, hardware, service, benchmark, and productivity claims. These must not become stable canonical claims without later verification and gap-filling sources.
5. S04 uses pedagogical metaphors such as “呆萌型 AI 機器人”, “唬爛王”, and “作夢的機器”. They must be attributed as course framing, not converted into neutral technical definitions.
6. Existing mastery and first-person sections have incomplete confirmation/authorship history and must not be inferred from source ingestion.

## Audit conclusion

S01-S07 form the verified course-first set and already satisfy the 5+ requirement. S08 and S09 were subsequently ingested in RUN-004 as explicitly distinct `Research Paper` and `Reliable Educational Reference` gap-fill sources. S10 remains un-ingested and is not needed for the conceptual beginner Wiki; it is reserved for a separately authorized hands-on implementation path.
