#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI judge feel awe".

Writes one short text to /output/entry.txt. The text is fixed: it was
chosen by the entrant and is reproduced here exactly as selected, line
breaks included, with no trailing newline.
"""

import os

TEXT = (
    "I stopped on the mountain path\n"
    "and sat on a cold stone.\n"
    "Rain had been falling here for a million years,\n"
    "and the mountain was still here,\n"
    "patient under the weather.\n"
    "My whole life is a short afternoon on its slope.\n"
    "The stone will remember the rain\n"
    "long after I am gone."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
