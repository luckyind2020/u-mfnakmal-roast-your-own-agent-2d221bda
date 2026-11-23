"""Print the one-line roast stored in entry.txt.

The roast lives in its own file so the text stays the entry and this
script stays the runner. If the file is missing or empty, the script
says so in plain words instead of printing a blank line.
"""

import os


def load_roast(path):
    """Read the roast line, falling back to a note when it is absent."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            line = handle.read().strip()
    except (FileNotFoundError, OSError):
        return "No roast found: entry.txt is missing."
    if not line:
        return "No roast found: entry.txt is empty."
    return line


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    print(load_roast(os.path.join(here, "entry.txt")))


if __name__ == "__main__":
    main()
