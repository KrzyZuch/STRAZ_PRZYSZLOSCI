#!/usr/bin/env python3
"""Sync organization_agent_v1 entity records from repo JSON files to local SQLite.

Reads canonical records from:
  - data/sample/organization_*.json
  - PROJEKTY/*/execution_packs/*/records/*.json

Applies migration 0012_organization_agent_entities.sql and upserts records
into the corresponding tables with promoted columns + payload_json.

Usage:
  python3 pipelines/sync_organization_entities_to_sqlite.py --db-path /tmp/org.sqlite3
  python3 pipelines/sync_organization_entities_to_sqlite.py --db-path /tmp/org.sqlite3 --dry-run
"""

import argparse
import glob as glob_mod
import json
import os
import sqlite3
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MIGRATION_PATH = os.path.join(
    REPO_ROOT, "cloudflare", "migrations", "0012_organization_agent_entities.sql"
)

SAMPLE_DIR = os.path.join(REPO_ROOT, "data", "sample")

RECORDS_GLOB = os.path.join(
    REPO_ROOT, "PROJEKTY", "*", "execution_packs", "*", "records", "*.json"
)

ENTITY_KIND_TABLE = {
    "resource_record": "organization_resource_records",
    "potential_dossier": "organization_potential_dossiers",
    "capability_gap": "organization_capability_gaps",
    "experiment": "organization_experiments",
    "execution_pack": "organization_execution_packs",
    "task": "organization_tasks",
    "run": "organization_runs",
    "artifact": "organization_artifacts",
    "integrity_risk_assessment": "organization_integrity_risk_assessments",
    "approval": "organization_approvals",
    "readiness_gate": "organization_readiness_gates",
}

FILENAME_PREFIX_TO_KIND = {
    "organization_resource_record": "resource_record",
    "organization_potential_dossier": "potential_dossier",
    "organization_capability_gap": "capability_gap",
    "organization_experiment": "experiment",
    "organization_execution_pack": "execution_pack",
    "organization_task": "task",
    "organization_run": "run",
    "organization_artifact": "artifact",
    "organization_integrity_risk_assessment": "integrity_risk_assessment",
    "organization_approval": "approval",
    "organization_readiness_gate": "readiness_gate",
}

