# Pack Project13 Curation 01

To jest pack dla `curation chain` w `Project 13`.

Jego celem nie jest discovery, OCR ani eksport downstream.
Jego celem jest formalizacja etapu review i kuracji kandydatow, ktorzy przeszli przez verification, przed dopuszczeniem do kanonicznego katalogu.

## Zakres

- execution mode: `local_agent`
- status: `draft`
- docelowy output: `pull_request`

## Rola w lancuchu

```text
enrichment -> verification -> curation -> export
```

Ten pack ma:

- przyjmowac zweryfikowanych kandydatow z etapu verification,
- porzadkowac ich do kanonicznych schematow katalogu (`devices.jsonl`, `parts_master.jsonl`, `device_parts.jsonl`),
- oznaczac kandydatow jako `ready_for_catalog` albo `needs_more_work`,
- zostawiac jawny audit trail decyzji kuracyjnych,
- otwierac PR do kanonicznego katalogu z czytelnym opisem decyzji.

## Najwazniejsza roznica wzgledem packow verification i export

- `verification` sprawdza, czy kandydaci sa poprawni wzgledem zrodla
- `curation` decyduje, czy kandydaci nadaja sie do kanonicznego katalogu i jak ich ukladac
- `export` przebudowuje downstream artefakty z juz przyjetego katalogu

Bez curation review i kuracja pozostalyby niejawnym krokiem miedzy packami.

## Wejscie dla kolejnego agenta

Zacznij od:

1. `manifest.json`
2. `RUNBOOK.md`
3. `REVIEW_CHECKLIST.md`
4. `../CHAIN_MAP.md`
