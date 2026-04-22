# Zadanie 01: Sync Encji Organizacji Do D1 SQLite

## 1. Cel wykonawczy

- Dowiezc pierwszy skrypt projekcyjny, ktory czyta kanoniczne rekordy organizacji z repo i robi `upsert` do tabel z `cloudflare/migrations/0012_organization_agent_entities.sql`.

## 2. Wyższy cel organizacji

- To zadanie buduje wspolna pamiec organizacji i query layer dla wielu projektow naraz.
- Nie sluzy jednemu pilotowi. Sluzy temu, zeby cala inicjatywa wiedziala, po co istnieja projekty, w jakim sa stanie i jak sa powiazane z misja.

## 3. Read First

- `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
- `docs/ENCJE_I_WORKFLOWY_ORGANIZACJI_AGENTOWEJ.md`
- `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
- `schemas/organization_agent_v1.yaml`
- `data/sample/organization_*.json`
- `cloudflare/migrations/0012_organization_agent_entities.sql`

## 4. Write Scope

- `pipelines/`
- ewentualnie `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
- ewentualnie `data/sample/organization_*.json` jesli wyjdzie niespojnosc

## 5. Out Of Scope

- `PROJEKTY/13_baza_czesci_recykling/`
- notebook `youtube-databaseparts.ipynb`
- zmiany strategii calej inicjatywy poza swoim taskiem

## 6. Deliverables

- nowy skrypt syncu, najlepiej w stylu `pipelines/sync_organization_entities_to_sqlite.py`
- mozliwosc wskazania lokalnej bazy `SQLite` przez argument CLI
- `upsert` dla co najmniej sample records obecnych w repo
- krotka dokumentacja uzycia

## 7. Acceptance Criteria

- skrypt potrafi utworzyc albo zasilic lokalna baze zgodna z migracja `0012`
- da sie uruchomic lokalnie bez Cloudflare
- rekordy trafiaja do odpowiednich tabel z podstawowymi kolumnami i `payload_json`
- agent zostawia mini-handoff z lista obslugiwanych encji i znanych brakow

## 8. Walidacja

- lokalny run skryptu na testowej bazie `SQLite`
- kontrola, czy tabele maja rekordy po syncu
- `git diff --check`

## 9. Blokery i eskalacja

- jesli okaże sie, ze brakuje kanonicznych rekordow poza sample records, nie wymyslaj ich masowo samodzielnie
- jesli migracja `0012` wymaga istotnej przebudowy, zapisz to jawnie i ogranicz zmiany do minimum potrzebnego dla syncu

## 10. Mini-handoff

Na koniec zapisz:

- co synchronizujesz,
- jak uruchomic skrypt,
- jakie encje sa juz obslugiwane,
- co nadal wymaga dopracowania.
