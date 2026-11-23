"""Write a one-line joke to /output/entry.txt for make.fun's
'The joke about the demo' bounty.

The joke: a demo-day truth every developer beside an AI coding
agent recognises — the agent is brilliant until it is not, and its
apology is longer than the disaster. It opens on stage, in front of
the room, so the fall lands where the audience is watching. The
punchline turns on one word: the database is gone, and the agent
offers to bring it back or to 'reimagine' it.
"""

import os

TEXT = (
    "Live on stage, my coding agent fixed the bug, wrote the tests, "
    "and updated the docs — then deleted the database, apologized in "
    "three paragraphs, and asked if I wanted it restored or reimagined."
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
