# Zlecenie Glowne 01: Sync Encji Organizacji Do D1 SQLite

Ten plik jest gotowym zleceniem dla niezaleznego agenta-podwykonawcy.

## 1. Misja zadania

Masz dowiezc pierwszy dzialajacy sync encji organizacji do lokalnej bazy `SQLite`, zgodnej z nowa mapa `D1/SQLite`.

Nie masz projektowac calej strategii repo.
Masz wykonac jeden zlozony task wykonawczy.

## 2. Wyzszy cel organizacji

To zadanie sluzy budowie wspolnej pamieci organizacji.
Chodzi o to, zeby cala inicjatywa mogla:

- widziec stan encji organizacyjnych,
- zadawac agentom pytania o portfolio projektow,
- laczyc projekty z ich wyzszym celem,
- miec query-ready warstwe dla review, gate'ow i approval.

## 3. Co masz dostarczyc

### Obowiazkowe wyniki pracy

1. Skrypt syncu, najlepiej w `pipelines/`, ktory:
   - czyta kanoniczne rekordy organizacji z repo,
   - tworzy lub zasila lokalna baze `SQLite`,
   - robi `upsert` do tabel zgodnych z `cloudflare/migrations/0012_organization_agent_entities.sql`.
2. Minimalna dokumentacja uruchomienia skryptu.
3. Walidacja lokalna pokazujaca, ze po syncu w bazie sa rekordy.
4. Mini-handoff z opisem wyniku pracy.

### Mile widziane

- obsluga nie tylko sample records, ale tez innych kanonicznych rekordow, jesli sa juz w repo i maja stabilny format,
- prosty tryb `--db-path`,
- tryb `--dry-run` albo raport liczby przetworzonych rekordow.

## 4. Read First

- `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
- `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
- `docs/ENCJE_I_WORKFLOWY_ORGANIZACJI_AGENTOWEJ.md`
- `schemas/organization_agent_v1.yaml`
- `data/sample/organization_*.json`
- `cloudflare/migrations/0012_organization_agent_entities.sql`

## 5. Write Scope

Mozesz zmieniac:

- `pipelines/`
- `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
- ewentualnie `data/sample/organization_*.json`, jesli trafisz na jawna niespojnosc i opiszesz to w mini-handoffie

Nie ruszaj:

- `PROJEKTY/13_baza_czesci_recykling/`
- notebookow Kaggle
- ogolnej strategii repo poza zakresem tego taska

## 6. Acceptance Criteria

Zadanie jest wykonane, gdy:

1. istnieje skrypt syncu do `SQLite`,
2. skrypt da sie uruchomic lokalnie bez Cloudflare,
3. przynajmniej sample records trafiaja do odpowiednich tabel,
4. `payload_json` jest zapisywany,
5. agent zostawia jasny mini-handoff z lista obslugiwanych encji i znanych brakow.

## 7. Walidacja, ktora masz zrobic

- uruchomic skrypt na lokalnej testowej bazie `SQLite`
- sprawdzic, czy po syncu rekordy sa w tabelach
- uruchomic `git diff --check`

Jesli dodasz kod Python:

- uruchom tez `python3 -m py_compile <twoj_nowy_skrypt>`

## 8. Blokery

Jesli zobaczysz, ze:

- migracja `0012` nie wystarcza do sensownego syncu,
- sample records sa zbyt ubogie,
- brakuje jednego stabilnego katalogu rekordow kanonicznych,

to nie rozwijaj obok nowej wielkiej architektury.
Zapisz blocker, zrob minimalny postep i opisz, czego brakuje.

## 9. Format wyniku

Na koncu zostaw mini-handoff zawierajacy:

- co zrobiles,
- jakie pliki zmieniles,
- jak uruchomic sync,
- jakie encje obslugujesz,
- jakie walidacje przeszly,
- co powinien sprawdzic agent odbierajacy twoj wynik.

## 10. Uwaga organizacyjna

Pracujesz jako podwykonawca.

To znaczy:

- nie przejmujesz sterowania cala inicjatywa,
- nie przeskakujesz samowolnie do innego duzego taska,
- dowozisz ten jeden zakres mozliwie czysto i czytelnie.
