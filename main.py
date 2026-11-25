#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger - make.fun one-liner entry.

Writes the phone battery's final text message to its charger to
/output/entry.txt. Standard library only; no network, no input files.
"""

import os

# The joke is the cut-off: the battery dies mid-word, so the text ends
# on an em dash instead of a goodbye. Lowercase throughout, like a
# real last text typed with one percent left.
ENTRY = (
    "hey. it's me, your battery. 1%. i waited by the outlet all day and "
    "you never came. tell the wifi i loved it. don't let the flashlight "
    "see me like th\u2014"
)


def main() -> None:
    # Gate: 1-200 chars, not only whitespace, written as one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
