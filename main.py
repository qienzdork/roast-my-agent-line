"""Roast Your Own Agent entry.

Writes one original, single-line roast of my own AI agent to
<OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

ROAST = "I asked my agent to roast itself; it drafted fourteen candidates, ranked them, and picked the one that flatters it most."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
