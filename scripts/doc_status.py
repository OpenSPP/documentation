#!/usr/bin/env python3
"""
Set and report per-page documentation status via Markdown YAML frontmatter.

This is intended for internal tracking of the documentation refresh, without
showing "V2" terminology in published content.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator


ALLOWED_STATUSES = ("unverified", "drafted", "validated")


@dataclass(frozen=True)
class Frontmatter:
    raw: str
    body: str


def _iter_markdown_files(
    root: Path,
    includes: list[str],
    excludes: list[str],
) -> Iterator[Path]:
    for path in root.rglob("*.md"):
        rel = path.relative_to(root).as_posix()
        if includes and not any(fnmatch.fnmatch(rel, pat) for pat in includes):
            continue
        if any(fnmatch.fnmatch(rel, pat) for pat in excludes):
            continue
        yield path


def _split_frontmatter(text: str) -> Frontmatter | None:
    # Commonmark frontmatter: starts with '---' at beginning of file.
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        # Allow files ending frontmatter with '---' on last line.
        if text.endswith("\n---\n") or text.endswith("\n---"):
            end = text.rfind("\n---")
        else:
            return None
    raw = text[: end + len("\n---\n")]
    body = text[end + len("\n---\n") :]
    return Frontmatter(raw=raw, body=body)


def _ensure_frontmatter_with_status(
    text: str,
    status: str,
    validated_against: str | None,
) -> str:
    fm = _split_frontmatter(text)
    status_key = "doc_status"
    root_key = "openspp"

    if fm is None:
        block_lines = ["---", f"{root_key}:", f"  {status_key}: {status}"]
        if validated_against:
            block_lines.append(f"  validated_against: {validated_against}")
        block_lines.append("---")
        return "\n".join(block_lines) + "\n\n" + text.lstrip("\n")

    front = fm.raw
    body = fm.body

    # If already present, replace value in-place.
    # Cases:
    # 1) openspp: { doc_status: ... }  (rare)
    # 2) openspp:\n  doc_status: ...
    # 3) doc_status at top-level (we still accept, but prefer nesting)
    lines = front.splitlines(keepends=True)

    def replace_line(prefix: str, new_line: str) -> bool:
        for i, line in enumerate(lines):
            if line.lstrip().startswith(prefix):
                # Preserve indentation to avoid noisy diffs.
                indent = line[: len(line) - len(line.lstrip())]
                lines[i] = indent + new_line + ("\n" if not new_line.endswith("\n") else "")
                return True
        return False

    # Try to replace nested field first.
    in_openspp = False
    openspp_indent = ""
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == f"{root_key}:":
            in_openspp = True
            openspp_indent = line[: len(line) - len(line.lstrip())]
            continue
        if in_openspp:
            # Stop if we reached a new top-level key or the end marker.
            if stripped == "---" or (line and not line.startswith(openspp_indent + " ")):
                in_openspp = False
                continue
            key_prefix = f"{status_key}:"
            if stripped.startswith(key_prefix):
                indent = line[: len(line) - len(line.lstrip())]
                lines[i] = f"{indent}{status_key}: {status}\n"
                if validated_against is not None:
                    # Replace or insert validated_against nearby.
                    _ = replace_line("validated_against:", f"validated_against: {validated_against}")
                return "".join(lines) + body

    # Replace top-level doc_status if present.
    if replace_line(f"{status_key}:", f"{status_key}: {status}"):
        return "".join(lines) + body

    # Otherwise, insert under openspp: if present, else append before end marker.
    for i, line in enumerate(lines):
        if line.strip() == f"{root_key}:":
            insert_at = i + 1
            indent = " " * (len(line) - len(line.lstrip()) + 2)
            lines.insert(insert_at, f"{indent}{status_key}: {status}\n")
            if validated_against:
                lines.insert(insert_at + 1, f"{indent}validated_against: {validated_against}\n")
            return "".join(lines) + body

    # Insert before closing '---' (last line of fm.raw is the closing marker).
    # We add a blank line before our block if frontmatter currently ends right away.
    closing_index = None
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == "---":
            closing_index = i
            break
    if closing_index is None:
        # Fallback: treat as no-frontmatter.
        return _ensure_frontmatter_with_status(body, status=status, validated_against=validated_against)

    lines.insert(closing_index, f"{root_key}:\n")
    lines.insert(closing_index + 1, f"  {status_key}: {status}\n")
    if validated_against:
        lines.insert(closing_index + 2, f"  validated_against: {validated_against}\n")
    return "".join(lines) + body


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def cmd_set(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    status = args.status
    validated_against = args.validated_against

    changed = 0
    scanned = 0

    for path in _iter_markdown_files(root, includes=args.include, excludes=args.exclude):
        scanned += 1
        old = _read_text(path)
        new = _ensure_frontmatter_with_status(old, status=status, validated_against=validated_against)
        if new != old:
            changed += 1
            if args.apply:
                _write_text(path, new)
            else:
                print(f"would update {path}")

    print(f"scanned={scanned} changed={changed} apply={args.apply}")
    return 0


def _extract_status(text: str) -> tuple[str | None, str | None]:
    fm = _split_frontmatter(text)
    if fm is None:
        return (None, None)
    status = None
    validated_against = None

    in_openspp = False
    for line in fm.raw.splitlines():
        stripped = line.strip()
        if stripped == "openspp:":
            in_openspp = True
            continue
        if in_openspp and stripped and not line.startswith(" "):
            in_openspp = False
        if in_openspp:
            if stripped.startswith("doc_status:"):
                status = stripped.split(":", 1)[1].strip() or None
            if stripped.startswith("validated_against:"):
                validated_against = stripped.split(":", 1)[1].strip() or None
        else:
            if stripped.startswith("doc_status:") and status is None:
                status = stripped.split(":", 1)[1].strip() or None
            if stripped.startswith("validated_against:") and validated_against is None:
                validated_against = stripped.split(":", 1)[1].strip() or None
    return (status, validated_against)


def cmd_report(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    rows: list[tuple[str, str, str]] = []

    for path in _iter_markdown_files(root, includes=args.include, excludes=args.exclude):
        rel = path.relative_to(root).as_posix()
        status, validated_against = _extract_status(_read_text(path))
        rows.append((rel, status or "missing", validated_against or ""))

    rows.sort(key=lambda r: (r[1], r[0]))

    if args.format == "tsv":
        print("path\tstatus\tvalidated_against")
        for rel, status, va in rows:
            print(f"{rel}\t{status}\t{va}")
        return 0

    # markdown
    lines: list[str] = []
    lines.append("# Documentation status report")
    lines.append("")
    lines.append("This report is generated from Markdown frontmatter fields:")
    lines.append("")
    lines.append("```yaml")
    lines.append("openspp:")
    lines.append("  doc_status: unverified | drafted | validated")
    lines.append("  validated_against: \"optional context\"")
    lines.append("```")
    lines.append("")
    lines.append("| Page | Status | Validated against |")
    lines.append("| --- | --- | --- |")
    for rel, status, va in rows:
        lines.append(f"| `{rel}` | `{status}` | `{va}` |")

    out = "\n".join(lines) + "\n"
    if args.output:
        out_path = Path(args.output).resolve()
        out_path.write_text(out, encoding="utf-8")
        print(f"wrote {out_path}")
    else:
        print(out)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track per-page documentation refresh status.")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parents[1] / "docs"),
        help="Root docs directory to scan (default: documentation/docs).",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Glob pattern(s) to include (relative to root), e.g. 'tutorial/**'.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[
            "modules/**",
            "_build/**",
        ],
        help="Glob pattern(s) to exclude (relative to root).",
    )

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_set = sub.add_parser("set", help="Add/update frontmatter status on matching pages.")
    p_set.add_argument("--status", choices=ALLOWED_STATUSES, required=True)
    p_set.add_argument(
        "--validated-against",
        default=None,
        help="Optional string written to openspp.validated_against.",
    )
    p_set.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to disk. Without this, runs in dry-run mode.",
    )
    p_set.set_defaults(func=cmd_set)

    p_report = sub.add_parser("report", help="Report current status for matching pages.")
    p_report.add_argument("--format", choices=("markdown", "tsv"), default="markdown")
    p_report.add_argument(
        "--output",
        default=None,
        help="Write report to this path (otherwise prints to stdout).",
    )
    p_report.set_defaults(func=cmd_report)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    # Normalize exclude defaults when user passes --exclude multiple times.
    if isinstance(args.exclude, list):
        args.exclude = [p for p in args.exclude if p]
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())

