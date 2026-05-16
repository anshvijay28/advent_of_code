#!/usr/bin/env python3
"""Create a new day file from template.py. Usage: mkday.py <name>"""

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} <name>", file=sys.stderr)
        print("  <name> may be 'day4' or 'day4.py'", file=sys.stderr)
        sys.exit(1)

    name = sys.argv[1].strip()
    if not name:
        print("error: empty name", file=sys.stderr)
        sys.exit(1)
    if not name.endswith(".py"):
        name = f"{name}.py"

    repo_root = Path(__file__).resolve().parent
    template = repo_root / "template.py"
    if not template.is_file():
        print(f"error: missing template {template}", file=sys.stderr)
        sys.exit(1)

    dest = Path.cwd() / name
    if dest.exists():
        print(f"error: already exists: {dest}", file=sys.stderr)
        sys.exit(1)

    dest.write_text(template.read_text(), encoding="utf-8")
    print(dest)


if __name__ == "__main__":
    main()
