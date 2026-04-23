# Runbook Dla Pack Project13 Curation 01

## Cel

Ten pack formalizuje etap review i kuracji miedzy verification a downstream exportem.

Docelowy przeplyw:

```text
verified candidates -> schema alignment -> curation decisions -> catalog-ready records -> PR
```

## Co trzeba miec przed startem

- verification report i disagreement log z packa verification
- kandydacki snapshot `test_db_verified.jsonl` z packa verification
- lokalne repo z kanonicznym katalogiem `Project 13`
- znajomosc schematow katalogu: `devices.jsonl`, `parts_master.jsonl`, `device_parts.jsonl`

## Krok 1. Przejrzyj wejscie z verification

1. Wczytaj `verification_report.md` i `verification_disagreements.jsonl` z packa verification.
2. Zrozum, ktore rekordy sa potwierdzone, ktore sporne i ktore odrzucone.
3. Dla rekordow spornych podjac decyzje kuracyjna: accept, defer albo reject.

## Krok 2. Ukladanie do kanonicznych schematow

1. Dla kandydatow oznaczonych jako `confirmed` w verification:
   - sprawdz, czy sa zgodne ze schematem `devices.jsonl`, `parts_master.jsonl` i `device_parts.jsonl`,
   - uzupelnij brakujace pola kanoniczne: donor device, part number, kategoria, parametry,
   - oznacz jako `ready_for_catalog`.
2. Dla kandydatow spornych:
   - jesli istnieje silny dowod z verification, oznacz jako `deferred` z wyjasnieniem,
   - jesli dowod jest slabym falszywym pozytywem, oznacz jako `rejected`.
3. Dla kandydatow odrzuconych w verification:
   - nie promuj do katalogu,
   - zapisz decyzje w audit trail.

## Krok 3. Zapisz decyzje kuracyjne

1. Zapisz `curation_decisions.jsonl` z wpisami:
   - `candidate_id`, `decision` (accept/defer/reject), `rationale`, `provenance` (odniesienie do verification reportu).
2. Zapisz `curation_report.md` z:
   - counts: accepted, deferred, rejected,
   - najwazniejsze przypadki wymagajace review,
   - provenance do wejsciowego verification reportu.

## Krok 4. Zaktualizuj kanoniczny katalog

1. Dodaj zaakceptowanych kandydatow do odpowiednich plikow katalogu:
   - `data/devices.jsonl` - nowy donor device albo aktualizacja istniejacego,
   - `data/parts_master.jsonl` - nowe czesci kanoniczne,
   - `data/device_parts.jsonl` - nowe relacje czesc-donor.
2. Upewnij sie, ze nie dublujesz istniejacych rekordow.
3. Sprawdz spojnosc relacji miedzy plikami katalogu.

## Krok 5. Otworz PR

1. Stworz branch z zakresie curation.
2. Commituj zmiany w katalogu i raport kuracyjny.
3. Otworz PR do upstream z trescia z `PR_TEMPLATE.md`.
4. Dolacz `curation_report.md` i `curation_decisions.jsonl` jako czesc PR.

## Czego pack nie powinien robic

- nie powinien automatycznie akceptowac wszystkich kandydatow
- nie powinien uruchamiac discovery, OCR ani exportu downstream
- nie powinien recznie edytowac wygenerowanych plikow exportowych
- nie powinien pomijac audit trail decyzji kuracyjnych

## Aktualny status

To jest pack `draft`.

Na obecnym etapie:

- kontrakt dokumentacyjny jest gotowy,
- outputy i acceptance criteria sa nazwane,
- nadal trzeba wydzielic realny execution surface curation, np. skrypt do automatycznego ukladania kandydatow do schematow katalogu,
- pierwszy realny run wymaga dostepu do verification reportu i disagreement logu z poprzedniego etapu.

## Minimalne kryterium sukcesu

Pack bedzie gotowy do pierwszego realnego uruchomienia, gdy:

- bedzie mial stabilny input z verification,
- bedzie mial jawny output curation decisions,
- reviewer dostanie audit trail zamiast czarnej skrzynki.
