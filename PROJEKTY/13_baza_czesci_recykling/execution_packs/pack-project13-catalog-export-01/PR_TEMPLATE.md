## Pack

- `pack_id`: `pack-project13-catalog-export-01`
- `source_catalog_revision`:

## Run Provenance

- `operator_kind`:
- `branch_name`:
- `command`: `python3 PROJEKTY/13_baza_czesci_recykling/scripts/build_catalog_artifacts.py export-all`
- `validation_command`: `python3 PROJEKTY/13_baza_czesci_recykling/scripts/build_catalog_artifacts.py validate`

## Outputs

- [ ] `data/inventory.csv`
- [ ] `data/recycled_parts_seed.sql`
- [ ] `data/mcp_reuse_catalog.json`
- [ ] `data/inventree_import.jsonl`

## What Changed

- liczba zmienionych donor devices:
- liczba zmienionych canonical parts:
- najwazniejsze zmiany downstream:

## Known Issues

- 

## Integrity Notes

- [ ] export pochodzi z reviewowanego katalogu GitHub-first
- [ ] nie bylo recznej edycji wygenerowanych plikow downstream
- [ ] walidacja katalogu przeszla przed otwarciem PR
- [ ] PR nie miesza exportu z discovery albo OCR
