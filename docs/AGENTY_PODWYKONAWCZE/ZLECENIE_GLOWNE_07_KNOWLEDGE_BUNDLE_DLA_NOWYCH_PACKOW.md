# Zlecenie Glowne 07 Knowledge Bundle Dla Nowych Packow

## 1. Misja zadania

Wlacz nowe packi i mape lancucha `Project 13` do knowledge bundle tak, aby agenty onboardingowe i chatbotowe widzialy aktualna architekture pracy.

## 2. Wyzszy cel organizacji

To zadanie wzmacnia wspolna pamiec organizacji i zmniejsza ryzyko, ze kolejne agenty beda pracowac na starym obrazie projektu.

## 3. Read First

- `pipelines/export_chatbot_knowledge_bundle.py`
- `PROJEKTY/13_baza_czesci_recykling/execution_packs/CHAIN_MAP.md`
- README nowych packow w `execution_packs/`

## 4. Write Scope

- `pipelines/export_chatbot_knowledge_bundle.py`
- dokumenty `Project 13`
- wygenerowane bundle files

## 5. Deliverables

- zaktualizowany allowlist albo logika bundle
- odswiezony bundle wiedzy
- mini-handoff z opisem, co teraz trafia do bundle

## 6. Acceptance Criteria

- bundle obejmuje nowa mape lancucha albo kluczowe packi
- eksport bundle przechodzi lokalnie
- dokumentacja odpowiada temu, co trafia do bundle

## 7. Walidacja

- `python3 pipelines/export_chatbot_knowledge_bundle.py`
- `python3 -m py_compile pipelines/export_chatbot_knowledge_bundle.py`
- `git diff --check`

## 8. Blokery

Jesli bundle zrobi sie zbyt duzy, wybierz najwazniejsze dokumenty zamiast wrzucac wszystko.

## 9. Mini-handoff

Zapisz:

- jakie nowe dokumenty trafily do bundle,
- jakie zostaly pominięte i dlaczego,
- jakie walidacje przeszly.
