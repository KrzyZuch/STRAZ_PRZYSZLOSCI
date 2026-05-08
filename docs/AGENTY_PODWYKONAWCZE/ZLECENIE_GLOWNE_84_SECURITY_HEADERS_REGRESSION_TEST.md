# ZLECENIE GLOWNE 84 - Security Headers Regression Test

## Cel

Automatyczny test regresji sprawdzajacy, ze kazdy jsonResponse zawiera wymagane security headers (HSTS, nosniff, XFO, Referrer). Test powinien failowac gdy ktokolwiek usunie lub zmodyfikuje security headers.

## Scenariusz

Kazdy endpoint w worker.js zwraca Response przez jsonResponse. jsonResponse ustawia stale security headers. Testy powinny:

1. Sprawdzac ze response zwraca 200 OK z obecnymi headers
2. Weryfikowac ze kazdy header security jest obecny i poprawny
3. Failowac gdy jakikolwiek header brakuje lub ma zla wartosc

## Testy do implementacji

- test: `/health` zwraca HSTS, nosniff, XFO, Referrer, CORS
- test: OPTIONS preflight zwraca te same headers (CORS)
- test: `jsonResponse` helper zawsze zawiera wszystkie security headers
- test: bledne zapytania (400) tez zawieraja security headers (defense-in-depth)

## Konsekwencje dla innych endpointow

Kazdy nowy endpoint musi przechodzic ten test. Jesli endpoint nie zwraca jsonResponse (np. zwraca surowy Response), musi tez zwracac security headers.

## Status

IN_PROGRESS
