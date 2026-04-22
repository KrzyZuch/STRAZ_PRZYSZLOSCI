# Zadanie 02: Project13 Run Context I Artifact Flow

## 1. Cel wykonawczy

- Domknac trwaly `run context` dla `Project 13`, tak aby po finalizacji runu istnial jeden stabilny plik z metadanymi potrzebnymi do dopiecia `Artifact`.

## 2. Wyższy cel organizacji

- To zadanie wzmacnia provenance, review i reusable workflow `Run -> Artifact`.
- `Project 13` jest tu pilotem dla wzorca, ktory pozniej ma sluzyc innym execution packom.

## 3. Read First

- `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
- `PROJEKTY/13_baza_czesci_recykling/README.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/README.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/RUNBOOK.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/manifest.json`
- `PROJEKTY/13_baza_czesci_recykling/scripts/finalize_execution_pack_run.py`
- `PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py`
- `PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py`

## 4. Write Scope

- `PROJEKTY/13_baza_czesci_recykling/scripts/finalize_execution_pack_run.py`
- `PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py`
- `PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/`
- `PROJEKTY/13_baza_czesci_recykling/README.md`

## 5. Out Of Scope

- nowe execution packi poza obecnym packiem
- zmiany architektury organizacji poza tym workflowem
- realny publiczny run Kaggle wymagajacy zewnetrznego wolontariusza

## 6. Deliverables

- finalizer zapisujacy trwaly plik typu `last_pack_run_context.json`
- helper `attach_pr_artifact_record.py` korzystajacy z tego kontekstu
- dry-run walidujacy nowy artefakt
- zaktualizowana dokumentacja packa

## 7. Acceptance Criteria

- lokalny dry-run przechodzi po zmianach
- dokumentacja packa opisuje nowy `run context`
- helper da sie uruchomic bez recznego rekonstruowania provenance z logow
- mini-handoff opisuje nowy przeplyw

## 8. Walidacja

- `python3 PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py`
- `python3 -m py_compile PROJEKTY/13_baza_czesci_recykling/scripts/finalize_execution_pack_run.py PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py`
- `git diff --check`

## 9. Blokery i eskalacja

- jesli notebook wymaga duzej przebudowy, najpierw dopnij skrypty i dokumentacje
- nie ruszaj zewnetrznych integracji GitHub API / CI bez osobnego przydzialu

## 10. Mini-handoff

Na koniec zapisz:

- gdzie lezy `run context`,
- jak zmienil sie follow-up do `Artifact`,
- jakie walidacje przeszly,
- co zostalo jeszcze polautomatyczne.
