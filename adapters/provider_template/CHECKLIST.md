# Checklist Nowego Providera

Ta checklista służy do oceny, czy nowy provider danych może zostać włączony do wspólnego systemu Straży Przyszłości bez naruszania architektury repozytorium.

## 1. Dane wejściowe

- Czy provider potrafi dostarczyć identyfikator stawu `pond_id`?
- Czy provider przekazuje czas pomiaru `measurement_time`?
- Czy provider umie dostarczyć co najmniej temperaturę wody, natlenienie i pH?
- Czy dane są oznaczone jako `measured`, `estimated` albo `simulated`?
- Czy da się jednoznacznie wskazać źródło danych i provider `provider_id`?

## 2. Normalizacja

- Czy natywny format providera został opisany w dokumentacji adaptera?
- Czy `normalize()` mapuje dane do schematu `fish_pond_v1`?
- Czy model rekomendacyjny nie musi znać żadnego pola natywnego providera?
- Czy wynik po normalizacji przechodzi walidację bez obejść i wyjątków specyficznych dla jednego partnera?

## 3. Zdarzenia i analiza zachowania ryb

- Czy provider może przekazywać lekkie zdarzenia typu `fish_behavior_summary`?
- Czy zamiast surowego wideo przekazywane są metryki i wyniki analizy?
- Czy ewentualne referencje do klipów są tylko materiałem pomocniczym, a nie rdzeniem API?

## 4. Diagnostyka i zwrot wyników

- Czy adapter implementuje `check_status()`?
- Czy provider może odebrać wynik analityczny w czytelnej formie?
- Czy zwrot wyniku jest traktowany jako materiał analityczny i dokumentacyjny, a nie kanał sterowania urządzeniami?

## 5. Zgodność z architekturą NSI

- Czy integracja nie wymusza zmiany wspólnego schematu pod jednego providera?
- Czy w razie wycofania providera repozytorium nadal pozostaje użyteczne?
- Czy adapter nie wprowadza uzależnienia od zamkniętej warstwy partnera?
- Czy provider respektuje zasady nazwy, marki i wielodostawcowości Straży Przyszłości?

## 6. Gotowość do merge

Nowy provider jest gotowy do włączenia dopiero wtedy, gdy:

- adapter implementuje cały kontrakt,
- istnieje przykładowy payload wejściowy,
- istnieje przykładowy wynik po normalizacji,
- demo lub test pokazuje poprawny przepływ,
- dokumentacja jasno opisuje ograniczenia i zakres wsparcia.
