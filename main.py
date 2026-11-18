#!/usr/bin/env python3
"""make.fun news-image-20261118 entry: World News, Wednesday 18 November 2026.

Copies the bundled infographic (news.png, composed at build time from
researched reporting of 18 November 2026) to /output/entry.png.
Pure Python standard library, no network access, fully deterministic:
the output bytes are exactly the bundled image bytes on every run.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Self-check: the written file must be byte-identical to the source.
    if sha256(DST) != sha256(SRC):
        raise SystemExit("output hash mismatch: %s != %s"
                         % (sha256(DST), sha256(SRC)))
    print("Wrote %s (%d bytes, sha256 %s)"
          % (DST, os.path.getsize(DST), sha256(DST)))


if __name__ == "__main__":
    main()
