# Portfel 18 Zlecen Dla Podwykonawcow - Zadania 77-80 + nastepne

## Cel portfela

Weryfikacja i dalsze security hardening: testy Content-Length dla Telegrama, CORS whitelist, audit security headers.

## Zadania

| ID | Plik | Cel | Status |
|----|------|-----|--------|
| 77 | ZLECENIE_GLOWNE_77_TELEGRAM_CONTENT_LENGTH_413_TEST.md | Telegram webhook Content-Length 413 testy | PASS |
| 79 | ZLECENIE_GLOWNE_79_CORS_WHITELIST.md | CORS whitelist zamiast global wildcard | PASS |
| 80 | ZLECENIE_GLOWNE_80_SECURITY_HEADERS.md | Audit security headers | DONE |

## Zadania domkniete w tej sesji

### Z77
- `tests/telegram_issues_413_test.mjs` — 14 testow: payload within/exceeding/at limit, custom env, fallback, missing/malformed Content-Length, response body. 14/14 PASS.

### Z79
- `cloudflare/src/worker.js` — `getCorsAllowOrigin(env, request)`: `CORS_ALLOWED_ORIGINS` (comma-separated), default wildcard dla backward compat, whitelist mode → sprawdza Origin. `wrangler.toml`: `CORS_ALLOWED_ORIGINS = "*"`.

### Z80
- Audit security headers — HSTS (31536000, includeSubDomains), nosniff, XFO DENY, Referrer-Policy strict-origin-when-cross-origin. CSP i Permissions-Policy niski priorytet (API bez web assets).

## Statystyki testow
```
Suites: 33, Tests: 149, PASS: 149, FAIL: 0
```

## Zasada portfela

Testy odtwarzalne bez zewnetrznych API. CORS domyslnie wildcard dla backward compat. Per-model rate limiter fail-open.

## Zadania na pozniej

| ID | Opis | Priorytet |
|----|------|-----------|
| Z55 | ESP runtime - real hardware bench i maintainer signature | blocked |
