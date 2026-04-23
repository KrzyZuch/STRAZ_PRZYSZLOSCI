# Chain Map Dla Execution Packow Project 13

Ten dokument opisuje, jak obecne i planowane execution packi ukladaja sie w wiekszy workflow `Project 13`.

## Dlaczego to istnieje

`Project 13` nie moze zostac sklejony z jednym notebookiem i jednym packiem.
Z punktu widzenia calej inicjatywy potrzebujemy mniejszych, czytelnych jednostek pracy, ktore:

- maja rozny koszt uruchomienia,
- daja sie delegowac roznych osobom i agentom,
- zostawiaja jawne handoff points,
- nie mieszaja discovery, verification i exportu w jednym kroku.

## Wyzszy cel organizacji

Rozbicie packow nie jest celem samym w sobie. Sluzy ono:

- zamianie pojedynczego pilota w reusable architecture dla rozproszonej pracy wolontariuszy z agentami,
- dekompozycji pracy na mniejsze, rownolegle odpalane jednostki wykonawcze,
- budowie warstwy, w ktorej nowe zasoby obliczeniowe i nowe kierunki da sie podpinac bez przepisywania calego lancucha,
- ochronie przed zawlaszczeniem pracy wolontariuszy przez jawne handoff points i audit trail.

## Aktualna mapa

```text
                        pack-project13-kaggle-enrichment-01
                                   |
                      +------------+------------+
                      |                         |
pack-project13-kaggle-verification-01    pack-project13-benchmark-comparison-01
                      |                   (diagnostyczny, rownolegly)
                      |
pack-project13-curation-01
                      |
pack-project13-catalog-export-01
```

## Zaleznosci miedzy packami

| Pack | Upstream | Downstream | Status |
|------|----------|------------|--------|
| `enrichment-01` | brak | `verification-01`, `benchmark-comparison-01` | `active` |
| `verification-01` | `enrichment-01` | `curation-01` | `draft` |
| `curation-01` | `verification-01` | `catalog-export-01` | `draft` |
| `catalog-export-01` | `curation-01` | brak | `ready` |
| `benchmark-comparison-01` | `enrichment-01` | brak | `draft` |

Zaleznosci oznaczaja: output upstream packa jest wejsciem downstream packa.
Pack `benchmark-comparison-01` jest rownolegly i diagnostyczny - nie jest czescia glownego lancucha produkcyjnego, ale korzysta z wynikow `enrichment-01` jako probki testowej.

## Packi i ich role

### `pack-project13-kaggle-enrichment-01`

- status: `active`
- execution mode: `kaggle_notebook`
- rola: discovery i enrichment kandydatow czesci z materialow YouTube
- glowny output: kandydaci review-ready, raport runu, `Run record`, branch do `PR`
- handoff point: wynik trafia do verification albo benchmarku

### `pack-project13-kaggle-verification-01`

- status: `draft`
- execution mode: `kaggle_notebook`
- rola: twardsza weryfikacja kandydatow przez frame check, OCR i scoring rozbieznosci
- glowny output: `verified_candidates`, `verification_report`, `disagreement log`
- handoff point: wynik trafia do curation, a nie bezposrednio do downstream exportow

### `pack-project13-curation-01`

- status: `draft`
- execution mode: `local_agent`
- rola: formalizacja review i kuracji kandydatow z verification do kanonicznego katalogu
- glowny output: `curation_decisions.jsonl`, `curation_report.md`, zaktualizowane `devices.jsonl`, `parts_master.jsonl`, `device_parts.jsonl`
- handoff point: wynik trafia do exportu dopiero po przyjeciu kandydatow do katalogu

### `pack-project13-catalog-export-01`

- status: `ready`
- execution mode: `local_agent`
- rola: przebudowa downstream exportow z kanonicznego katalogu GitHub-first po review
- glowny output: `inventory.csv`, `recycled_parts_seed.sql`, `mcp_reuse_catalog.json`, `inventree_import.jsonl`
- handoff point: wynik trafia do review jako diff eksportow i log walidacyjny

### `pack-project13-benchmark-comparison-01`

- status: `draft`
- execution mode: `kaggle_notebook`
- rola: porownywanie promptow, modeli i workflowow na tej samej probce danych
- glowny output: `benchmark_report.md`, `benchmark_metrics.json`, `benchmark_sample.jsonl`
- handoff point: wynik jest diagnostyczny, nie modyfikuje kanonicznego katalogu ani downstream artefaktow

## Dlaczego tak dzielimy lancuch

- `enrichment` sluzy do pozyskania i uporzadkowania kandydatow
- `verification` sluzy do obnizenia ryzyka falszywych trafien i jawnego pokazania rozbieznosci
- `curation` sluzy do formalizacji decyzji o przyjeciu kandydatow do kanonicznego katalogu
- `export` sluzy do mechanicznej przebudowy artefaktow downstream dopiero po review zrodlowych danych
- `benchmark-comparison` sluzy do budowy reusable capability porownywania metod pracy

Ten podzial chroni projekt przed trzema zlymi wzorcami:

- jednym wielkim notebookiem, ktory robi wszystko i trudno go reviewowac
- bezposrednim przejsciem od sygnalu do downstream exportu bez czytelnego etapu sprawdzenia
- niejawna, nieauditowalna decyzja o tym, co trafia do kanonicznego katalogu

## Co nadal jest brakujace

- rozdzielenie wykonawcze `verification` od obecnego notebooka `youtube-databaseparts.ipynb`
- realny execution surface dla `curation` (skrypt do automatycznego ukladania kandydatow do schematow katalogu)
- stabilna probka testowa z ground-truth labelami dla `benchmark-comparison`
- pierwszy realny run nowych packow poza samym szkieletem dokumentacyjnym
- osobny pack `discovery chain`, jesli hunting filmow ma byc wydzielony z `enrichment`
