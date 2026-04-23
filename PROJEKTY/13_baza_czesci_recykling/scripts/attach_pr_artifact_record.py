#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any


PACK_ID = "pack-project13-kaggle-enrichment-01"
PROJECT_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
RECORDS_DIR = PROJECT_DIR / "execution_packs" / PACK_ID / "records"
RUN_CONTEXT_PATH = (
    PROJECT_DIR / "autonomous_test" / "reports" / "last_pack_run_context.json"
)
CREATE_RECORDS_SCRIPT = PROJECT_DIR / "scripts" / "create_execution_records.py"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_branch_ref(output_refs: list[str]) -> tuple[str | None, str | None]:
    for ref in output_refs:
        if not ref.startswith("branch://"):
            continue
        remainder = ref.removeprefix("branch://")
        owner, _, branch_name = remainder.partition("/")
        if owner and branch_name:
            return owner, branch_name
    return None, None


def extract_timestamp_slug(run_id: str) -> str | None:
    match = re.search(r"(\d{8}T\d{6}Z)$", run_id)
    if match:
        return match.group(1)
    return None


def discover_run_record(
    records_dir: Path, *, run_id: str | None, fork_owner: str | None
) -> Path:
    candidate_paths = sorted(records_dir.glob("run-project13-kaggle-enrichment-*.json"))
    scored_candidates: list[tuple[str, Path]] = []

    for path in candidate_paths:
        payload = load_json(path)
        if payload.get("pack_id") != PACK_ID:
            continue
        if run_id and payload.get("run_id") != run_id:
            continue
        if not run_id:
            if payload.get("environment_kind") != "kaggle":
                continue
            if payload.get("operator_kind") != "hybrid_team":
                continue

        if fork_owner:
            owner, _ = parse_branch_ref(payload.get("output_refs", []))
            if owner != fork_owner:
                continue

        sort_key = payload.get("started_at") or payload.get("ended_at") or path.name
        scored_candidates.append((sort_key, path))

    if not scored_candidates:
        criteria = []
        if run_id:
            criteria.append(f"run_id={run_id}")
        if fork_owner:
            criteria.append(f"fork_owner={fork_owner}")
        detail = ", ".join(criteria) if criteria else "latest kaggle/hybrid_team run"
        raise SystemExit(f"Nie znaleziono rekordu Run dla kryterium: {detail}")

    scored_candidates.sort(key=lambda item: item[0])
    return scored_candidates[-1][1]


