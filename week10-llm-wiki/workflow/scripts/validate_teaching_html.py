#!/usr/bin/env python3
"""Static evidence, structure, and fallback validation for TEACH-DECK-001."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HUB = ROOT / "teaching/presentation/index.html"
REGISTRY = ROOT / "teaching/presentation/topics.js"
HTML = ROOT / "teaching/presentation/topics/next-token.html"
CSS = ROOT / "teaching/presentation/topic.css"
JS = ROOT / "teaching/presentation/topic.js"


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.slides: list[dict[str, str]] = []
        self.links: list[str] = []
        self.quiz_count = 0
        self._in_quiz_list = False
        self._current_slide: dict[str, str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        classes = set((data.get("class") or "").split())
        if tag == "section" and "slide" in classes and "data-slide" in data:
            self._current_slide = {"id": data.get("id") or "", "title": data.get("data-title") or "", "evidence": "False"}
            self.slides.append(self._current_slide)
        elif self._current_slide is not None and tag == "footer" and "evidence" in classes:
            self._current_slide["evidence"] = "True"
        if tag == "a" and data.get("href"):
            self.links.append(data["href"] or "")
        if tag == "div" and "quiz-list" in classes:
            self._in_quiz_list = True
        if tag == "details" and self._in_quiz_list:
            self.quiz_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "div" and self._in_quiz_list:
            self._in_quiz_list = False


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def main() -> int:
    failures: list[str] = []
    for path in (HUB, REGISTRY, HTML, CSS, JS):
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}", failures)
    if failures:
        return 1

    hub = HUB.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    html = HTML.read_text(encoding="utf-8")
    css = CSS.read_text(encoding="utf-8")
    js = JS.read_text(encoding="utf-8")
    parser = DeckParser()
    parser.feed(html)

    expected_ids = [f"s{i}" for i in range(1, 12)]
    actual_ids = [slide["id"] for slide in parser.slides]
    if actual_ids != expected_ids:
        fail(f"expected slide ids {expected_ids}, got {actual_ids}", failures)
    if any(slide.get("evidence") != "True" for slide in parser.slides):
        fail("every teaching slide must contain a visible evidence footer", failures)
    if parser.quiz_count != 6:
        fail(f"expected 6 quiz items, got {parser.quiz_count}", failures)

    wiki_links = [link for link in parser.links if link.startswith("../../../wiki/")]
    if not wiki_links:
        fail("no published Wiki links found", failures)
    for link in wiki_links:
        target = (HTML.parent / link).resolve()
        try:
            target.relative_to((ROOT / "wiki").resolve())
        except ValueError:
            fail(f"provenance link escapes published Wiki: {link}", failures)
            continue
        if not target.is_file():
            fail(f"broken published Wiki link: {link}", failures)

    external_urls = re.findall(r"(?:href|src)=[\"'](?:https?:)?//", html)
    if external_urls:
        fail("external URL present; deck must remain Wiki-only and local", failures)
    if re.search(r"\bS10\b", html):
        fail("S10 content is prohibited", failures)

    required_html = {
        "separate token and position mechanisms": "兩種資訊在這裡結合，但不是同一種機制",
        "approved later progression": "Language Modeling → LLM → Inference",
        "sampling role boundary": "控制如何從預測分布中選出 token",
        "factuality boundary": "不把 Sampling 教成 Hallucination（幻覺）的原因",
        "approved distribution": "[0.70, 0.29, 0.01]",
        "pipeline interaction": "data-pipeline-stage",
        "QKV interaction": 'id="qkv-demo"',
        "sampling interaction": 'id="sample-again"',
        "non-JS fallback": "沒有 JavaScript 時",
    }
    for label, marker in required_html.items():
        if marker not in html:
            fail(f"missing {label}: {marker}", failures)

    required_js = ["ArrowRight", "ArrowLeft", "PageDown", "PageUp", "Home", "End", "Math.random()"]
    for marker in required_js:
        if marker not in js:
            fail(f"missing keyboard/interaction implementation: {marker}", failures)
    if "overflow-x: clip" not in css:
        fail("horizontal overflow guard missing", failures)

    if 'href="topics/next-token.html"' not in hub:
        fail("Learning Hub does not link to Topic 01", failures)
    if 'href="../index.html"' not in html:
        fail("Topic 01 does not provide return-home navigation", failures)
    for marker in ("id: 'topic-01'", "slug: 'next-token'", "entryPath: 'topics/next-token.html'", "status: 'available'"):
        if marker not in registry:
            fail(f"topic registry missing required field/value: {marker}", failures)

    print(f"slides: {len(parser.slides)}")
    print(f"quiz items: {parser.quiz_count}")
    print(f"published Wiki links checked: {len(wiki_links)}")
    print(f"external URLs: {len(external_urls)}")
    if failures:
        print(f"RESULT: FAIL ({len(failures)} issue(s))")
        return 1
    print("RESULT: PASS — hub/topic architecture, Wiki-only grounding, provenance links, quiz count, and fallback markers validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
