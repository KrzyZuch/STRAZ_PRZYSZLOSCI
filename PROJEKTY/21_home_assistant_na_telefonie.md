# 21. Home Assistant na Starym Smartfonie (Węzeł NSIP)

## **Intelekt wyprzedza Kapitał!**

## Wizja Projektu
Każdy stary smartfon zalegający w szufladzie to potężny komputer z wbudowanym ekranem, baterią (UPS), Wi-Fi, Bluetooth i zestawem sensorów. Projekt **"Węzeł NSIP"** pozwala każdemu obywatelowi w kilka minut przekształcić taki telefon w lokalne centrum inteligentnego domu oparte na **Home Assistant**, które jest fabrycznie zintegrowane z inicjatywą **Straży Przyszłości**.

Dzięki temu rozwiązaniu:
1. **Odzyskujemy zasoby:** Zamiast kupować nowe urządzenia (np. Raspberry Pi), wykorzystujemy istniejący e-waste.
2. **Budujemy sieć:** Każdy użytkownik może (opcjonalnie) udostępniać zanonimizowane dane (np. jakość powietrza, temperatura zewnętrzna) do wspólnego API NSIP, budując mapę potencjału kraju.
3. **Automatyzujemy codzienność:** Użytkownik zyskuje darmowe, profesjonalne narzędzie do zarządzania własnym domem, energią i bezpieczeństwem.

## Ścieżki wdrożenia (Wybierz swoją)

### 🟢 Ścieżka 1: Najprostsza (Dla każdego)
**Metoda:** Oficjalna aplikacja **Home Assistant Companion**.
Idealna do szybkiego onboarding'u i wykorzystania telefonu jako panelu sterowania oraz zestawu sensorów.

1. Zainstaluj [Home Assistant Companion](https://play.google.com/store/apps/details?id=io.homeassistant.companion.android) ze sklepu Play.
2. **Co zyskujesz od razu:**
   - Pełny dashboard HA na ekranie telefonu (tryb kiosku).
   - Udostępnianie sensorów (bateria, WiFi, lokalizacja, światło, akcelerometr) do sieci NSIP.
   - Możliwość wykorzystania kamery jako monitoringu (np. dla akwakultury).
   - Obsługa wake word (asystent Assist).

### 🟡 Ścieżka 2: Zaawansowana (Dedykowany Serwer)
**Metoda:** Instalacja **Home Assistant Core** bezpośrednio na Androidzie (bez roota).
Zmienia telefon w samodzielny serwer, który może działać 24/7.

- **[HomeAssistant-Termux](https://github.com/huytungst/HomeAssistant-Termux):** Gotowe skrypty instalacyjne HA Core + Matter Server + Wyoming (głos).
- **[termux-home-assistant-installer](https://github.com/talss89/termux-home-assistant-installer):** Automatyczny instalator HA Core dla aarch64.
- **[postmarketOS](https://bryansplace.github.io):** Prawdziwy Linux na telefonie. Umożliwia uruchomienie Docker'a i pełnej instancji HA.

### 🔵 Ścieżka 3: Bluetooth Proxy i Satelita (Infrastruktura IoT)
Zmienia telefon w "przedłużacz" sygnału dla inteligentnych urządzeń BLE w terenie.

- **[homeassistant-mobile-ble-proxy](https://github.com/Zen3515/homeassistant-mobile-ble-proxy):** Zamienia telefon w Bluetooth Proxy dla HA/ESPHome. Działa w tle, przekazując dane z czujników BLE.
- **[Ava](https://github.com/brownard/Ava):** Zaawansowany asystent głosowy i satelita ESPHome w jednym.

## Dlaczego to jest ważne dla Inicjatywy?
- **Masowość:** Najprostsza ścieżka wejścia dla przeciętnego użytkownika przez Google Play.
- **Rozproszona moc obliczeniowa:** Tysiące smartfonów tworzą sieć brzegową (Edge Computing).
- **Bluetooth Mesh:** Telefony w roli Bluetooth Proxy tworzą suwerenną sieć łączności z czujnikami (np. w rolnictwie czy medycynie).

## Kierunki rozwoju
- **Panel Strażnika:** Dedykowany dashboard HA pokazujący postępy NSIP.
- **Głosowy Asystent NSIP:** Lokalna kontrola bez chmury (Local AI).
- **Integracja z Meshtastic:** Wykorzystanie telefonu jako bramki między siecią Mesh a Home Assistantem.

---
*Budujemy Polską Niepodległość Technologiczną — smartfon po smartfonie.*
