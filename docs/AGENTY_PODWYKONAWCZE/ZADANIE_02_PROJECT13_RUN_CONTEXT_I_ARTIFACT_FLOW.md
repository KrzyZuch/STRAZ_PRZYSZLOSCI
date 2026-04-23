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

### Wynik mini-handoffu (2026-04-23)

#### Gdzie lezy run context

`PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/last_pack_run_context.json`

Plik jest generowany automatycznie przez `finalize_execution_pack_run.py` (run rzeczywisty) oraz `dry_run_execution_pack.py` (dry-run lokalny). Ostatni zapisany kontekst pochodzi z dry-runu `20260422T210903Z` (`dry_run: true`). Zawiera: `pack_id`, `task_id`, `fork_owner`, `branch_name`, `run_id`, `run_ref`, `run_status`, `summary_ref`, `run_record_ref`, `artifact_record_ref`, `artifact_follow_up_command`, `generated_at`, `dry_run`.

#### Jak zmienil sie follow-up do Artifact

Wczesniej: dopiecie Artifact wymagalo recznego odtworzenia `run_id`, fork_owner i sciezek z logow.

Teraz: `attach_pr_artifact_record.py` obsluguje **domyslny tryb `--pr-url` z run context**. Trzy tryby odkrycia Run:

1. `--run-context <path>` — czyta `last_pack_run_context.json` (domyslna sciezka: `PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/last_pack_run_context.json`)
2. `--run-id <id>` + opcjonalnie `--fork-owner`
3. Autodiscovery — skanuje `records/` i wybiera najnowszy Run matching fork_owner

Polecenie follow-up jest gotowe w polu `artifact_follow_up_command` run context, np.:

```
python3 PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py \
  --run-context PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/last_pack_run_context.json \
  --pr-url https://github.com/StrazPrzyszlosci/STRAZ_PRZYSZLOSCI/pull/<numer>
```

#### Jakie walidacje przeszly

- `python3 PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py` — **22/22 checkow PASS**, status overall: `pass` (dry-run `20260422T210903Z`)
- `python3 -m py_compile` na `finalize_execution_pack_run.py` i `attach_pr_artifact_record.py` — bez bledow
- Smoke-test finalizera (`finalize_execution_pack_run.py` z `--git-mode none`) — Run `20260422T190657Z`, status `needs_review` (local smoke, nie Kaggle)
- Walidacja outputow: 82 test_db records, 74 inventree/ecoEDA accepted, 5 skipped z audit trail

#### Co zostalo jeszcze polautomatyczne

**Dopiecie Artifact nadal wymaga recznego podania URL PR** (`--pr-url`). Skrypt `attach_pr_artifact_record.py` nie:

- nie otwiera PR automatycznie (to celowe — PR wymaga ludzkiego review przed merge),
- nie wykrywa URL PR z CI/env (brak integracji z GitHub API do listowania otwartych PR),
- nie jest wywolywany automatycznie po finalizerze — to osobny, celowy krok w RUNBOOK (krok 9).

Zatem przeplyw jest: **Run -> finalizer (automatyczny) -> otwarcie PR (reczne) -> dopiecie Artifact (polautomatyczne: `--pr-url` reczne, reszta z run context automatyczna)**.
