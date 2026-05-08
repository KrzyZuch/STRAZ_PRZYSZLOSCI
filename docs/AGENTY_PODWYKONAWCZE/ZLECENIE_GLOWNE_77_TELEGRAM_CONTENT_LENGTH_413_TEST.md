# ZLECENIE GLOWNE 77 - Telegram Webhook Content-Length 413 Testy

## Cel

Stworzyc testy unit dla sprawdzenia Content-Length w Telegram webhook handlerze (`handleTelegramWebhook`), analogiczne do Z74 dla Discord.

## Osiagniete

- Wydobyto `checkTelegramPayloadSize` z inline w `handleTelegramWebhook` do eksportowanej funkcji w `telegram_issues.js` (linie 1909-1914, + wartosc w handlerze)
- Stworzono `tests/telegram_issues_413_test.mjs` — 14 testow:
  - payload within/below/at limit → no 413 (3 testy)
  - payload exceeding default 5MB → 413 (3 testy)
  - custom TELEGRAM env → respects custom (2 testy)
  - fallback env (MAX_WEBHOOK_BODY_BYTES) → 413 (1 test)
  - prefers explicit TELEGRAM_ var over generic (1 test)
  - missing Content-Length → no 413 (1 test)
  -磨 małe/duze liczby → NaN/negative → no 413 (2 testy)
  - response body contains error info (1 test)
  - non-numeric → parseInt NaN, no 413 (1 test, zabezpieczenie)

## Testy

```bash
node --test tests/telegram_issues_413_test.mjs
# suites: 1, tests: 14, pass: 14, fail: 0
```
