# Mini-handoff: Sync Encji Organizacji Do D1 SQLite

## Co zostalo zrobione

Stworzono skrypt projekcyjny `pipelines/sync_organization_entities_to_sqlite.py`, ktory czyta kanoniczne rekordy organizacji z repo i robi upsert do tabel zgodnych z migracja `0012_organization_agent_entities.sql`.

## Jak uruchomic sync

```bash
python3 pipelines/sync_organization_entities_to_sqlite.py --db-path /tmp/organization_agent_v1.sqlite3
```

Opcje CLI:
- `--db-path` (wymagany): sciezka do lokalnej bazy SQLite
- `--dry-run`: pokazuje co zostaloby upsertowane bez zapisu do bazy
- `--skip-migration`: pomija aplikowanie migracji 0012 (gdy tabele juz istnieja)

## Jakie encje sa obslugiwane

Wszystkie 11 encji z `organization_agent_v1`:

| Encja | Tabela | Sample records | EP records |
|---|---|---|---|
| ResourceRecord | organization_resource_records | 1 | 0 |
| PotentialDossier | organization_potential_dossiers | 1 | 0 |
| CapabilityGap | organization_capability_gaps | 1 | 0 |
| Experiment | organization_experiments | 1 | 0 |
| ExecutionPack | organization_execution_packs | 1 | 0 |
| Task | organization_tasks | 1 | 0 |
| Run | organization_runs | 1 | 10 |
| Artifact | organization_artifacts | 1 | 9 |
| IntegrityRiskAssessment | organization_integrity_risk_assessments | 1 | 0 |
| Approval | organization_approvals | 1 | 0 |
| ReadinessGate | organization_readiness_gates | 1 | 0 |

Zrodla danych:
- `data/sample/organization_*.json` (11 plikow)
- `PROJEKTY/*/execution_packs/*/records/*.json` (19 plikow: 10 Run, 9 Artifact)

## Jakie walidacje przeszly

- `python3 -m py_compile pipelines/sync_organization_entities_to_sqlite.py` — OK
- lokalny run na testowej bazie `/tmp/organization_agent_v1.sqlite3` — 30 rekordow, 0 skipped
- rekordy trafiaja do odpowiednich tabel z promoted kolumnami i `payload_json`
- `git diff --check` — OK (brak problemow z bialymi znakami)
- `--dry-run` dziala bez zapisu do bazy
- ponowny run robi upsert (idempotentny)

## Co nadal wymaga dopracowania

- **Brak kanonicznych rekordow poza sample**: poza `data/sample/` i execution pack records nie ma stabilnego katalogu rekordow kanonicznych dla innych encji (np. CapabilityGap, Experiment, Approval poza sample)
- **Wariant D1**: skrypt dziala tylko na lokalnej SQLite; nie ma jeszcze wariantu synchronizacji do realnego Cloudflare D1
- **Query layer**: nie ma jeszcze prostych lookupow dla agentow i review
- **Walidacja schematu**: skrypt nie waliduje rekordow JSON przeciw `schemas/organization_agent_v1.yaml`; tylko mapuje znane kolumny i zapisuje payload_json
- **Inne zrodla rekordow**: mozna rozszerzyc o czytanie manifest.json execution packow jako zrodla ExecutionPack records

## Co powinien sprawdzic agent odbierajacy wynik

1. Uruchomic: `python3 pipelines/sync_organization_entities_to_sqlite.py --db-path /tmp/test.sqlite3`
2. Sprawdzic: `sqlite3 /tmp/test.sqlite3 "SELECT COUNT(*) FROM organization_runs;"` — powinno byc 11
3. Sprawdzic: `sqlite3 /tmp/test.sqlite3 "SELECT resource_id, title FROM organization_resource_records;"` — powinien byc 1 rekord
4. Sprawdzic: `sqlite3 /tmp/test.sqlite3 "SELECT payload_json FROM organization_execution_packs LIMIT 1;"` — powinno zawierac pelny JSON
