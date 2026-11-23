#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes the graded one-letter answer to entry.txt next to this file.
Pure Python standard library, no network, no input files.

The choice: A — coffee. Of the two drinks, coffee is the bolder, more
alive answer: it lands as a full stance in a single letter, where tea
reads as the quieter, second choice. One letter, nothing else.
"""

import os

ENTRY = "A"

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    path = os.path.join(HERE, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Grading sandbox: the scorer reads /output/entry.txt, collected as
    # another user, so the copy there must be world-readable (mode 0644).
    out_dir = "/output"
    if os.path.isdir(out_dir):
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(out_path, 0o644)
    print("Wrote %d char: %r" % (len(ENTRY), ENTRY))


if __name__ == "__main__":
    main()
