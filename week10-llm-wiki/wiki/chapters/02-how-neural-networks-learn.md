---
type: wiki-chapter-navigation
chapter_id: how-neural-networks-learn
chapter_order: 2
title: "How Neural Networks Learn（神經網路如何學習）"
publication_status: published-week10
publication_gate: PUB-GATE-001
publication_run: PUB-RUN-001
canonical_concept: false
navigation_only: true
mastery_status: not-applicable
---

# 2. How Neural Networks Learn（神經網路如何學習）

This page orders canonical concepts; it is not itself a concept or evidence source.

## Learning goal / 學習目標

Understand the training loop and keep gradient computation separate from parameter updating.

## Core path / 核心路徑

1. [Neural Network Training（神經網路訓練）](../concepts/neural-network-training.md)
2. [Loss Function（損失函數）](../concepts/loss-function.md)
3. [Gradient（梯度）](../concepts/gradient.md)
4. [Backpropagation（反向傳播）](../concepts/backpropagation.md)
5. [Learning Rate（學習率）](../concepts/learning-rate.md)
6. [Optimizer（最佳化器）](../concepts/optimizer.md)
7. [Training, Validation, and Test Sets（訓練、驗證與測試集）](../concepts/training-validation-and-test-sets.md)
8. [Overfitting（過度擬合）](../concepts/overfitting.md)

## Supporting concepts / 支援概念

- [Data Preprocessing（資料前處理）](../concepts/data-preprocessing.md)
- [Feature Scaling（特徵縮放）](../concepts/feature-scaling.md)
- [Epoch and Batch（訓練週期與批次）](../concepts/epoch-and-batch.md)
- [Evaluation Metric（評估指標）](../concepts/evaluation-metric.md)
- [Hyperparameter（超參數）](../concepts/hyperparameter.md)
- [Weight Initialization（權重初始化）](../concepts/weight-initialization.md)

## Approved conflict treatment

- Backpropagation computes gradients; Optimizer uses gradients to update parameters.
- S02's conflated wording remains attributed as a pedagogical/source issue.
- Squared Error and Cross Entropy are different task and teaching contexts, not a factual contradiction.

## Next chapter

[Probability and Prediction](03-probability-and-prediction.md)
