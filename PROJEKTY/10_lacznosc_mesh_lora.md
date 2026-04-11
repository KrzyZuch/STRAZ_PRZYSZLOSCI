# 10. Łączność Mesh i LoRa w Gospodarce (MeshCore, Reticulum, Meshtastic)

## **Intelekt wyprzedza Kapitał!**

## Opis Projektu
Projekt zakłada budowę suwerennej, odpornej na awarie infrastruktury komunikacyjnej opartej na sieciach kratowych (Mesh). Fundamentem są **wbudowane systemy łączności smartfonów z odzysku** (GSM, LTE/4G, Wi-Fi, Bluetooth), które uzupełniamy technologią LoRa dla uzyskania ekstremalnych zasięgów. Wykorzystujemy "elektrośmieci" jako uniwersalne mosty komunikacyjne (Gateways), które mogą inteligentnie przełączać się między siecią komórkową a darmowymi sieciami Mesh w zależności od dostępności sygnału i kosztów.

W "Straży Przyszłości" sieć Mesh służy jako **Nerw Gospodarczy**, przesyłając dane z sensorów rolnych, informując o stanie sieci energetycznej oraz zabezpieczając komunikację bez polegania wyłącznie na zewnętrznych dostawcach.

## Filary Technologiczne i Gotowy Kod

### 1. Meshtastic – Gotowe Moduły Sterowania (Ekosystem Open-Source)
Wykorzystujemy wbudowane funkcjonalności Meshtastic, które eliminują potrzebę pisania oprogramowania układowego od zera:
- **[Remote Hardware Module](https://meshtastic.org/docs/configuration/modules/remote-hardware/):** Kluczowy moduł pozwalający na zdalne sterowanie pinami GPIO (przekaźnikami) przez sieć Mesh.
    - **Zastosowanie:** Zdalne włączanie pomp nawadniających (Projekt 01/08) lub otwieranie bram wirtualnych ogrodzeń (Projekt 02).
- **[Telemetry Module](https://meshtastic.org/docs/configuration/modules/telemetry/):** Automatyczne przesyłanie danych z czujników środowiskowych (temperatura, wilgotność gleby, ciśnienie).
    - **Zastosowanie:** Węzły monitorujące stan upraw i parametry w oborach (Projekt 09).
- **Integracja Python:** Wykorzystanie [Meshtastic Python API](https://github.com/meshtastic/python) do budowy automatyzacji (np. "jeśli wilgotność gleby < X, wyślij komendę do przekaźnika pompy").

### 2. Reticulum Network Stack (RNS) – Bezpieczny "Pipe" dla SCADA
Mimo że RNS jest ogólnego przeznaczenia, służy jako doskonały "tunel" dla danych sterowniczych w trudnych warunkach:
- **[Sideband](https://github.com/markqvist/Sideband):** Gotowy komunikator graficzny do bezpiecznej wymiany raportów technicznych i logistycznych między pracownikami dużych gospodarstw i zakładów.
- **Implementacja Transportowa:** Możliwość tunelowania protokołów przemysłowych (np. Modbus over Reticulum) w celu nadzorowania pracy magazynów energii (Projekt 05) w miejscach bez zasięgu komórkowego.

### 3. Łączność Hybrydowa: Smartfon jako "Brama Intelektualna"
Wykorzystujemy pełen stos komunikacyjny wbudowany w smartfony:
- **GSM/LTE/4G (Wbudowane):** Smartfon służy jako brama (Gateway), która zbiera dane z lokalnej sieci Mesh (Wi-Fi/BT/LoRa) i przesyła je do centralnych systemów analitycznych NSI przez sieć komórkową, gdy ta jest dostępna.
- **[Briar](https://github.com/briar/briar) & P2P Protocols:** Wykorzystanie Bluetooth i Wi-Fi do tworzenia lokalnych, darmowych sieci bez dostępu do Internetu. Pozwala to na darmową wymianę danych sensorowych i wiadomości w obrębie gospodarstwa.
- **Wi-Fi Aware / Wi-Fi Direct:** Tworzenie dynamicznych sieci "telefon-do-telefonu" przez natywne funkcje Androida, co pozwala na przekazywanie informacji (np. z Projektu 09) przez kolejne urządzenia aż do punktu z zasięgiem LTE lub LoRa.
- **[MeshCore Firmware](https://github.com/meshcore-dev/MeshCore):** Energooszczędne zarządzanie modułami radiowymi w celu wydłużenia pracy węzła.

## Implementacja Gospodarcza (Scenariusze PoC)

1. **Efektywność Energetyczna i Grid Health:** Wykorzystanie sieci Mesh do monitorowania stanu transformatorów i magazynów energii (OZE). W przypadku wykrycia awarii przez sensory, system przesyła zapytanie przez sieć Mesh o dostępność energii w sąsiednich mikrosieciach lub informuje operatora o dokładnej lokalizacji usterki bez użycia Internetu.
2. **Monitoring Gatunkowy i Inwentarski:** Smartfony na obrożach (Projekt 09) działają jako ruchome węzły (repeatery), dynamicznie budując zasięg sieci Mesh tam, gdzie przebywa stado. Pozwala to na pełny monitoring wizyjny (Sentinel) klatek/zagród w głębi pola.
3. **Logistyka Gospodarcza (Suwerenny Komunikator):** Wymiana informacji o zapotrzebowaniu na paliwo, paszę czy gotowość produktów do odbioru, z pełnym szyfrowaniem end-to-end, niezależnie od awarii globalnych platform komunikacyjnych.

## Dlaczego LoRa Mesh?
- **Koszty:** Brak opłat za przesył danych (brak kart SIM).
- **Zasięg:** Od kilku do kilkunastu kilometrów na jednym skoku (hop), z możliwością nieskończonego przedłużania przez kolejne węzły.
- **Suwerenność:** Infrastruktura należy do użytkowników, nie do korporacji.

---
*Intelekt wyprzedza Kapitał!*
