# Portfel 19 Zlecen Dla Podwykonawcow - Zadania 84-86 + nastepne

## Cel portfela

Automatyzacja bezpieczenstwa: regresyjne testy security headers, globalny rate limit API, framework migracji D1 schema. Kontynuacja paradygmatu zero-regression security pipeline.

## Zadania

| ID | Plik | Cel | Status |
|----|------|-----|--------|
| 84 | ZLECENIE_GLOWNE_84_SECURITY_HEADERS_REGRESSION_TEST.md | Automatyczne testy regresji security headers (HSTS, nosniff, XFO, Referrer) | PASS |
| 85 | ZLECENIE_GLOWNE_85_GLOBAL_API_RATE_LIMIT.md | Globalny rate limit API (per IP / per API key) - rozszerzenie per-chat rate limitera | PASS |
| 86 | ZLECENIE_GLOWNE_86_D1_SCHEMA_MIGRATIONS.md | Framework migracji schema D1 (ALTER TABLE, CREATE INDEX, transakcje) | PASS |

## Zadania z PORTFEL_18 (uzupelnienie)

| ID | Cel | Status |
|----|-----|--------|
| Z81 | CSP (Content-Security-Policy) dla API response | TODO |
| Z82 | Permissions-Policy dla API response | TODO |
| Z83 | Global checkWebhookPayloadSize — refaktoryzacja Discord + Telegram | TODO |

## Zadania domkniete w tej sesji

### Z84
- `cloudflare/src/security_headers.js` — nowy modul wspoldzielony (getCorsAllowOrigin + jsonResponse)
- `cloudflare/src/worker.js` — importuje zamiast inline definicji
- `tests/worker_security_headers_test.mjs` — 12 testow: CORS (matching/non-matching Origin, info disclosure guard), security headers dla roznych statusow (200, 400, 403, 413), HSTS max-age 31536000. 12/12 PASS.

### Z85
- `cloudflare/src/global_rate_limiter.js` — globalny rate limiter (per IP, per API key, per project)
- Uzywa `telegram_chat_limits` table (prefixowane klucze `gl:ip:*`, `gl:key:*`, `gl:proj:*`)
- Domyslne limity: IP=60 RPM, API key=120 RPM, project=600 RPM
- `cloudflare/src/worker.js` — checkGlobalRateLimit przed routing, zwraca 429 jesli przekroczony
- `tests/global_rate_limiter_test.mjs` — 6 testow: allow below limit, block per-IP, block per-API-key, fail-open no DB, fail-open no IP. 6/6 PASS.

### Z86
- `cloudflare/src/schema_migrations.js` — framework migracji D1 z MIGRATIONS array
- `applyMigrations(db)` — tworzy schema_migrations, stosuje brakujace migracje idempotentnie (CREATE TABLE IF NOT EXISTS), zapisuje historie
- `getSchemaVersion(db)` — czyta najnowsza wersje schema
- `cloudflare/src/worker.js` — wywoluje `applyMigrations(env.DB)` na poczatku handlera `fetch()` jako startup hook
- `tests/schema_migrations_test.mjs` — 6 testow: first run creates table, idempotent second run, getSchemaVersion, fail-open no DB, ordered migrations, idempotent SQL. 6/6 PASS.

## Statystyki testow

```
Suites: 36, Tests: 173, PASS: 173, FAIL: 0
```

## Zasada portfela

Testy regresji > manual audit. Kazdy nowy endpoint musi przechodzic test security headers. Globalny rate limiter fail-open przy braku DB. Migracje idempotentne (IF NOT EXISTS). Zero downtime (continue on migration failure, log error).

## Zadania na pozniej

| ID | Opis | Priorytet |
|----|------|-----------|
| Z55 | ESP runtime - real hardware bench i maintener signature | blocked |
| Z81 | CSP (Content-Security-Policy) dla API response | niski |
| Z82 | Permissions-Policy dla API response | niski |
| Z83 | Global checkWebhookPayloadSize refaktoryzacja | niski |
| Z87 | CORS preflight caching (Access-Control-Max-Age) | niski |
| Z88 | Webhook replay idempotency (deduplikacja) | niski |

## Pliki utworzone/zmienione

- `cloudflare/src/security_headers.js` — nowy modul (Z84)
- `cloudflare/src/global_rate_limiter.js` — nowy modul (Z85)
- `cloudflare/src/schema_migrations.js` — nowy modul (Z86)
- `cloudflare/src/worker.js` — importy Z84/Z85/Z86, checkGlobalRateLimit przed routing, applyMigrations na startup
- `tests/worker_security_headers_test.mjs` — 12 testow (Z84)
- `tests/global_rate_limiter_test.mjs` — 6 testow (Z85)
- `tests/schema_migrations_test.mjs` — 6 testow (Z86)
- `cloudflare/wrangler.toml` — CORS_ALLOWED_ORIGINS (Z79)
