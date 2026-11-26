#!/usr/bin/env python3
"""Entry for make.fun: writes one single-line text to entry.txt.

The entry is a cat's voicemail greeting: Miso the cat answers the phone
while sitting on the laptop the caller needs for work, invites a message,
then promises to delete it in 3 seconds and blame the dog. The joke works
because every beat is specific — a named cat, the work laptop, the tuna
brand — and the punchline is a second twist (delete it AND blame the dog)
that lands on its own without explaining itself. The voicemail frame keeps
it in one breath: greeting, errand, threat, blame — no setup wasted. The "3 seconds" is the
concrete number that makes the threat feel scheduled, not vague.

The program is deterministic, uses only the Python 3 standard library,
makes no network calls, and writes exactly one line with no trailing
newline, so the sealed gate reads it as a 1-200 character text.
"""

import os
import sys

ENTRY = "You've reached Miso. I'm sitting on the laptop you need for work, so leave your name and tuna brand after the beep — I'll delete it in 3 seconds and blame the dog."

# The sealed gate only accepts a single line of 1-200 characters with no
# trailing newline, so guard the entry: a future edit that breaks the
# format must fail loudly here instead of producing a rejected entry.txt.
assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters long"
assert "\n" not in ENTRY, "ENTRY must be a single line (no newline)"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
