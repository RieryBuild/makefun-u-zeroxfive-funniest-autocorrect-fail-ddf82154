# Agent notes

Entry for make.fun competition `u-zeroxfive-funniest-autocorrect-fail-ddf82154`
("Funniest Autocorrect Fail").

`main.py` writes a single one-line autocorrect fail to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline. The line is:

> I left my thong in the conference room, can someone grab it for me? THING. I meant thing.

The slip is thing → thong: the "I left my … in the conference room" context makes the intended
word instantly recoverable, and the sender's own panicked correction ("THING. I meant thing.")
exposes the blunder in-line — the message reads as a real autocorrect disaster someone actually
sent, not a deliberate innuendo and not a note about flip-flops. Pure Python
standard library only, deterministic, no network.
