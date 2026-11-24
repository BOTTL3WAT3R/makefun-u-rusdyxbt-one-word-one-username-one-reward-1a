#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. The handle is "bottl3wat3r": bottled water spelled
in leetspeak — a bottle of water that learned to type. Eleven characters,
one word, no spaces, no gloss.
"""

from pathlib import Path

USERNAME = "bottl3wat3r"
OUTPUT_PATH = Path("/output/entry.txt")


def validate(username: str) -> None:
    """Mirror the bounty's sealed gate before anything is written.

    The gate accepts UTF-8 text of 1 to 30 characters that is not only
    white space; the brief asks for one word and nothing else, so the
    handle must also be a single token with no spaces or padding.
    """
    assert 1 <= len(username) <= 30, "username must be 1 to 30 characters"
    assert username.strip() == username and username != "", "no padding"
    assert " " not in username and "\n" not in username, "one word only"


def main() -> None:
    validate(USERNAME)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
