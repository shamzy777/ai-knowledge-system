# Proposed Ingest Set

Date: 2026-11-23 (Asia/Taipei)

S01-S07 have now been verified and ingested as the primary course-first set. Each has a separate manifest and provenance identity; RUN-001, RUN-002, and RUN-003 reached validated staging. No source has been published.

## Recommended course-first set

The primary set preserves the user's course context. External sources are optional later gap-fill material, not automatic inputs.

| ID | Candidate source | Type | Intended contribution | Readiness |
|---|---|---|---|---|
| S01 | `AI程式設計 ~9_29 筆記.pdf` | Course Material | Data representation, neural-network and training prerequisites | RUN-003 validated staging; OCR/handwriting caution |
| S02 | `02神經網路的概念.pdf` | Course Material | Function-learning view, parameters, loss, gradient, and training | RUN-003 validated staging |
| S03 | `Copy of 03AI為什麼每次都不一樣？.pdf` | Course Material | Distribution, Softmax, sampling, and generative framing | RUN-002 validated staging |
| S04 | `Copy of 04LLM只是在猜下一個字？.pdf` | Course Material | Language models, RNN/Transformer, attention, sampling, embeddings, prompting | RUN-001 validated staging |
| S05 | `06 Concepts of Neural Networks.pdf` | Course Material | Neural-network architecture prerequisites | RUN-003 validated staging |
| S06 | `07 Implementation of Neural Networks.pdf` | Course Material | Implementation and training workflow | RUN-003 validated staging |
| S07 | `AI程式設計-筆記10/6.jpg` | Course Material | Later implementation context and validation | RUN-003 validated staging; handwriting caution |

S01-S07 are now separately manifested and ingested. The existing aggregate MLP note remains excluded as a substitute for those source records.

## External gap-fill status

S08 and S09 were explicitly authorized for RUN-004 and retain non-course provenance. S10 remains deferred and must not be ingested automatically.

| ID | Candidate source | Type | Stable locator | Intended contribution |
|---|---|---|---|---|
| S08 | Vaswani et al., **Attention Is All You Need** (2017) | Research Paper | https://arxiv.org/abs/1706.03762 | RUN-004 validated staging; original Transformer, attention, multi-head attention, positional encoding |
| S09 | Jurafsky & Martin, **Speech and Language Processing**, 3rd ed. online manuscript, 2026 release | Reliable Educational Reference | https://web.stanford.edu/~jurafsky/slp3/ | RUN-004 validated staging; tokens, embeddings, language modeling, pre/post-training, inference |
| S10 | Hugging Face, **LLM Course** | Official Documentation / Educational Reference | https://huggingface.co/learn/llm-course/chapter1/1 | Not ingested; only needed for a future hands-on implementation path |

## Primary 5+ assignment set

S01-S07 constitute the seven-source primary assignment set and exceed the five-source minimum while preserving course provenance. S08-S09 are supplementary ingests and are not blended into Course Material. S10 contributes zero because it remains un-ingested.

## Execution status

RUN-001 (S04), RUN-002 (S03), RUN-003 (S01/S02/S05/S06/S07), and RUN-004 (S08/S09) are validated staging executions. S10 remains un-ingested. Nothing may publish without the required human confirmation.

## Model knowledge

Model knowledge is not an ingest candidate. It may later supply clearly labelled supplementary explanations, but it contributes zero toward the 5+ source count.
