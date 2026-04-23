# Mini-Handoff: ZADANIE_03_PROJECT13_NEXT_EXECUTION_PACKS

## Co zostalo zrobione

Utworzono dwa nowe execution packi dla `Project 13` i zaktualizowano dokumentacje lancucha:

### Nowe packi

1. **`pack-project13-curation-01`** - curation chain
   - scope: formalizacja review i kuracji kandydatow z verification do kanonicznego katalogu
   - execution mode: `local_agent`
   - status: `draft`
   - pliki: `manifest.json`, `RUNBOOK.md`, `PR_TEMPLATE.md`, `REVIEW_CHECKLIST.md`, `task.json`, `integrity_risk_assessment.json`, `readiness_gate.json`, `README.md`

2. **`pack-project13-benchmark-comparison-01`** - benchmark chain
   - scope: porownywanie promptow, modeli i workflowow na tej samej probce danych
   - execution mode: `kaggle_notebook`
   - status: `draft`
   - pliki: `manifest.json`, `RUNBOOK.md`, `PR_TEMPLATE.md`, `REVIEW_CHECKLIST.md`, `task.json`, `integrity_risk_assessment.json`, `readiness_gate.json`, `README.md`

### Zaktualizowane dokumenty

- `CHAIN_MAP.md` - pelna mapa 5 packow z wyzszym celem organizacji, diagramem zaleznosci, tabela upstream/downstream
- `PROJEKTY/13_baza_czesci_recykling/README.md` - odswiezony opis kolejnych packow
- `PROJEKTY/13_baza_czesci_recykling/docs/MODEL_WOLONTARIACKICH_NOTEBOOKOW_KAGGLE.md` - odswiezony opis kolejnych packow

## Jak nowe packi lacza sie z obecnym packiem enrichment

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

- `curation-01` przyjmuje output z `verification-01` (verified candidates, disagreement log)
- `curation-01` produkuje wejscie dla `catalog-export-01` (zaktualizowany kanoniczny katalog)
- `benchmark-comparison-01` korzysta z wynikow `enrichment-01` jako probki testowej, ale nie jest czescia glownego lancucha produkcyjnego

## Czego jeszcze brakuje przed pierwszym uruchomieniem

### Curation pack

- realny execution surface: skrypt do automatycznego ukladania kandydatow do schematow katalogu (`devices.jsonl`, `parts_master.jsonl`, `device_parts.jsonl`)
- dostep do wynikow packa verification (verification report + disagreement log z pierwszego realnego runu)
- decyzja, czy curation ma byc w pelni automatyczna, czy wymaga mandatory human review dla spornych przypadkow

### Benchmark-comparison pack

- stabilna probka testowa z ground-truth labelami (`benchmark_sample.jsonl`)
- definicja wariantow do porownania (konkretne prompty, modele, workflowy)
- realny execution surface: wydzielony notebook Kaggle albo tryb notebooka dla benchmarku

### Ogolnie

- rozdzielenie wykonawcze `verification` od obecnego notebooka `youtube-databaseparts.ipynb`
- pierwszy realny run kazdego z nowych packow poza szkieletem dokumentacyjnym
- osobny pack `discovery chain`, jesli hunting filmow ma byc wydzielony z `enrichment`

## Komendy walidacyjne

- parsowanie `manifest.json`: przeszlo dla obu nowych packow
- parsowanie `task.json`, `integrity_risk_assessment.json`, `readiness_gate.json`: przeszlo
- `git diff --check`: czysto
