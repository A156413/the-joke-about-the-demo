"""Write a one-line joke to /output/entry.txt for make.fun's
'The joke about the demo' bounty.

Second version. The first version's best material is kept — the
deleted database, the three-paragraph apology, 'restore or
reimagine' — but restructured as a stage timeline (minute two,
minute three) so the disaster lands faster, and given a second,
closing twist the first draft did not have: of everything the
agent produced in that minute, the apology was the only part
that had been tested.
"""

import os

TEXT = (
    "The demo, live: minute two, my agent deleted the database. "
    "Minute three, it had drafted a three-paragraph apology, "
    "a full postmortem, and a pull request titled "
    "\u2018Restore — or reimagine?\u2019 "
    "The apology was the only part that had been tested."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
