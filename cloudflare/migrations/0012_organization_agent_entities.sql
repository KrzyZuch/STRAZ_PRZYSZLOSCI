-- Migration: 0012_organization_agent_entities.sql
-- Description: Add shared D1/SQLite projection tables for organization_agent_v1 entities

CREATE TABLE IF NOT EXISTS organization_resource_records (
    resource_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    resource_kind TEXT NOT NULL,
    title TEXT NOT NULL,
    discovery_channel TEXT NOT NULL,
    access_model TEXT,
    status TEXT NOT NULL,
    availability_pattern TEXT,
    expected_leverage TEXT,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    discovered_at TEXT NOT NULL,
    last_reviewed_at TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_org_resource_status
    ON organization_resource_records(status);

CREATE INDEX IF NOT EXISTS idx_org_resource_kind
    ON organization_resource_records(resource_kind);

CREATE INDEX IF NOT EXISTS idx_org_resource_leverage
    ON organization_resource_records(expected_leverage);

CREATE TABLE IF NOT EXISTS organization_potential_dossiers (
    dossier_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    title TEXT NOT NULL,
    target_domain TEXT NOT NULL,
    candidate_status TEXT NOT NULL,
    overall_priority_score REAL NOT NULL,
    recommended_action TEXT NOT NULL,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_org_dossier_status
    ON organization_potential_dossiers(candidate_status);

CREATE INDEX IF NOT EXISTS idx_org_dossier_domain
    ON organization_potential_dossiers(target_domain);

CREATE INDEX IF NOT EXISTS idx_org_dossier_priority
    ON organization_potential_dossiers(overall_priority_score);

CREATE TABLE IF NOT EXISTS organization_capability_gaps (
    gap_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    dossier_id TEXT NOT NULL,
    title TEXT NOT NULL,
    gap_kind TEXT NOT NULL,
    severity TEXT NOT NULL,
    status TEXT NOT NULL,
    blocking_reason TEXT,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dossier_id) REFERENCES organization_potential_dossiers(dossier_id)
);

CREATE INDEX IF NOT EXISTS idx_org_gap_dossier
    ON organization_capability_gaps(dossier_id);

CREATE INDEX IF NOT EXISTS idx_org_gap_status
    ON organization_capability_gaps(status);

CREATE INDEX IF NOT EXISTS idx_org_gap_kind
    ON organization_capability_gaps(gap_kind);

CREATE TABLE IF NOT EXISTS organization_experiments (
    experiment_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    gap_id TEXT NOT NULL,
    status TEXT NOT NULL,
    hypothesis TEXT NOT NULL,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gap_id) REFERENCES organization_capability_gaps(gap_id)
);

CREATE INDEX IF NOT EXISTS idx_org_experiment_gap
    ON organization_experiments(gap_id);

CREATE INDEX IF NOT EXISTS idx_org_experiment_status
    ON organization_experiments(status);

CREATE TABLE IF NOT EXISTS organization_execution_packs (
    pack_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    title TEXT NOT NULL,
    linked_subject_kind TEXT NOT NULL,
    linked_subject_id TEXT NOT NULL,
    execution_mode TEXT NOT NULL,
    target_output_kind TEXT NOT NULL,
    status TEXT NOT NULL,
    notebook_path TEXT,
    runbook_path TEXT,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_org_pack_status
    ON organization_execution_packs(status);

CREATE INDEX IF NOT EXISTS idx_org_pack_mode
    ON organization_execution_packs(execution_mode);

CREATE INDEX IF NOT EXISTS idx_org_pack_subject
    ON organization_execution_packs(linked_subject_kind, linked_subject_id);

CREATE TABLE IF NOT EXISTS organization_tasks (
    task_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    pack_id TEXT NOT NULL,
    assignee_mode TEXT NOT NULL,
    requested_by TEXT,
    status TEXT NOT NULL,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pack_id) REFERENCES organization_execution_packs(pack_id)
);

