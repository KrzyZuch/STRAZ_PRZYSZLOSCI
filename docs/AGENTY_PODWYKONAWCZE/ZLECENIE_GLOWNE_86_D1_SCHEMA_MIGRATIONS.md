# ZLECENIE GLOWNE 86 - D1 Schema Migrations

## Cel

Stworzyc framework migracji schema Cloudflare D1 oparty na `split_d1_backup.py`. Obecnie schema D1 jest zarzadzane recznie. Framework powinien:

1. Przechowywac historie migracji w tabeli `schema_migrations`
2. Automatycznie stosowac brakujace migracje przy starcie workera
3. Wspierac idempotentne migracje (mozna uruchomic wielokrotnie bez bledu)

## Architektura

- Tabela `schema_migrations` (version TEXT PRIMARY KEY, applied_at TIMESTAMP, checksum TEXT)
- Pila migracji w `migrations/` (nazwane YYYYMMDDHHMMSS_description.sql)
- Funkcja `applyMigrations(db)` sprawdza ktore migracje zostaly zastosowane i stosuje brakujace w transakcji
- Fallback: `on_startup_migrations` — lista SQLi do wykonania przy starcie (bez historii, idempotentna)

## Status

TODO
