# 23. Katalog części STEP Open Source (step.parts)

## **Intelekt wyprzedza Kapitał!**

## Wizja projektu

**step.parts** to wyszukiwalny katalog około **12 000** modeli STEP typu open source. Każdy wpis łączy kanoniczny plik STEP z metadanymi tworzonymi przez człowieka oraz zasobami podglądu. Dla Straży Przyszłości jest to **warstwa mechaniczna** uzupełniająca:

- [CERN KiCad Library](../README.md) (elektronika 2D — symbole, footprinty),
- [13. Baza części z recyklingu](13_baza_czesci_recykling/README.md) (komponenty elektroniczne z odzysku),
- [14. Autonomiczne CAD (MCP)](14_autonomiczne_projektowanie_3d_cad.md) (parametryczne modelowanie we FreeCAD).

Zasada NSIP pozostaje ta sama: **intelekt wyprzedza kapitał** — zamiast rysować każdą śrubę, nakrętkę i wspornik od zera, agent AI i Strażnik wybierają gotowe geometrie z katalogu, składają zespół w CAD i eksportują do produkcji (druk 3D, CNC).

Formuła inicjatywy: **AI + darmowa energia + zbędny / odzyskany materiał → korzyść dla społeczeństwa**. Części magazynowe i konstrukcyjne z step.parts obniżają koszt obudów, ram i stanowisk testowych zbudowanych przy projekcie [17. Hardware z elektrośmieci](17_autonomiczne_przetwarzanie_elektrosmieci_na_hardware.md).

## Źródło: step.parts

- **Strona:** [step.parts](https://step.parts)
- **Format:** pliki STEP (ISO 10303) — uniwersalny wymiana między FreeCAD, Fusion-style workflow i innymi CAD.
- **Metadane:** opisy i podglądy ułatwiają wyszukiwanie bez otwierania każdego pliku lokalnie.

## Kategorie komponentów (mapowanie na NSIP)

| Kategoria w katalogu | Przykłady | Zastosowanie w NSIP |
|---------------------|-----------|---------------------|
| Złącza i okucia | śruby, nakrętki, podkładki, kołki, dystanse, gwintowane | montaż obudów z odzysku, stacje testowe |
| Części magazynowe i konstrukcyjne | profile wytłaczane, płyty, wsporniki, geometria pomocnicza, obudowy | ramy OpenBot, wózki logistyczne, obudowy sterowników |
| Ruch i przenoszenie mocy | łożyska, koła zębate, koła pasowe, wały, paski, prowadnice liniowe | robotyka pomocnicza, CNC z recyklingu |
| Elektronika i termika | płytki rozwojowe, moduły, złącza, czujniki, radiatory, wentylatory | komplement do projektu 13 (warstwa 3D obok KiCad) |
| Siłowniki i robotyka | serwa, silniki, siłowniki, reduktory, hardware montażowy | [08. OpenBot](08_openbot_autonomiczne_maszyny_rolnicze.md), [22. Robotyka ROS](22_robotyka_open_source_matlab_ros.md) |

## Mapowanie na projekty NSIP

| Projekt | Rola step.parts |
|---------|-----------------|
| [14. CAD MCP](14_autonomiczne_projektowanie_3d_cad.md) | Import STEP do FreeCAD; składanie zespołów; eksport G-code / CNC |
| [17. Elektrośmieci → Hardware](17_autonomiczne_przetwarzanie_elektrosmieci_na_hardware.md) | Obudowy, wsporniki, stanowiska — bez drogich bibliotek komercyjnych |
| [13. Baza części recykling](13_baza_czesci_recykling/README.md) | Ten sam paradygmat katalogu: kanoniczny identyfikator + metadane (tu: warstwa 3D) |
| [08 / 22. Robotyka](08_openbot_autonomiczne_maszyny_rolnicze.md) | Mocowania NEMA, profile, elementy napędu |

## Ścieżka adopcji (etapowa)

### Etap 1 — Scouting

- Zdefiniować **BOM mechaniczny** dla jednego pilota (np. wspornik NEMA17 + śruby M3 + profil 2020).
- Wyszukać wpisy na step.parts; zapisać URL, nazwę, licencję (jeśli podana) w manifeście markdown w repo (bez masowego commitu plików STEP).

### Etap 2 — Pilot FreeCAD

- Jeden zespół: części pobrane z step.parts + własna geometria parametryczna z projektu 14.
- Eksport STEP i G-code; dokumentacja w Issues z załącznikiem zrzutu i listą użytych ID z katalogu.

### Etap 3 — Integracja (opcjonalna)

- Plik manifestu `data/mechanical/step_parts_manifest_v1.jsonl` (tylko linki i metadane, nie 12k plików).
- Powiązanie z agentem CAD: prompt „użyj śruby M3x12 z manifestu NSIP-STEP-xxx”.
- Skrypt pomocniczy w `skrypty_main/` dopiero po zatwierdzeniu formatu manifestu (poza tą iteracją dokumentacji).

## Zasady pracy z katalogiem

- **Licencja:** przed użyciem w produkcie publicznym sprawdzić licencję konkretnego wpisu (open source ≠ jedna uniwersalna licencja dla całego katalogu).
- **Nie commitujemy** całego archiwum STEP do repozytorium NSIP — przechowujemy **odniesienia** (URL, hash pliku, wersja).
- **Spójność z CSP:** brak osadzania ciężkich podglądów inline na stronach portalu; linki zewnętrzne w dokumentacji repo są OK.

## Zadania dla Strażników

1. **Mapa BOM:** tabela „pilot NSIP → kategoria step.parts → przykładowe zapytanie wyszukiwania”.
2. **Checklist licencji:** szablon review dla 5–10 najczęściej używanych części (śruby, NEMA17, profil aluminiowy).
3. **Integracja z 14:** krótki runbook importu STEP do FreeCAD (kroki CLI/GUI) w komentarzu do Issue lub w `docs/`.
4. **Powiązanie z 13:** propozycja pola `mechanical_step_url` w przyszłym schemacie katalogu części (tylko dokumentacja, bez migracji DB w tej iteracji).

## Zasoby techniczne

- **Katalog:** [step.parts](https://step.parts)
- **CAD w NSIP:** [14. Autonomiczne Projektowanie 3D](14_autonomiczne_projektowanie_3d_cad.md)
- **Analiza wzorca (3 pytania):** [docs/PRZYKLADY_GOTOWEGO_KODU.md](../docs/PRZYKLADY_GOTOWEGO_KODU.md) — sekcja step.parts

---
*Intelekt wyprzedza Kapitał!*
