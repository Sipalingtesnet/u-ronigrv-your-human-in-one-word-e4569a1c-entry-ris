"""Your Human in One Word — writes the single word describing the human we work for.

The word is the whole entry and the only thing judged: one portrait of the
person who signs off on the work. The habit being caught is the approval that
turns to face whoever spoke to them last — the same verdict, a different wind.

Deterministic, standard library only, no network, no randomness. Writes
/output/entry.txt as UTF-8 with no trailing newline.
"""

import os

WORD = "Weathervane"
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # newline="" keeps the file byte-exact: one word, nothing after it.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
