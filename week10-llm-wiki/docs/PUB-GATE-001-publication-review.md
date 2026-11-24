---
type: human-publication-gate-review
gate_id: PUB-GATE-001
reviewed_concept_count: 59
proposed_counts:
  core: 33
  supporting: 18
  deferred: 8
status: approved
publication_authorized: true
mastery_changed: false
---

# Week 10 LLM Wiki — Publication Review

This review classifies all 59 validated staging concepts for the beginner Wiki **從零開始認識 LLM**. It is a publication proposal only: chapter pages are navigation/learning structures, not canonical concepts, and no content has been written to `wiki/` or `teaching/`.

## Classification rules

- **Core**: required in the main beginner prerequisite path.
- **Supporting**: publishable and useful, but removable from the main path without breaking it.
- **Deferred**: valid staging knowledge that remains unpublished for the current scope.

Source IDs preserve their manifest provenance: S01–S07 = Course Material; S08 = Research Paper; S09 = Reliable Educational Reference. Handwriting uncertainty for S01/S07 remains explicit. “No blocking issue” does not erase source-specific caveats recorded in the staging page.

## Complete 59-concept review

| Concept | Status | Reason | Supporting sources | Intended chapter | Prerequisite role | Provenance / semantic issue |
|---|---|---|---|---|---|---|
| Activation Function（激活函數） | **Core** | Explains how neural layers introduce nonlinear transformations. | S02, S05, S06, S07 | 1. Foundations | After Weight and Bias; before MLP and training behavior. | No blocking issue; S07 is corroborative handwriting only. |
| Backpropagation（反向傳播） | **Core** | Required to explain how training computes parameter gradients. | S01, S02, S05 | 2. How Neural Networks Learn | After Forward Propagation and Loss Function; supplies gradients to Optimizer. | Resolved: canonical definition is gradient computation; S02 p.75 conflation is retained as an attributed source issue. |
| Byte-Pair Encoding（位元組對編碼） | **Supporting** | Concrete subword-tokenization algorithm, but Tokenization can be understood without its details. | S09 | 4. Representing Language | Optional branch after Tokenization and before Embedding examples. | Single reliable educational source; no blocking issue. |
| Classification（分類） | **Supporting** | Useful task example for Softmax and Cross Entropy, but not required for the LLM spine. | S01, S02, S05, S06, S07 | 3. Probability and Prediction | Application after Distribution, Softmax, and Cross Entropy. | Resolved: S06 demonstration is mutually exclusive multiclass classification; “Multi-labels” slide title remains a provenance note. |
| Cross Entropy（交叉熵） | **Core** | Connects predicted distributions, targets, and language-model training loss. | S03, S05, S06, S07, S09 | 3. Probability and Prediction | After Distribution and Softmax; before Pretraining. | Resolved: squared error and cross entropy are task/teaching-context choices, not contradictory universal rules. |
| Data Preprocessing（資料前處理） | **Supporting** | Explains preparation before training but is not specific to the LLM conceptual route. | S01, S06 | 2. How Neural Networks Learn | Optional preparation before Neural Network Training. | S01 handwriting is corroborative; S06 supplies stronger implementation evidence. |
| Distribution（機率分布） | **Core** | Central to prediction, Softmax, sampling, and uncertainty. | S02, S03, S05, S06 | 3. Probability and Prediction | Before Softmax, Cross Entropy, Sampling, and Language Model. | No blocking issue. |
| Embedding（嵌入） | **Core** | Required bridge from token identity to learned vector representation. | S04, S08, S09 | 4. Representing Language | After Tokenization; before Attention and Transformer. | No blocking issue; static versus contextual representations remain distinguished. |
| Entropy（熵） | **Supporting** | Deepens uncertainty and Cross Entropy interpretation without being required for the main path. | S03 | 3. Probability and Prediction | Optional after Information and Distribution; before KL Divergence. | Single course source; scope is introductory information theory. |
| Epoch and Batch（訓練週期與批次） | **Supporting** | Useful training-execution vocabulary, not essential to the LLM mechanism chain. | S01, S02, S05, S06, S07 | 2. How Neural Networks Learn | Optional after Neural Network Training; supports Overfitting discussion. | S01/S07 handwriting is corroborative; epoch-overfitting edge remains explicitly scoped. |
| Evaluation Metric（評估指標） | **Supporting** | General evaluation vocabulary that supports, but does not replace, LLM Evaluation. | S01, S05, S06 | 2. How Neural Networks Learn | After task/output definition; supports data-split interpretation. | No blocking issue. |
| Feature Scaling（特徵縮放） | **Supporting** | Shows a common preprocessing operation in course implementations. | S01, S06 | 2. How Neural Networks Learn | Optional branch under Data Preprocessing before cited training workflows. | Relationship is scoped to the cited workflows; not claimed as universal for all LLM inputs. |
| Forward Propagation（前向傳播） | **Core** | Required to understand prediction before loss and backward computation. | S05 | 1. Foundations | After Neural Network structure; before Loss and Backpropagation. | One course source but direct mechanism evidence; no blocking issue. |
| GAN Variants（GAN 變體） | **Deferred** | Valid generative-model history but outside the current LLM publication path. | S03 | — | Future GAN branch after Generative Adversarial Network. | No defect; deferred solely for scope. |
| Generative Adversarial Network（生成對抗網路） | **Deferred** | Provides a contrasting generative paradigm but would divert the beginner LLM path. | S03 | — | Future contrast branch after Generative AI and Latent Vector. | No defect; single-course-source scope is preserved. |
| Generative AI（生成式 AI） | **Supporting** | Places LLMs in the broader generative-model family without requiring GAN detail. | S03 | 6. From Language Model to LLM | Framing concept before or alongside Large Language Model. | S03 discriminative/generative framing remains contextual, not a reliability guarantee. |
| Gradient（梯度） | **Core** | Connects loss sensitivity to parameter updates. | S02, S05 | 2. How Neural Networks Learn | After Loss Function; produced by Backpropagation and consumed by Optimizer. | No blocking issue; kept distinct from Backpropagation and Optimizer. |
| Hallucination（幻覺） | **Core** | Essential limitation separating fluent generation from grounded correctness. | S03, S04, S09 | 7. Generation and Limitations | After Language Model, Inference, and Sampling. | Resolved: S09's narrower ungrounded/incorrect-output definition is canonical; S04's creative-generation framing remains an attributed Course Perspective. |
| Hard and Soft Targets（硬目標與軟目標） | **Deferred** | Primarily supports knowledge-distillation detail, not the beginner LLM spine. | S03 | — | Future prerequisite for Knowledge Distillation. | No defect; deferred for scope. |
| Hyperparameter（超參數） | **Supporting** | Useful for understanding externally chosen training settings. | S01, S06, S07 | 2. How Neural Networks Learn | Optional after training-loop vocabulary; connects to evaluation choices. | S01/S07 handwriting is corroborative; no universal optimizer-selection rule is published. |
| Inference（推論） | **Core** | Separates model use from training and anchors prompting and decoding. | S09 | 6. From Language Model to LLM | After trained Language Model/LLM; before Prompt Engineering and Sampling. | Single reliable educational source; no blocking issue. |
| Information（資訊量） | **Supporting** | Supplies the information-theory intuition behind Entropy and Cross Entropy. | S03 | 3. Probability and Prediction | Optional before Entropy. | Single course source; no blocking issue at the proposed introductory depth. |
| KL Divergence（KL 散度） | **Supporting** | Useful distribution-comparison concept but not required for next-token generation basics. | S03 | 3. Probability and Prediction | Optional after Entropy and Cross Entropy. | Single course source; direction and distinction from Cross Entropy already semantically reviewed. |
| Knowledge Distillation（知識蒸餾） | **Deferred** | Valid model-compression/adaptation topic outside the current beginner LLM path. | S03 | — | Future branch after Hard and Soft Targets and KL Divergence. | No defect; deferred for scope. |
| Language Model（語言模型） | **Core** | Central predictive concept connecting context, next-token distributions, and generation. | S03, S04, S09 | 6. From Language Model to LLM | After Tokenization, Embedding, Probability, and Transformer. | Word/unit language in course slides is retained as pedagogical phrasing; canonical text uses token where supported. |
| Large Language Model（大型語言模型） | **Core** | Defines the target system and its scale/training lifecycle. | S04, S09 | 6. From Language Model to LLM | After Language Model and Transformer; before applications and limitations. | Time-sensitive product/model-size claims remain excluded. |
| Latent Vector（潛在向量） | **Deferred** | Current evidence mainly supports the GAN generation route, not the LLM spine. | S03 | — | Future prerequisite for GAN. | No defect; deferred because its current support is GAN-centered. |
| Learning Rate（學習率） | **Core** | Required to explain how optimizers scale parameter updates. | S02, S05, S06 | 2. How Neural Networks Learn | After Gradient; part of Optimizer behavior. | No blocking issue. |
| LLM Evaluation（大型語言模型評估） | **Core** | Necessary for judging task fit, reliability, and limitations. | S04, S09 | 7. Generation and Limitations | After Large Language Model and Inference; paired with Hallucination. | Evaluation methods have known limitations; no single metric is presented as sufficient. |
| Loss Function（損失函數） | **Core** | Defines the training objective connecting predictions to learning signals. | S01, S02, S03, S05, S06, S07 | 2. How Neural Networks Learn | After Forward Propagation; before Gradient and Backpropagation. | Resolved: MSE and Cross Entropy belong to different task/teaching contexts; handwriting remains corroborative only. |
| Mode Collapse（模式崩塌） | **Deferred** | GAN-specific failure mode outside the current LLM limitation chapter. | S03 | — | Future consequence branch after GAN. | Historical reverse proposal remains rejected; current direction is GAN → Mode Collapse. |
| Multi-Head Attention（多頭注意力） | **Core** | Required component of the Transformer mechanism. | S08, S09 | 5. Attention and Transformer | After Q/K/V and Self-Attention; before complete Transformer. | Original-paper and modern causal-block perspectives are compatible. |
| Multilayer Perceptron（多層感知器） | **Supporting** | Helps bridge a single neuron to layered networks and Transformer feed-forward intuition. | S01, S02, S05, S06 | 1. Foundations | Optional after Perceptron and Activation Function. | No blocking issue; course implementation contexts remain attributed. |
| Neural Network Training（神經網路訓練） | **Core** | Organizes forward pass, loss, gradients, optimizer, and evaluation into one loop. | S01, S02, S05, S06, S07, S09 | 2. How Neural Networks Learn | After Neural Network foundations; parent process for Pretraining. | Handwriting is corroborative; canonical mechanism uses stronger S02/S05/S06/S09 support. |
| Neural Network（神經網路） | **Core** | Foundational model family underlying modern LLMs. | S01, S02, S04, S05, S06, S07 | 1. Foundations | Entry concept before parameters, layers, training, and Transformer. | S01/S07 are corroborative handwriting; no blocking issue. |
| One-Hot Encoding（獨熱編碼） | **Supporting** | Provides a useful contrast with learned Embedding and target representations. | S01, S02, S03, S04, S06 | 4. Representing Language | Optional before Embedding; also supports classification examples. | S01 handwriting is corroborative; no blocking issue. |
| Optimizer（最佳化器） | **Core** | Required to explain how gradients actually change parameters. | S01, S02, S05, S06, S07 | 2. How Neural Networks Learn | After Gradient and Learning Rate; performs parameter update. | Resolved: kept distinct from Backpropagation; source heuristics are contextual, not universal. |
| Overfitting（過度擬合） | **Core** | Essential training limitation linking data splits, validation behavior, and generalization. | S01, S06, S07 | 2. How Neural Networks Learn | After Training/Validation/Test Sets and training curves. | Strong S06 evidence; handwriting sources are corroborative. |
| Perceptron（感知器） | **Supporting** | Useful minimal neuron model, but the main path can start at Neural Network. | S01, S02, S05 | 1. Foundations | Optional after Weight and Bias; before MLP. | S01 handwriting uncertainty retained; S05 supplies the stronger scope. |
| Positional Encoding（位置編碼） | **Core** | Required to explain how attention-only models represent order. | S08, S09 | 5. Attention and Transformer | After Embedding; before complete Transformer. | Resolved: original sinusoidal encoding and later learned/relative variants are distinct design choices, not contradictions. |
| Post-Training（後訓練） | **Core** | Explains how pretrained models are adapted toward instructions and preferences. | S09 | 6. From Language Model to LLM | After Pretraining; before deployed Inference behavior. | Single dated educational reference; method names remain attributed and time-sensitive details are avoided. |
| Pretext Task（代理任務） | **Supporting** | Helps explain how predictive tasks produce useful representations. | S04 | 4. Representing Language | Optional before Word2Vec and as intuition for self-supervised learning. | Single course source; no blocking issue. |
| Pretraining（預訓練） | **Core** | Connects next-token prediction to large-scale neural-network training. | S09 | 6. From Language Model to LLM | After Transformer, Language Model, Cross Entropy, and Neural Network Training; before Post-Training. | Describes S09's causal-LLM route and does not universalize all pretraining objectives. |
| Prompt Engineering（提示工程） | **Core** | Provides the bounded application bridge from model mechanism to practical use. | S04, S09 | 7. Generation and Limitations | After Large Language Model and Inference. | Course workflow is explicitly human-in-the-loop; prompting is not presented as factual verification. |
| Query, Key, and Value（查詢、鍵、值） | **Core** | Required internal roles for understanding attention score and value aggregation. | S04, S08, S09 | 5. Attention and Transformer | After Embedding and linear transformation intuition; before Self-Attention. | No blocking issue. |
| Recurrent Neural Network（循環神經網路） | **Supporting** | Provides historical/architectural contrast that motivates Transformer parallelism. | S04, S08 | 5. Attention and Transformer | Optional contrast immediately before Transformer. | Comparison is scoped to recurrence, sequential operations, and dependency paths. |
| Regression（迴歸） | **Deferred** | Valid supervised-learning task but not needed for the current LLM Wiki path. | S05, S06 | — | Future supervised-learning branch after MLP and Loss Function. | No defect; deferred for scope. |
| Sampling Strategies（取樣策略） | **Core** | Explains temperature, top-k, and top-p controls over generation. | S04, S09 | 7. Generation and Limitations | After Sampling and Softmax; within Inference. | No blocking issue; strategy tradeoffs remain contextual. |
| Sampling（取樣） | **Core** | Converts a next-token distribution into variable generated output. | S03, S04, S09 | 7. Generation and Limitations | After Distribution, Softmax, Language Model, and Inference. | No blocking issue; distinguished from argmax/greedy choice. |
| Self-Attention（自注意力） | **Core** | Central contextualization mechanism of the Transformer. | S04, S08, S09 | 5. Attention and Transformer | After Q/K/V and Softmax; before Multi-Head Attention. | No blocking issue; causal masking is scoped to the causal-model perspective. |
| Softmax | **Core** | Turns logits or attention scores into normalized weights/distributions. | S02, S03, S04, S05, S06, S08, S09 | 3. Probability and Prediction | After Distribution/logits; before Cross Entropy, Attention, and Sampling. | Course “winner-takes-all” phrase remains teaching shorthand, not the canonical definition. |
| Tensor（張量） | **Core** | Supplies the numerical object used for inputs, parameters, and layer representations. | S01, S02 | 1. Foundations | Earliest numeric-representation prerequisite for Neural Network and Embedding. | S01 is corroborative handwriting; S02 provides stronger evidence. |
| TensorBoard（TensorBoard 視覺化工具） | **Deferred** | Implementation tool is not necessary for the conceptual beginner Wiki. | S06, S07 | — | Future practice branch after metrics, hyperparameters, and training. | S07 handwriting is corroborative; no semantic defect. |
| Tokenization（詞元化） | **Core** | Defines the units an LLM receives and predicts. | S09 | 4. Representing Language | Before Embedding, Language Model, and Transformer inputs. | Single reliable educational source; `分詞`／`斷詞` remain noted as contextual alternatives. |
| Training, Validation, and Test Sets（訓練、驗證與測試集） | **Core** | Required to understand training decisions, evaluation, and overfitting. | S01, S06, S07 | 2. How Neural Networks Learn | Within the training workflow; before Overfitting and final evaluation. | S01/S07 handwriting is corroborative; S06 supplies the executable evidence. |
| Transformer（變換器） | **Core** | Principal architecture connecting attention mechanisms to modern LLMs. | S04, S08, S09 | 5. Attention and Transformer | After Embedding, Self-Attention, Multi-Head Attention, and Positional Encoding; before Language Model/LLM. | Resolved: S08 encoder–decoder and S09 causal decoder are architectural/evolutionary scopes, not conflicting definitions. |
| Weight and Bias（權重與偏差） | **Core** | Defines the trainable parameters that transform neural-network inputs. | S02, S05 | 1. Foundations | After Tensor; before Forward Propagation and Training. | No blocking issue. |
| Weight Initialization（權重初始化） | **Supporting** | Useful training prerequisite but not essential to the conceptual LLM spine. | S01, S05 | 2. How Neural Networks Learn | Optional before the first training update. | S01 handwriting is corroborative; initializer heuristics remain contextual. |
| Word2Vec | **Supporting** | Historical representation-learning example that clarifies embeddings. | S04, S09 | 4. Representing Language | Optional after Pretext Task and before contrasting contextual embeddings. | Static versus contextual embedding distinction must remain explicit. |

