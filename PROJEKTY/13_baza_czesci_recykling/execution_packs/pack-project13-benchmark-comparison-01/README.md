# Pack Project13 Benchmark Comparison 01

To jest pack dla `benchmark chain` w `Project 13`.

Nie sluzy do discovery, verification, kuracji ani eksportu.
Sluzy do porownywania jakosci, kosztu i czasu roznych promptow, modeli i workflowow na tej samej probce danych.

## Zakres

- execution mode: `kaggle_notebook`
- status: `draft`
- docelowy output: `report`

## Rola w lancuchu

```text
enrichment -> verification -> curation -> export
     |
     +--> benchmark-comparison (rownolegly, diagnostyczny)
```

Ten pack ma:

- definiowac stabilna probke testowa dla `Project 13`,
- uruchamiac rozne warianty promptow, modeli i workflowow na tej samej probce,
- porownywac wyniki wzgledem metryk jakosci, kosztu i czasu,
- zostawiac jawny benchmark report z reusable wynikami,
- nie modyfikowac kanonicznego katalogu ani downstream artefaktow.

## Najwazniejsza roznica wzgledem innych packow

- `enrichment` produkuje kandydatow do lancucha
- `verification` sprawdza poprawnosc kandydatow
- `curation` decyduje o przyjeciu do katalogu
- `export` przebudowuje downstream artefakty
- `benchmark-comparison` jest diagnostyczny: nie produkuje kandydatow do katalogu, tylko porownuje metody pracy

## Wejscie dla kolejnego agenta

Zacznij od:

1. `manifest.json`
2. `RUNBOOK.md`
3. `REVIEW_CHECKLIST.md`
4. `../CHAIN_MAP.md`
