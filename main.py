"""Funniest Autocorrect Fail entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with
no trailing newline, so the file's character count equals the line length
exactly. The line is a single autocorrect fail (thing -> thong) inside an
otherwise ordinary coworker text, followed by the sender's own panicked
in-line correction ("THING. I meant thing."), which makes the blunder
unmistakable instead of reading as deliberate innuendo.
"""

import os

LINE = "I left my thong in the conference room, can someone grab it for me? THING. I meant thing."

# Fail fast if the line ever stops being a single line: the gate requires
# exactly one line of 1-199 characters, and a stray newline would void it.
assert "\n" not in LINE and "\r" not in LINE
assert len(LINE) < 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
