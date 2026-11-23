#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one letter to $MAKEFUN_OUTPUT_DIR/entry.txt.

The letter is D. The word behind it is "doomscrolling": the day was
spent with the phone glowing at 2 a.m., thumb scrolling disaster
after disaster, unable to stop. Vivid, funny, and true — D fits the
word the way the sound of "doom" fits the mood.
"""

import os
import sys

LETTER = "D"

# The gate accepts exactly one character, A–Z, and nothing else.
# Fail loudly here rather than ever writing an invalid entry.
if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
    raise ValueError(f"LETTER must be one A–Z character, got {LETTER!r}")


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        print(f"entry.txt holds {written!r}, expected {LETTER!r}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
