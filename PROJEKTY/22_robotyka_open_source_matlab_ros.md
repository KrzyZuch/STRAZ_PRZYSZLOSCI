# 22. Robotyka Open Source (MathWorks / ROS)

## **Intelekt wyprzedza Kapitał!**

## Wizja projektu

Firma MathWorks udostępniła repozytorium GitHub o otwartym kodzie źródłowym, wypełnione zasobami związanymi z robotyką, dla wszystkich zainteresowanych zdobyciem praktycznej wiedzy. Dla Straży Przyszłości ten katalog nie jest celem samym w sobie — jest **warstwą gotowych ogniw** skracającą drogę od koncepcji do prototypu ramienia robota, pojazdu naziemnego (UGV) lub drona.

Zgodnie z wizją NSIP: **AI + darmowa energia (OZE) + nadmiarowy materiał (recykling, elektrośmieci)** przekształcane są w automatyzację i produkty na rzecz społeczeństwa. Robotyka open source dostarcza sprawdzonych wzorców sterowania, symulacji i integracji, które można zaadoptować przy minimalnym kapitale — zamiast budować cały stos od zera.

To uzupełnia wizję **samopowielającej się platformy** z głównego README: zaawansowane ramię zintegrowane z CNC lub drukarką 3D potrzebuje nie tylko elektroniki (projekty 12–13), lecz także gotowych ścieżek nawigacji, ROS i symulacji.

## Źródło: awesome-matlab-robotics

- **Repozytorium:** [mathworks-robotics/awesome-matlab-robotics](https://github.com/mathworks-robotics/awesome-matlab-robotics)
- **Charakter:** kuratorowany indeks przykładów, tutoriali i projektów — dobrze udokumentowany, z linkami ułatwiającymi przejście od koncepcji do prototypu.

### Co zawiera katalog

- **Manipulatory i mobilność:** przykłady ramion robotów, pojazdów naziemnych i dronów.
- **ROS i ROS2:** projekty pokazujące, jak łączyć się z ekosystemem ROS; wdrażanie modeli Simulink bezpośrednio jako węzły ROS.
- **Symulacja zaawansowana:** modelowanie środowisk terenowych, testowanie algorytmów nawigacji w fotorealistycznych symulacjach.
- **Edukacja:** samouczki i ścieżki „tutorial → prototyp”.

## Mapowanie na projekty NSIP

| Obszar NSIP | Projekt | Jak wykorzystać zasób |
|-------------|---------|------------------------|
| Maszyny rolnicze, nawigacja CV | [08. OpenBot](08_openbot_autonomiczne_maszyny_rolnicze.md) | Wzorce nawigacji, omijania przeszkód, floty tanich robotów |
| Transport, trasy | [18. Automatyzacja Transportu](18_automatyzacja_transportu_i_logistyki.md) | UGV, planowanie tras, symulacje terenu |
| Hardware z odzysku | [17. Elektrośmieci → Hardware](17_autonomiczne_przetwarzanie_elektrosmieci_na_hardware.md) | Sterowniki z recyklingu + warstwa wykonawcza (silniki, serwa) |
| Edge brain | [06. Smartfony jako Sterowniki](06_smartfony_jako_sterowniki.md), [07. Platforma Sterowania](07_uniwersalna_platforma_sterowania.md) | Most smartfon/ESP ↔ ROS2 jako węzeł niskokosztowy |
| Mechanika zespołów | [23. Katalog STEP](23_katalog_czesci_step_open_source.md) | Mocowania, reduktory, profile pod konstrukcję ramienia/UGV |

## Ścieżka adopcji (etapowa)

Repozytorium MathWorks traktujemy jak **warstwę RAG i resource scoutingu**, nie jako natychmiastowy fork całego kodu do monorepo NSIP.

### Etap 1 — Scouting (niski koszt)

- Wybrać 10–20 pozycji z katalogu pod polskie piloty: rolnictwo (OpenBot), logistyka (UGV), stacja testowa z odzysku.
- Zbudować tabelę: **problem NSIP → link do demo → wymagane licencje (MATLAB / tylko ROS)**.
- Dodać skrócone opisy do kontekstu agentów planujących (README, ten dokument, `docs/PRZYKLADY_GOTOWEGO_KODU.md`).

### Etap 2 — Pilot (jeden wąski use-case)

Przykładowe pilotaże (wybór jednego na start):

- symulacja nawigacji w środowisku terenowym (bez fizycznego robota),
- most ROS2 ↔ sterownik ESP/smartfon z projektu 06/07,
- analiza jednego tutoriala ramienia pod BOM z [step.parts](23_katalog_czesci_step_open_source.md).

### Etap 3 — Integracja (po review)

- Jawna ocena licencji i zależności (MATLAB/Simulink vs czysty ROS/Python).
- Oddzielenie **wzorców architektonicznych** (do kopiowania koncepcji) od **kodu do deploy** (wymagającego pełnego stacku MathWorks).
- Powiązanie z execution packami dopiero po pozytywnym przeglądzie technicznym.

## Ograniczenia i zasady

- **Część materiałów wymaga ekosystemu MathWorks** (MATLAB, Simulink). Wkład Strażnika może polegać na kuracji i dokumentacji alternatyw czysto-ROS bez płatnej licencji.
- **Nie klonujemy** całego repozytorium awesome-list do monorepo — linkujemy, opisujemy, adaptujemy wybrane ogniwa.
- Priorytet: rozwiązania zgodne z **open-source**, niskim CAPEX i zasilaniem OZE (np. solarne platformy jak Acorn w projekcie 08).

## Zadania dla Strażników

1. **Kuracja pilotów:** 10–20 linków z README awesome-matlab-robotics z przypisaniem do projektów 08, 17, 18.
2. **Tabela zgodności licencji:** które dema działają bez MATLAB (tylko ROS2 / Gazebo / inne).
3. **Most NSIP:** jednostronicowy „ścieżka od filmu/tutorialu do listy części z recyklingu + STEP”.
4. **Resource scouting:** wpisy do backlogu Issues z tagiem `resource-scouting` i linkiem do konkretnego podprojektu w katalogu MathWorks.

## Zasoby techniczne

- **Główny katalog:** [awesome-matlab-robotics](https://github.com/mathworks-robotics/awesome-matlab-robotics)
- **Powiązane w NSIP:** [OpenBot](08_openbot_autonomiczne_maszyny_rolnicze.md), [Acorn Rover](08_openbot_autonomiczne_maszyny_rolnicze.md) (Twisted Fields)
- **Analiza wzorca (3 pytania):** [docs/PRZYKLADY_GOTOWEGO_KODU.md](../docs/PRZYKLADY_GOTOWEGO_KODU.md) — sekcja awesome-matlab-robotics

---
*Intelekt wyprzedza Kapitał!*
