# Handoff dla Nastepnego Agenta - 2026-05-08 po Z77-Z80

## Cel sesji

Domkniecie security hardening Z77-Z80: Telegram Content-Length testy, CORS whitelist, security headers audit.

## Zmiany w kodzie (Z77-Z80)

### Z77
- `cloudflare/src/telegram_issues.js`: wyodrebniono `checkTelegramPayloadSize(request, env)` jako eksportowana funkcja (refaktoryzacja inline check w handlerze)
- `tests/telegram_issues_413_test.mjs`: 14 testow Content-Length dla Telegram webhook
  - payload within/at/exceeding limit (3 testy)
  - custom TELEGRAM_MAX_WEBHOOK_BODY_BYTES (2 testy)
  - fallback MAX_WEBHOOK_BODY_BYTES (1 test)
  - missing/negative/zero/non-numeric Content-Length (4 testy)
  - response body info (1 test)
  - preferencia TELEGRAM_ var nad MAX_ (1 test)
  - very large payload (1 test)

### Z79
- `cloudflare/src/worker.js`: dodano `getCorsAllowOrigin(env, request)` — wyczytuje `CORS_ALLOWED_ORIGINS` (comma-separated), domyslnie `"*"` (backward compat). Przy whitelist sprawdza `Origin` header.
- `cloudflare/wrangler.toml`: dodano `CORS_ALLOWED_ORIGINS = "*"` we wszystkich env (preview, staging, prod)
- `jsonResponse(payload, status, env, request)` — dodano opcjonalne env/request dla dynamicznego CORS

### Z80
- Audit security headers (juz istnialy w jsonResponse od wczesniejszej sesji):
  - `Strict-Transport-Security: max-age=31536000; includeSubDomains`
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `Access-Control-Allow-Origin: configurable` (Z79)
- CSP i Permissions-Policy: nie priorytet (API bez web assets)

## Wynik testow

```bash
node --test tests/telegram_issues_413_test.mjs
# suites: 1, tests: 14, pass: 14, fail: 0

node --test tests/discord_bot_security_test.mjs tests/discord_bot_ed25519_test.mjs tests/discord_rate_limiter_load_test.mjs tests/discord_api_handler_413_and_timing_safe_test.mjs tests/telegram_issues_413_test.mjs
# suites: 33, tests: 149, pass: 149, fail: 0
```

## Decyzje

| Decyzja | Uzasadnienie |
|---------|-------------|
| `CORS_ALLOWED_ORIGINS` domyslnie `*` | Backward compat; whitelist wymaga swiadomego ustawienia przez operatora |
| `getCorsAllowOrigin` przy braku request zwraca pierwszy origin | Zapobiega ujawnienieniu listy allowed origins nieautoryzowanemu hostowi |
| CSP/Permissions-Policy niski priorytet | System dziala jako API (JSON), nie serwuje web assets |

## Luki pozostale (slabe priorytet)

| ID | Opis | Priorytet |
|----|------|-----------|
| Z55 | ESP runtime - real hardware bench i maintainer signature | blocked |
| Z81 | Content-Security-Policy (gdy bedzie web UI) | low |
| Z82 | Permissions-Policy (gdy bedzie web UI) | low |
| Z83 | Global `checkWebhookPayloadSize` refaktoryzujaca Discord + Telegram | low |

## Portfel

`docs/AGENTY_PODWYKONAWCZE/PORTFEL_18_ZLECEN_DLA_PODWYKONAWCOW_2026-05-08.md`

## ZLECENIE_GLOWNE

- `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_77_TELEGRAM_CONTENT_LENGTH_413_TEST.md`
- `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_79_CORS_WHITELIST.md`
- `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_80_SECURITY_HEADERS.md`
