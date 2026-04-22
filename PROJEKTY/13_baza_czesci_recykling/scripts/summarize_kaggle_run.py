#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_BASE_DIR = PROJECT_DIR / "autonomous_test"
DEFAULT_OUTPUT = DEFAULT_BASE_DIR / "reports" / "last_run_summary.md"


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def count_csv_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        rows = list(reader)
    if not rows:
        return 0
    return max(len(rows) - 1, 0)


def file_size_bytes(path: Path) -> int:
    if not path.exists():
        return 0
    return path.stat().st_size


def build_report(
    base_dir: Path,
    output_path: Path,
    *,
    pack_id: str | None = None,
    notebook_path: str | None = None,
    fork_owner: str | None = None,
    branch_name: str | None = None,
    run_ref: str | None = None,
) -> Path:
    results_dir = base_dir / "results"
    processed_path = base_dir / "processed_videos.json"
    test_db_path = results_dir / "test_db.jsonl"
    inventree_path = results_dir / "inventree_import.jsonl"
    ecoeda_path = results_dir / "ecoEDA_inventory.csv"

    processed_videos = []
    if processed_path.exists():
        processed_videos = json.loads(processed_path.read_text(encoding="utf-8"))

    test_records = load_jsonl(test_db_path)
    inventree_records = load_jsonl(inventree_path)
    ecoeda_rows = count_csv_rows(ecoeda_path)

    unique_devices = sorted({str(record.get("device", "")).strip() for record in test_records if record.get("device")})
    recent_parts = []
    for record in test_records[-10:]:
        recent_parts.append(
            {
                "device": record.get("device", "Unknown"),
                "part_number": record.get("part_number", "Unknown"),
                "source_video": record.get("source_video", ""),
            }
        )

    output_entries = [
        {
            "label": "processed_videos",
            "path": processed_path,
            "count": len(processed_videos),
            "count_label": "records",
        },
        {
            "label": "test_db",
            "path": test_db_path,
            "count": len(test_records),
            "count_label": "records",
        },
        {
            "label": "inventree_import",
            "path": inventree_path,
            "count": len(inventree_records),
            "count_label": "records",
        },
        {
            "label": "ecoeda_inventory",
            "path": ecoeda_path,
            "count": ecoeda_rows,
            "count_label": "rows",
        },
    ]

    missing_outputs = [entry for entry in output_entries if not entry["path"].exists()]
    empty_outputs = [
        entry
        for entry in output_entries
        if entry["path"].exists() and entry["count"] == 0
    ]

    report_lines = [
        "# Project 13 Kaggle Run Summary",
        "",
        f"- generated_at_utc: {datetime.now(timezone.utc).isoformat()}",
        f"- base_dir: {base_dir}",
        f"- pack_id: {pack_id or 'unknown'}",
        f"- notebook_path: {notebook_path or 'unknown'}",
        f"- fork_owner: {fork_owner or 'unknown'}",
        f"- branch_name: {branch_name or 'unknown'}",
        f"- run_ref: {run_ref or 'unknown'}",
        f"- processed_videos_count: {len(processed_videos)}",
        f"- test_db_records_count: {len(test_records)}",
        f"- inventree_records_count: {len(inventree_records)}",
        f"- ecoeda_rows_count: {ecoeda_rows}",
        f"- unique_devices_count: {len(unique_devices)}",
        "",
        "## Output Files",
        "",
    ]

    for entry in output_entries:
        relative_path = entry["path"].relative_to(PROJECT_DIR)
        report_lines.append(
            f"- {entry['label']}: {relative_path} | exists={entry['path'].exists()} | "
            f"{entry['count_label']}={entry['count']} | size_bytes={file_size_bytes(entry['path'])}"
        )

    report_lines.extend(
        [
        "",
        "## Recent Devices",
        "",
        ]
    )

    if unique_devices:
        report_lines.extend([f"- {device}" for device in unique_devices[:15]])
    else:
        report_lines.append("- none")

    report_lines.extend(["", "## Recent Parts", ""])
    if recent_parts:
        for part in recent_parts:
            report_lines.append(
                f"- {part['device']} :: {part['part_number']} :: {part['source_video']}"
            )
    else:
        report_lines.append("- none")

    report_lines.extend(
        [
            "",
            "## Known Limits",
            "",
            "- Summary pokazuje stan plikow roboczych po runie, nie rozroznia automatycznie tylko nowych rekordow z jednej sesji.",
            "- Reviewer powinien porownac report z diffem PR i z notebook logiem.",
        ]
    )

    if missing_outputs:
        report_lines.extend(
            [
                "",
                "## Missing Outputs",
                "",
            ]
        )
        for entry in missing_outputs:
            report_lines.append(f"- {entry['label']}: brak pliku {entry['path'].relative_to(PROJECT_DIR)}")

    if empty_outputs:
        report_lines.extend(
            [
                "",
                "## Empty Outputs",
                "",
            ]
        )
        for entry in empty_outputs:
            report_lines.append(
                f"- {entry['label']}: plik istnieje, ale ma {entry['count']} {entry['count_label']}"
            )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Buduje prosty raport markdown po runie Kaggle dla Project 13.")
    parser.add_argument("--base-dir", type=Path, default=DEFAULT_BASE_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--pack-id", default="pack-project13-kaggle-enrichment-01")
    parser.add_argument("--notebook-path", default="PROJEKTY/13_baza_czesci_recykling/youtube-databaseparts.ipynb")
    parser.add_argument("--fork-owner")
    parser.add_argument("--branch-name")
    parser.add_argument("--run-ref")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = build_report(
        args.base_dir.resolve(),
        args.output.resolve(),
        pack_id=args.pack_id,
        notebook_path=args.notebook_path,
        fork_owner=args.fork_owner,
        branch_name=args.branch_name,
        run_ref=args.run_ref,
    )
    print(json.dumps({"status": "ok", "output": str(output_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
