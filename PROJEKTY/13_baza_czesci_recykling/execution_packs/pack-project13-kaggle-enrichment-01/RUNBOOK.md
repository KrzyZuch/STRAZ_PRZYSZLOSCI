# Runbook Wolontariusza Dla Pack Project13 Kaggle Enrichment 01

## Cel

Ten runbook prowadzi wolontariusza i jego lokalnego agenta przez pierwszy realny loop `KaggleNotebookPack` dla `Project 13`.

Docelowy przeplyw:

```text
fork -> Kaggle notebook -> branch na forku -> PR -> review -> merge
```

## Co trzeba miec przed startem

- konto `GitHub`
- wlasny fork repo `StrazPrzyszlosci/STRAZ_PRZYSZLOSCI`
- konto `Kaggle`
- notebook `PROJEKTY/13_baza_czesci_recykling/youtube-databaseparts.ipynb`
- sekrety ustawione w `Kaggle Secrets`

## Wymagane sekrety

- `GITHUB_PAT`: token z uprawnieniem pushu do Twojego forka
- `YOUTUBE_API_KEY`: klucz do YouTube Data API
- `GEMINI_API_KEY`: klucz do analizy multimodalnej

Nie zapisuj tych sekretow w repozytorium ani w tresci PR.

## Krok 1. Przygotuj fork

1. Otworz repo upstream `StrazPrzyszlosci/STRAZ_PRZYSZLOSCI`.
2. Utworz albo odswiez swoj fork.
3. Upewnij sie, ze mozesz pushowac do swojego forka przez PAT.

## Wariant lokalny: dry-run przed prawdziwym Kaggle runem

Zanim wolontariusz odpali prawdziwy notebook na `Kaggle`, maintainer albo lokalny agent moze wykonac suchy przebieg kontraktu packa:

```bash
python3 PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py
```

Ten dry-run:

- nie zuzywa sekretow wolontariusza ani zasobow `Kaggle`,
- buduje lokalny raport walidacyjny packa,
- generuje szkic PR oraz rekord `Run` i `Artifact` dla suchego przebiegu,
- pokazuje, czy kontrakt artefaktow i provenance jest juz gotowy do publicznego uruchomienia.

## Krok 2. Importuj notebook do Kaggle

1. Otworz `Kaggle`.
2. Utworz nowy notebook przez import pliku `youtube-databaseparts.ipynb`.
3. Przed uruchomieniem uzupelnij w komorce konfiguracyjnej:
   - `FORK_OWNER`
   - `GIT_USER_NAME`
   - `GIT_USER_EMAIL`
4. Nie zostawiaj placeholderow ani danych innej osoby.

## Krok 3. Ustaw sekrety

Dodaj w `Kaggle Secrets`:

- `GITHUB_PAT`
- `YOUTUBE_API_KEY`
- `GEMINI_API_KEY`

Notebook powinien uzyc tylko tych sekretow i tylko do deklarowanego celu packa.

## Krok 4. Uruchom notebook

1. Uruchom komorki po kolei.
2. Poczekaj na wygenerowanie plikow w `autonomous_test/`.
3. Sprawdz, czy notebook wygenerowal:
   - `processed_videos.json`
   - `results/test_db.jsonl`
   - `results/inventree_import.jsonl`
   - `results/ecoEDA_inventory.csv`
   - `reports/last_run_summary.md`

Jesli ktorys plik nie powstal, zatrzymaj sie i opisz to w raporcie runu oraz PR.

## Krok 5. Zweryfikuj wynik przed pushem

Przed pushem sprawdz:

- czy branch jest nowy i nalezy do Twojego forka
- czy commit author wskazuje Ciebie albo adres `noreply`
- czy raport runu opisuje zakres danych i known issues
- czy w artefaktach nie ma sekretow, plikow tymczasowych ani pobranych filmow

## Krok 6. Push do forka

Notebook powinien:

- utworzyc branch o nazwie podobnej do `pack-project13-kaggle-enrichment-<timestamp>`
- dodac tylko artefakty review-ready
- wypchnac branch do `origin`, czyli do Twojego forka

Upstream nie powinien byc celem pushu z poziomu notebooka.

## Krok 7. Otworz PR

1. Na GitHubie otworz PR z brancha forka do `StrazPrzyszlosci/STRAZ_PRZYSZLOSCI`.
2. Skopiuj tresc z `PR_TEMPLATE.md`.
3. Wklej link do notebooka Kaggle lub opisz identyfikator runu.
4. Dolacz ograniczenia i znane problemy.

## Krok 8. Zapisz kanoniczny rekord `Run` i opcjonalnie `Artifact`

Po wykonaniu notebooka i przed albo po otwarciu PR uruchom lokalnie:

```bash
python3 PROJEKTY/13_baza_czesci_recykling/scripts/create_execution_records.py \
  --fork-owner <twoj-login-github> \
  --run-ref kaggle://project13/<twoj-run-id> \
  --summary-ref PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/last_run_summary.md \
  --output-ref branch://<twoj-login-github>/pack-project13-kaggle-enrichment-<timestamp> \
  --artifact-storage-ref https://github.com/StrazPrzyszlosci/STRAZ_PRZYSZLOSCI/pull/<numer>
```

Skrypt zapisze rekord `Run` i, jesli podasz `--artifact-storage-ref`, rowniez rekord `Artifact` w katalogu:

- `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/records/`

## Krok 9. Czego nie robic

- nie pushuj bezposrednio do upstream
- nie commituj sekretow ani pelnych URL-i z tokenem
- nie podmieniaj autora commita na maintainera lub inna osobe
- nie promuj wynikow bez raportu runu i jawnego PR

## Minimalne kryterium sukcesu

Pack jest wykonany poprawnie, gdy:

- notebook przechodzi end-to-end na koncie wolontariusza
- wynik laduje na branchu w jego forku
- powstaje raport runu
- PR daje sie zreviewowac bez recznego odtwarzania calego przebiegu
