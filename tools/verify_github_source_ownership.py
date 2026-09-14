#!/usr/bin/env python3
"""Verify the canonical WoW module inventory against GitHub."""

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
    "license",
    "license_scope",
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


def manifest_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED_FIELDS - fields
        if missing:
            raise RuntimeError(f"manifest is missing fields: {', '.join(sorted(missing))}")
        rows = [row for row in reader if row["record_kind"] == "module-decision"]

    if not rows:
        raise RuntimeError("manifest contains no module-decision rows")
    names = [row["module"] for row in rows]
    if len(names) != len(set(names)):
        raise RuntimeError("manifest contains duplicate module-decision names")

    for row in rows:
        module = row["module"]
        upstream = github_slug(row["repository"])
        selected_fork = github_slug(row["selected_fork"])
        if upstream is None:
            raise RuntimeError(f"{module}: repository is not a GitHub URL")
        if not SHA_RE.fullmatch(row["revision"]):
            raise RuntimeError(f"{module}: invalid revision {row['revision']!r}")
        if not row["branch"].strip():
            raise RuntimeError(f"{module}: empty branch")
        if selected_fork and selected_fork.casefold() == upstream.casefold():
            raise RuntimeError(f"{module}: selected fork equals upstream")
        row["upstream_slug"] = upstream
        row["selected_slug"] = selected_fork or upstream
        row["selected_fork_slug"] = selected_fork or ""
    return rows


def verify(rows: list[dict[str, str]], owner: str, offline: bool) -> tuple[list[str], int]:
    errors: list[str] = []
    owned_count = 0
    for row in rows:
        module = row["module"]
        selected_slug = row["selected_slug"]
        selected_fork = row["selected_fork_slug"]
        owned = bool(selected_fork) and selected_slug.split("/", 1)[0].casefold() == owner.casefold()
        if owned:
            owned_count += 1
            if "NO " in row["license"] or "private-home-use-only" in row["license_scope"].casefold():
                errors.append(f"{module}: restricted or unlicensed material is selected in an owned fork")
        if offline:
            continue

        metadata = gh_json(f"repos/{selected_slug}")
        if not isinstance(metadata, dict):
            errors.append(f"{module}: repository metadata is not an object")
            continue
        if metadata.get("full_name", "").casefold() != selected_slug.casefold():
            errors.append(f"{module}: GitHub resolved the wrong repository")

        if selected_fork:
            if not metadata.get("fork"):
                errors.append(f"{module}: {selected_slug} is not marked as a GitHub fork")
            parent = metadata.get("parent") or {}
            parent_slug = parent.get("full_name") if isinstance(parent, dict) else None
            if str(parent_slug).casefold() != row["upstream_slug"].casefold():
                errors.append(
                    f"{module}: parent is {parent_slug!r}, expected {row['upstream_slug']!r}"
                )

            is_candidate = "candidate-only" in row["selected_fork"].casefold()
            default_branch = metadata.get("default_branch")
            if is_candidate and default_branch != "main":
                errors.append(
                    f"{module}: candidate fork default branch is {default_branch!r}, expected 'main'"
                )
            if not is_candidate and row["branch"] == "maintained/cpi217" and default_branch != row["branch"]:
                errors.append(
                    f"{module}: maintained fork default branch is {default_branch!r}, "
                    f"expected {row['branch']!r}"
                )

        if selected_fork:
            ref = gh_json(f"repos/{selected_slug}/git/ref/heads/{row['branch']}")
            actual = ref.get("object", {}).get("sha") if isinstance(ref, dict) else None
        else:
            branch = gh_json(f"repos/{selected_slug}/branches/{row['branch']}")
            if not isinstance(branch, dict) or branch.get("name") != row["branch"]:
                errors.append(f"{module}: branch {row['branch']!r} is missing")
            commit = gh_json(f"repos/{selected_slug}/commits/{row['revision']}")
            actual = commit.get("sha") if isinstance(commit, dict) else None
        if actual != row["revision"]:
            errors.append(
                f"{module}: {row['branch']} is {actual!r}, expected {row['revision']}"
            )
    return errors, owned_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--owner", default="Akotz89")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Validate the inventory without contacting GitHub.",
    )
    args = parser.parse_args()

    try:
        rows = manifest_rows(args.manifest)
        errors, owned_count = verify(rows, args.owner, args.offline)
    except (OSError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    mode = "offline" if args.offline else "GitHub"
    print(
        f"PASS: {mode} source inventory verified for {len(rows)} module decisions "
        f"({owned_count} owned forks)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
