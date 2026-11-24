"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about an everyday annoyance (the supermarket
self-checkout) to /output/entry.txt. The rant is validated to be UTF-8 text
of 1 to 400 characters and not only whitespace before it is written.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

RANT = (
    "The self-checkout has ONE job and it still calls for help more than I do. "
    "'Unexpected item in the bagging area.' That item is the one YOU just told "
    "me to scan! Then a human must approve my bananas like they are controlled "
    "substances. I came in for milk. I left as an unpaid employee whose "
    "manager is a beeping robot."
)


def validate(text: str) -> str:
    """Return text unchanged when it is a valid entry, else raise ValueError.

    A valid entry is UTF-8 encodable text of 1 to 400 characters (counted as
    Unicode code points, the way the contest gate counts) that is not only
    whitespace. The failure reason names exactly which rule was broken.
    """
    if not isinstance(text, str):
        raise ValueError(f"entry must be str, got {type(text).__name__}")
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    # Round-trip through UTF-8 so a stray surrogate can never reach the file.
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("entry is not clean UTF-8 text")
    return text


def build_entry() -> str:
    """Return the validated rant text this program writes."""
    return validate(RANT)


def main() -> None:
    text = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
