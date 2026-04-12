# Architektura Węzłów Pomiarowych

## Cel dokumentu

Ten dokument opisuje, jak w ekosystemie Straży Przyszłości rozumiane są węzły pomiarowe oraz jaką rolę mogą odgrywać stare smartfony i niskokosztowe konfiguracje społecznościowe.

## Rola węzła pomiarowego

Węzeł pomiarowy to dowolna konfiguracja sprzętowo-programowa zdolna do:

- pozyskania pomiaru,
- oznaczenia go w czasie,
- przypisania go do źródła lub obiektu obserwacji,
- znormalizowania go do wspólnego schematu,
- przekazania go do API Straży Przyszłości,
- odebrania wyniku analitycznego do dalszej interpretacji i dokumentacji.

Węzeł pomiarowy nie musi być urządzeniem przemysłowym. Może być prostą konstrukcją społeczną, jeżeli jest dobrze opisana i potrafi współpracować z API.

## Stare smartfony jako bramki danych

Stary smartfon może pełnić rolę taniej bramki danych, ponieważ łączy:

- łączność,
- zegar systemowy,
- lokalną pamięć,
- możliwość uruchamiania aplikacji integracyjnych,
- kamerę, GPS i inne sensory pomocnicze,
- łatwość dokumentowania eksperymentów w terenie.

W praktyce smartfon może:

- odbierać dane z zewnętrznych czujników,
- wykonywać wstępną walidację,
- uzupełniać metadane pomiaru,
- wysyłać dane do wspólnego API,
- odbierać wynik analityczny i zapisywać go jako część obserwacji terenowej.

## Typy węzłów pomiarowych

### Węzeł społecznościowy

Budowany niskim kosztem przez członka społeczności. Może bazować na starym smartfonie, prostych czujnikach oraz lekkim adapterze.

### Węzeł gospodarstwa

Konfiguracja należąca do gospodarstwa lub hodowli, używana do systematycznego przesyłania danych do wspólnej warstwy wiedzy.

### Węzeł partnerski

Konfiguracja związana z partnerem zewnętrznym, który przekazuje dane z własnej infrastruktury przez adapter zgodny z API.

## Wzorzec przepływu danych

Docelowy przepływ powinien wyglądać następująco:

```text
czujnik -> węzeł pomiarowy -> adapter -> wspólny schemat -> model -> wynik analityczny -> dokumentacja i baza wiedzy
```

Najważniejsze jest to, że warstwa modeli nie zna konkretnego sprzętu ani natywnego formatu danego czujnika.

## Pilotaż stawu hodowlanego

W kontekście pierwszego pilota węzeł pomiarowy powinien umieć zebrać lub przekazać co najmniej:

```text
pond_id
measurement_time
water_temperature
dissolved_oxygen
pH
optional ammonia
optional flow_rate
```

Wynik zwrotny z systemu powinien być zapisywany jako materiał analityczny:

```text
risk_level
recommendation
confidence
reason_codes
provider_id
schema_version
```

Zwrot ten ma wspierać interpretację danych i budowę wspólnej wiedzy. Nie jest definiowany jako mechanizm zdalnego sterowania urządzeniami.

## Wymagania dokumentacyjne dla społeczności

Każda konfiguracja węzła pomiarowego opisywana w repozytorium powinna dokumentować:

- jaki obiekt obserwuje,
- jakie pomiary zbiera,
- z jakich komponentów korzysta,
- jak dane są mapowane do wspólnego schematu,
- jakie są ograniczenia i warunki pracy,
- czy dane są rzeczywiste, testowe czy symulowane.

To właśnie dokumentacja czyni z pojedynczego eksperymentu trwały wkład do Narodowych Sił Intelektualnych.

## Zasada końcowa

Węzły pomiarowe mają służyć demokratyzacji pozyskiwania danych i rozbudowie bazy wiedzy Straży Przyszłości. Stare smartfony nie są tu ciekawostką, lecz realnym, niskokosztowym narzędziem wejścia do systemu dla społeczności.
