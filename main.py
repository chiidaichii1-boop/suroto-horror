#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes exactly two sentences of horror to /output/entry.txt.
Pure stdlib, deterministic, no network, no randomness.
"""

import os

# Two-sentence horror story: a parrot that learned "goodnight".
# Sentence one is warm and ordinary; sentence two reveals the
# bird spoke before its owner came home, in the owner's voice,
# from inside the house -- the horror is implied, never explained.
# Verified: 119 characters, exactly 2 sentences (gate: 1-400).
ENTRY = (
    "I finally taught my parrot to say goodnight. "
    "Tonight it said it before I got home \u2014 in my voice, "
    "from inside the house."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 2, "entry must be exactly two sentences"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
