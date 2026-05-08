import sys
import os
import re


PUBLIC_TABLES = {
    "d1_migrations",
    "schema_migrations",
    "datasheets",
    "recycled_devices",
    "recycled_parts",
    "recycled_part_master",
    "recycled_device_parts",
    "recycled_device_aliases",
    "recycled_part_aliases",
    "recycled_device_evidence",
}

PRIVATE_TABLES = {
    "_cf_kv",
    "events",
    "injection_audit_log",
    "observations",
    "olx_offer_parts_xref",
    "olx_offer_photos",
    "olx_offer_tags",
    "olx_offers",
    "olx_price_history",
    "olx_scan_batches",
    "organization_approvals",
    "organization_artifacts",
    "organization_capability_gaps",
    "organization_execution_packs",
    "organization_experiments",
    "organization_integrity_risk_assessments",
    "organization_potential_dossiers",
    "organization_readiness_gates",
    "organization_resource_records",
    "organization_runs",
    "organization_tasks",
    "providers",
    "recommendations",
    "recycled_device_submissions",
    "telegram_chat_limits",
    "telegram_chat_messages",
    "telegram_issue_moderation_audit",
    "telegram_issue_throttle",
    "telegram_issues",
    "telegram_user_sessions",
    "user_sessions",
}

SQL_IDENTIFIER = r'"?([a-zA-Z_][a-zA-Z0-9_]*)"?'
INDEX_IDENTIFIER = r'"?[a-zA-Z_][a-zA-Z0-9_]*"?'

TABLE_PATTERNS = [
    re.compile(
        r'^\s*CREATE\s+(?:VIRTUAL\s+)?TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?'
        + SQL_IDENTIFIER,
        re.IGNORECASE,
    ),
    re.compile(r'^\s*INSERT\s+INTO\s+' + SQL_IDENTIFIER, re.IGNORECASE),
    re.compile(r'^\s*ALTER\s+TABLE\s+' + SQL_IDENTIFIER, re.IGNORECASE),
    re.compile(r'^\s*DELETE\s+FROM\s+' + SQL_IDENTIFIER, re.IGNORECASE),
    re.compile(
        r'^\s*DROP\s+TABLE\s+(?:IF\s+EXISTS\s+)?' + SQL_IDENTIFIER,
        re.IGNORECASE,
    ),
    re.compile(
        r'^\s*CREATE\s+(?:UNIQUE\s+)?INDEX\s+(?:IF\s+NOT\s+EXISTS\s+)?'
        + INDEX_IDENTIFIER
        + r'\s+ON\s+'
        + SQL_IDENTIFIER,
        re.IGNORECASE,
    ),
]

PRAGMA_PATTERN = re.compile(r'^\s*PRAGMA\s+', re.IGNORECASE)
TRANSACTION_PATTERN = re.compile(
    r'^\s*(BEGIN(?:\s+TRANSACTION)?|COMMIT|ROLLBACK)(?:\s*;|\s|$)',
    re.IGNORECASE,
)


def extract_table_name(line):
    for pattern in TABLE_PATTERNS:
        match = pattern.search(line)
        if match:
            return match.group(1).lower()
    return None


def route_for_table(table_name):
    if not table_name:
        return "both"
    if table_name in PUBLIC_TABLES:
        return "public"
    if table_name in PRIVATE_TABLES:
        return "private"
    return "private"


def split_sql(input_file, public_output, private_output):
    public_lines = []
    private_lines = []

    current_table = None

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            table_name = extract_table_name(line)
            if table_name:
                current_table = table_name

            transaction_match = TRANSACTION_PATTERN.match(line)
            pragma_match = PRAGMA_PATTERN.match(line)

            is_meta = bool(transaction_match or pragma_match)

            if is_meta:
                public_lines.append(line)
                private_lines.append(line)
                continue

            route = route_for_table(current_table)
            if route == "both":
                public_lines.append(line)
                private_lines.append(line)
            elif route == "public":
                public_lines.append(line)
            elif route == "private":
                private_lines.append(line)

    public_sql = "PRAGMA foreign_keys = OFF;\nBEGIN TRANSACTION;\n" + "".join(public_lines) + "COMMIT;\n"
    private_sql = "PRAGMA foreign_keys = OFF;\nBEGIN TRANSACTION;\n" + "".join(private_lines) + "COMMIT;\n"

    with open(public_output, 'w', encoding='utf-8') as f:
        f.write(public_sql)

    with open(private_output, 'w', encoding='utf-8') as f:
        f.write(private_sql)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python split_d1_backup.py <input.sql> <public.sql> <private.sql>")
        sys.exit(1)
    
    split_sql(sys.argv[1], sys.argv[2], sys.argv[3])
