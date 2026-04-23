# Runbook Dla Pack Project13 Benchmark Comparison 01

## Cel

Ten pack pozwala porownywac rozne prompty, modele i workflowy na tej samej probce danych `Project 13`.

Docelowy przeplyw:

```text
fixed test sample -> variant A vs variant B -> metrics -> benchmark report -> PR
```

## Co trzeba miec przed startem

- konto `GitHub` i fork repo
- konto `Kaggle`
- klucz `GEMINI_API_KEY`
- opcjonalnie `YOUTUBE_API_KEY`, jesli benchmark wymaga odswiezenia probki discovery
- zdefiniowana probke testowa albo gotowosc do jej utworzenia

## Krok 1. Zdefiniuj probke testowa

1. Wybierz stabilny zestaw kandydatow z `autonomous_test/results/test_db.jsonl`.
2. Zapisz probke jako `benchmark_sample.jsonl` z jawnym lista recordow i ich ground-truth labelami.
3. Probka musi byc stala miedzy uruchomieniami, zeby wyniki byly porownywalne.

Jesli nie masz jeszcze stabilnej probki testowej, opisz kontrakt probki w benchmark report zamiast wymyslac dane z powietrza.

## Krok 2. Zdefiniuj warianty do porownania

Kazdy wariant powinien miec:

- nazwe: np. `prompt-v2-gemini-flash`, `prompt-v1-gemini-pro`,
- opis: co sie zmienia miedzy wariantami,
- konfiguracje: model, prompt template, parametry.

Przykladowe wymiary porownania:

- rozne prompty extraction parts,
- rozne modele multimodalne,
- rozne strategie OCR i frame check,
- rozne progi filtrowania kandydatow.

## Krok 3. Uruchom benchmark

1. Uruchom kazdy wariant na tej samej probce testowej.
2. Zbierz wyniki z kazdego przebiegu.
3. Oblicz metryki:
   - `precision`: ile z wygenerowanych kandydatow jest poprawnych,
   - `recall`: ile z oczekiwanych kandydatow zostalo znalezionych,
   - `false_positive_rate`: ile falszywych trafien na rekord,
   - `cost_per_record`: zuzycie tokenow API na rekord,
   - `time_per_record`: czas przetwarzania na rekord.

## Krok 4. Zapisz wyniki

1. Zapisz `benchmark_metrics.json` z metrykami dla kazdego wariantu.
2. Zapisz `benchmark_report.md` z:
   - opisem probki testowej,
   - opisem wariantow,
   - porownaniem metryk w formie tabeli,
   - wnioskami i rekomendacjami,
   - jawnymi ograniczeniami benchmarku.

## Krok 5. Otworz PR

1. Stworz branch z zakresie benchmark.
2. Commituj raport, metryki i probke testowa.
3. Otworz PR do upstream z trescia z `PR_TEMPLATE.md`.

## Czego pack nie powinien robic

- nie powinien modyfikowac kanonicznego katalogu
- nie powinien generowac kandydatow do lancucha kuracji
- nie powinien uruchamiac exportu downstream
- nie powinien automatycznie promowac wynikow benchmarku do katalogu

## Aktualny status

To jest pack `draft`.

Na obecnym etapie:

- kontrakt dokumentacyjny jest gotowy,
- outputy, metryki i acceptance criteria sa nazwane,
- nadal trzeba wydzielic stabilna probke testowa i realny execution surface benchmarku,
- pierwszy realny run wymaga dostepu do wynikow enrichment i definicji ground-truth.

## Minimalne kryterium sukcesu

Pack bedzie gotowy do pierwszego realnego uruchomienia, gdy:

- bedzie mial stala probke testowa z ground-truth,
- bedzie mial jasne metryki porownawcze,
- reviewer dostanie raport zamiast pojedynczych intuicji.
