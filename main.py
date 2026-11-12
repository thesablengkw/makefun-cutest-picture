"""cutest-picture-01 entry (v3): copy the staged picture to the output.

The picture (art.jpg, a chubby baby bunny with huge open eyes blowing a
giant dandelion, one seed landed on its nose) ships in the repository
next to this file. The run is a byte-for-byte copy, so both grading
runs write identical bytes.

The image bytes are JPEG; the rules name the output entry.png either
way and tell the formats apart by their first bytes.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("art.jpg")

MAX_BYTES = 1_048_576  # the gate's 1 MiB cap on the picture file
MAGICS = (b"\xff\xd8\xff", b"\x89PNG")  # JPEG and PNG, told apart by first bytes


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Guard the gate before copying: refuse to ship a missing, oversized
    # or non-image source instead of silently copying bad bytes (an
    # invalid file scores 0 and never reaches the judge).
    if not SOURCE.is_file():
        raise SystemExit(f"missing source picture: {SOURCE}")
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"source picture is {len(data)} bytes; gate allows at most {MAX_BYTES}")
    if not data.startswith(MAGICS):
        raise SystemExit("source picture is neither JPEG nor PNG (bad magic bytes)")
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    # Byte-for-byte means byte-for-byte: hash the copy and compare, so a
    # copy that merely matches in size but differs in content still fails.
    if hashlib.sha256(dest.read_bytes()).hexdigest() != hashlib.sha256(data).hexdigest():
        raise SystemExit("copy mismatch: written bytes differ from the source picture")


if __name__ == "__main__":
    main()