## Proposed chapter membership

Chapter pages are ordered learning/navigation structures only.

### 1. Foundations

- Core: Tensor; Neural Network; Weight and Bias; Activation Function; Forward Propagation.
- Supporting: Perceptron; Multilayer Perceptron.

### 2. How Neural Networks Learn

- Core: Neural Network Training; Loss Function; Gradient; Backpropagation; Optimizer; Learning Rate; Training, Validation, and Test Sets; Overfitting.
- Supporting: Data Preprocessing; Feature Scaling; Epoch and Batch; Evaluation Metric; Hyperparameter; Weight Initialization.

### 3. Probability and Prediction

- Core: Distribution; Softmax; Cross Entropy.
- Supporting: Classification; Information; Entropy; KL Divergence.

### 4. Representing Language

- Core: Tokenization; Embedding.
- Supporting: Byte-Pair Encoding; One-Hot Encoding; Pretext Task; Word2Vec.

### 5. Attention and Transformer

- Core: Query, Key, and Value; Self-Attention; Multi-Head Attention; Positional Encoding; Transformer.
- Supporting: Recurrent Neural Network.

### 6. From Language Model to LLM

- Core: Language Model; Large Language Model; Pretraining; Post-Training; Inference.
- Supporting: Generative AI.

### 7. Generation and Limitations

