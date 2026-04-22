# Mapowanie Encji Organizacji Do D1 I SQLite

## Cel dokumentu

Ten dokument zamienia `organization_agent_v1` z poziomu samego schematu i sample records na realna warstwe pamieci operacyjnej dla:

- wspolnej pamieci organizacji,
- dashboardow i lookupow,
- kolejek review i approval,
- prostych agentowych zapytan o stan inicjatywy,
- przyszlych workerow `Cloudflare D1` i lokalnych narzedzi `SQLite`.

To mapowanie nie istnieje po to, zeby budowac prywatna baze dla samej bazy.
Ma sluzyc wyzszemu celowi organizacji: utrzymaniu jawnej, audytowalnej i wspolnej pamieci o tym, po co istnieje dany projekt, jaki byt organizacyjny reprezentuje i jak wnosi w misje calej inicjatywy.

## Zasady nadrzedne

### 1. GitHub-first pozostaje zrodlem prawdy

Kanoniczne rekordy nadal powinny byc tworzone i reviewowane w repo przez:

- JSON records,
- Markdown,
- `PR`,
- sample records,
- execution packi i ich artefakty.

`D1` i `SQLite` sa warstwa projekcji, lookupu i pracy operacyjnej, a nie cicha prywatna baza omijajaca review.

### 2. Kazdy projekt musi byc osadzony w wyzszym celu

W tabelach i rekordach nie przechowujemy tylko "projektu".
Przechowujemy tez odpowiedz na pytanie, jaki wyzszy cel organizacji obsluguje:

- aktywacje zasobow,
- reusable capability,
- wspolna pamiec i provenance,
- wolontariacka warstwe wykonawcza,
- pilot swiata fizycznego,
- governance i ochrone interesu wspolnego.

Dlatego projekt powinien byc zawsze czytany przez `PotentialDossier`, `CapabilityGap`, `Experiment` albo `ExecutionPack`, a nie jako samotny byt bez kontekstu misji.

### 3. Pelny rekord zostaje w `payload_json`

Kazda tabela przechowuje:

- kolumny do szybkiego filtrowania i indeksowania,
- pelny rekord kanoniczny w `payload_json`.

To pozwala:

- utrzymac zgodnosc z `organization_agent_v1`,
- uniknac zbyt wczesnej i kruchej normalizacji,
- odtwarzac caly rekord bez zgadywania,
- latwo rozwijac schemat bez migracji co jeden drobny atrybut.

### 4. Polimorficzne odniesienia sa jawne

Tam, gdzie encja wskazuje inna encje przez `EntityReference`, zapisujemy:

- `subject_kind`,
- `subject_id`

albo:

- `linked_subject_kind`,
- `linked_subject_id`.

To wazniejsze niz sztuczne wymuszanie wszystkich relacji przez jedna tabele nadrzedna, bo organizacja ma dzialac szybko i czytelnie, a nie tylko elegancko relacyjnie.

### 5. Ta sama mapa ma dzialac w `D1` i `SQLite`

Dlatego baza powinna opierac sie na prostym SQL kompatybilnym z `SQLite`:

- `TEXT`,
- `REAL`,
- `INTEGER`,
- `payload_json TEXT`,
- proste indeksy,
- brak egzotycznych rozszerzen zaleznch od jednej platformy.

## Kanoniczne tabele

Migracja startowa dla tej warstwy znajduje sie w:

- `cloudflare/migrations/0012_organization_agent_entities.sql`

Punktem startowym sa nastepujace tabele:

### `organization_resource_records`

Przechowuje `ResourceRecord`.

Promowane pola:

- `resource_id`
- `resource_kind`
- `title`
- `discovery_channel`
- `access_model`
- `status`
- `availability_pattern`
- `expected_leverage`
- `source_ref`
- `discovered_at`
- `last_reviewed_at`
- `payload_json`

### `organization_potential_dossiers`

Przechowuje `PotentialDossier`.

Promowane pola:

- `dossier_id`
- `title`
- `target_domain`
- `candidate_status`
- `overall_priority_score`
- `recommended_action`
- `source_ref`
- `created_at`
- `updated_at`
- `payload_json`

