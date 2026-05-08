# ZLECENIE GLOWNE 81 - Content-Security-Policy (CSP) dla API

## Cel

Dodac naglowek `Content-Security-Policy` do wszystkich response z `jsonResponse` w `worker.js`. Mimo ze system to API (nie web UI), CSP chroni przed atakami content injection do uzytkownikow, ktorzy moga otwierac JSON w przegladarce jako text/html (np. przez text/html Content-Type poisoning).

## Polityka CSP

```http
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
```

- `default-src 'none'`: blokuje wszystkie zrodla (XHR, scripts, images, media). API zwraca JSON, nie potrzebuje zadnych zasobow.
- `frame-ancestors 'none'`: strona nie bedzie zaladowana w iframe (X-Frame-Options: DENY juz to robi, ale CSP dodaje dodatkowa warstwe).

## Uwaga

CSP w tym kontekscie to "defense-in-depth". API zwraca JSON, ale jesli ktos injectuje malicious `content-type: text/html`, CSP zablokuje wykonanie scriptow.

## Status

TODO — low priority (API bez web assets). Mozna zmergowac z Z84 (security headers regression test).
