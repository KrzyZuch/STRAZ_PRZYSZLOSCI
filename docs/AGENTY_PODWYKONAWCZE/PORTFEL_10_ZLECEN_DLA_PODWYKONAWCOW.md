# Portfel 10 Zlecen Dla Podwykonawcow

Ten dokument jest zbiorcza mapa prac, ktore mozna rozdysponowac rownolegle podwykonawcom.

## Kolejnosc pracy

Najpierw dawaj zadania z priorytetu `A`, potem `B`, potem `C`.

## Portfel

1. `A` - `ZLECENIE_GLOWNE_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`
   - zaleznosci: brak
   - odbior: `CHECKLISTA_ODBIORU_ZLECENIA_GLOWNEGO_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`
2. `A` - `ZLECENIE_GLOWNE_02_PROJECT13_RUN_CONTEXT_I_ARTIFACT_FLOW.md`
   - zaleznosci: brak
   - odbior: acceptance criteria z pliku zadania
3. `A` - `ZLECENIE_GLOWNE_03_PROJECT13_VERIFICATION_EXECUTION_SURFACE.md`
   - zaleznosci: `pack-project13-kaggle-verification-01`
   - odbior: acceptance criteria z pliku zadania
4. `B` - `ZLECENIE_GLOWNE_04_PROJECT13_CURATION_CHAIN_PACK.md`
   - zaleznosci: `CHAIN_MAP.md`, obecne packi `enrichment` i `verification`
   - odbior: acceptance criteria z pliku zadania
5. `B` - `ZLECENIE_GLOWNE_05_PROJECT13_EXPORT_PACK_SMOKE_RUN.md`
   - zaleznosci: `pack-project13-catalog-export-01`
   - odbior: acceptance criteria z pliku zadania
6. `B` - `ZLECENIE_GLOWNE_06_PROJECT13_BENCHMARK_COMPARISON_PACK.md`
   - zaleznosci: README `Project 13`, model notebookow Kaggle
   - odbior: acceptance criteria z pliku zadania
7. `B` - `ZLECENIE_GLOWNE_07_KNOWLEDGE_BUNDLE_DLA_NOWYCH_PACKOW.md`
   - zaleznosci: aktualne packi i `CHAIN_MAP.md`
   - odbior: acceptance criteria z pliku zadania
8. `B` - `ZLECENIE_GLOWNE_08_REVIEW_ROTATION_GOVERNANCE.md`
   - zaleznosci: dokumenty organizacyjne i handoff
   - odbior: acceptance criteria z pliku zadania
9. `C` - `ZLECENIE_GLOWNE_09_D1_SQLITE_QUERY_COOKBOOK.md`
   - zaleznosci: wynik zadania `01`
   - odbior: acceptance criteria z pliku zadania
10. `C` - `ZLECENIE_GLOWNE_10_PUBLIC_VOLUNTEER_RUN_READINESS.md`
   - zaleznosci: wynik zadan `02` i `03` jest pomocny, ale nieobowiazkowy
   - odbior: acceptance criteria z pliku zadania

## Zasada dla glownego agenta

Glowny agent:

- nie wykonuje tych zadan za podwykonawcow,
- rozdysponowuje je i odbiera,
- sprawdza wynik wzgledem acceptance criteria,
- wpisuje do handoffu, co zostalo przyjete, a co wymaga poprawek.
