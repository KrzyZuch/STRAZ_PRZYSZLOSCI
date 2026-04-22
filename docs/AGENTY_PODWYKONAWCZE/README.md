# Agenty Podwykonawcze

Ten katalog zawiera pliki robocze dla agentow, ktorzy maja wykonywac konkretne zadania w repo, ale nie przejmowac roli glownego agenta rozwijajacego cala inicjatywe.

## Jak tego uzywac

1. Kazdy agent podwykonawczy najpierw czyta:
   - `docs/AGENTY_PODWYKONAWCZE/INSTRUKCJA_DLA_AGENTA_PODWYKONAWCZEGO.md`
   - `docs/AGENTY_PODWYKONAWCZE/PORTFEL_10_ZLECEN_DLA_PODWYKONAWCOW.md`
   - przydzielony plik `ZLECENIE_GLOWNE_*.md`
2. Agent pracuje tylko w zakresie plikow wskazanych w swoim zadaniu.
3. Agent ma rozumiec, czemu jego zadanie sluzy wyzszemu celowi inicjatywy, ale nie ma samodzielnie przestawiac priorytetow calego repo.
4. Jesli trafi na blocker, raportuje go w swoim pliku wynikowym lub mini-handoffie i nie zaczyna samowolnie innego duzego watku bez nowego przydzialu.

## Co tu jest

- `INSTRUKCJA_DLA_AGENTA_PODWYKONAWCZEGO.md`: kanoniczna instrukcja roli
- `PORTFEL_10_ZLECEN_DLA_PODWYKONAWCOW.md`: zbiorcza mapa 10 zadan z priorytetami i zaleznosciami
- `SZABLON_ZADANIA_DLA_AGENTA_PODWYKONAWCZEGO.md`: wzorzec do kolejnych task file
- `ZLECENIE_GLOWNE_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`: aktualne glowne zlozone zadanie do niezaleznego wykonania
- `ZLECENIE_GLOWNE_02_PROJECT13_RUN_CONTEXT_I_ARTIFACT_FLOW.md`
- `ZLECENIE_GLOWNE_03_PROJECT13_VERIFICATION_EXECUTION_SURFACE.md`
- `ZLECENIE_GLOWNE_04_PROJECT13_CURATION_CHAIN_PACK.md`
- `ZLECENIE_GLOWNE_05_PROJECT13_EXPORT_PACK_SMOKE_RUN.md`
- `ZLECENIE_GLOWNE_06_PROJECT13_BENCHMARK_COMPARISON_PACK.md`
- `ZLECENIE_GLOWNE_07_KNOWLEDGE_BUNDLE_DLA_NOWYCH_PACKOW.md`
- `ZLECENIE_GLOWNE_08_REVIEW_ROTATION_GOVERNANCE.md`
- `ZLECENIE_GLOWNE_09_D1_SQLITE_QUERY_COOKBOOK.md`
- `ZLECENIE_GLOWNE_10_PUBLIC_VOLUNTEER_RUN_READINESS.md`
- `CHECKLISTA_ODBIORU_ZLECENIA_GLOWNEGO_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`: checklista dla glownego agenta sprawdzajacego wynik pracy podwykonawcy
- `ZADANIE_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`: task dla warstwy wspolnej pamieci
- `ZADANIE_02_PROJECT13_RUN_CONTEXT_I_ARTIFACT_FLOW.md`: task dla dopiecia `Run -> Artifact`
- `ZADANIE_03_PROJECT13_NEXT_EXECUTION_PACKS.md`: task dla rozbicia kolejnych packow

## Zasada nadrzedna

Agent podwykonawczy nie jest "mniejsza kopia glownego stratega".
Jest wykonawca konkretnego zakresu.

Ma:

- dobrze dowiezc powierzony zakres,
- nie rozwalac pracy innych,
- zostawic po sobie czysty wynik i krotki mini-handoff,
- rozumiec wyzszy cel zadania.

Nie ma:

- sam wybierac nowej strategii dla calej inicjatywy,
- tunelowac pobocznych tematow poza swoim write scope,
- przepisywac architektury repo bez wyraznego przydzialu.
