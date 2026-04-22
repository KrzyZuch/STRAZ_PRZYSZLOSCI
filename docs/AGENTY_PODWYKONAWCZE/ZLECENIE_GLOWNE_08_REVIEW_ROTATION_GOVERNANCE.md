# Zlecenie Glowne 08 Review Rotation Governance

## 1. Misja zadania

Przygotuj dokument governance opisujacy role reviewerow, rotacje review i minimalne zasady approval, zeby ograniczac ryzyko nepotyzmu i centralizacji.

## 2. Wyzszy cel organizacji

To zadanie chroni interes wspolny i zamienia rozproszona architekture agentowa w bardziej odporny system organizacyjny.

## 3. Read First

- `docs/ARCHITEKTURA_ORGANIZACJI_AGENTOWEJ.md`
- `docs/ENCJE_I_WORKFLOWY_ORGANIZACJI_AGENTOWEJ.md`
- `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`

## 4. Write Scope

- `docs/`
- ewentualnie `schemas/organization_agent_v1.yaml`, jesli wyniknie potrzeba doprecyzowania reviewer roles

## 5. Deliverables

- nowy dokument governance dla review i approval
- ewentualne drobne doprecyzowania dokumentow organizacyjnych
- mini-handoff z otwartymi decyzjami

## 6. Acceptance Criteria

- dokument nazywa role reviewerow
- opisuje rotacje albo minimalne zasady unikania koncentracji review
- laczy governance z `IntegrityRiskAssessment`, `ReadinessGate` i `Approval`

## 7. Walidacja

- kontrola spojnosci z dokumentami organizacyjnymi
- `git diff --check`

## 8. Blokery

Jesli pojawi sie kilka sensownych wariantow governance, opisz je jawnie zamiast udawac jednej oczywistej odpowiedzi.

## 9. Mini-handoff

Zapisz:

- jaki model governance proponujesz,
- co jest twarda regula,
- co wymaga decyzji maintainerow.