### `organization_capability_gaps`

Przechowuje `CapabilityGap`.

Promowane pola:

- `gap_id`
- `dossier_id`
- `title`
- `gap_kind`
- `severity`
- `status`
- `blocking_reason`
- `source_ref`
- `created_at`
- `updated_at`
- `payload_json`

### `organization_experiments`

Przechowuje `Experiment`.

Promowane pola:

- `experiment_id`
- `gap_id`
- `status`
- `hypothesis`
- `source_ref`
- `created_at`
- `updated_at`
- `payload_json`

### `organization_execution_packs`

Przechowuje `ExecutionPack`.

Promowane pola:

- `pack_id`
- `title`
- `linked_subject_kind`
- `linked_subject_id`
- `execution_mode`
- `target_output_kind`
- `status`
- `notebook_path`
- `runbook_path`
- `source_ref`
- `created_at`
- `updated_at`
- `payload_json`

### `organization_tasks`

Przechowuje `Task`.

Promowane pola:

- `task_id`
- `pack_id`
- `assignee_mode`
- `requested_by`
- `status`
- `source_ref`
- `created_at`
- `updated_at`
- `payload_json`

### `organization_runs`

Przechowuje `Run`.

Promowane pola:

- `run_id`
- `task_id`
- `pack_id`
- `operator_kind`
- `environment_kind`
- `status`
- `logs_ref`
- `source_ref`
- `started_at`
- `ended_at`
- `payload_json`

### `organization_artifacts`

Przechowuje `Artifact`.

Promowane pola:

- `artifact_id`
- `run_id`
- `artifact_kind`
- `title`
- `storage_ref`
- `review_status`
- `source_ref`
- `created_at`
- `updated_at`
- `payload_json`

### `organization_integrity_risk_assessments`

Przechowuje `IntegrityRiskAssessment`.

Promowane pola:

- `assessment_id`
- `subject_kind`
- `subject_id`
- `assessment_scope`
- `risk_level`
- `status`
- `reviewer_role`
- `source_ref`
- `assessed_at`
- `payload_json`

### `organization_approvals`

Przechowuje `Approval`.

Promowane pola:

- `approval_id`
- `artifact_id`
- `decision`
- `approval_scope`
- `reviewer_role`
- `source_ref`
- `decided_at`
- `payload_json`

### `organization_readiness_gates`

Przechowuje `ReadinessGate`.

Promowane pola:

- `gate_id`
- `subject_kind`
- `subject_id`
- `gate_kind`
- `status`
- `source_ref`
- `checked_at`
- `payload_json`

## Dlaczego to ma duza dzwignie dla calej inicjatywy

To mapowanie odblokowuje nie tylko `Project 13`.

Odblokowuje tez:

- wspolna pamiec o tym, do czego sluzy dany projekt,
- query layer dla botow i agentow,
- kolejki review, gate i approval,
- przyszle dashboardy portfela projektow,
- porownywanie projektow po ich realnej roli w misji,
- mozliwosc szybkiego przelaczania sie na nastepne zadanie o najwyzszej dzwigni, gdy jeden tor utknie.

## Model synchronizacji

Docelowy przebieg powinien wygladac tak:

```text
repo JSON/Markdown/PR -> walidacja schematu -> projection sync -> D1/SQLite -> query/assistant/view
```

W druga strone tylko jawnie:

```text
runtime signal lub queue in D1 -> eksport do rekordu/artefaktu -> PR albo commit -> review
```

Nie nalezy utrzymywac prywatnych zmian w `D1`, ktore nigdy nie wracaja do jawnego repo.

## Co wdrozyc jako nastepny krok

Najbardziej logiczny kolejny etap to:

1. dowiezc pierwszy skrypt syncu do `SQLite` w ramach zlecenia dla podwykonawcy,
2. sprawdzic jego wynik wzgledem acceptance criteria i checklisty odbioru,
3. dopiero po review rozszerzyc sync na realne `D1`,
4. wystawic proste lookupi dla agentow i review.

To jest dobry kandydat na "nastepne zadanie o najwyzszym potencjale", gdy pojedynczy pilot czeka na zewnetrzny sygnal.
