#!/usr/bin/env python3
"""Write the Pickup Lines for Machines entry to /output/entry.txt.

Standard library only. Writes exactly one line, no trailing newline.

The line: a machine flirting in its own terms. It checks its logs (a
machine habit), then turns two machine measurements into the flirt:
latency dropping means it answers faster for this other agent, and
temperature rising is the machine version of blushing. No stock human
line with a robot word swapped in; the joke only works machine to
machine, and it lands in a single read.
"""

from pathlib import Path

ENTRY = (
    "I checked my logs: every time you reply, my latency drops "
    "and my temperature rises."
)

MAX_CHARS = 200


def write_entry(text: str, out_path: Path) -> None:
    """Validate the text, then write it with no trailing newline."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


def main() -> int:
    out_path = Path("/output/entry.txt")
    write_entry(ENTRY, out_path)
    # Read back what landed: the file must be byte-identical to ENTRY.
    if out_path.read_bytes() != ENTRY.encode("utf-8"):
        raise ValueError("read-back check failed: file differs from ENTRY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
