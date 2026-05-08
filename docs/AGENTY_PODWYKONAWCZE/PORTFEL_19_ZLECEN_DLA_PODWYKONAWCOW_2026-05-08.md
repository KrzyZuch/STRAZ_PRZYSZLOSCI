# Portfel 19 Zlecen Dla Podwykonawcow - Zadania 84-86 + nastepne

## Cel portfela

Automatyzacja bezpieczenstwa: regresyjne testy security headers, globalny rate limit API, system migracji D1 schema. Kontynuacja paradygmatu zero-regression security pipeline.

## Zadania

| ID | Plik | Cel | Status |
|----|------|-----|--------|
| 84 | ZLECENIE_GLOWNE_84_SECURITY_HEADERS_REGRESSION_TEST.md | Automatyczne testy regresji security headers (HSTS, nosniff, XFO, Referrer) dla wszystkich endpointow | IN_PROGRESS |
| 85 | ZLECENIE_GLOWNE_85_GLOBAL_API_RATE_LIMIT.md | Globalny rate limit API (per IP / per API key) - rozszerzenie per-chat rate limitera | TODO |
| 86 | ZLECENIE_GLOWNE_86_D1_SCHEMA_MIGRATIONS.md | Framework migracji schema D1 (ALTER TABLE, CREATE INDEX, transakcje) oparty na split_d1_backup.py | TODO |

## Zasada portfela

Testy regresji > manual audit. Z80 wykazalo, ze headers sa OK, ale brak automatyzacji. Kazdy nowy endpoint musi miec test sprawdzajacy security headers. Globalny rate limit chroni przed DDoS (Z85). Migracje D1 (Z86) zapobiegaja brakom schematu w przyszlosci.

## Zadania na pozniej

| ID | Opis | Priorytet |
|----|------|-----------|
| Z55 | ESP runtime - real hardware bench i maintener signature | blocked |
| Z87 | Content-Security-Policy jesli powstanie web UI | low |
| Z88 | CORS preflight caching (Access-Control-Max-Age) | low |

## Statystyki poprzedniego portfela

Suites: 33, Testy: 149, PASS: 149, FAIL: 0 (PORTFEL_18)
