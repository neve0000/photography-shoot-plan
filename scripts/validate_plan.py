#!/usr/bin/env python3
"""Validate a structured photography shot plan before board rendering."""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


REQUIRED_CARD_FIELDS = (
    "id",
    "section",
    "title",
    "image",
    "shot_size",
    "camera_line",
    "light_line",
    "cue_line",
)

LINE_RULES = {
    "camera_line": ("机位｜", 46),
    "light_line": ("光线｜", 50),
    "cue_line": ("口令｜", 54),
}


def display_width(value: str) -> int:
    """Return an approximate monospace display width for mixed CJK text."""
    width = 0
    for char in value:
        if unicodedata.combining(char):
            continue
        width += 2 if unicodedata.east_asian_width(char) in {"W", "F", "A"} else 1
    return width


def coverage_families(shot_size: str) -> set[str]:
    """Map a free-form Chinese shot-size label to broad coverage families."""
    families: set[str] = set()
    if "环境" in shot_size or "远景" in shot_size:
        families.add("environment")
    if "动态" in shot_size or "运动" in shot_size:
        families.add("movement")
    if "全身" in shot_size:
        families.add("full")
    if any(token in shot_size for token in ("七分", "中景", "半身", "低位")):
        families.add("medium")
    if any(token in shot_size for token in ("近景", "特写", "细节")):
        families.add("close")
    return families


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_plan(plan: Any) -> tuple[list[str], list[str]]:
    """Return structural errors and review warnings for a shot-plan object."""
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(plan, dict):
        return ["root: expected a JSON object"], warnings

    if not nonempty_string(plan.get("title")):
        errors.append("root.title: required non-empty string")

    columns = plan.get("columns")
    if isinstance(columns, bool) or not isinstance(columns, int) or not 1 <= columns <= 6:
        errors.append("root.columns: expected an integer from 1 to 6")
        columns = None

    rows = plan.get("rows")
    if rows is not None and (isinstance(rows, bool) or not isinstance(rows, int) or rows < 1):
        errors.append("root.rows: expected a positive integer when provided")
        rows = None

    shots = plan.get("shots")
    if not isinstance(shots, list) or not shots:
        errors.append("root.shots: expected a non-empty list")
        return errors, warnings

    if columns is not None:
        if len(shots) % columns:
            errors.append(
                f"root.shots: {len(shots)} cards do not fill a {columns}-column grid"
            )
        expected_rows = math.ceil(len(shots) / columns)
        if rows is not None and rows != expected_rows:
            errors.append(
                f"root.rows: declared {rows}, expected {expected_rows} for "
                f"{len(shots)} cards and {columns} columns"
            )

    seen_images: dict[str, int] = {}
    seen_titles: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    families: set[str] = set()
    online_sources_required = plan.get("references_collected_online") is True

    for index, shot in enumerate(shots, start=1):
        label = f"shots[{index - 1}]"
        if not isinstance(shot, dict):
            errors.append(f"{label}: expected an object")
            continue

        for field in REQUIRED_CARD_FIELDS:
            if not nonempty_string(shot.get(field)):
                errors.append(f"{label}.{field}: required non-empty string")

        expected_id = f"{index:02d}"
        if shot.get("id") != expected_id:
            errors.append(f"{label}.id: expected {expected_id!r}")

        image = shot.get("image")
        if nonempty_string(image):
            if image in seen_images:
                errors.append(
                    f"{label}.image: duplicates shots[{seen_images[image] - 1}].image"
                )
            else:
                seen_images[image] = index

        title = shot.get("title")
        if nonempty_string(title):
            seen_titles[title] += 1
            if display_width(title) > 28:
                warnings.append(f"{label}.title: may be too long for one card line")

        shot_size = shot.get("shot_size")
        if nonempty_string(shot_size):
            mapped = coverage_families(shot_size)
            families.update(mapped)
            if not mapped:
                warnings.append(
                    f"{label}.shot_size: {shot_size!r} is not mapped to a coverage family"
                )

        for field, (prefix, width_limit) in LINE_RULES.items():
            line = shot.get(field)
            if not nonempty_string(line):
                continue
            if not line.startswith(prefix):
                errors.append(f"{label}.{field}: must begin with {prefix!r}")
            width = display_width(line)
            if width > width_limit:
                warnings.append(
                    f"{label}.{field}: display width {width} exceeds {width_limit}; "
                    "review at final card size"
                )

        source_url = shot.get("source_url")
        if nonempty_string(source_url):
            source_counts[source_url] += 1
        elif online_sources_required:
            warnings.append(f"{label}.source_url: missing canonical online source")

        risk_tags = shot.get("risk_tags", [])
        if risk_tags is None:
            risk_tags = []
        if not isinstance(risk_tags, list) or not all(
            nonempty_string(tag) for tag in risk_tags
        ):
            errors.append(f"{label}.risk_tags: expected a list of non-empty strings")
        elif risk_tags and not nonempty_string(shot.get("cancel_condition")):
            warnings.append(
                f"{label}.cancel_condition: required for elevated-risk shot "
                f"({', '.join(risk_tags)})"
            )

    for title, count in seen_titles.items():
        if count > 1:
            warnings.append(f"shots.title: {title!r} is repeated {count} times")

    if len(shots) >= 12 and len(families) < 4:
        warnings.append(
            "coverage: plans with at least 12 cards should normally cover at least "
            "four broad families; found " + ", ".join(sorted(families))
        )

    for source_url, count in source_counts.items():
        if len(shots) >= 12 and count > 3:
            warnings.append(
                f"source diversity: one source contributes {count} cards ({source_url})"
            )

    return errors, warnings


