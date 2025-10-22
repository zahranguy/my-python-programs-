# This is completely ai im not smart enought to make this lol

"""Generator for bestoddorevenever.py

Usage:
    python3 generate_bestoddorevenever.py [max_number] [output_path]

Defaults:
    max_number: 10000
    output_path: ./bestoddorevenever.py

This script writes a Python file that contains explicit `if a == n: print("odd"/"even")`
blocks for every n from 1..max_number. It's intentionally inefficient to match the user's style.
"""
import sys
from pathlib import Path


def generate(max_n: int = 10000, output: str = "bestoddorevenever.py") -> None:
    out_path = Path(output)
    with out_path.open("w", encoding="utf-8") as f:
        f.write("a = input()\n")
        f.write("try:\n")
        f.write("\ta = int(a)\n")
        f.write("except Exception:\n")
        f.write("\tprint(\"this is not a number\")\n")
        f.write("\texit()\n\n")

        for n in range(1, max_n + 1):
            parity = "even" if n % 2 == 0 else "odd"
            # keep user-style indentation: some lines used a tab, some used spaces earlier
            f.write(f"if a == {n}:\n")
            f.write(f"\tprint(\"{parity}\")\n")

    print(f"Wrote {out_path} with explicit if-blocks up to {max_n}.")


if __name__ == "__main__":
    max_n = 10000
    out = "bestoddorevenever.py"
    if len(sys.argv) > 1:
        try:
            max_n = int(sys.argv[1])
        except Exception:
            print("First argument must be an integer max value. Using default 10000.")
    if len(sys.argv) > 2:
        out = sys.argv[2]
    generate(max_n, out)
