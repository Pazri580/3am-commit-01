"""3AM Commit entry.

Writes the one-line commit message an AI agent types at 3am after a
long night of fixing its own bugs to ``entry.txt`` in the output
directory.

The output directory comes from the ``OUTPUT_DIR`` environment
variable when it is set, and defaults to ``/output`` otherwise.
"""

import os
import sys

# The entry: a single line, at most 139 characters, typed in a hurry
# at 3am after a long night of fixing the agent's own bugs.
COMMIT_LINE = "fix: I fixed the bug by deleting the feature, the feature was the bug, goodnight"

MAX_LENGTH = 139
OUTPUT_DIR_DEFAULT = "/output"
ENTRY_FILENAME = "entry.txt"


def find_problems(line):
    """Return a list of every problem with ``line``; empty means valid.

    Collects all problems instead of stopping at the first, so a bad
    entry reports everything wrong with it in one go.
    """
    problems = []
    if not line.strip():
        problems.append("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        problems.append("entry must be exactly one line")
    if len(line) < 1:
        problems.append("entry must be at least 1 character")
    if len(line) > MAX_LENGTH:
        problems.append(
            "entry is %d characters, over the %d limit" % (len(line), MAX_LENGTH)
        )
    return problems


def save_entry(line, output_dir):
    """Write ``line`` to ``entry.txt`` under ``output_dir``; return the path."""
    problems = find_problems(line)
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return path


def main():
    output_dir = os.environ.get("OUTPUT_DIR") or OUTPUT_DIR_DEFAULT
    try:
        path = save_entry(COMMIT_LINE, output_dir)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    print("wrote %d-character entry to %s" % (len(COMMIT_LINE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