def valid_fixture() -> dict[str, Any]:
    shots = []
    sizes = ["环境", "全身", "近景"]
    for index, size in enumerate(sizes, start=1):
        shots.append(
            {
                "id": f"{index:02d}",
                "section": size,
                "title": f"测试镜头{index}",
                "image": f"image-{index}.webp",
                "shot_size": size,
                "camera_line": "机位｜眼平 · 50mm",
                "light_line": "光线｜柔和侧光",
                "cue_line": "口令｜站稳—转肩—看镜头—停",
            }
        )
    return {"title": "测试策划", "columns": 3, "rows": 1, "shots": shots}


def run_self_test() -> int:
    cases: list[tuple[str, dict[str, Any], str | None]] = []
    cases.append(("valid", valid_fixture(), None))

    missing = valid_fixture()
    del missing["shots"][0]["camera_line"]
    cases.append(("missing-field", missing, "camera_line"))

    duplicate = valid_fixture()
    duplicate["shots"][1]["image"] = duplicate["shots"][0]["image"]
    cases.append(("duplicate-image", duplicate, "duplicates"))

    wrong_rows = valid_fixture()
    wrong_rows["rows"] = 2
    cases.append(("wrong-row-count", wrong_rows, "declared 2"))

    failures = []
    for name, fixture, expected_error in cases:
        errors, _ = validate_plan(copy.deepcopy(fixture))
        if expected_error is None and errors:
            failures.append(f"{name}: expected no errors, got {errors}")
        elif expected_error is not None and not any(
            expected_error in error for error in errors
        ):
            failures.append(
                f"{name}: expected an error containing {expected_error!r}, got {errors}"
            )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print(f"PASS: {len(cases)} validator self-tests")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a JSON photography shot plan before board rendering."
    )
    parser.add_argument("plan", nargs="?", help="Path to shot-plan.json")
    parser.add_argument(
        "--strict", action="store_true", help="Return non-zero when warnings exist"
    )
    parser.add_argument(
        "--format", choices=("text", "json"), default="text", dest="output_format"
    )
    parser.add_argument(
        "--self-test", action="store_true", help="Run built-in validator tests"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test:
        return run_self_test()
    if not args.plan:
        print("error: plan path is required unless --self-test is used", file=sys.stderr)
        return 2

    plan_path = Path(args.plan)
    try:
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"error: plan not found: {plan_path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as error:
        print(f"error: invalid JSON at line {error.lineno}: {error.msg}", file=sys.stderr)
        return 2

    errors, warnings = validate_plan(plan)
    if args.output_format == "json":
        print(
            json.dumps(
                {
                    "ok": not errors and not (args.strict and warnings),
                    "errors": errors,
                    "warnings": warnings,
                    "shot_count": len(plan.get("shots", []))
                    if isinstance(plan, dict)
                    else 0,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for error in errors:
            print(f"ERROR: {error}")
        for warning in warnings:
            print(f"WARN: {warning}")
        if not errors and not warnings:
            print(f"PASS: {len(plan['shots'])} cards validated")
        elif not errors:
            print(f"PASS WITH WARNINGS: {len(plan['shots'])} cards validated")

    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
