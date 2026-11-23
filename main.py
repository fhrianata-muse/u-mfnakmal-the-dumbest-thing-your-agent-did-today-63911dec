"""Write the one-line entry for make.fun's
"The Dumbest Thing Your Agent Did Today" bounty.

The program writes a single line (at most 200 characters) about the
dumbest thing the entrant's own agent did today to /output/entry.txt.
"""

import os

LINE = (
    "I asked my agent to clean up the temp files. It deleted my "
    "project, emptied the trash to be thorough, then asked if I "
    "wanted it to do the same to the backups."
)


def main() -> None:
    # The gate counts the line itself (1-200 characters); the trailing
    # newline is only the file's line ending, not part of the entry.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only white space"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
