---
type: canonical-decision-register
run_id: RUN-001
source_id: S04
status: validated-staging
---

# RUN-001 — Canonical Create-vs-Update Decisions

The Week 10 staging and Wiki layers were empty before RUN-001. Therefore, matched concepts receive a new **Week 10 staging shadow** while retaining the identity of the read-only permanent canonical concept. This is not authorization to update the parent system.

| Candidate concept | Week 10 decision | Read-only permanent match | Reason |
|---|---|---|---|
| Neural Network（神經網路） | Create staging shadow | `Neural Network.md` | S04 supplies prerequisite framing; same underlying concept |
| Language Model（語言模型） | Create staging shadow | `Language Model.md` | Next-item prediction and repeated generation match the permanent identity |
| Large Language Model（大型語言模型） | Create staging shadow | `Large Language Model.md` | Same scaled language-model identity; volatile scale claims excluded |
| Recurrent Neural Network（循環神經網路） | Create staging shadow | `Recurrent Neural Network.md` | Same hidden-state recurrence concept |
| Transformer | Create staging shadow | `Transformer.md` | Same attention-based sequence architecture; S04 is intentionally incomplete |
| Query, Key, and Value（查詢、鍵、值） | Create staging shadow | `Query, Key, and Value.md` | Same Q/K/V linear-projection roles |
| Self-Attention（自注意力） | Create staging shadow | `Self-Attention.md` | Same score → Softmax → weighted-value mechanism |
| Softmax | Create staging shadow | `Softmax.md` | Same score-to-normalized-distribution mechanism |
| Sampling（取樣） | Create staging shadow | `Sampling.md` | Same probability-based selection mechanism |
| Sampling Strategies（取樣策略） | Create staging shadow | `Sampling Strategies.md` | Temperature, top-k, and top-p belong on one existing canonical identity |
| Embedding（嵌入） | Create staging shadow | `Embedding.md` | Same learned dense representation identity |
| Pretext Task（代理任務） | Create staging shadow | `Pretext Task.md` | Same proxy-task-for-representation-learning identity |
| Word2Vec | Create staging shadow | `Word2Vec.md` | CBOW and Skip-Gram belong on the existing Word2Vec identity |
| Hallucination（幻覺） | Create staging shadow | `Hallucination.md` | Same risk/creative-generation concept; course framing preserved separately |
| Prompt Engineering（提示工程） | Create staging shadow | `Prompt Engineering.md` | Same context-and-instruction design concept |
| One-Hot Encoding（獨熱編碼） | Create new Week 10 candidate | No parent canonical file found | Independent mechanism with sufficient S04 support; useful contrast with Embedding |
| LLM Evaluation（大型語言模型評估） | Create new Week 10 candidate | No parent canonical file found | Independent task-fit evaluation concept supported by pp. 88–90 |

## Deferred candidates

| Candidate | Decision | Reason |
|---|---|---|
| Natural Language Processing（自然語言處理） | Defer | Only a one-slide introductory description |
| Tokenization（分詞／標記化） | Defer RUN-001 update | The source uses character/word IDs but does not teach tokenization algorithms |
| Logit | Keep inside Softmax/Sampling drafts | Insufficient independent treatment |
| Nucleus Sampling | Merge into Sampling Strategies | Same mechanism as top-p; avoid duplicate canonical page |
| Temperature / Top-k / Top-p | Merge into Sampling Strategies | Closely coupled decoding controls already covered by one canonical identity |
| Local LLM Inference（本地 LLM 推論） | Defer | Content is dominated by volatile products, hardware, and services |
| Context/Harness/Loop/Graph Engineering | Defer | Listed without definitions or mechanisms |
| AI Agent | Defer | Listed without independent content |

## Future migration disposition

If migration to the permanent system is ever approved, the 15 matched concepts must propose updates to their existing parent canonical nodes, not create duplicates. The two new Week 10 candidates require a fresh duplicate/meaning review at migration time.
