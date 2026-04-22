# Zlecenie Glowne 09 D1 SQLite Query Cookbook

## 1. Misja zadania

Przygotuj cookbook zapytan i lookupow dla warstwy `D1/SQLite` po tym, jak podwykonawca z zadania `01` dowiezie sync encji.

## 2. Wyzszy cel organizacji

To zadanie zamienia sama baze i sync na realne narzedzie operacyjne dla maintainerow i agentow.

## 3. Read First

- `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
- wynik zadania `01`
- `cloudflare/migrations/0012_organization_agent_entities.sql`

## 4. Write Scope

- `docs/`
- ewentualnie `cloudflare/` lub `pipelines/`, jesli potrzebny bedzie maly helper query-only

## 5. Deliverables

- dokument cookbooka z przykladowymi zapytaniami
- opcjonalny lekki helper do uruchamiania najwazniejszych lookupow
- mini-handoff z lista najbardziej przydatnych query

## 6. Acceptance Criteria

- cookbook pokazuje, jak pytac o stan encji, packow, runow i approval
- query sa zgodne z realna migracja `0012`
- dokument przydaje sie glownego agentowi przy odbiorze i portfelowym review

## 7. Walidacja

- lokalne odpalenie query na bazie z zadania `01`
- `git diff --check`

## 8. Blokery

To zadanie zalezy od wyniku `01`. Jesli sync nie istnieje albo jest wadliwy, nie omijaj tego przez wymyslanie fikcyjnych query.

## 9. Mini-handoff

Zapisz:

- jakie query dodales,
- do czego sluza,
- od czego zalezy ich poprawne dzialanie.
