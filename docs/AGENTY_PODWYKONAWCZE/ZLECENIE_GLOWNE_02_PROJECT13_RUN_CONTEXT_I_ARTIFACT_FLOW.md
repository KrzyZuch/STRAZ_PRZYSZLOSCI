# Zlecenie Glowne 02 Project13 Run Context I Artifact Flow

## 1. Misja zadania

Domknij trwaly `run context` dla `Project 13`, tak aby po finalizacji runu istnial jeden stabilny plik z metadanymi potrzebnymi do dopiecia `Artifact`.

## 2. Wyzszy cel organizacji

To zadanie wzmacnia provenance i reusable workflow `Run -> Artifact`, ktory pozniej ma sluzyc tez innym execution packom.

## 3. Read First

- `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
- `PROJEKTY/13_baza_czesci_recykling/README.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/README.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/RUNBOOK.md`
- `PROJEKTY/13_baza_czesci_recykling/scripts/finalize_execution_pack_run.py`
- `PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py`
- `PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py`

## 4. Write Scope

- `PROJEKTY/13_baza_czesci_recykling/scripts/`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/`
- `PROJEKTY/13_baza_czesci_recykling/README.md`

## 5. Deliverables

- trwaly plik `run context`
- helper `Artifact` korzystajacy z tego kontekstu
- dry-run potwierdzajacy nowy kontrakt
- mini-handoff z opisem nowego przeplywu

## 6. Acceptance Criteria

- finalizer zapisuje `run context`
- helper `attach_pr_artifact_record.py` umie z niego skorzystac
- dry-run przechodzi po zmianach
- dokumentacja packa opisuje nowy kontrakt

## 7. Walidacja

- `python3 PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py`
- `python3 -m py_compile PROJEKTY/13_baza_czesci_recykling/scripts/finalize_execution_pack_run.py PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py`
- `git diff --check`

## 8. Blokery

Jesli notebook wymaga zbyt duzej przebudowy, najpierw dopnij skrypty i dokumentacje, a brakujacy element zostaw jawnie opisany.

## 9. Mini-handoff

Zapisz:

- gdzie lezy `run context`,
- jak teraz dopina sie `Artifact`,
- jakie walidacje przeszly,
- co nadal zostalo polautomatyczne.
