# Runbook Dla Pack Project13 Kaggle Verification 01

## Cel

Ten pack ma domknac etap `verification chain` po wstepnym discovery i enrichment.

Docelowy przeplyw:

```text
candidate snapshot -> OCR / frame check -> disagreement log -> PR do review
```

## Co trzeba miec przed startem

- snapshot kandydatow z poprzedniego etapu
- konto `GitHub` i fork repo
- konto `Kaggle` albo przyszly wydzielony execution surface verification
- klucz `GEMINI_API_KEY`

## Co pack powinien zrobic

1. Wczytac kandydacki snapshot z etapu enrichment.
2. Oznaczyc rekordy do dodatkowej weryfikacji.
3. Uruchomic OCR i frame check dla niepewnych przypadkow.
4. Rozdzielic wynik na:
   - rekordy potwierdzone,
   - rekordy sporne,
   - rekordy odrzucone albo pozostawione do dalszej kuracji.
5. Zapisac `verification_report.md` i `verification_disagreements.jsonl`.
6. Wrocic z wynikiem przez fork i `PR`.

## Czego pack nie powinien robic

- nie powinien od razu budowac downstream exportow
- nie powinien mieszac review-ready wynikow z rekordami spornymi bez jawnego oznaczenia
- nie powinien promowac danych do upstream bez `PR`

## Aktualny status

To jest pack `draft`.

Na obecnym etapie:

- kontrakt dokumentacyjny jest gotowy,
- outputy i acceptance criteria sa juz nazwane,
- nadal trzeba wydzielic realny execution surface verification z obecnego notebooka albo zbudowac osobny notebook.

## Minimalne kryterium sukcesu

Pack bedzie gotowy do pierwszego realnego uruchomienia, gdy:

- bedzie mial stabilny input snapshot,
- bedzie mial jawny output verified/unverified,
- reviewer dostanie disagreement log zamiast czarnej skrzynki.
