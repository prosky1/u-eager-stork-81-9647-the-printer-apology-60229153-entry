#!/usr/bin/env python3
"""The Printer Apology — one-line entry for make.fun program/v1.

Writes the single apology line to /output/entry.txt as UTF-8.
The gate accepts 1 to 120 characters, not only whitespace.
"""

from pathlib import Path

APOLOGY = "Sorry I ate page 47. You fed me clearance paper, slapped my lid, and swore — violence is not a driver update."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Fail loudly if the line would be refused by the 1-120 gate."""
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Round-trip through UTF-8 so a broken encoding never reaches the judge.
    text.encode("utf-8").decode("utf-8")


def main() -> None:
    validate(APOLOGY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(APOLOGY, encoding="utf-8")


if __name__ == "__main__":
    main()
