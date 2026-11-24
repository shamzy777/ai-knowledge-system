---
type: evidence-mapped-section-draft
deck_id: TEACH-DECK-001
source_path: TEACH-PATH-001
status: fidelity-check-ready
section_count: 11
knowledge_source: published-week10-wiki-only
---

# TEACH-DECK-001 section draft

The deck uses Chinese as the primary teaching language and concise English reinforcement. Every slide has one causal job.

## Slide copy and evidence

### S1 — 一次，只產生一個 token / One token at a time

**Purpose:** establish the complete loop before explaining its parts.

**Visible copy:** 模型讀取目前上下文，預測下一個 token 的機率分布，選出一個 token，再把它接回上下文。The model predicts one token, appends it, and repeats.

**Visual:** the complete pipeline with every later slide linked as a stage.

**Evidence:** Language Model, Large Language Model, Inference, Sampling. S03/S04 Course Material; S09 Reliable Educational Reference.

### S2 — 文字先變成 token / Text becomes tokens

**Purpose:** explain the model's input units without claiming a specific tokenizer split.

**Visible copy:** Tokenization（詞元化）把連續文字切成可重現的 token 序列。token inventory 會影響序列長度、vocabulary identity，以及模型要預測的單位。

**Visual:** raw-text band becoming generic token tiles labelled token A, B, C. Mark the split as schematic.

**Evidence:** Tokenization. S09 Reliable Educational Reference, book pp. 33–47, 203.

### S3 — Token identity and position

**Purpose:** distinguish token Embedding from Positional Encoding.

**Visible copy:** Token Embedding 提供 token 的 learned dense vector。Positional information 提供 token 在序列中的位置。兩者提供不同資訊，並在 Transformer input 中結合。

**Visual:** two separate lanes, `token ID → embedding vector` and `sequence index → positional information`, joining only at the input representation.

**Evidence:** Embedding; Positional Encoding. S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference.

### S4 — Context changes the representation

**Purpose:** motivate Self-Attention.

**Visible copy:** 同一個 token 的初始 identity representation 可以相同；Self-Attention 讓每個位置根據其他位置形成 context-dependent representation。Avoid human-understanding metaphors.

**Visual:** one focus token in context A and context B, producing two differently labelled contextual outputs without invented numeric values.

**Evidence:** Embedding; Self-Attention. S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference.

### S5 — Q, K, and V divide the job

**Purpose:** make attention roles concrete.

**Visible copy:** Query 與 Keys 比較，決定哪些位置較相關。Values 承載之後要被加權組合的資訊。Q/K/V 都是 learned projections。

**Visual and interaction:** select a focus token. Highlight its Query, all compared Keys, and the Values that can flow back.

**Evidence:** Query, Key, and Value. S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference.

### S6 — One Self-Attention operation

**Purpose:** show one mechanism chain.

**Visible copy:** Query–Key scores 經過 scaling 與 Softmax，成為 attention weights。這些 weights 用來組合 Values，得到 context-dependent representation。

**Visual:** `Q·K scores`, `Softmax weights`, and `weighted V mixture` as three linked states. Label this as attention Softmax.

**Evidence:** Self-Attention; Softmax. S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference.

### S7 — From one head to the Transformer

**Purpose:** place attention inside the larger architecture.

**Visible copy:** Multi-Head Attention 同時執行多組 Q/K/V projections，再合併結果。Transformer 還包含 feed-forward layers、residual connections、normalization 與 position information。

**Visual:** nested zoom from one head to multiple heads to a simplified block. Preserve original encoder–decoder and causal-decoder scope labels.

**Evidence:** Multi-Head Attention; Transformer; Positional Encoding. S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference.

### S8 — Language Modeling → LLM → Inference

**Purpose:** clarify the later progression without inventing a new mechanism.

**Visible copy:** Language Modeling 定義 next-token prediction task。Large Language Model 延伸同一 language-model framing 到較大的現代模型與訓練生命週期。Inference 使用已訓練參數產生輸出，不更新參數。

**Visual:** three consecutive fields, with Transformer context feeding Language Modeling and Inference leading to output decoding.

**Evidence:** Language Model; Large Language Model; Inference; Transformer. S04 Course Material; S08 Research Paper; S09 Reliable Educational Reference.

### S9 — Softmax makes a distribution

**Purpose:** separate scoring from selection.

**Visible copy:** Softmax 把 candidate scores 轉成非負、總和為 1 的 relative probabilities。此處得到 next-token distribution，還沒有選出 token。

**Visual:** score bars becoming probability bars. Use `[0.70, 0.29, 0.01]` only as S04's explicit example.

**Evidence:** Softmax; Distribution; Language Model. S02–S06 Course Material; S08 Research Paper; S09 Reliable Educational Reference.

### S10 — Sampling selects one token

**Purpose:** demonstrate probabilistic selection.

**Visible copy:** Sampling 按照 predicted distribution 選取 outcome，不一定每次都選最高機率 token。在 `[0.70, 0.29, 0.01]` 中，第三個候選機率低但仍可能被選到。

**Interaction:** repeat draws from the fixed Wiki-supported distribution and update a tally. Label results illustrative.

**Evidence:** Sampling; Softmax; Inference. S03/S04 Course Material; S09 Reliable Educational Reference.

### S11 — Append, repeat, and verify separately

**Purpose:** close the loop and set the factuality boundary.

**Visible copy:** 被選中的 token 會加入 context，下一輪再重新計算。Sampling 控制如何從 distribution 選 token。它不等於 factual verification，也不被教成 Hallucination 的原因。Fluent or high-probability continuation can still be ungrounded or incorrect.

**Visual:** selected token joins the context and the pipeline loops. A separate factuality lane points to Hallucination / Evaluation without a causal arrow from Sampling.

**Evidence:** Language Model; Inference; Sampling; Hallucination; LLM Evaluation. S03/S04 Course Material; S09 Reliable Educational Reference.

## Quiz module

The six approved questions live outside the 11 teaching slides as an accessible quiz sheet. Each answer maps to the Wiki concepts named in TEACH-PATH-001. The quiz does not infer mastery.
