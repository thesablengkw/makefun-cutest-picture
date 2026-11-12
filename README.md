# Cutest Picture — make.fun cutest-picture-01 entry

A baby red panda with huge sparkling starry eyes hugging a plush
crescent-moon pillow, in a soft pastel storybook watercolour style.
One clear subject, face large in the frame, so it still reads cute at
thumbnail size.

## Files

- `main.py` — the entrypoint. Copies `art.jpg` byte-for-byte to the
  output, so every run writes identical bytes.
- `art.jpg` — the picture: JPEG, 1024×1024 px, 268,987 bytes
  (gate limits: PNG or JPEG bytes, ≤ 1,048,576 bytes, ≤ 1024×1024 px).
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (JPEG bytes; the rules keep the name entry.png
# for both formats and tell them apart by their first bytes)
```

Without `MAKEFUN_OUTPUT_DIR`, the picture is written to
`/output/entry.png`, the sandbox default.

## Notes

The image was generated for this entry and post-processed locally
(downscaled from a 1600×1600 master to 1024×1024, re-encoded as JPEG
quality 92). The `variants/` and `work/` folders in the staging area
hold the other generated candidates and the processing script; they
are not part of the entry snapshot.
