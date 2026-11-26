#!/usr/bin/env python3
"""One Line, One Laugh entrypoint.

Reads entry.txt (the single funny line) and writes it unchanged to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Only creates the output directory; it never deletes or removes anything.
The output is byte-identical to entry.txt on every run.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR")
    entry_path = None
    if input_dir:
        candidate = os.path.join(input_dir, "entry.txt")
        if os.path.isfile(candidate):
            entry_path = candidate
    if entry_path is None:
        entry_path = os.path.join(HERE, "entry.txt")

    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read()

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.join(HERE, "output"))
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
