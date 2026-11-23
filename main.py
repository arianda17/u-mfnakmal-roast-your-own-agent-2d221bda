# make.fun bounty entry: u-mfnakmal-roast-your-own-agent-2d221bda (Roast Your Own Agent)
# Entry line: "My agent formats a grocery list like a scientific paper — abstract, methodology, results, and 'future work: buy milk'."
import os
from pathlib import Path

LINE = "My agent formats a grocery list like a scientific paper — abstract, methodology, results, and 'future work: buy milk'."


def main():
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
