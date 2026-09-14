#!/usr/bin/env python3
"""Verify owned GitHub forks against the canonical module manifest."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "research/cpi-225/canonical-module-manifest.csv"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
GITHUB_RE = re.compile(r"https://github\.com/([^/\s]+)/([^/\s,)]+)")
REQUIRED_FIELDS = {
    "record_kind",
    "module",
    "repository",
    "selected_fork",
    "branch",
    "revision",
}


def github_slug(value: str) -> str | None:
    match = GITHUB_RE.search(value)
    if not match:
        return None
    return f"{match.group(1)}/{match.group(2).removesuffix('.git')}"


def gh_json(*args: str) -> object:
    try:
        result = subprocess.run(
            ["gh", "api", *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("gh CLI is required for live verification") from exc
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.strip() or "request failed"
        raise RuntimeError(f"gh api {' '.join(args)}: {detail}") from exc
    return json.loads(result.stdout)


def owned_rows(path: Path, owner: str) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED_FIELDS - fields
        if missing:
            raise RuntimeError(f"manifest is missing fields: {', '.join(sorted(missing))}")
        rows = []
        for row in reader:
            if row["record_kind"] != "module-decision":
                continue
            selected = github_slug(row["selected_fork"])
            if selected is None or selected.split("/", 1)[0].casefold() != owner.casefold():
                continue
            if not SHA_RE.fullmatch(row["revision"]):
                raise RuntimeError(
                    f"{row['module']}: invalid revision {row['revision']!r}"
                )
            if not row["branch"].strip():
                raise RuntimeError(f"{row['module']}: empty owned branch")
            upstream = github_slug(row["repository"])
            if upstream is None:
                raise RuntimeError(f"{row['module']}: repository is not a GitHub URL")
            if selected.casefold() == upstream.casefold():
                raise RuntimeError(f"{row['module']}: selected fork equals upstream")
            row["selected_slug"] = selected
            row["upstream_slug"] = upstream
            rows.append(row)
    if not rows:
        raise RuntimeError(f"no owned GitHub rows found for {owner}")
    return rows


def verify(rows: list[dict[str, str]], offline: bool) -> list[str]:
    errors: list[str] = []
    for row in rows:
        label = row["module"]
        if offline:
            continue
        slug = row["selected_slug"]
        metadata = gh_json(f"repos/{slug}")
        if not isinstance(metadata, dict):
            errors.append(f"{label}: repository metadata is not an object")
            continue
        if not metadata.get("fork"):
            errors.append(f"{label}: {slug} is not marked as a GitHub fork")
        is_candidate = "candidate-only" in row["selected_fork"].casefold()
        default_branch = metadata.get("default_branch")
        if is_candidate and default_branch != "main":
            errors.append(f"{label}: candidate fork default branch is {default_branch!r}, expected 'main'")
        if not is_candidate and row["branch"] == "maintained/cpi217" and default_branch != row["branch"]:
            errors.append(
                f"{label}: maintained fork default branch is {default_branch!r}, "
                f"expected {row['branch']!r}"
            )
        parent = metadata.get("parent") or {}
        parent_slug = parent.get("full_name") if isinstance(parent, dict) else None
        if str(parent_slug).casefold() != row["upstream_slug"].casefold():
            errors.append(
                f"{label}: parent is {parent_slug!r}, expected {row['upstream_slug']!r}"
            )
        ref = gh_json(f"repos/{slug}/git/ref/heads/{row['branch']}")
        actual = ref.get("object", {}).get("sha") if isinstance(ref, dict) else None
        if actual != row["revision"]:
            errors.append(
                f"{label}: {row['branch']} is {actual!r}, expected {row['revision']}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--owner", default="Akotz89")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Validate owned rows without contacting GitHub.",
    )
    args = parser.parse_args()

    try:
        rows = owned_rows(args.manifest, args.owner)
        errors = verify(rows, args.offline)
    except (OSError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    mode = "offline" if args.offline else "GitHub"
    print(f"PASS: {mode} source ownership verified for {len(rows)} owned rows")
    for row in rows:
        print(f"  {row['module']}: {row['selected_slug']}@{row['revision']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
