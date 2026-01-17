#!/usr/bin/env python3
"""
TEOS Institutional ZIP Packager
- Bundles /docs, /demos, /dashboards, /governance (and optional /briefs, /diagrams, /integrations, /modules)
- Includes key root files (README.md, LICENSE.md, ROADMAP.md, SECURITY.md) if present
- Produces a single ZIP suitable for offline institutional review

Usage:
  python scripts/package_institutional_zip.py
  python scripts/package_institutional_zip.py --name TEOS_Egypt_SovereignStack_v1.0 --out dist
  python scripts/package_institutional_zip.py --include-all
"""

from __future__ import annotations

import argparse
import os
import sys
import zipfile
from datetime import datetime
from pathlib import Path

DEFAULT_INCLUDE = [
    "docs",
    "demos",
    "dashboards",
    "governance",
]

OPTIONAL_INCLUDE = [
    "briefs",
    "diagrams",
    "integrations",
    "modules",
]

ROOT_FILES = [
    "README.md",
    "LICENSE.md",
    "ROADMAP.md",
    "SECURITY.md",
]

DEFAULT_EXCLUDE_DIRS = {
    ".git",
    ".github",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
}

DEFAULT_EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".DS_Store",
}


def iter_files(repo_root: Path, rel_dir: str) -> list[Path]:
    base = repo_root / rel_dir
    if not base.exists() or not base.is_dir():
        return []

    files: list[Path] = []
    for p in base.rglob("*"):
        if p.is_dir():
            # Skip excluded directories anywhere in path
            if any(part in DEFAULT_EXCLUDE_DIRS for part in p.parts):
                continue
            continue

        if any(part in DEFAULT_EXCLUDE_DIRS for part in p.parts):
            continue

        if p.suffix in DEFAULT_EXCLUDE_SUFFIXES:
            continue

        # Skip very large binaries if any accidentally exist
        try:
            if p.stat().st_size > 50 * 1024 * 1024:  # 50MB
                continue
        except OSError:
            continue

        files.append(p)
    return files


def safe_write(zipf: zipfile.ZipFile, repo_root: Path, file_path: Path) -> None:
    # Store paths inside ZIP relative to repo root
    arcname = file_path.relative_to(repo_root).as_posix()
    zipf.write(file_path, arcname=arcname)


def main() -> int:
    parser = argparse.ArgumentParser(description="Package TEOS institutional ZIP bundle.")
    parser.add_argument(
        "--name",
        default="TEOS-Egypt-SovereignStack-2026_v1.0_Sovereign-Reference",
        help="Base name for the ZIP (without .zip).",
    )
    parser.add_argument(
        "--out",
        default="dist",
        help="Output directory for ZIP.",
    )
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Include optional folders (briefs/diagrams/integrations/modules) in addition to defaults.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    out_dir = repo_root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    # Add a date stamp for traceability (safe for institutions)
    date_tag = datetime.utcnow().strftime("%Y%m%d")
    zip_name = f"{args.name}_{date_tag}.zip"
    zip_path = out_dir / zip_name

    include_dirs = list(DEFAULT_INCLUDE)
    if args.include_all:
        include_dirs.extend(OPTIONAL_INCLUDE)

    # Collect files
    files_to_add: list[Path] = []

    # Root files
    for rf in ROOT_FILES:
        p = repo_root / rf
        if p.exists() and p.is_file():
            files_to_add.append(p)

    # Included directories
    for d in include_dirs:
        files_to_add.extend(iter_files(repo_root, d))

    if not files_to_add:
        print("No files found to package. Ensure the repo has content committed.", file=sys.stderr)
        return 2

    # Deterministic ordering
    files_to_add = sorted(set(files_to_add), key=lambda p: p.as_posix())

    # Create ZIP
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for fp in files_to_add:
            safe_write(zipf, repo_root, fp)

    print(f"Created: {zip_path.relative_to(repo_root).as_posix()}")
    print(f"Included folders: {', '.join(include_dirs)}")
    print("Included root files:", ", ".join([f for f in ROOT_FILES if (repo_root / f).exists()]))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
