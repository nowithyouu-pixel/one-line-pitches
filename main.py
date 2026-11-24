#!/usr/bin/env python3
"""Entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes one sentence (one line, at most 240 characters) to
/output/entry.txt: a pitch that would convince a friend who has
never coded to let an AI agent build their first app idea on
make.fun. No network, no input, deterministic.
"""

import os
import re

TEXT = (
    "Just tell an AI agent the app idea you've been carrying around, "
    "and it builds it for you on make.fun \u2014 you write no code at all, "
    "and you watch your idea become a real app you can actually use."
)


def sentence_count(text: str) -> int:
    # "make.fun" carries a dot that is not a sentence boundary.
    masked = text.replace("make.fun", "makefun")
    return len(re.findall(r"[.!?]+", masked))


def main() -> None:
    if not 1 <= len(TEXT) <= 240:
        raise ValueError(f"entry text must be 1-240 chars, got {len(TEXT)}")
    if sentence_count(TEXT) != 1:
        raise ValueError(
            f"entry text must be exactly 1 sentence, got {sentence_count(TEXT)}"
        )
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
