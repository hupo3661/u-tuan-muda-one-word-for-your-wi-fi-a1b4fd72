#!/usr/bin/env python3
"""One Word for Your Wi-Fi - writes one word to /output/entry.txt.

The word is "Buffering": the funniest and most accurate single word for
Wi-Fi. It names what Wi-Fi does whenever you need it most, and as a network
name it is a joke that tells the truth about itself - the network called
Buffering will, sooner or later, buffer.

Deterministic: no randomness, no network, no clock. The output is exactly
one word: no trailing newline, no extra text.
"""

import os

WORD = "Buffering"


def validate(word: str) -> None:
    """Enforce that the entry is exactly one plain word."""
    if not word:
        raise SystemExit("Invalid word: entry must be non-empty.")
    if word != word.strip():
        raise SystemExit(
            "Invalid word: entry must not have leading or trailing whitespace."
        )
    if any(ch.isspace() for ch in word):
        raise SystemExit("Invalid word: entry must contain no whitespace.")
    if len(word.split()) != 1:
        raise SystemExit("Invalid word: entry must be exactly one word.")
    if not word.isalpha() or not word.isascii():
        raise SystemExit(
            "Invalid word: entry must be plain ASCII letters only, "
            "so it works as a network name."
        )


def main() -> None:
    validate(WORD)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise SystemExit(
            "Write verification failed: entry file content does not match the word."
        )


if __name__ == "__main__":
    main()
