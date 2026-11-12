"""cutest-picture-01 entry: copy the staged picture to the output.

The picture (art.jpg, a baby red panda hugging a plush moon pillow)
ships in the repository next to this file. The run is a byte-for-byte
copy, so both grading runs write identical bytes.

The image bytes are JPEG; the rules name the output entry.png either
way and tell the formats apart by their first bytes.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("art.jpg")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