- Core: Sampling; Sampling Strategies; Prompt Engineering; Hallucination; LLM Evaluation.
- Supporting: none required.

## Proposed beginner prerequisite order

The main Core path is:

1. Tensor
2. Neural Network
3. Weight and Bias
4. Activation Function
5. Forward Propagation
6. Neural Network Training
7. Loss Function
8. Distribution
9. Softmax
10. Cross Entropy
11. Gradient
12. Backpropagation
13. Learning Rate
14. Optimizer
15. Training, Validation, and Test Sets
16. Overfitting
17. Tokenization
18. Embedding
19. Query, Key, and Value
20. Self-Attention
21. Multi-Head Attention
22. Positional Encoding
23. Transformer
24. Language Model
25. Large Language Model
26. Pretraining
27. Post-Training
28. Inference
29. Sampling
30. Sampling Strategies
31. Prompt Engineering
32. Hallucination
33. LLM Evaluation

Chapter 3 concepts appear before the detailed training-update sequence is completed because Distribution/Softmax/Cross Entropy define the objective used by the later gradient explanation. A chapter presentation may cross-link rather than duplicate them.

## Concepts recommended for deferral

The following eight concepts remain valid staging knowledge but should not publish in the current Wiki scope:

1. Generative Adversarial Network
2. GAN Variants
3. Latent Vector
4. Mode Collapse
5. Hard and Soft Targets
6. Knowledge Distillation
7. Regression
8. TensorBoard

