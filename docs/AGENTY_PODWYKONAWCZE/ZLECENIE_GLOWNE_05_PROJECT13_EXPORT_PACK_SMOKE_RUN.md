# Zlecenie Glowne 05 Project13 Export Pack Smoke Run

## 1. Misja zadania

Wykonaj pierwszy lokalny smoke run `pack-project13-catalog-export-01` i zostaw review-ready raport z wyniku.

## 2. Wyzszy cel organizacji

To zadanie zamienia pack `export chain` z samego kontraktu dokumentacyjnego w realnie sprawdzona jednostke pracy.

## 3. Read First

- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-catalog-export-01/manifest.json`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-catalog-export-01/RUNBOOK.md`
- `PROJEKTY/13_baza_czesci_recykling/scripts/build_catalog_artifacts.py`
- `PROJEKTY/13_baza_czesci_recykling/README.md`

## 4. Write Scope

- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-catalog-export-01/`
- ewentualnie `PROJEKTY/13_baza_czesci_recykling/README.md`
- ewentualnie raport w `docs/AGENTY_PODWYKONAWCZE/`

## 5. Deliverables

- raport smoke runu
- ewentualne poprawki manifestu, runbooka lub checklisty
- mini-handoff z wynikiem

## 6. Acceptance Criteria

- komenda exportu i walidacji przechodzi lokalnie albo ma jawnie opisany blocker
- raport pokazuje, co zadzialalo, a co nie
- pack po smoke runie jest bardziej operacyjny niz przed nim

## 7. Walidacja

- `python3 PROJEKTY/13_baza_czesci_recykling/scripts/build_catalog_artifacts.py export-all`
- `python3 PROJEKTY/13_baza_czesci_recykling/scripts/build_catalog_artifacts.py validate`
- `git diff --check`

## 8. Blokery

Jesli smoke run ujawni brakujacy kontrakt lub plik, opisz go jawnie i popraw tylko to, co niezbedne.

## 9. Mini-handoff

Zapisz:

- jakie komendy uruchomiono,
- co przeszlo,
- co nie przeszlo,
- jakie poprawki byly potrzebne.
