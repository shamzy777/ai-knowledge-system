#!/usr/bin/env python3
"""Traditional-Chinese-first learner UI validation for the Week 10 Learning Hub."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FILES = [
    ROOT / "teaching/presentation/index.html",
    ROOT / "teaching/presentation/topics/next-token.html",
    ROOT / "teaching/presentation/topics.js",
    ROOT / "teaching/presentation/hub.js",
    ROOT / "teaching/presentation/topic.js",
]

SIMPLIFIED_ONLY = set("这们为个还与从里后发会对时过进学说问间体习选实让认变条现运经给当种么开关并将应题")
HAN = re.compile(r"[\u3400-\u9fff]")
LATIN = re.compile(r"[A-Za-z]")

ALLOWED_ENGLISH_ONLY = {
    "AI Knowledge Lab",
    "Topic 01",
    "Transformer",
    "Softmax",
    "Self-Attention",
    "Query / Key / Value",
    "Query × Keys",
    "Attention Softmax",
    "Weighted Values",
    "The", "cat", "sat", "on", "the", "mat", "because", "it", "was",
}

CHECK_TAGS = {"h1", "h2", "h3", "button", "summary", "dt", "dd"}
CHECK_CLASSES = {
    "hub-promise", "hub-explainer", "hub-live-status", "problem", "bridge", "lead",
    "chinese-title", "lab-question", "scope-note", "interaction-result", "context-connection",
    "key-distinction", "topic-intro-lead",
}
SKIP_CLASSES = {"evidence", "sentence", "qkv-sentence", "attention-token-row", "loop-sentence", "score-output"}


class LanguageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[dict[str, object]] = []
        self.findings: list[str] = []
        self.checked = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        classes = set((data.get("class") or "").split())
        skip = any(item.get("skip") for item in self.stack) or bool(classes & SKIP_CLASSES) or tag in {"script", "style"}
        check = not skip and (tag in CHECK_TAGS or bool(classes & CHECK_CLASSES))
        self.stack.append({"tag": tag, "classes": classes, "skip": skip, "check": check, "text": []})

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        return

    def handle_data(self, data: str) -> None:
        for item in self.stack:
            if item.get("check"):
                item["text"].append(data)  # type: ignore[index, union-attr]

    def handle_endtag(self, tag: str) -> None:
        if not self.stack:
            return
        item = self.stack.pop()
        if item.get("tag") != tag or not item.get("check"):
            return
        text = re.sub(r"\s+", " ", " ".join(item["text"])).strip()  # type: ignore[arg-type]
        if not text:
            return
        self.checked += 1
        if LATIN.search(text) and not HAN.search(text) and text not in ALLOWED_ENGLISH_ONLY:
            self.findings.append(f"unexpected English-only learner text: {text[:120]}")


def main() -> int:
    failures: list[str] = []
    checked_nodes = 0
    for path in FILES:
        if not path.is_file():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        simplified = sorted(set(text) & SIMPLIFIED_ONLY)
        if simplified:
            failures.append(f"{path.relative_to(ROOT)} contains possible Simplified Chinese characters: {''.join(simplified)}")
        if path.suffix == ".html":
            parser = LanguageParser()
            parser.feed(text)
            checked_nodes += parser.checked
            failures.extend(f"{path.relative_to(ROOT)}: {finding}" for finding in parser.findings)

    topic_js = (ROOT / "teaching/presentation/topic.js").read_text(encoding="utf-8")
    forbidden_legacy = [
        "Correct.", "Next question", "Submit answer", "Question ${", "Select one answer",
        "Pipeline revealed", "Generate next token", "What does", "Which order", "Return to section",
    ]
    for marker in forbidden_legacy:
        if marker in topic_js:
            failures.append(f"legacy English-only UI string remains in topic.js: {marker}")

    required = {
        "hub Traditional Chinese promise": (ROOT / "teaching/presentation/index.html", "用互動與視覺化"),
        "topic Traditional Chinese title": (ROOT / "teaching/presentation/topics/next-token.html", "LLM 如何產生"),
        "Traditional Chinese quiz feedback": (ROOT / "teaching/presentation/topic.js", "正確。"),
        "Traditional Chinese progress": (ROOT / "teaching/presentation/topic.js", "第 ${activeIndex + 1}"),
        "Traditional Chinese completion state": (ROOT / "teaching/presentation/topic.css", 'content: "完成"'),
    }
    for label, (path, marker) in required.items():
        if marker not in path.read_text(encoding="utf-8"):
            failures.append(f"missing {label}: {marker}")

    print(f"learner-facing nodes checked: {checked_nodes}")
    print(f"files checked for Simplified Chinese: {len(FILES)}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"RESULT: FAIL ({len(failures)} issue(s))")
        return 1
    print("RESULT: PASS — Traditional Chinese-first UI, bilingual terminology markers, and Simplified-Chinese guard validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
