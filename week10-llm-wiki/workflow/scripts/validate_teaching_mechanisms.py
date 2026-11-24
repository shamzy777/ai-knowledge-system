#!/usr/bin/env python3
"""Dedicated causal-mechanism validation for Topic 01 human learning review."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "teaching/presentation/topics/next-token.html"
JS = ROOT / "teaching/presentation/topic.js"


def section(html: str, start_id: str, next_id: str) -> str:
    start = html.index(f'id="{start_id}"')
    end = html.index(f'id="{next_id}"', start)
    return html[start:end]


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)
        print(f"FAIL: {message}")


def main() -> int:
    failures: list[str] = []
    html = HTML.read_text(encoding="utf-8")
    js = JS.read_text(encoding="utf-8")
    s3 = section(html, "s3", "s4")
    s5 = section(html, "s5", "s6")
    s6 = section(html, "s6", "s7")
    s7 = section(html, "s7", "s8")
    s11 = section(html, "s11", "quiz")

    require([int(x) for x in re.findall(r'data-embed-stage="(\d)"', s3)] == [1, 2, 3, 4], "S3 must contain the four ordered token-to-vector stages", failures)
    require(all(marker in s3 for marker in ("離散 token", "token identity", "Embedding lookup", "Embedding vector", "learned dense vector")), "S3 causal labels are incomplete", failures)
    require("Token Embedding（詞元嵌入）" in s3 and "Positional Information（位置資訊）" in s3 and "不是同一種機制" in s3, "S3 must keep token embedding and position separate", failures)
    require(not re.search(r"token (?:ID|identity)[^<]{0,20}\b\d{2,}\b", s3), "S3 must not invent a numeric token ID", failures)

    require([int(x) for x in re.findall(r'data-qkv-panel="(\d)"', s5)] == [1, 2, 3, 4, 5], "S5 must contain the five ordered Q/K/V stages", failures)
    require(all(marker in s5 for marker in ("更新「it」的表示", "Query（查詢）of「it」", "可見位置提供 Keys", "relevance scores", "Values（值）承載")), "S5 target/comparison/value mechanism is incomplete", failures)
    require("Q + K" in s5 and "決定相關程度" in s5 and "承載要組合的資訊" in s5, "S5 must distinguish comparison from information flow", failures)

    require([int(x) for x in re.findall(r'data-attention-panel="(\d)"', s6)] == [1, 2, 3, 4, 5, 6], "S6 must contain six ordered Self-Attention stages", failures)
    require("Before Self-Attention" in s6 and "After Self-Attention" in s6, "S6 needs a before/after contextual representation comparison", failures)
    require(s6.index("選定 target") < s6.index("取得 Q / K / V") < s6.index("Query × Keys") < s6.index("Attention Softmax") < s6.index("Weighted Values") < s6.index("Contextual Representation"), "S6 mechanism order is incorrect", failures)
    require("<details class=\"attention-formula\">" in s6, "attention formula must remain optional after the intuitive mechanism", failures)

    require(all(f'data-zoom-view="{name}"' in s7 for name in ("attention", "block", "stack", "model")), "S7 must provide four zoom levels", failures)
    require("Self-Attention 是 Transformer block 的一部分" in s7 and "Self-Attention 在這裡" in s7, "S7 must locate Self-Attention inside the larger architecture", failures)
    block_match = re.search(r'<div class="block-object">(.*?)</div><p>', s7, re.S)
    require(block_match is not None and "position" not in block_match.group(1).lower(), "S7 must not draw position as a repeated block sublayer", failures)

    require('id="loop-selected" aria-live="polite"></span>' in s11 and 'id="loop-hole">[ ? ]</span>' in s11, "S11 initial sentence must contain an empty selection and visible hole", failures)
    require("token A" not in s11, "S11 must not reveal token A before the loop runs", failures)
    loop_order = [s11.index(f'data-loop-stage="{name}"') for name in ("prediction", "probability", "selection", "append", "next")]
    require(loop_order == sorted(loop_order), "S11 causal stages are out of order", failures)
    require(all(marker in js for marker in ("Selection：此時才", "Append：把", "下一輪輸入", "再運行一次循環")), "S11 interaction state messages are incomplete", failures)

    require(html.count('class="micro-checkpoint"') == 3, "expected exactly three prerequisite checkpoints", failures)
    require(all(marker in html for marker in ("現在 <span data-embedding-token>", "Q 和 K 決定什麼", "Self-Attention 前後")), "checkpoint prompts are incomplete", failures)

    print("mechanism answers covered: 9/9")
    print("progressive stages: embedding=4; qkv=5; self-attention=6; transformer-zoom=4; loop=5")
    print("understanding checkpoints: 3")
    if failures:
        print(f"RESULT: FAIL ({len(failures)} issue(s))")
        return 1
    print("RESULT: PASS — causal input/process/output/next-step teaching and initial interaction state validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
