from __future__ import annotations

import re
import sys
from pathlib import Path


def check_albucore_version(filename: str) -> int:
    with Path(filename).open() as file:
        content = file.read()

    # Look for albucore in pyproject.toml dependencies
    match = re.search(r'albucore\s*=\s*"([^"]*)"', content)
    if not match:
        print(f"Error: albucore not found in {filename}")
        return 1

    albucore_version = match[1]
    if not re.match(r"\d+\.\d+\.\d+$", albucore_version):
        print(f"Error: albucore version must be exact (no operators) in {filename}. Found: {albucore_version}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(check_albucore_version("pyproject.toml"))
