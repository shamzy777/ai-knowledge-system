---
type: source-claim-register
run_id: RUN-004
source_id: S08
provenance: Research Paper
status: staged
---

# S08 source-supported claims

| Claim ID | Locator | Supported claim |
|---|---|---|
| S08-C01 | pp. 1-3 | The paper proposes the Transformer as an encoder-decoder sequence-transduction architecture based on attention rather than recurrent or convolutional sequence processing. |
| S08-C02 | p. 3, Fig. 1 | The original encoder and decoder use stacked multi-head attention and position-wise feed-forward sublayers with residual connections and layer normalization; decoder masking prevents access to later output positions. |
| S08-C03 | pp. 3-4, Fig. 2, Eq. 1 | Scaled dot-product attention maps queries and key-value pairs to weighted sums of values using `softmax(QK^T/sqrt(d_k))V`. |
| S08-C04 | pp. 4-5, Fig. 2 | Multi-head attention performs learned Q/K/V projections in parallel, concatenates the head outputs, and applies an output projection. |
| S08-C05 | p. 5 | The original Transformer uses encoder self-attention, masked decoder self-attention, and encoder-decoder attention for different information-flow roles. |
| S08-C06 | p. 5 | Learned token embeddings provide vector inputs, while a linear transformation and Softmax produce next-token probabilities at the decoder output. |
| S08-C07 | p. 6 | Positional encodings are added to input embeddings because the architecture otherwise has neither recurrence nor convolution to encode sequence order; the paper uses sinusoidal encodings. |
| S08-C08 | pp. 6-7, Table 1 | Self-attention reduces sequential operations and path length relative to recurrent computation under the paper's comparison, with a sequence-length-dependent computational tradeoff. |

Excluded: historical benchmark superiority as a timeless claim; later decoder-only LLM architecture conventions; post-2017 positional and attention variants.
