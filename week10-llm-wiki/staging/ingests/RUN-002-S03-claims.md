---
type: staged-source-claims
run_id: RUN-002
source_id: S03
status: validated-staging
publication_status: unpublished
---

# RUN-002 — S03 Source-supported Claims

These claims come from S03, not model knowledge. Locators refer to physical PDF pages and were cross-checked against rendered pages where formulas or layout mattered.

| Claim ID | Source-supported claim | Pages | Confidence / handling |
|---|---|---:|---|
| C201 | A generative system may map the same apparent input to multiple plausible outputs; forcing a single deterministic target can average incompatible possibilities. | 4–10 | High; pedagogical motivation, not a proof |
| C202 | A random latent tensor/vector `z` can represent variation that a generator maps into different outputs. | 9–12 | High |
| C203 | A GAN contains a Generator and Discriminator trained adversarially: the generator seeks realistic outputs and the discriminator distinguishes generated from real data. | 19–23 | High |
| C204 | GAN training compares the data distribution `p_data`, latent distribution `p_z`, and generator-induced distribution `p_g`; alternating updates aim to make generated and real distributions harder to distinguish. | 24–32 | High after visual check of p. 30 |
| C205 | Mode collapse occurs when a generator maps many latent inputs to a narrow subset of outputs instead of covering the data distribution. | 35 | High; the source's “WGAN solves it” phrasing is treated as simplified, not absolute |
| C206 | Progressive GAN, StyleGAN, Pix2Pix, and CycleGAN alter architecture, conditioning, or training data assumptions while retaining the broader generative-model goal. | 36–58 | High; grouped as GAN variants rather than separate pages in this run |
| C207 | Softmax converts output scores into a probability distribution; a classifier may choose the highest-probability class, while a generative task may sample from the distribution. | 61–64, 93–96 | High |
| C208 | Information content is represented as `I(x)=-log P(x)`, so less probable events carry more information. | 65–67 | High |
| C209 | Entropy is the expected information content of a distribution. | 72–75 | High |
| C210 | Cross entropy measures expected negative log probability under target distribution `P` when predictions use distribution `Q`; one-hot targets reduce the expression to the negative log probability of the correct class. | 68–81 | High after visual check of p. 77 |
| C211 | Cross entropy reaches `H(P)` rather than necessarily zero when `Q=P`; KL divergence subtracts `H(P)` and reaches zero when the distributions match. | 84–87 | High after visual checks of pp. 84–85 |
| C212 | One-hot targets are hard targets; a teacher distribution can provide a soft target for a student model in knowledge distillation. | 88–92 | High |
| C213 | GAN variability enters through random latent input, whereas classification can use argmax and language generation can sample a next unit from a Softmax distribution. | 93–96 | High after visual checks |
| C214 | The source contrasts discriminative and generative uses but argues that their underlying probabilistic principles overlap; task framing and output use matter. | 97–98 | Medium; broad pedagogical framing |
| C215 | S03 reports the claim that generative AI hallucinates and discriminative AI should therefore be used, then cautions that the underlying principles are similar. | 98 | Medium; preserve as a perspective, not a resolved rule |

## Detected but not promoted claims

- S03 names Diffusion only as a later development; it does not independently support a Diffusion concept page.
- S03 does not teach temperature, top-k, top-p, or nucleus sampling, so RUN-002 does not update `Sampling Strategies`.
- The source's statement that WGAN “solves” mode collapse is too absolute to promote without another source.
- “Discriminative AI” is discussed mainly as a contrast label and does not receive a separate concept page in this run.
- MSE appears as a comparison to cross entropy but is not developed enough for a separate Week 10 concept.

## Provenance boundary

The permanent Knowledge System was consulted read-only only for canonical identity comparison. It is neither an ingested S03 source nor evidence for these claims.
