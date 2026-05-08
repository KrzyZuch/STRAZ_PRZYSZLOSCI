# Handoff dla Nastepnego Agenta — PORTFEL_19 (Z84-86)

## Cel portfela

Automatyzacja bezpieczenstwa: regresyjne testy security headers, globalny rate limit API, framework migracji D1 schema. Kontynuacja paradygmatu zero-regression security pipeline.

## Zlecenia z PORTFEL_19

| ID | Cel | Status |
|----|-----|--------|
| Z84 | Automatyczne testy regresji security headers (HSTS, nosniff, XFO, Referrer) | IN_PROGRESS |
| Z85 | Globalny rate limit API (per IP / per API key) | TODO |
| Z86 | Framework migracji schema D1 (ALTER TABLE, CREATE INDEX) | TODO |

## Zadania z PORTFEL_18 (uzupelnienie)

| ID | Cel | Status |
|----|-----|--------|
| Z81 | CSP (Content-Security-Policy) dla API response | TODO |
| Z82 | Permissions-Policy dla API response | TODO |
| Z83 | Global checkWebhookPayloadSize — refaktoryzacja Discord + Telegram | TODO |

## Testy do momentu

```bash
node --test tests/discord_bot_security_test.mjs tests/discord_bot_ed25519_test.mjs tests/discord_rate_limiter_load_test.mjs tests/discord_api_handler_413_and_timing_safe_test.mjs tests/telegram_issues_413_test.mjs
# 33 suites, 149 tests, PASS, FAIL: 0
```

## Zadania na pozniej

| ID | Opis | Priorytet |
|----|------|-----------|
| Z55 | ESP runtime — real hardware bench + maintainer signature | blocked |
| Z87 | CORS preflight caching (Access-Control-Max-Age) | niski |
| Z88 | Webhook replay idempotency (deduplikacja) | niski |

## Decyzje

| Decyzja | Uzasadnienie |
|---------|-------------|
| Z84 pierwszy (przed Z85/Z86) | Automatyzacja testow > nowe funkcjonalnosci. Regresja jest krytyczniejsza niz rozszerzenie. |
| CSP/Permissions-Policy niski priorytet | API zwraca JSON, nie web assets. Defense-in-depth. |
| Z83 niski priorytet | Funkcjonalny duplikat, nie luka bezpieczenstwa. |
| Tests fail-hard | Jakikolwiek brak security headera = test FAIL. |
