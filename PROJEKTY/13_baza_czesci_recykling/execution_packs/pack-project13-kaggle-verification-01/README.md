# Pack Project13 Kaggle Verification 01

To jest szkiel `verification chain` dla `Project 13`.

Nie sluzy do discovery nowych kandydatow.
Sluzy do sprawdzania i doszczelniania kandydatow, ktorzy juz przeszli przez etap enrichment.

## Zakres

- execution mode: `kaggle_notebook`
- status: `draft`
- docelowy output: `report`

## Rola w lancuchu

```text
enrichment -> verification -> review / curation -> export
```

Ten pack ma:

- uruchamiac OCR i frame check dla niepewnych rekordow,
- budowac jawny raport rozbieznosci,
- przygotowywac kandydatow do review,
- zatrzymywac falszywe trafienia przed exportem downstream.

## Najwazniejsza roznica wzgledem packa enrichment

- `enrichment` szuka i wzbogaca kandydatow
- `verification` nie ma generowac nowych downstream exportow
- `verification` ma zostawic jawny `verification_report` i `disagreement log`

## Wejscie dla kolejnego agenta

Zacznij od:

1. `manifest.json`
2. `RUNBOOK.md`
3. `REVIEW_CHECKLIST.md`
4. `../CHAIN_MAP.md`
