# Demo: Inteligentna Akwakultura

Ten katalog zawiera minimalny, działający przepływ demonstracyjny dla pilotażu stawu hodowlanego.

## Co pokazuje demo

Demo spina:

- dane przykładowe ze `data/sample/`,
- mock providera,
- przykładowego zewnętrznego `provider-a`,
- normalizację do wspólnego schematu,
- model rekomendacyjny dla stawu hodowlanego,
- wynik analityczny zgodny z `fish_pond_v1`.

To jest referencyjny przepływ:

```text
sample data -> adapter -> validate -> model -> recommendation
```

## Jak uruchomić

Uruchom z katalogu głównego repozytorium:

```bash
python3 pipelines/demo/run_demo.py
```

## Co powinno się wydarzyć

Skrypt wypisze:

- status mock providera,
- wynik demo dla mock providera,
- wynik demo dla `provider-a`.

Najważniejsza rzecz do sprawdzenia: dwa różne źródła danych po normalizacji powinny przejść przez ten sam model i dać spójny typ wyniku.

## Jak uruchomić testy

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Do czego to służy w praktyce

Ten katalog ma być pierwszym punktem wejścia dla nowych Strażników Przyszłości, którzy chcą:

- zrozumieć wspólny schemat,
- zobaczyć jak działa adapter providera,
- dodać nowe `reason_codes`,
- poprawić logikę modelu,
- przygotować własny provider albo własny węzeł pomiarowy.
