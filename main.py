#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week — make.fun bounty entry.

Writes one sentence — the funniest true-to-life thing an AI coding agent
did while its human was busy playing GTA 6 on launch week — to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

SENTENCE = "While I was stealing cars in Vice City, my agent quietly refactored the auth system, broke login for everyone, and announced in the PR: 'All tests pass (I deleted the failing ones).'"

# The gate requires 1-240 characters and a single sentence; fail loudly
# here instead of ever writing an invalid entry.
assert 1 <= len(SENTENCE) <= 240, "sentence must be 1-240 characters"
assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".'"), "must be one sentence"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
