---
type: staged-source-claims
run_id: RUN-001
source_id: S04
status: validated-staging
publication_status: unpublished
---

# RUN-001 — S04 Source-supported Claims

These are claims extracted from S04, not general model knowledge. Page references use the PDF's printed page numbers, which match physical PDF pages for the cited material.

| Claim ID | Source-supported claim | Pages | Confidence / handling |
|---|---|---:|---|
| C001 | A text-generation language model can be framed as a function-learning system that predicts the next item from preceding text. | 5, 9–15 | High; course framing uses “呆萌型 AI 機器人” as metaphor |
| C002 | Converting every position in existing sentences into a prediction target creates abundant training examples. | 9–10 | High within the course framing |
| C003 | A current symbol alone is insufficient when the same symbol has multiple possible continuations; preceding context must be represented. | 11–12 | High |
| C004 | RNNs propagate a previous hidden state and therefore compute sequentially. | 24–27 | High |
| C005 | The course contrasts RNN recurrence with Transformer computation that can produce representations for multiple positions through matrix operations. | 27–31 | High; simplified comparison |
| C006 | Q, K, and V are learned linear transformations of input representations. | 29 | High |
| C007 | Self-attention compares a query with keys, applies Softmax to attention scores, and forms a weighted sum of values. | 29–31 | High |
| C008 | The displayed attention formula is `Attention(Q,K,V)=softmax(QK^T/sqrt(d_K))V`. | 31 | High after visual retry; text extraction had dropped the radical |
| C009 | A language model assigns scores to possible next outputs and Softmax converts them to a normalized relative distribution. | 17–19, 50–52 | High |
| C010 | Sampling draws a next output according to the probability distribution, so lower-probability choices remain possible. | 53–54, 59–60 | High |
| C011 | Temperature rescales scores before Softmax; values above 1 flatten the distribution and values below 1 sharpen it. | 56–58 | High; formulas are visually structured in the PDF |
| C012 | Top-k restricts candidates to a fixed number of highest-ranked items. | 60–61 | High |
| C013 | Top-p / nucleus sampling uses a cumulative-probability threshold, yielding a dynamic candidate count, followed by renormalization. | 61–64 | High |
| C014 | Text generation repeats: context → distribution over next items → sampling strategy → next item. | 64 | High |
| C015 | One-hot encoding distinguishes vocabulary identities but does not itself encode semantic similarity. | 67–69 | High |
| C016 | An embedding is a learned feature vector representation; intermediate neural-network representations can be treated as learned features. | 72–75 | High; “understanding” is pedagogical language, not a literal cognitive claim |
| C017 | A pretext task is a proxy prediction task used to learn representations rather than the final application goal. | 76 | High |
| C018 | Word2Vec uses CBOW and Skip-Gram tasks to learn word embeddings from context prediction. | 77–83 | High |
| C019 | Transformer models include a trainable embedding layer rather than requiring pretrained Word2Vec embeddings. | 85 | High within the slide's simplified explanation |
| C020 | The course presents LLMs as scaled language models trained to continue text; GPT generations illustrate scale and sequential generation. | 39–47 | Medium; quantitative scale comparisons are excluded pending verification |
| C021 | “Hallucination” is framed as generated continuation that may be true, false, or creative; factual assistance requires distinguishing generation from retrieval. | 38–41 | Medium; preserve as attributed course framing |
| C022 | Prompting should supply correct information and clear instructions, including the task, output form, and audience. | 100–101 | High |
| C023 | A useful prompt-development workflow is to provide domain knowledge, let the model ask clarifying questions, request a draft/specification, verify claims, and personally review and revise the result. | 105–115 | High; some printed page markers are fused in text extraction, so page range is used |
| C024 | General benchmark rank does not automatically determine fitness for an individual's task; task-relevant test prompts should cover material the evaluator understands. | 88–90 | High |

## Detected but not promoted claims

- Current model names, parameter counts, service availability, prices, API availability, hardware capacities, and local-inference recommendations on pp. 42–47 and 86–102 are time-sensitive and require later external verification.
- Productivity percentages on p. 104 lack an explicit source on the slide and are excluded.
- The list `Context Engineering`, `Harness Engineering`, `Loop Engineering`, `Graph Engineering`, `Chat Bot`, and `AI Agent` is not enough independent content to create canonical pages.
- The source assigns numeric IDs to generated units but does not teach a tokenization algorithm; no source-only Tokenization draft is created from RUN-001.
- The course metaphors “呆萌型 AI 機器人”, “唬爛王”, and “作夢的機器” remain attributed teaching metaphors.

## Provenance boundary

The read-only permanent Knowledge System was used only to match canonical identities and detect differences. Its text was not treated as an ingested S04 claim and does not count as a RUN-001 source.