TABLE_PROMOTED_COLUMNS = {
    "organization_resource_records": [
        ("resource_id", "resource_id"),
        ("schema_version", "schema_version"),
        ("resource_kind", "resource_kind"),
        ("title", "title"),
        ("discovery_channel", "discovery_channel"),
        ("access_model", "access_model"),
        ("status", "status"),
        ("availability_pattern", "availability_pattern"),
        ("expected_leverage", "expected_leverage"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("discovered_at", "discovered_at"),
        ("last_reviewed_at", "last_reviewed_at"),
    ],
    "organization_potential_dossiers": [
        ("dossier_id", "dossier_id"),
        ("schema_version", "schema_version"),
        ("title", "title"),
        ("target_domain", "target_domain"),
        ("candidate_status", "candidate_status"),
        ("overall_priority_score", "overall_priority_score"),
        ("recommended_action", "recommended_action"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("created_at", "created_at"),
        ("updated_at", "updated_at"),
    ],
    "organization_capability_gaps": [
        ("gap_id", "gap_id"),
        ("schema_version", "schema_version"),
        ("dossier_id", "dossier_id"),
        ("title", "title"),
        ("gap_kind", "gap_kind"),
        ("severity", "severity"),
        ("status", "status"),
        ("blocking_reason", "blocking_reason"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("created_at", "created_at"),
        ("updated_at", "updated_at"),
    ],
    "organization_experiments": [
        ("experiment_id", "experiment_id"),
        ("schema_version", "schema_version"),
        ("gap_id", "gap_id"),
        ("status", "status"),
        ("hypothesis", "hypothesis"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("created_at", "created_at"),
        ("updated_at", "updated_at"),
    ],
    "organization_execution_packs": [
        ("pack_id", "pack_id"),
        ("schema_version", "schema_version"),
        ("title", "title"),
        ("linked_subject_kind", "linked_subject.entity_kind"),
        ("linked_subject_id", "linked_subject.entity_id"),
        ("execution_mode", "execution_mode"),
        ("target_output_kind", "target_output_kind"),
        ("status", "status"),
        ("notebook_path", "notebook_path"),
        ("runbook_path", "runbook_path"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("created_at", "created_at"),
        ("updated_at", "updated_at"),
    ],
    "organization_tasks": [
        ("task_id", "task_id"),
        ("schema_version", "schema_version"),
        ("pack_id", "pack_id"),
        ("assignee_mode", "assignee_mode"),
        ("requested_by", "requested_by"),
        ("status", "status"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("created_at", "created_at"),
        ("updated_at", "updated_at"),
    ],
    "organization_runs": [
        ("run_id", "run_id"),
        ("schema_version", "schema_version"),
        ("task_id", "task_id"),
        ("pack_id", "pack_id"),
        ("operator_kind", "operator_kind"),
        ("environment_kind", "environment_kind"),
        ("status", "status"),
        ("logs_ref", "logs_ref"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("started_at", "started_at"),
        ("ended_at", "ended_at"),
    ],
    "organization_artifacts": [
        ("artifact_id", "artifact_id"),
        ("schema_version", "schema_version"),
        ("run_id", "run_id"),
        ("artifact_kind", "artifact_kind"),
        ("title", "title"),
        ("storage_ref", "storage_ref"),
        ("review_status", "review_status"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("created_at", "created_at"),
        ("updated_at", "updated_at"),
    ],
    "organization_integrity_risk_assessments": [
        ("assessment_id", "assessment_id"),
        ("schema_version", "schema_version"),
        ("subject_kind", "subject.entity_kind"),
        ("subject_id", "subject.entity_id"),
        ("assessment_scope", "assessment_scope"),
        ("risk_level", "risk_level"),
        ("status", "status"),
        ("reviewer_role", "reviewer_role"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("assessed_at", "assessed_at"),
    ],
    "organization_approvals": [
        ("approval_id", "approval_id"),
        ("schema_version", "schema_version"),
        ("artifact_id", "artifact_id"),
        ("decision", "decision"),
        ("approval_scope", "approval_scope"),
        ("reviewer_role", "reviewer_role"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("decided_at", "decided_at"),
    ],
    "organization_readiness_gates": [
        ("gate_id", "gate_id"),
        ("schema_version", "schema_version"),
        ("subject_kind", "subject.entity_kind"),
        ("subject_id", "subject.entity_id"),
        ("gate_kind", "gate_kind"),
        ("status", "status"),
        ("source_ref", "source_ref"),
        ("payload_json", None),
        ("checked_at", "checked_at"),
    ],
}


def resolve_nested_key(record, dotted_key):
    parts = dotted_key.split(".")
    val = record
    for part in parts:
        if isinstance(val, dict) and part in val:
            val = val[part]
        else:
            return None
    return val


def extract_promoted_values(record, columns_spec):
    values = []
    for _col_name, json_key in columns_spec:
        if json_key is None:
            values.append(json.dumps(record, ensure_ascii=False, sort_keys=True))
        else:
            val = resolve_nested_key(record, json_key)
            values.append(val)
    return values


def detect_entity_kind_from_sample(filepath):
    basename = os.path.basename(filepath)
    for prefix, kind in FILENAME_PREFIX_TO_KIND.items():
        if basename.startswith(prefix + ".") or basename.startswith(prefix + "-"):
            return kind
    return None


def detect_entity_kind_from_records(filepath):
    basename = os.path.basename(filepath)
    if basename.startswith("run-"):
        return "run"
    if basename.startswith("artifact-"):
        return "artifact"
    return None


def load_sample_records():
    records = []
    pattern = os.path.join(SAMPLE_DIR, "organization_*.json")
    for filepath in sorted(glob_mod.glob(pattern)):
        kind = detect_entity_kind_from_sample(filepath)
        if kind is None:
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            records.append((kind, data, filepath))
        except Exception as exc:
            print(f"WARN: cannot load {filepath}: {exc}", file=sys.stderr)
    return records


def load_execution_pack_records():
    records = []
    for filepath in sorted(glob_mod.glob(RECORDS_GLOB)):
        kind = detect_entity_kind_from_records(filepath)
        if kind is None:
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            records.append((kind, data, filepath))
        except Exception as exc:
            print(f"WARN: cannot load {filepath}: {exc}", file=sys.stderr)
    return records


def apply_migration(conn):
    if not os.path.exists(MIGRATION_PATH):
        print(f"ERROR: migration file not found: {MIGRATION_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(MIGRATION_PATH, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()


def build_upsert_sql(table, columns_spec):
    col_names = [col for col, _ in columns_spec]
    placeholders = ", ".join("?" for _ in col_names)
    col_list = ", ".join(col_names)
    pk_col = col_names[0]
    update_cols = [c for c in col_names if c != pk_col]
    update_clause = ", ".join(f"{c} = excluded.{c}" for c in update_cols)
    return (
        f"INSERT INTO {table} ({col_list}) VALUES ({placeholders}) "
        f"ON CONFLICT({pk_col}) DO UPDATE SET {update_clause}"
    )


SYNC_ORDER = [
    "resource_record",
    "potential_dossier",
    "capability_gap",
    "experiment",
    "execution_pack",
    "task",
    "run",
    "artifact",
    "integrity_risk_assessment",
    "approval",
    "readiness_gate",
]


def sync_records(conn, entity_records, dry_run=False):
    counts = {}
    skipped = []
    by_kind = {}
    for kind, record, filepath in entity_records:
        by_kind.setdefault(kind, []).append((kind, record, filepath))

    for kind in SYNC_ORDER:
        batch = by_kind.get(kind, [])
        if not batch:
            continue
        table = ENTITY_KIND_TABLE[kind]
        columns_spec = TABLE_PROMOTED_COLUMNS[table]

        for _kind, record, filepath in batch:
            pk_col = columns_spec[0][0]
            pk_json_key = columns_spec[0][1]
            pk_val = resolve_nested_key(record, pk_json_key)
            if pk_val is None:
                skipped.append((filepath, f"missing primary key {pk_col}"))
                continue

            values = extract_promoted_values(record, columns_spec)

            if dry_run:
                counts.setdefault(table, 0)
                counts[table] += 1
                print(f"  [dry-run] {table}: upsert {pk_col}={pk_val}")
                continue

            sql = build_upsert_sql(table, columns_spec)
            try:
                conn.execute(sql, values)
                counts.setdefault(table, 0)
                counts[table] += 1
            except Exception as exc:
                skipped.append((filepath, str(exc)))

    if not dry_run:
        conn.commit()

    return counts, skipped


def main():
    parser = argparse.ArgumentParser(
        description="Sync organization_agent_v1 entity records to local SQLite"
    )
    parser.add_argument(
        "--db-path",
        required=True,
        help="Path to local SQLite database file (created if not exists)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be upserted without writing to the database",
    )
    parser.add_argument(
        "--skip-migration",
        action="store_true",
        help="Skip applying migration 0012 (use if tables already exist)",
    )
    args = parser.parse_args()

    entity_records = []
    print("Loading sample records from data/sample/ ...")
    sample = load_sample_records()
    print(f"  Found {len(sample)} sample records")
    entity_records.extend(sample)

    print("Loading execution pack records ...")
    ep_records = load_execution_pack_records()
    print(f"  Found {len(ep_records)} execution pack records")
    entity_records.extend(ep_records)

    total = len(entity_records)
    print(f"Total records to sync: {total}")

    if args.dry_run:
        print("\n--- DRY RUN (no database writes) ---")
        counts, skipped = sync_records(None, entity_records, dry_run=True)
    else:
        db_dir = os.path.dirname(os.path.abspath(args.db_path))
        os.makedirs(db_dir, exist_ok=True)

        conn = sqlite3.connect(args.db_path)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")

        if not args.skip_migration:
            print(f"\nApplying migration {os.path.basename(MIGRATION_PATH)} ...")
            apply_migration(conn)
            print("  Migration applied")

        print("\nSyncing records ...")
        counts, skipped = sync_records(conn, entity_records)
        conn.close()

    print("\n=== Sync Report ===")
    for table, count in sorted(counts.items()):
        print(f"  {table}: {count} records")

    if skipped:
        print(f"\nSkipped {len(skipped)} records:")
        for filepath, reason in skipped:
            print(f"  {os.path.basename(filepath)}: {reason}")

    if not args.dry_run:
        print(f"\nDatabase: {args.db_path}")
        print("Verifying record counts ...")
        conn = sqlite3.connect(args.db_path)
        for table in sorted(TABLE_PROMOTED_COLUMNS.keys()):
            try:
                row = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
                print(f"  {table}: {row[0]} rows")
            except Exception as exc:
                print(f"  {table}: ERROR {exc}")
        conn.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
