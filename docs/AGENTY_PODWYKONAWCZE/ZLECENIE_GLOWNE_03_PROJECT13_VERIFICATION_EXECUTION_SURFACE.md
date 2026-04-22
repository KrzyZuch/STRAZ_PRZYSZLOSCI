# Zlecenie Glowne 03 Project13 Verification Execution Surface

## 1. Misja zadania

Zmien `pack-project13-kaggle-verification-01` z samego szkieletu dokumentacyjnego w realny execution surface: osobny notebook, tryb notebooka albo stabilny skrypt uruchomieniowy.

## 2. Wyzszy cel organizacji

To zadanie oddziela `verification chain` od `enrichment`, dzieki czemu lancuch robi sie bardziej reviewowalny i bardziej modularny.

## 3. Read First

- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/CHAIN_MAP.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-verification-01/manifest.json`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-verification-01/RUNBOOK.md`
- `PROJEKTY/13_baza_czesci_recykling/youtube-databaseparts.ipynb`

## 4. Write Scope

- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-verification-01/`
- `PROJEKTY/13_baza_czesci_recykling/scripts/`
- ewentualnie nowy notebook lub wydzielony tryb notebooka

## 5. Deliverables

- realny execution surface dla verification
- zaktualizowany manifest i runbook
- jasny input i output contract
- mini-handoff z opisem brakow do pierwszego realnego runu

## 6. Acceptance Criteria

- verification nie jest juz tylko opisem
- istnieje realny punkt uruchomienia packa
- output verified/disagreement jest jawnie zdefiniowany
- pack nadal nie miesza verification z exportem downstream

## 7. Walidacja

- parsowanie manifestu
- walidacja lokalna wybranego execution surface
- `git diff --check`

## 8. Blokery

Jesli nie da sie jeszcze wydzielic calosci, dowiez przynajmniej review-ready stub wykonawczy z jawnymi brakami.

## 9. Mini-handoff

Zapisz:

- co jest execution surface,
- jak go uruchomic,
- jakie outputy produkuje,
- co nadal blokuje pierwszy publiczny run.
