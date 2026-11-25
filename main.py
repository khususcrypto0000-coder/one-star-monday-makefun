"""One Star for Monday - make.fun bounty entry.

Writes a one-star restaurant review of Monday to /output/entry.txt.
Standard library only.
"""

import os
import sys

ENTRY = "One star. Monday reheated Sunday's roast, served it with a side of deadlines, and the bill charged overtime."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    words = text.split()
    if not 1 <= len(text) <= 180:
        sys.exit("entry must be 1-180 characters")
    if len(words) > 25:
        sys.exit("entry must be at most 25 words")
    if not text.strip():
        sys.exit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "output is not byte-identical to ENTRY"
    assert not data.endswith(b"\n"), "no trailing newline allowed"
    # Gate summary: one line, plain text, <=25 words, 1-180 chars.
    print("Wrote %d bytes to %s (%d words, %d chars)"
          % (len(data), OUTPUT_PATH, len(words), len(text)))


if __name__ == "__main__":
    main()
