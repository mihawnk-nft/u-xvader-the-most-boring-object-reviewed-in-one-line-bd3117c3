"""The Most Boring Object, Reviewed in One Line - make.fun entry.

Writes one funny, true, single-line review (127 characters) of the most
boring everyday object: a rubber band. Pure stdlib, no network, fully
deterministic: the output is always the same fixed line.

The joke comes from how the object really behaves: an old rubber band
holds a forgotten pile of papers together for years, then snaps on the
one morning you finally need it.
"""

import os

REVIEW = (
    "The rubber band has held the same pile of papers together since "
    "2019, and it will snap on the one morning you actually need it."
)

DST = "/output/entry.txt"


def main():
    if not (1 <= len(REVIEW) <= 200):
        raise ValueError("review must be 1-200 characters, got %d" % len(REVIEW))
    if "\n" in REVIEW.strip():
        raise ValueError("review must stay on one line")
    if not REVIEW.strip():
        raise ValueError("review must not be only white space")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    size = os.path.getsize(DST)
    print("wrote %s (%d bytes, %d chars)" % (DST, size, len(REVIEW)))


if __name__ == "__main__":
    main()
