---
type: canonical-decision-register
run_id: RUN-002
source_id: S03
status: validated-staging
---

# RUN-002 — Canonical Create-vs-Update Decisions

RUN-002 compares S03 first with the existing RUN-001 staging concepts, then with the read-only permanent system. A Week 10 staging shadow is created only when no staged identity exists.

## Existing Week 10 concepts updated

| Concept | Decision | S03 contribution |
|---|---|---|
| Softmax | Update existing staging concept | Classification distribution, argmax/sampling distinction, bridge to cross entropy |
| Sampling（取樣） | Update existing staging concept | Same distribution can be decoded deterministically or sampled; contrasts GAN input randomness with LM output sampling |
| Language Model（語言模型） | Update existing staging concept | Next-unit Softmax distribution and probability sampling |
| One-Hot Encoding（獨熱編碼） | Update existing staging concept | Hard-target role in cross entropy and contrast with soft targets |
| Hallucination（幻覺） | Update existing staging concept | Preserve S03's p. 98 generative/discriminative framing as a distinct perspective |

## New Week 10 staging shadows/candidate

| Candidate | Decision | Read-only permanent match | Reason |
|---|---|---|---|
| Generative AI（生成式 AI） | Create staging shadow | `Generative AI.md` | Independent task/output framing with sufficient S03 support |
| Latent Vector（潛在向量） | Create staging shadow | `Latent Vector.md` | Independent representation of generative variation |
| Generative Adversarial Network（生成對抗網路） | Create staging shadow | `Generative Adversarial Network.md` | Independent two-network adversarial mechanism |
| Mode Collapse（模式崩塌） | Create staging shadow | `Mode Collapse.md` | Independent GAN failure mode |
| GAN Variants（GAN 變體） | Create staging shadow | `GAN Variants.md` | Closely related variants belong together in one overview identity |
| Distribution（機率分布） | Create staging shadow | `Distribution.md` | Prerequisite concept used across GANs, Softmax, sampling, and divergence |
| Information（資訊量） | Create staging shadow | `Information.md` | Independent `-log P(x)` mechanism |
| Entropy（熵） | Create staging shadow | `Entropy.md` | Independent expectation of information |
| Cross Entropy（交叉熵） | Create staging shadow | `Cross Entropy.md` | Independent loss/divergence mechanism |
| KL Divergence（KL 散度） | Create staging shadow | `KL Divergence.md` | Independent distribution discrepancy measure |
| Hard and Soft Targets（硬／軟目標） | Create staging shadow | `Hard and Soft Targets.md` | Independent target-representation distinction |
| Loss Function（損失函數） | Create staging shadow | `Loss Function.md` | Independent training objective role; S03 compares MSE and cross entropy |
| Knowledge Distillation（知識蒸餾） | Create new Week 10 candidate | No parent canonical file found | Teacher/student soft-target mechanism is independently taught on pp. 88–92 |

## Duplicate candidates avoided

| Candidate | Decision | Reason |
|---|---|---|
| Sampling Strategies | No S03 content update | S03 covers sampling but not temperature/top-k/top-p; do not imply absent evidence |
| Probability Distribution | Merge with `Distribution` | Same underlying concept; bilingual alias, not a new node |
| Generative Model | Merge into `Generative AI` for this run | S03 does not establish a separate canonical boundary sufficient for a second page |
| Discriminative AI | Keep as a contrast perspective | Mentioned mainly to frame task differences; insufficient standalone mechanism |
| MSE | Keep inside `Loss Function` / `Cross Entropy` comparison | Insufficient independent treatment |
| Diffusion Model | Defer | Named only as a transition |
| StyleGAN / Pix2Pix / CycleGAN / Progressive GAN | Merge into `GAN Variants` | Related variants form one coherent chapter-like concept overview at this evidence depth |

## Conflict handling

No direct factual contradiction between S03 and S04 was found. Scope differences are preserved in `RUN-002-S03-conflicts.md`; the unresolved Hallucination terminology conflict from RUN-001 remains a publication gate.
