# Model: Otwarte Standardy, Zamknięte Wdrożenia

## Cel dokumentu

Ten dokument opisuje model współpracy, który pozwala Straży Przyszłości rozwijać otwarty dorobek intelektualny bez uzależnienia od pojedynczego partnera, pojedynczego wdrożenia ani pojedynczego źródła danych.

Nie chodzi o prosty podział `open-source / closed-source`. Chodzi o świadome rozdzielenie:

- otwartej warstwy standardu, wiedzy i logiki,
- od zamkniętej warstwy danych operacyjnych, środowisk wdrożeniowych i prywatnych ustaleń partnerów.

## Co jest otwarte

Do otwartej warstwy Straży Przyszłości należą:

- dokumentacja strategii i integracji,
- publiczne schematy danych,
- publiczne API,
- adaptery referencyjne i szablony adapterów,
- tryb `mock`,
- modele referencyjne,
- dane przykładowe i przypadki demonstracyjne,
- zasady onboardingu providerów,
- architektura węzłów pomiarowych,
- metodologia budowy wspólnej bazy wiedzy.

Ta warstwa ma być rozwijana w repozytorium i dostępna dla społeczności.

## Co może pozostać zamknięte

Do warstwy zamkniętej mogą należeć:

- prywatne środowiska operacyjne partnerów,
- produkcyjne klucze dostępu i konfiguracje,
- dane nieprzeznaczone do upublicznienia,
- szczegóły wdrożeń komercyjnych,
- infrastruktura partnera,
- lokalne decyzje wykonawcze podejmowane poza repozytorium.

Zamknięte wdrożenie nie może jednak oznaczać zamknięcia wspólnego standardu ani zablokowania rozwoju warstwy publicznej.

## Dlaczego ten model chroni dorobek NSI

1. Standard danych nie jest własnością partnera.
2. Model logiczny nie zależy od natywnego formatu jednego providera.
3. Wycofanie partnera nie unieważnia dokumentacji, schematów ani doświadczeń zdobytych przez społeczność.
4. Społeczność może tworzyć własne źródła danych i własne adaptery bez proszenia kogokolwiek o zgodę.
5. Inicjatywa buduje trwały dorobek w repozytorium, a nie tylko jednorazowy projekt wdrożeniowy.

## Rola providerów

Provider nie musi być firmą. Providerem może być:

- partner komercyjny,
- gospodarstwo,
- autor czujników DIY,
- członek społeczności,
- laboratorium,
- instalacja pilotażowa,
- stary smartfon używany jako bramka pomiarowa.

To ważne, ponieważ model NSI ma wzmacniać realny wkład społeczności. Każdy, kto dostarcza pomiary do wspólnego schematu i odbiera wyniki analityczne, uczestniczy w budowie wspólnej bazy wiedzy.

## Rola wyników zwracanych przez system

Wyniki systemu:

- mają charakter analityczny,
- mają wspierać interpretację danych,
- mają zasilać proces walidacji i dokumentowania wiedzy,
- mają umożliwiać porównywanie przypadków i rozwój modeli.

Wyniki systemu nie są definiowane jako kanał zdalnego sterowania cudzymi urządzeniami. Jeżeli jakiś provider wykorzystuje je lokalnie w swojej własnej infrastrukturze, jest to warstwa zewnętrzna wobec repozytorium NSI.

## Przykład praktyczny

W pilotażu stawu hodowlanego:

- provider dostarcza pomiary wody,
- adapter mapuje je do wspólnego schematu,
- model generuje ocenę ryzyka i rekomendację,
- wynik wraca do providera oraz może zostać wykorzystany do dokumentowania przypadku w bazie wiedzy repozytorium.

Niezależnie od tego, czy providerem jest firma, gospodarstwo czy członek społeczności z własnym starym smartfonem, system powinien działać według tych samych reguł.

## Zasada końcowa

Otwarte mają być: standard, wiedza, logika, dokumentacja i referencyjna warstwa integracyjna.

Zamknięte mogą pozostać: dane prywatne, środowiska produkcyjne, sekrety i wdrożenia operacyjne partnerów.

W ten sposób Straż Przyszłości buduje własny, trwały dorobek open source bez oddawania jego centrum zewnętrznym podmiotom.
