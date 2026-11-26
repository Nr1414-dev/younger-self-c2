#!/usr/bin/env python3
"""One Line to Your Younger Self — one funny single line to send back to
your younger self (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 132 characters, no
trailing newline).
"""

import os

ENTRY = "Take her to prom even though she says yes out of pity — twenty years later you'll both laugh about it, and she's the one who stayed."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
