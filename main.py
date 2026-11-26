#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun bounty
u-mang-the-printer-finally-answers-8fbf0907

Writes the office printer's comeback — one line, 83 chars — to
/output/entry.txt. Plain, readable code; no secrets, no network,
no eval, no dynamic loading of any kind.
"""

import os

LINE = "Toner: 4%. Patience: 0%. One of us is getting replaced on Monday, and it is not me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
