# Handoff dla Nastepnego Agenta - PORTFEL_19 (Z84-86) - 2026-05-08

## Cel sesji

Domkniecie Z84 (security headers regression test), Z85 (global API rate limit), Z86 (D1 schema migrations framework).

## Zmiany w kodzie

### Nowe pliki

- `cloudflare/src/security_headers.js` — wspoldzielony modul security headers (getCorsAllowOrigin + jsonResponse)
- `cloudflare/src/global_rate_limiter.js` — global API rate limit (per IP / per API key / per project)
- `cloudflare/src/schema_migrations.js` — D1 schema migration framework
- `tests/worker_security_headers_test.mjs` — 12 testow
- `tests/global_rate_limiter_test.mjs` — 6 testow
- `tests/schema_migrations_test.mjs` — 6 testow

### Zmienione pliki

- `cloudflare/src/worker.js` — importuje security_headers, global_rate_limiter, schema_migrations; checkGlobalRateLimit przed routing; applyMigrations na startup

## Architektura security headers (security_headers.js)

```javascript
export function getCorsAllowOrigin(env, request) { ... }
export function jsonResponse(payload, status, env, request) { ... }
```

- getCorsAllowOrigin: wyczytaj CORS_ALLOWED_ORIGINS (comma-separated), default "*". Whitelist: sprawdza Origin header; przy braku request zwraca pierwszy origin (info disclosure guard).
- jsonResponse: zwraca Response z security headers (HSTS, nosniff, XFO, Referrer, CORS).

## Architektura global rate limiter (global_rate_limiter.js)

```javascript
export async function checkGlobalRateLimit(request, env) { ... }
```

- 3 buckety: per-IP (CF-Connecting-IP), per-API-key (X-Provider-Token), per-project (DEPLOYMENT_ENVIRONMENT)
- Domyslne limity: 60 RPM (IP), 120 RPM (API key), 600 RPM (project)
- Uzywa tej samej tabeli telegram_chat_limits z prefixowymi kluczami (gl:ip:*, gl:key:*, gl:proj:*)
- Zintegrowano w worker.js: przed routing zwraca 429 jesli przekroczony

## Architektura schema migrations (schema_migrations.js)

```javascript
export const MIGRATIONS = [ ... ];
export async function applyMigrations(db) { ... }
export async function getSchemaVersion(db) { ... }
```

- Idempotentne migracje (CREATE TABLE IF NOT EXISTS)
- applyMigrations tworzy tabel schema_migrations, stosuje brakujace migracje, zapisuje historie
- getSchemaVersion zwraca najnowszą wersje
- Zintegrowano w worker.js: applyMigrations(env.DB) na poczatku fetch() (startup hook)
- Continue on migration failure (log error), zero downtime

## Wynik testow

```bash
node --test tests/worker_security_headers_test.mjs
# suites: 1, tests: 12, pass: 12, fail: 0

node --test tests/global_rate_limiter_test.mjs
# suites: 1, tests: 6, pass: 6, fail: 0

node --test tests/schema_migrations_test.mjs
# suites: 1, tests: 6, pass: 6, fail: 0

node --test tests/discord_bot_security_test.mjs tests/discord_bot_ed25519_test.mjs ...
# suites: 36, tests: 173, pass: 173, fail: 0
```

## Decyzje

| Decyzja | Uzasadnienie |
|---------|-------------|
| Sync prepare() w mock D1 | Chodzi o spójność z Cloudflare D1 API (prepare jest sync, zwraca D1PreparedStatement z async metodami). |
| Global rate limit fail-open | Nie blokowac chatow gdy infrastructure nieoperacyjna. |
| applyMigrations on startup | Cold starts = migration check. Idempotent = zero harm. Error handling = zero downtime (continue + log). |

## Nastepne zadania

| ID | Opis | Priorytet |
|----|------|-----------|
| Z81 | CSP (Content-Security-Policy) dla API | low |
| Z82 | Permissions-Policy dla API | low |
| Z83 | Global checkWebhookPayloadSize refaktoryzacja | low |
| Z55 | ESP runtime - real hardware bench | blocked |

## Pliki

- `docs/AGENTY_PODWYKONAWCZE/PORTFEL_19_ZLECEN_DLA_PODWYKONAWCOW_2026-05-08.md`
- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-05-08_POZ_19.md`
