#!/usr/bin/env python3
"""Structural-only lint for RUN-003 relationship proposals."""
from __future__ import annotations
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "staging/relationships/RUN-003-batch-relationship-proposals.md"
ALLOWED = {"prerequisite", "part-of", "cause/effect", "evolution", "application", "contrast", "theory ↔ practice", "cross-domain analogy"}

def titles() -> set[str]:
    result: set[str] = set()
    for path in (ROOT / "staging/concepts").glob("*.md"):
        match = re.search(r'^canonical_title:\s*"(.+)"$', path.read_text(encoding="utf-8"), re.M)
        if match:
            result.add(match.group(1)); result.add(match.group(1).split("（", 1)[0])
    return result

def main() -> int:
    errors: list[str] = []
    known = titles(); seen: set[str] = set(); rows = 0
    if not REGISTER.exists(): errors.append("proposal register missing")
    else:
        for line in REGISTER.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| R3-"): continue
            rows += 1
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != 6: errors.append(f"malformed row: {cells}"); continue
            rid, action, source, relation, target, support = cells
            if not re.fullmatch(r"R3-\d{3}", rid) or rid in seen: errors.append(f"invalid/duplicate ID {rid}")
            seen.add(rid)
            if action not in {"add", "add-source-support"} and not action.startswith("replacement-for-R3-"): errors.append(f"{rid}: invalid action")
            if relation not in ALLOWED: errors.append(f"{rid}: invalid relationship {relation!r}")
            if source not in known or target not in known: errors.append(f"{rid}: invalid endpoint {source!r} -> {target!r}")
            if not re.search(r"S(?:01|02|05|06|07) (?:p\.|pp\.|full image)", support): errors.append(f"{rid}: source/page locator missing")
    if rows != 37: errors.append(f"expected 37 proposals, found {rows}")
    print(f"RUN-003 relationship structural lint: {len(errors)} error(s); {rows} proposal(s)")
    for e in errors: print(f"ERROR: {e}")
    return 1 if errors else 0

if __name__ == "__main__": sys.exit(main())
