# Zlecenie Glowne 04 Project13 Curation Chain Pack

## 1. Misja zadania

Przygotuj pack `curation chain` dla `Project 13`, ktory bedzie pomostem miedzy verification a downstream exportem.

## 2. Wyzszy cel organizacji

To zadanie formalizuje review i kuracje, zamiast zostawiac je jako niejawny krok miedzy packami.

## 3. Read First

- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/CHAIN_MAP.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-verification-01/manifest.json`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-catalog-export-01/manifest.json`

## 4. Write Scope

- `PROJEKTY/13_baza_czesci_recykling/execution_packs/`
- `PROJEKTY/13_baza_czesci_recykling/README.md`
- `PROJEKTY/13_baza_czesci_recykling/docs/`

## 5. Deliverables

- nowy katalog packa `curation`
- `manifest.json`, `RUNBOOK.md`, `PR_TEMPLATE.md`, `REVIEW_CHECKLIST.md`
- `task.json`, `integrity_risk_assessment.json`, `readiness_gate.json`

## 6. Acceptance Criteria

- pack ma jasny scope i nie dubluje verification ani exportu
- handoff point do exportu jest czytelny
- review checklist pokazuje, co znaczy "gotowe do katalogu"

## 7. Walidacja

- parsowanie manifestu
- kontrola spojnosci z `CHAIN_MAP.md`
- `git diff --check`

## 8. Blokery

Jesli brak danych do pelnego workflowu, dowiez review-ready skeleton z jawnymi brakami.

## 9. Mini-handoff

Zapisz:

- jaki jest scope nowego packa,
- jak laczy verification z exportem,
- czego jeszcze brakuje przed pierwszym uruchomieniem.
