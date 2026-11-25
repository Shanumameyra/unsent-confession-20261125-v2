"""Unsent: The Micro-Confession Sprint — entry program.

Writes one micro-confession in exactly two parts to /output/entry.txt
(and ./output/entry.txt): a To: line naming who it was meant for, and
the unsent message itself, one line written exactly as it was typed,
with no explanation after it.
"""

import os

TO_LINE = "To: my first boss"
MESSAGE = (
    "I cried in the stairwell after you praised my quarterly report in "
    "front of the whole team, because I was sure you would take the praise "
    "back if you knew how lost I was."
)

ENTRY = TO_LINE + "\n" + MESSAGE


def main() -> None:
    # Two parts, exactly: a To: line, then one message line. No trailing
    # explanation, no extra lines.
    assert TO_LINE.startswith("To: "), "first line must be a To: line"
    assert TO_LINE.strip(), "To: line must not be empty"
    assert MESSAGE.strip(), "message must not be empty"
    assert "\n" not in MESSAGE and "\r" not in MESSAGE, (
        "message must be a single line"
    )
    assert ENTRY.count("\n") == 1, "entry must be exactly two lines"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY, (
        "entry must be valid UTF-8"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.makedirs("./output", exist_ok=True)
    with open("./output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