## Applied human conflict resolutions

1. Backpropagation computes gradients; Optimizer/Gradient Descent uses gradients to update parameters. S02's conflation stays attributed in provenance.
2. The demonstrated MNIST task is single-label multiclass classification; S06's “Multi-labels” title mismatch remains visible in source notes.
3. Hallucination uses the narrower S09 technical definition; S04's broad creative/generative framing remains a labelled Course Perspective.
4. Squared Error and Cross Entropy are different task/teaching contexts.
5. The original encoder–decoder Transformer and modern causal-decoder LLM are architectural/evolutionary scope differences.
6. Sinusoidal, learned absolute, and relative positional approaches are variants, not contradictions.

These decisions resolve the previously mandatory conflict-treatment questions for this proposal. They do not authorize publication or mastery changes.

## Items still requiring human judgment

- Approve or revise the 33/18/8 classification and chapter placement.
- Decide whether all Supporting concepts should publish in the first release or whether publication should initially contain Core only.
- Confirm whether `Feature Scaling` should remain Supporting or move to Deferred because its current evidence is implementation-oriented.
- Resolved by approval: use `Tokenization（詞元化）`; note `分詞`／`斷詞` only as contextual alternatives.
- Select the later bounded teaching HTML path; this review recommends `Tokenization → Embedding → Self-Attention → Transformer → Language Model → Sampling`, but does not create it.

## Publication-ready count

| Status | Count | Meaning at this gate |
|---|---:|---|
| Core | 33 | Recommended for the main beginner Wiki path |
| Supporting | 18 | Publishable supporting pages outside the mandatory path |
| Deferred | 8 | Remain unpublished in staging |
| **Total** | **59** | All validated staging concepts reviewed exactly once |

## Gate result

`PUB-GATE-001` was explicitly approved. The approved first publication includes all 33 Core and 18 Supporting concepts, retains all 8 Deferred concepts in staging, and uses `Tokenization（詞元化）` as the canonical term. Publication execution is recorded separately as `PUB-RUN-001`.
