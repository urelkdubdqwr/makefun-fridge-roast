"""Roast a fridge: write a single funny line to entry.txt in the output dir."""

import os

TEXT = (
    "My fridge's firmware update failed at 98%. Its one job since 1913 has been "
    "to stay cold, and it bricked itself trying to get better at it.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
