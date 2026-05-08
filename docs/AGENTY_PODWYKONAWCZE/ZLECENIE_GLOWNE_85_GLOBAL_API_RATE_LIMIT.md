# ZLECENIE GLOWNE 85 - Global API Rate Limit

## Cel

Rozszerzyc obecny per-chat rate limiter o globalny rate limit API (per IP / per API key / per project), aby zapobiec atakom DDoS i abuse API. Obecnie rate limit dziala tyle per-chat (5 min, doba), ale globalny rate limit chroni przed agregowanym abuse.

## Architektura

Dodac nowa tabele w D1: `api_rate_limits` z kolumnami: `identifier` (ip lub api_key), `window_started_at`, `request_count`, `last_request_at`, `platform`, `limit_type` (ip|api_key|project).

## Punkty wejscia

- `worker.js`: `fetch()` handler — przed routing sprawdz globalny rate limit per IP
- `discord_api_handler.js`: przed `handleDiscordWebhook()` — global rate limit per Discord bot secret
- `telegram_issues.js`: przed `handleTelegramWebhook()` — global rate limit per Telegram webhook secret

## Wartosci domyslne

- `API_MAX_REQUESTS_PER_MINUTE_PER_IP`: 60 (1 req/sec)
- `API_MAX_REQUESTS_PER_MINUTE_PER_API_KEY`: 120 (2 req/sec)
- `API_MAX_REQUESTS_PER_MINUTE_PER_PROJECT`: 600 (10 req/sec)

## Status

TODO