def run_json_command(command: list[str], *, cwd: Path) -> dict[str, Any]:
    result = subprocess.run(
        command,
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    stdout = result.stdout.strip().splitlines()
    if not stdout:
        return {}
    return json.loads(stdout[-1])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dopina Artifact record do istniejacego Run po otwarciu PR dla execution packa Project 13. "
        "Domyslnie korzysta z last_pack_run_context.json, jesli nie podano --run-id ani --fork-owner."
    )
    parser.add_argument("--pr-url", required=True)
    parser.add_argument(
        "--run-context",
        type=Path,
        help="Sciezka do trwalego pliku last_pack_run_context.json wygenerowanego przez finalizer. Jesli nie podano, skrypt sprobuje uzyc domyslnej sciezki.",
    )
    parser.add_argument(
        "--run-id",
        help="Jawny run_id. Jesli brak, skrypt sprobuje znalezc najnowszy kaggle run albo uzyc run context.",
    )
    parser.add_argument(
        "--run-record", type=Path, help="Sciezka do konkretnego rekordu Run."
    )
    parser.add_argument(
        "--fork-owner",
        help="Opcjonalny filtr dla autodiscovery, np. login wolontariusza.",
    )
    parser.add_argument("--records-dir", type=Path, default=RECORDS_DIR)
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Opcjonalny katalog docelowy dla nowego Artifact record.",
    )
    parser.add_argument("--artifact-kind", default="pull_request")
    parser.add_argument(
        "--artifact-title",
        default="PR z artefaktami Project 13 po uruchomieniu KaggleNotebookPack",
    )
    parser.add_argument(
        "--artifact-summary",
        default="Artefakt zawiera provenance do packa, runu i raportu przebiegu.",
    )
    parser.add_argument("--artifact-review-status", default="review_ready")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records_dir = args.records_dir.resolve()
    run_context_ref = None
    run_context_payload = None

    if args.run_context:
        run_context_path = args.run_context.resolve()
        run_context_payload = load_json(run_context_path)
        run_context_ref = (
            str(run_context_path.relative_to(REPO_ROOT))
            if run_context_path.is_relative_to(REPO_ROOT)
            else str(run_context_path)
        )

    inferred_run_id = args.run_id or (run_context_payload or {}).get("run_id")
    inferred_fork_owner = args.fork_owner or (run_context_payload or {}).get(
        "fork_owner"
    )
    inferred_task_id = (run_context_payload or {}).get("task_id")
    inferred_pack_id = (run_context_payload or {}).get("pack_id", PACK_ID)

    if args.run_record:
        run_record_path = args.run_record.resolve()
    elif run_context_payload and run_context_payload.get("run_record_ref"):
        run_record_path = (REPO_ROOT / run_context_payload["run_record_ref"]).resolve()
    elif not args.run_id and not args.fork_owner and RUN_CONTEXT_PATH.exists():
        run_context_payload = load_json(RUN_CONTEXT_PATH)
        run_context_ref = str(RUN_CONTEXT_PATH.relative_to(REPO_ROOT))
        inferred_run_id = run_context_payload.get("run_id")
        inferred_fork_owner = run_context_payload.get("fork_owner")
        inferred_task_id = run_context_payload.get("task_id")
        inferred_pack_id = run_context_payload.get("pack_id", PACK_ID)
        run_record_path = (REPO_ROOT / run_context_payload["run_record_ref"]).resolve()
    else:
        run_record_path = discover_run_record(
            records_dir,
            run_id=inferred_run_id,
            fork_owner=inferred_fork_owner,
        )

    run_payload = load_json(run_record_path)
    run_id = run_payload["run_id"]
    timestamp_slug = extract_timestamp_slug(run_id)
    if not timestamp_slug:
        raise SystemExit(f"Nie udalo sie wyciagnac timestamp slug z run_id={run_id}")

    discovered_owner, branch_name = parse_branch_ref(run_payload.get("output_refs", []))
    fork_owner = inferred_fork_owner or discovered_owner
    if not fork_owner:
        raise SystemExit(
            "Nie udalo sie ustalic fork_owner. Podaj --fork-owner albo zapewnij branch://... w Run output_refs."
        )

    command = [
        "python3",
        str(CREATE_RECORDS_SCRIPT),
        "--fork-owner",
        fork_owner,
        "--existing-run-id",
        run_id,
        "--timestamp-slug",
        timestamp_slug,
        "--artifact-storage-ref",
        args.pr_url,
        "--artifact-kind",
        args.artifact_kind,
        "--artifact-title",
        args.artifact_title,
        "--artifact-summary",
        args.artifact_summary,
        "--artifact-review-status",
        args.artifact_review_status,
    ]
    if args.output_dir:
        command.extend(["--output-dir", str(args.output_dir.resolve())])

    result = run_json_command(command, cwd=REPO_ROOT)
    artifact_record_path = Path(result["artifact_record"])

    print(
        json.dumps(
            {
                "status": "ok",
                "run_id": run_id,
                "run_record_ref": str(run_record_path.resolve().relative_to(REPO_ROOT)),
                "run_context_ref": run_context_ref,
                "fork_owner": fork_owner,
                "branch_name": branch_name,
                "artifact_record_ref": str(
                    artifact_record_path.resolve().relative_to(REPO_ROOT)
                )
                if artifact_record_path.is_relative_to(REPO_ROOT)
                else str(artifact_record_path.resolve()),
                "pr_url": args.pr_url,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