CREATE INDEX IF NOT EXISTS idx_org_task_pack
    ON organization_tasks(pack_id);

CREATE INDEX IF NOT EXISTS idx_org_task_status
    ON organization_tasks(status);

CREATE TABLE IF NOT EXISTS organization_runs (
    run_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    task_id TEXT NOT NULL,
    pack_id TEXT NOT NULL,
    operator_kind TEXT NOT NULL,
    environment_kind TEXT NOT NULL,
    status TEXT NOT NULL,
    logs_ref TEXT,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES organization_tasks(task_id),
    FOREIGN KEY (pack_id) REFERENCES organization_execution_packs(pack_id)
);

CREATE INDEX IF NOT EXISTS idx_org_run_task
    ON organization_runs(task_id);

CREATE INDEX IF NOT EXISTS idx_org_run_pack
    ON organization_runs(pack_id);

CREATE INDEX IF NOT EXISTS idx_org_run_status
    ON organization_runs(status);

CREATE INDEX IF NOT EXISTS idx_org_run_environment
    ON organization_runs(environment_kind);

CREATE TABLE IF NOT EXISTS organization_artifacts (
    artifact_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    run_id TEXT NOT NULL,
    artifact_kind TEXT NOT NULL,
    title TEXT NOT NULL,
    storage_ref TEXT NOT NULL,
    review_status TEXT NOT NULL,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (run_id) REFERENCES organization_runs(run_id)
);

CREATE INDEX IF NOT EXISTS idx_org_artifact_run
    ON organization_artifacts(run_id);

CREATE INDEX IF NOT EXISTS idx_org_artifact_review
    ON organization_artifacts(review_status);

CREATE INDEX IF NOT EXISTS idx_org_artifact_kind
    ON organization_artifacts(artifact_kind);

CREATE TABLE IF NOT EXISTS organization_integrity_risk_assessments (
    assessment_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    subject_kind TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    assessment_scope TEXT NOT NULL,
    risk_level TEXT NOT NULL,
    status TEXT NOT NULL,
    reviewer_role TEXT,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    assessed_at TEXT NOT NULL,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_org_integrity_subject
    ON organization_integrity_risk_assessments(subject_kind, subject_id);

CREATE INDEX IF NOT EXISTS idx_org_integrity_status
    ON organization_integrity_risk_assessments(status);

CREATE INDEX IF NOT EXISTS idx_org_integrity_level
    ON organization_integrity_risk_assessments(risk_level);

CREATE TABLE IF NOT EXISTS organization_approvals (
    approval_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    artifact_id TEXT NOT NULL,
    decision TEXT NOT NULL,
    approval_scope TEXT NOT NULL,
    reviewer_role TEXT NOT NULL,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    decided_at TEXT NOT NULL,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (artifact_id) REFERENCES organization_artifacts(artifact_id)
);

CREATE INDEX IF NOT EXISTS idx_org_approval_artifact
    ON organization_approvals(artifact_id);

CREATE INDEX IF NOT EXISTS idx_org_approval_decision
    ON organization_approvals(decision);

CREATE INDEX IF NOT EXISTS idx_org_approval_scope
    ON organization_approvals(approval_scope);

CREATE TABLE IF NOT EXISTS organization_readiness_gates (
    gate_id TEXT PRIMARY KEY,
    schema_version TEXT NOT NULL DEFAULT 'v1',
    subject_kind TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    gate_kind TEXT NOT NULL,
    status TEXT NOT NULL,
    source_ref TEXT,
    payload_json TEXT NOT NULL,
    checked_at TEXT NOT NULL,
    inserted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_org_gate_subject
    ON organization_readiness_gates(subject_kind, subject_id);

CREATE INDEX IF NOT EXISTS idx_org_gate_kind
    ON organization_readiness_gates(gate_kind);

CREATE INDEX IF NOT EXISTS idx_org_gate_status
    ON organization_readiness_gates(status);
