# Chain Map Dla Execution Packow Project 13

Ten dokument opisuje, jak obecne i planowane execution packi ukladaja sie w wiekszy workflow `Project 13`.

## Dlaczego to istnieje

`Project 13` nie moze zostac sklejony z jednym notebookiem i jednym packiem.
Z punktu widzenia calej inicjatywy potrzebujemy mniejszych, czytelnych jednostek pracy, ktore:

- maja rozny koszt uruchomienia,
- daja sie delegowac roznych osobom i agentom,
- zostawiaja jawne handoff points,
- nie mieszaja discovery, verification i exportu w jednym kroku.

## Aktualna mapa

```text
pack-project13-kaggle-enrichment-01
  -> pack-project13-kaggle-verification-01
  -> review / curation przez czlowieka albo lokalnego agenta
  -> pack-project13-catalog-export-01
```

## Packi i ich role

### `pack-project13-kaggle-enrichment-01`

- status: `active`
- execution mode: `kaggle_notebook`
- rola: discovery i enrichment kandydatow czesci z materialow YouTube
- glowny output: kandydaci review-ready, raport runu, `Run record`, branch do `PR`

### `pack-project13-kaggle-verification-01`

- status: `draft`
- execution mode: `kaggle_notebook`
- rola: twardsza weryfikacja kandydatow przez frame check, OCR i scoring rozbieznosci
- glowny output: `verified_candidates`, `verification_report`, `disagreement log`
- handoff point: wynik trafia do review / curation, a nie bezposrednio do downstream exportow

### `pack-project13-catalog-export-01`

- status: `ready`
- execution mode: `local_agent`
- rola: przebudowa downstream exportow z kanonicznego katalogu GitHub-first po review
- glowny output: `inventory.csv`, `recycled_parts_seed.sql`, `mcp_reuse_catalog.json`, `inventree_import.jsonl`
- handoff point: wynik trafia do review jako diff eksportow i log walidacyjny

## Dlaczego tak dzielimy lancuch

- `enrichment` sluzy do pozyskania i uporzadkowania kandydatow
- `verification` sluzy do obnizenia ryzyka falszywych trafien i jawnego pokazania rozbieznosci
- `export` sluzy do mechanicznej przebudowy artefaktow downstream dopiero po review zrodlowych danych

Ten podzial chroni projekt przed dwoma zlymi wzorcami:

- jednym wielkim notebookiem, ktory robi wszystko i trudno go reviewowac
- bezposrednim przejsciem od sygnalu do downstream exportu bez czytelnego etapu sprawdzenia

## Co nadal jest brakujace

- osobny pack `curation chain`, jesli review ma zostac bardziej sformalizowane
- rozdzielenie wykonawcze `verification` od obecnego notebooka `youtube-databaseparts.ipynb`
- pierwszy realny run nowych packow poza samym szkieletem dokumentacyjnym
