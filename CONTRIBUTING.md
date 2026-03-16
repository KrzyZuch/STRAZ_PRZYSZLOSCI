# Jak zaangażować się w projekt (Poradnik i instrukcja obsługi)

Witamy w repozytorium **NARODOWYCH SIŁ INTELEKTUALNYCH**! Dziękujemy, że chcesz dołączyć do wspólnego wysiłku. Ten dokument ma na celu pomóc Ci w postawieniu pierwszych kroków – od zgłoszenia pomysłu do poprawnego scommitowania zmian.

Niezależnie od tego, czy pracujesz w IT, analizie danych, marketingu, czy zajmujesz się zarządzaniem – każda pomoc jest cenna.

## 1. Dołączenie do dyskusji (Dla wszystkich)

Nawet jeśli nie potrafisz programować, możesz aktywnie uczestniczyć w *"Burzy mózgów, analizie i planowaniu"*! 

**Jak to zrobić?**
1. Otwórz zakładkę **Issues** (Problemy/Zgłoszenia) w głównym menu repozytorium na GitHubie.
2. Przejrzyj otwarte tematy. Jeśli widzisz coś, na czym się znasz – zostaw komentarz.
3. Jeśli masz nową, autonomiczną propozycję (np. nowy moduł produkcyjny, pomysł na pozyskanie finansowania społecznego) – kliknij **"New Issue"** i opisz swój pomysł najdokładniej jak potrafisz.

## 2. Podstawy Git i GitHuba (Zgłaszanie kodu i tekstów)

Jeśli chcesz wnieść wkład bezpośrednio do plików w repozytorium (np. dodać kod, artykuł, instrukcję), postępuj zgodnie z modelem współtworzenia open source (tzw. "Fork & Pull Request").

### Krok po kroku: Jak to zrobić?

#### A. Stworzenie własnej kopii (Fork)
Wejdź na stronę naszego repozytorium: https://github.com/KrzyZuch/POLSKIEAi i w prawym górnym rogu kliknij przycisk **"Fork"**. Zostanie utworzona kopia tego projektu na Twoim własnym koncie GitHub.

#### B. Pobranie plików na swój komputer (Clone)
Otwórz terminal (konsolę) na swoim komputerze i wpisz:
```bash
git clone https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/POLSKIEAi.git
cd POLSKIEAi
```

#### C. Tworzenie gałęzi dla nowej funkcji (Branch)
Nigdy nie wprowadzaj zmian bezpośrednio na głównej gałęzi `main`. Zawsze twórz osobną gałąź na swoje poprawki:
```bash
git checkout -b nazwa-twojego-pomyslu
```

#### D. Wprowadzanie i zapisywanie zmian (Commit)
Zrób zmiany w plikach (napisz kod, poprawki itp.). Kiedy skończysz, zapisz je w historii u siebie lokalnie:
```bash
git add .
git commit -m "Krótki i zwięzły opis tego, co zmieniłeś"
```

#### E. Wysyłanie zmian na serwer (Push)
Wypchnij swoje zmiany do swojego forka na GitHubie:
```bash
git push origin nazwa-twojego-pomyslu
```

#### F. Zgłoszenie zmian do głównego projektu (Pull Request)
1. Wróć na stronę GitHuba, na swoje sforkowane repozytorium.
2. Zobaczysz tam zielony przycisk z napisem **"Compare & pull request"**. Kliknij go!
3. Opisz, co wprowadziłeś swoimi zmianami i dlaczego warto je akceptować. Następnie zatwierdź stworzenie Pull Requesta (PR).
4. Administracja lub inni twórcy przejrzą Twoje zmiany, mogą dodać swoje uwagi. Potem zostaną one połączone z głównym projektem!

## 3. Złote zasady naszego repozytorium
* **Bądźmy konstruktywni:** Oceniamy pomysły i kod, nie ludzi. Odnosimy się do siebie z szacunkiem i z dbałością o kulturę języka.
* **Intelekt ponad wszystko:** Zanim napiszesz komentarz lub kod, dobrze przemyśl jego cel. Wspólnie poszukujemy logiki i precyzji.
* **Nazewnictwo:** Nazywaj gałęzie i commity jasno, określając, co one robią (np. `dodanie-skryptu-analizy-rynku`).
* **Zademonstruj rozwiązanie:** Jeśli znajdziesz w kodzie problem, w miarę możliwości zaproponuj od razu rozwiązanie.

---

Cieszymy się, że chcesz z nami wspólnie pracować nad systemem budującym WSPÓLNE DOBRO NARODOWE!
