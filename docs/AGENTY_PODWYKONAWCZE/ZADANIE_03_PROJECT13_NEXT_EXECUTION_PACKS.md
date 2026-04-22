# Zadanie 03: Project13 Next Execution Packs

## 1. Cel wykonawczy

- Przygotowac kolejne packi dla `Project 13`, tak aby inicjatywa nie byla zlepiona z jednym notebookiem i jednym manifestem.

## 2. Wyższy cel organizacji

- To zadanie zamienia pojedynczy pilot w reusable architecture dla rozproszonej pracy wolontariuszy z agentami.
- Sluzy dekompozycji pracy na mniejsze, rownolegle odpalane jednostki wykonawcze.

## 3. Read First

- `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
- `PROJEKTY/13_baza_czesci_recykling/README.md`
- `PROJEKTY/13_baza_czesci_recykling/docs/MODEL_WOLONTARIACKICH_NOTEBOOKOW_KAGGLE.md`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/manifest.json`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/RUNBOOK.md`

## 4. Write Scope

- `PROJEKTY/13_baza_czesci_recykling/execution_packs/`
- `PROJEKTY/13_baza_czesci_recykling/docs/`
- ewentualnie `PROJEKTY/13_baza_czesci_recykling/README.md`

## 5. Out Of Scope

- zmiany w finalizerze lub helperze `Artifact`
- D1/SQLite sync dla encji organizacji
- realny run zewnetrzny na Kaggle

## 6. Deliverables

- co najmniej dwa nowe szkielety packow, np. `verification` i `export`
- dla kazdego packa: `manifest.json`, `RUNBOOK.md`, `PR_TEMPLATE.md`, `REVIEW_CHECKLIST.md`
- spis zaleznosci miedzy packami
- aktualizacja dokumentacji, ktora opisuje, jak te packi ukladaja sie w wiekszy workflow

## 7. Acceptance Criteria

- nowe packi maja jasny scope i nie dubluja bez sensu obecnego packa
- ich outputy, acceptance criteria i handoff points sa czytelne
- dokumentacja wyjasnia, czemu rozbicie packow sluzy wyzszemu celowi organizacji

## 8. Walidacja

- parsowanie `manifest.json`
- kontrola spojnosci sciezek i dokumentacji
- `git diff --check`

## 9. Blokery i eskalacja

- jesli okaże sie, ze brakuje danych do zdefiniowania jednego packa, przygotuj chociaz review-ready skeleton z jawnymi brakami
- nie probuj od razu automatyzowac wszystkich nowych packow kodem, jesli najpierw trzeba ustabilizowac kontrakt dokumentacyjny

## 10. Mini-handoff

Na koniec zapisz:

- jakie packi powstaly,
- jaki maja scope,
- jak lacza sie z obecnym packiem `enrichment`,
- czego jeszcze brakuje przed ich pierwszym uruchomieniem.
