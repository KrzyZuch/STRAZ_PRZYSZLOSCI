# 21. Home Assistant na Starym Smartfonie (Węzeł NSIP)

## **Intelekt wyprzedza Kapitał!**

## Wizja Projektu
Każdy stary smartfon zalegający w szufladzie to potężny komputer z wbudowanym ekranem, baterią (UPS), Wi-Fi, Bluetooth i zestawem sensorów. Projekt **"Węzeł NSIP"** pozwala każdemu obywatelowi w kilka minut przekształcić taki telefon w lokalne centrum inteligentnego domu oparte na **Home Assistant**, które jest fabrycznie zintegrowane z inicjatywą **Straży Przyszłości**.

Dzięki temu rozwiązaniu:
1. **Odzyskujemy zasoby:** Zamiast kupować nowe urządzenia (np. Raspberry Pi), wykorzystujemy istniejący e-waste.
2. **Budujemy sieć:** Każdy użytkownik może (opcjonalnie) udostępniać zanonimizowane dane (np. jakość powietrza, temperatura zewnętrzna) do wspólnego API NSIP, budując mapę potencjału kraju.
3. **Automatyzujemy codzienność:** Użytkownik zyskuje darmowe, profesjonalne narzędzie do zarządzania własnym domem, energią i bezpieczeństwem.

## Jak to działa? (Szybki start)

### Krok 1: Instalacja środowiska
Wykorzystujemy **Termux** (emulator terminala na Androida), aby uruchomić pełną instancję Home Assistant.
- Instalacja Pythona i zależności.
- Uruchomienie `hass` (Home Assistant Core).

### Krok 2: Integracja NSIP
Do standardowego Home Assistanta dodajemy dedykowany "NSIP Bridge" (w formie custom_component lub skryptu Python), który:
- Rejestruje urządzenie jako **Węzeł Straży Przyszłości**.
- Łączy się z naszym API na Cloudflare.
- Pozwala na odbieranie "rekomendacji narodowych" (np. optymalne godziny ładowania urządzeń w oparciu o stan sieci energetycznej).

### Krok 3: Wykorzystanie sensorów telefonu
Dzięki aplikacji **Home Assistant Companion**, wbudowane sensory telefonu (akcelerometr, barometr, światło, stan baterii) stają się encjami w systemie, które można wykorzystać do lokalnych automatyzacji.

## Dlaczego to jest ważne dla Inicjatywy?
- **Masowość:** To najprostsza ścieżka wejścia do Straży Przyszłości dla przeciętnego użytkownika.
- **Rozproszona moc obliczeniowa:** Tysiące smartfonów tworzą potężną sieć brzegową (Edge Computing), która może lokalnie przetwarzać dane bez obciążania centralnych serwerów.
- **Edukacja:** Użytkownicy uczą się obsługi otwartych technologii, co buduje suwerenność technologiczną społeczeństwa.

## Instrukcja Techniczna (Draft)

1. Zainstaluj **Termux** (najlepiej z F-Droid).
2. Wykonaj komendy:
   ```bash
   pkg update && pkg upgrade
   pkg install python pillow libjpeg-turbo libxml2 libxslt
   pip install homeassistant
   hass
   ```
3. Po uruchomieniu wejdź na `http://localhost:8123`.
4. Skopiuj plik integracji `nsip_integration.py` do folderu konfiguracji.

## Kierunki rozwoju
- **Wstępnie skonfigurowany obraz:** Gotowy instalator "jeden klik", który konfiguruje wszystko za użytkownika.
- **Panel Strażnika:** Dedykowany dashboard w Home Assistant, pokazujący postępy inicjatywy i lokalne zadania do wykonania.
- **Głosowy Asystent NSIP:** Wykorzystanie mikrofonu telefonu do lokalnego sterowania domem bez wysyłania głosu do chmury (Local AI).

---
*Budujemy Polską Niepodległość Technologiczną — smartfon po smartfonie.*
