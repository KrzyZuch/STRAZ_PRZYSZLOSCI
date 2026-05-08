# ZLECENIE GLOWNE 83 - Global checkWebhookPayloadSize

## Cel

Zrefaktoryzowac duplikowana logike Content-Length 413 dla Discord i Telegram do jednej shared funkcji.

## Obecny stan

- `discord_api_handler.js`: `checkDiscordPayloadSize(request, env)` (inline, lokalna funkcja)
- `telegram_issues.js`: `checkTelegramPayloadSize(request, env)` (eksportowana)

## Docelowy stan

Jedna funkcja `_checkPayloadSize(request, env, opts)` uzywana przez oba handlery, z parametrami:
- `envKey`: nazwa specyficznej zmiennej env (np. TELEGRAM_MAX_WEBHOOK_BODY_BYTES)
- `fallbackKey`: nazwa fallbackowej zmiennej (np. MAX_WEBHOOK_BODY_BYTES)
- `defaultMax`: defaultowa wartosc (np. 5242880)

## Status

TODO — low priority (duplikat dziala poprawnie, nie security luka).
