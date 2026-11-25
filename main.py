#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes exactly one patch-note line (127 characters, no trailing
newline) to /output/entry.txt, using only the Python standard library.
"""

import os

ENTRY = (
    "Patch 1.0.1: Humans now remember why they opened the fridge. "
    "Known issue: remembering why they entered a room is still in beta."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_contents(directory):
    """Remove the contents of the output folder, never the folder itself."""
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    os.remove(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
            os.rmdir(path)
        else:
            os.remove(path)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_contents(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
