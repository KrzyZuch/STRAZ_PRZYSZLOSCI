# Checklista Odbioru Zlecenia Glownego 01 Sync Encji Organizacji Do D1 SQLite

Ten plik sluzy glownemu agentowi albo czlowiekowi do sprawdzenia, czy podwykonawca dobrze wykonal `ZLECENIE_GLOWNE_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`.

## 1. Co ma dostarczyc podwykonawca

Sprawdz, czy w wyniku pracy istnieja:

- skrypt syncu do `SQLite`,
- minimalna dokumentacja uruchomienia,
- lokalna walidacja,
- mini-handoff podwykonawcy.

## 2. Checklista merytoryczna

- Czy skrypt rzeczywiscie czyta kanoniczne rekordy organizacji z repo, a nie wymaga recznego przepisywania danych?
- Czy skrypt tworzy albo zasila lokalna baze `SQLite`?
- Czy sync robi `upsert`, a nie tylko jednorazowy `insert`?
- Czy skrypt zapisuje `payload_json`?
- Czy skrypt obsluguje przynajmniej sample records?
- Czy wynik jest zgodny z migracja `cloudflare/migrations/0012_organization_agent_entities.sql`?

## 3. Checklista zakresu

- Czy podwykonawca trzymal sie write scope z zadania?
- Czy nie wszedl bez potrzeby w `Project 13` albo inne nieprzydzielone watki?
- Czy nie przepisal strategii repo zamiast dowiezc konkretny task?

## 4. Checklista walidacji

Sprawdz, czy podwykonawca uruchomil:

- lokalny run syncu na testowej bazie `SQLite`,
- kontrole, czy po syncu rekordy sa w tabelach,
- `git diff --check`,
- `py_compile`, jesli dodawal kod Python.

## 5. Co przeczytac przy odbiorze

- `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`
- mini-handoff zostawiony przez podwykonawce
- `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
- `cloudflare/migrations/0012_organization_agent_entities.sql`

## 6. Sygnały, ze wynik nie nadaje sie jeszcze do przyjecia

- brak realnego skryptu albo brak dzialajacego CLI,
- brak walidacji lokalnej,
- brak `payload_json`,
- sync dziala tylko na pojedynczym, recznie zahardcodowanym rekordzie,
- wynik wymaga od glownego agenta dopisania polowy logiki od zera,
- podwykonawca wyszedl poza write scope bez uzasadnienia.

## 7. Decyzja po odbiorze

Mozliwe decyzje:

- `accepted`: wynik spelnia acceptance criteria i mozna go integrowac dalej,
- `needs_changes`: kierunek jest dobry, ale trzeba poprawic konkretne braki,
- `rejected`: wynik nie dowozi celu zadania albo zbyt mocno wychodzi poza zakres.

## 8. Co ma wpisac glowny agent do handoffu

Po odbiorze wpisz w glownym handoffie:

- czy wynik podwykonawcy zostal przyjety,
- jakie pliki powstaly,
- jakie walidacje przeszly,
- jaki jest nastepny ruch po odbiorze.
