#!/usr/bin/env python3
"""Five Seconds to Explain the Glass -- make.fun entry.

Writes the cat's excuse (one sentence, in the cat's own voice) to entry.txt.
"""
import os

LINE = "At 7:30 I shoved the glass off because my 8 o'clock vet visit needed a distraction, and it worked: you forgot the vet."

def main():
    # Gate self-check: the competition accepts 1-200 UTF-8 characters.
    n = len(LINE)
    if not 1 <= n <= 200:
        raise ValueError(f"entry is {n} characters, outside the 1-200 gate")
    if LINE.count(".") != 1:
        raise ValueError("entry must be a single sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")

if __name__ == "__main__":
    main()
