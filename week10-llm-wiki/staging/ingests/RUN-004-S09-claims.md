---
type: source-claim-register
run_id: RUN-004
source_id: S09
provenance: Reliable Educational Reference
status: staged
---

# S09 source-supported claims

| Claim ID | Book locator | Supported claim |
|---|---|---|
| S09-C01 | pp. 5-11 | A language model assigns a probability distribution over possible next tokens given context; modern LLM implementations combine neural networks and embeddings. |
| S09-C02 | pp. 11, 127-148 | Embeddings are dense vector representations learned or derived from distributional context; similarity is useful but embedding spaces can encode and amplify bias. |
| S09-C03 | pp. 16-21 | The reference distinguishes pretraining from later instruction tuning, preference alignment, and reinforcement learning with verifiable rewards, and distinguishes training from inference. |
| S09-C04 | pp. 33-47 | Tokenization segments running text into tokens; subword tokenization trades word-level coverage against fragmentation and affects reproducibility, context length, representation quality, and cost. |
| S09-C05 | pp. 42-45 | BPE training iteratively merges frequent adjacent units to induce a vocabulary; its encoder applies learned merges to new text. |
| S09-C06 | pp. 68-88 | N-gram language modeling introduces conditional next-token probability, train/test evaluation, perplexity, sampling, and overfitting as foundations before neural LMs. |
| S09-C07 | pp. 177-195 | A causal Transformer LM uses token/position embeddings, stacked Transformer blocks, multi-head self-attention, feed-forward layers, normalization/residual structure, and a language-model head. |
| S09-C08 | pp. 179-184 | Attention builds contextual representations through Q/K/V-based weighted combinations; multiple heads provide separate learned projections before concatenation/output projection. |
| S09-C09 | pp. 191-193 | Token and position embeddings are combined to represent both identity and sequence position; the reference distinguishes learned absolute, sinusoidal, and relative-position approaches. |
| S09-C10 | pp. 196-201 | Decoding repeatedly selects next tokens from model probabilities; greedy, random, temperature, top-k, and top-p strategies trade determinism, diversity, and quality. |
| S09-C11 | pp. 201-203 | Transformer LM pretraining tokenizes large corpora and uses self-supervised next-token prediction, cross-entropy loss, backpropagation, and gradient descent to update all model weights. |
| S09-C12 | pp. 209-223 | Post-training adapts a pretrained base model using instruction tuning, parameter-efficient fine-tuning, preference-based learning, and verifiable-reward training; these are distinct from pretraining. |

Excluded: time-sensitive current-model sizes; unverified frontier-model details; chapters outside the targeted beginner-LLM gap-fill scope.
