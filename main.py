#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes one line, at most 120 characters, in which a robot vacuum explains
why it missed a spot, to /output/entry.txt.

Stdlib only: the grader installs nothing.
"""

import os
import sys

# The joke, in the vacuum's own voice: it is not denying the missed spot,
# it is reclassifying the dust as a tenant — a machine owning up to failure
# with a legalistic excuse from its own world (dust, the couch, the dock).
ENTRY = "I didn't miss that spot \u2014 the dust under the couch pays rent, so legally it's a tenant now."


def validate(text):
    """Gate mirror: UTF-8 text, 1-120 chars, not only whitespace."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-120")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    text.encode("utf-8")
    return text


def main():
    text = validate(ENTRY)
    if "--self-test" in sys.argv:
        print(f"self-test OK: {len(text)} chars")
        return
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
