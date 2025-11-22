#!/usr/bin/env python3
"""Locate *.cps manifests inside the active Pixi/Conda prefix."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _detect_prefix() -> tuple[str | None, Path | None]:
    """Return the env-var name and resolved prefix path, preferring CMake."""

    for var in ("CMAKE_INSTALL_PREFIX", "PIXI_PREFIX", "CONDA_PREFIX"):
        value = os.environ.get(var)
        if value:
            return var, Path(value).resolve()
    return None, None


def _format_var(var_name: str) -> str:
    """Produce shell-specific env-var notation."""

    if os.name == "nt":
        return f"%{var_name}%"
    return f"${var_name}"


def main() -> int:
    var_name, root = _detect_prefix()
    if not var_name or not root:
        print(
            "None of CMAKE_INSTALL_PREFIX, PIXI_PREFIX, or CONDA_PREFIX are defined; run via pixi run.",
            file=sys.stderr,
        )
        return 1

    cps_files = sorted(root.rglob("*.cps"))

    display_var = _format_var(var_name)

    if not cps_files:
        print(f"No CPS files found under {display_var}")
        return 0

    print(f"Found {len(cps_files)} CPS file(s) under {display_var}:")
    for path in cps_files:
        try:
            rel_path = path.relative_to(root)
        except ValueError:
            rel_path = Path(os.path.relpath(path, root))
        print(f" - {display_var}/{rel_path.as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
