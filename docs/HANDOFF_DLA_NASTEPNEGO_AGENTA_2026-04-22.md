# Handoff Dla Nastepnego Agenta 2026-04-22

## 1. Stan misji

- Glowny cel obecnej iteracji: zamienic ogolna wizje Strazy Przyszlosci na operacyjny system dokumentow, encji, workflowow i instrukcji dla kolejnych agentow oraz doprowadzic pierwszy realny `ExecutionPack` do stanu lokalnie review-ready i operacyjnie domknietego.
- Dlaczego ten cel byl priorytetowy: repo mialo juz mocna wizje i kilka wykonawczych klockow, ale brakowalo stabilnego loopa `pack -> run -> artifact -> review`, ktory nowy agent moglby rozwijac bez ciaglego dopisywania promptow przez czlowieka.
- Jaki efekt udalo sie uzyskac: warstwa architektoniczna organizacji agentowej nadal jest glownym szkieletem repo, `Project 13` ma pierwszy realny `KaggleNotebookPack`, deterministyczny rebuild outputow review-ready, audit trail rekordow odrzuconych, lokalny dry-run zakonczony statusem `pass`, notebook ma juz automatyczny finalizer zapisujacy kanoniczny `Run record`, a po otwarciu PR istnieje juz prosty helper do dopiecia `Artifact`, organizacja dostala jawna regule, ze projekt ma sluzyc wyzszemu celowi, a poza handoffem powstal tez osobny system zlecen dla agentow-podwykonawcow.
- Dodatkowy efekt ostatniej iteracji: `Project 13` przestal byc jednym packiem i dostal juz mape lancucha `enrichment -> verification -> curation -> export`, a katalog agentow-podwykonawcow ma teraz gotowy portfel `10` zlecen do rozdysponowania i odbioru.
- Jaki wyzszy cel organizacji obslugiwaly te prace: budowe `Straz OS`, wspolnej pamieci organizacji i reusable workflowow, dzieki ktorym projekty sa traktowane jako narzedzia rozwoju calej inicjatywy, a nie izolowane wyspy.

## 2. Zmiany wykonane

- Dokumenty dodane lub zaktualizowane:
  - `docs/ARCHITEKTURA_ORGANIZACJI_AGENTOWEJ.md`
  - `docs/PLAN_ROZWOJU_ORGANIZACJI_AGENTOWEJ.md`
  - `docs/ENCJE_I_WORKFLOWY_ORGANIZACJI_AGENTOWEJ.md`
  - `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
  - `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
  - `docs/SZABLON_HANDOFF_DLA_NASTEPNEGO_AGENTA.md`
  - `docs/AGENTY_PODWYKONAWCZE/README.md`
  - `docs/AGENTY_PODWYKONAWCZE/PORTFEL_10_ZLECEN_DLA_PODWYKONAWCOW.md`
  - `docs/AGENTY_PODWYKONAWCZE/INSTRUKCJA_DLA_AGENTA_PODWYKONAWCZEGO.md`
  - `docs/AGENTY_PODWYKONAWCZE/SZABLON_ZADANIA_DLA_AGENTA_PODWYKONAWCZEGO.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_02_PROJECT13_RUN_CONTEXT_I_ARTIFACT_FLOW.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_03_PROJECT13_VERIFICATION_EXECUTION_SURFACE.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_04_PROJECT13_CURATION_CHAIN_PACK.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_05_PROJECT13_EXPORT_PACK_SMOKE_RUN.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_06_PROJECT13_BENCHMARK_COMPARISON_PACK.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_07_KNOWLEDGE_BUNDLE_DLA_NOWYCH_PACKOW.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_08_REVIEW_ROTATION_GOVERNANCE.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_09_D1_SQLITE_QUERY_COOKBOOK.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_10_PUBLIC_VOLUNTEER_RUN_READINESS.md`
  - `docs/AGENTY_PODWYKONAWCZE/CHECKLISTA_ODBIORU_ZLECENIA_GLOWNEGO_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`
  - `docs/ARCHITEKTURA_ONBOARDINGU.md`
  - `docs/PRZYKLADY_GOTOWEGO_KODU.md`
  - `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
  - `PROJEKTY/13_baza_czesci_recykling/README.md`
  - `PROJEKTY/13_baza_czesci_recykling/docs/MODEL_WOLONTARIACKICH_NOTEBOOKOW_KAGGLE.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/README.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/CHAIN_MAP.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-verification-01/{README.md,manifest.json,RUNBOOK.md,PR_TEMPLATE.md,REVIEW_CHECKLIST.md,task.json,integrity_risk_assessment.json,readiness_gate.json}`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-catalog-export-01/{README.md,manifest.json,RUNBOOK.md,PR_TEMPLATE.md,REVIEW_CHECKLIST.md,task.json,integrity_risk_assessment.json,readiness_gate.json}`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/manifest.json`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/RUNBOOK.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/PR_TEMPLATE.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/REVIEW_CHECKLIST.md`
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/last_run_summary.md`
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/rebuild_autonomous_outputs_report.md`
  - `README.md`
- Schematy i sample records dodane lub zaktualizowane:
  - `schemas/organization_agent_v1.yaml`
  - `data/sample/organization_resource_record.json`
  - `data/sample/organization_potential_dossier.json`
  - `data/sample/organization_capability_gap.json`
  - `data/sample/organization_experiment.json`
  - `data/sample/organization_execution_pack.json`
  - `data/sample/organization_task.json`
  - `data/sample/organization_run.json`
  - `data/sample/organization_artifact.json`
  - `data/sample/organization_integrity_risk_assessment.json`
  - `data/sample/organization_approval.json`
  - `data/sample/organization_readiness_gate.json`
- Kod i workflowy dodane lub zaktualizowane:
  - `PROJEKTY/13_baza_czesci_recykling/youtube-databaseparts.ipynb`
  - `PROJEKTY/13_baza_czesci_recykling/scripts/summarize_kaggle_run.py`
  - `PROJEKTY/13_baza_czesci_recykling/scripts/create_execution_records.py`
  - `PROJEKTY/13_baza_czesci_recykling/scripts/rebuild_autonomous_outputs.py`
  - `PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py`
  - `PROJEKTY/13_baza_czesci_recykling/scripts/finalize_execution_pack_run.py`
  - `PROJEKTY/13_baza_czesci_recykling/scripts/dry_run_execution_pack.py`
  - `pipelines/export_chatbot_knowledge_bundle.py`
  - `cloudflare/migrations/0012_organization_agent_entities.sql`
  - `.gitattributes`
- Artefakty wygenerowane lub odswiezone:
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/results/inventree_import.jsonl`
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/results/ecoEDA_inventory.csv`
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/rebuild_autonomous_outputs_skipped.jsonl`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/dry_runs/dry_run_report_20260422T191422Z.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/dry_runs/summary_20260422T191422Z.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/dry_runs/pr_preview_20260422T191422Z.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/records/run-project13-kaggle-enrichment-dry-run-local-20260422T191422Z.json`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/records/artifact-project13-kaggle-enrichment-dry-run-local-20260422T191422Z.json`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/records/run-project13-kaggle-enrichment-local-finalizer-smoke-20260422T190657Z.json`
  - `data/chatbot/telegram_knowledge_bundle_v1.json`
  - `cloudflare/src/generated_knowledge_bundle.js`
- Najwazniejsze skutki merytoryczne:
  - repo pozostaje przestawione na model `resource scouting -> PotentialDossier -> CapabilityGap -> Experiment -> ExecutionPack -> Task -> Run -> Artifact -> IntegrityRiskAssessment -> Approval`
  - kolejny agent ma juz jawna regule, ze przed rozwojem projektu ma nazwac, czemu sluzy on wyzszemu celowi organizacji
  - kolejny agent ma tez jawna regule portfelowa: jesli aktywny watek blokuje sie na zewnetrznej zaleznosci albo schodzi do kosmetycznego dopieszczania, trzeba wybrac nastepne zadanie o najwyzszej dzwigni dla calej inicjatywy
  - onboarding uznaje wolontariusza z agentem AI oraz wolontariusza-resource scouta jako pelnoprawne role
  - `Project 13` jest pierwszym realnym pilotem resource scoutingu i wolontariackich chainow Kaggle
  - powstala nowa mapa encji organizacji do `D1/SQLite` oraz migracja `0012`, co przygotowuje query-ready warstwe pamieci dla wielu projektow, nie tylko `Project 13`
  - powstaly tez gotowe pliki zadan dla agentow-podwykonawcow, w tym portfel `10` zlecen z priorytetami, zaleznosciami i osobna checklista odbioru dla zadania `01`
  - `Project 13` ma juz nie tylko pack `enrichment`, ale tez mape lancucha oraz dwa kolejne packi: szkiel `verification` i gotowy kontrakt `catalog export`
  - notebook `youtube-databaseparts.ipynb` zostal przestawiony z hard-coded operatora na model `fork wolontariusza -> branch -> PR`
  - `rebuild_autonomous_outputs.py` odbudowuje review-ready outputy z `test_db.jsonl`, normalizuje rekordy i zapisuje tez audit trail rekordow odrzuconych
  - `create_execution_records.py` wspiera juz nie tylko tworzenie `Run`, ale tez tryb `artifact-only` przez `--existing-run-id`
  - nowy `finalize_execution_pack_run.py` robi `rebuild -> summary -> Run record -> git add/commit/push`, a notebook zostal do niego podpiety
  - notebook po finalizacji wypisuje `run_id`, `run_ref` i `run_record_ref`, zeby wolontariusz mogl latwo dopiac `Artifact` po otwarciu PR
  - nowy `attach_pr_artifact_record.py` potrafi dopiac `Artifact` po samym URL-u PR, z jawnym `run_id` albo przez autodiscovery najnowszego realnego runu `kaggle/hybrid_team`
  - `dry_run_execution_pack.py` zostal dopasowany do nowego modelu finalizera i nadal waliduje kontrakt outputow z manifestu
  - `.gitattributes` spina `ecoEDA_inventory.csv` do `LF`, zeby generowane artefakty nie psuly `git diff --check`

## 3. Aktywne encje

### `ResourceRecord`

- `resource-kaggle-volunteers-01`
  - status: `active`
  - znaczenie: rozproszone darmowe zasoby obliczeniowe wolontariuszy aktywowane przez notebooki Kaggle

### `PotentialDossier`

- `dossier-project13-resource-scouting-01`
  - status: `pilot_ready`
  - rekomendacja: `pilot`
  - znaczenie: `Project 13` jako pierwszy produkcyjny poligon resource scoutingu, reuse elektroniki i pracy wolontariuszy z agentami

### `CapabilityGap`

- `gap-project13-review-ready-artifacts-01`
  - status: `ready_for_pack`
  - glowny problem: brak stabilnej sciezki od sygnalu do review-ready artefaktu dla `Project 13`

### `Experiment`

- `experiment-kaggle-review-ready-pack-01`
  - status: `ready`
  - hipoteza: dobry Kaggle pack z acceptance criteria, audit trail, kanonicznym `Run` i fork-flow zwiekszy odsetek artefaktow gotowych do review

### `ExecutionPack`

- `pack-project13-kaggle-enrichment-01`
  - status: `active`
  - tryb: `kaggle_notebook`
  - cel: discovery i enrichment dla `Project 13` przez notebook Kaggle uruchamiany przez wolontariusza
  - realne pliki: `execution_packs/pack-project13-kaggle-enrichment-01/{manifest.json,RUNBOOK.md,PR_TEMPLATE.md,REVIEW_CHECKLIST.md}`
  - kontrakt outputow: `processed_videos.json`, `test_db.jsonl`, `inventree_import.jsonl`, `ecoEDA_inventory.csv`, `last_run_summary.md`, `rebuild_autonomous_outputs_report.md`, `rebuild_autonomous_outputs_skipped.jsonl`
  - finalize path: `scripts/finalize_execution_pack_run.py`

### `Task`

- `task-project13-kaggle-enrichment-01`
  - status: `submitted`
  - tryb przypisania: `volunteer_plus_agent`

### `Run`

- `run-project13-kaggle-enrichment-dry-run-local-20260422T191422Z`
  - status: `succeeded`
  - srodowisko: `local`
  - znaczenie: najnowszy lokalny dry-run packa, ktory potwierdzil spiety kontrakt outputow, provenance i nowy model finalizacji notebooka
- `run-project13-kaggle-enrichment-local-finalizer-smoke-20260422T190657Z`
  - status: `needs_review`
  - srodowisko logiczne: `kaggle` w rekordzie, ale faktycznie byl to lokalny smoke test nowego finalizera z `git_mode=none`
  - znaczenie: potwierdza, ze finalizer generuje `run_id`, `run_ref`, `run_record_ref` i command follow-up do `Artifact`
- Wczesniejsze dry-runy:
  - `20260422T183026Z`: wadliwy przez zle liczenie sciezek repo
  - `20260422T183112Z`: `needs_review`, pierwszy poprawiony dry-run z ostrzezeniami
  - `20260422T185012Z`, `20260422T185207Z`, `20260422T185307Z`, `20260422T185604Z`, `20260422T190706Z`, `20260422T190741Z`: kolejne przebiegi uszczelniajace rebuild, kontrakt outputow i walidator notebooka, wszystkie superseded przez stan `191422Z`

### `Artifact`

- `artifact-project13-kaggle-enrichment-dry-run-local-20260422T191422Z`
  - status review: `draft`
  - rodzaj: `report`
  - storage_ref: `execution_packs/pack-project13-kaggle-enrichment-01/dry_runs/dry_run_report_20260422T191422Z.md`
  - znaczenie: kanoniczny raport z najnowszego lokalnego dry-runu packa

### `IntegrityRiskAssessment`

- `integrity-pack-project13-kaggle-enrichment-01`
  - status: `pass`
  - zakres: `workflow_design`
  - sprawdzone sygnaly: `private_capture`, `volunteer_work_appropriation`, `opaque_approval_path`, `vendor_lock_in`

### `ReadinessGate`

- `gate-pack-ready-project13-kaggle-enrichment-01`
  - status: `pass`
  - zakres: `pack_ready`

### `Approval`

- status obecny:
  - brak jeszcze `Approval`, bo pack przeszedl tylko lokalne dry-runy i smoke test finalizera, a nie ma jeszcze publicznego PR od wolontariusza

## 4. Fakty operacyjne, ktore warto pamietac

- Nie wolno zakladac, ze aktualnie dotykany projekt jest automatycznie najwazniejszy. Najpierw nazwij, jaki wyzszy cel organizacji obsluguje i jaka reusable capability daje calej inicjatywie.
- Jesli aktywny tor blokuje sie na zewnetrznym PR, review, wolontariuszu, credentialach albo czeka tylko na runtime, trzeba przerwac tunelowanie i wybrac nastepny ruch portfelowy o najwyzszej dzwigni.
- Handoff ma pozostac glownym dokumentem przekazania. Jesli zlecasz duze zadanie innemu agentowi, tworzysz dla niego osobny plik zadania poza handoffem i w handoffie wpisujesz, ze trzeba sprawdzic wynik jego pracy.
- Glowny agent nie powinien realizowac `zadania 1` za podwykonawce. Ma sprawdzac jego wynik wedlug osobnej checklisty odbioru i dopiero po review decydowac o integracji.
- Podwykonawcy maja teraz portfel `10` zlecen. Najpierw powinny isc rownolegle zadania z priorytetu `A`, potem `B`, a dopiero na koncu `C`.
- `rebuild_autonomous_outputs.py` bierze `autonomous_test/results/test_db.jsonl` jako zrodlo prawdy dla odbudowy review-ready outputow.
- Ostatni rebuild dawal:
  - `total_records: 82`
  - `accepted_records: 77`
  - `skipped_records: 5`
  - `inventree_rows: 74`
  - `ecoeda_rows: 74`
- Powody odrzucen w ostatnim rebuildzie:
  - `empty_or_placeholder_part_number: 2`
  - `looks_like_designator_list: 1`
  - `looks_like_plain_text_phrase: 2`
- Jawny audit trail odrzuconych rekordow jest zapisany w:
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/rebuild_autonomous_outputs_skipped.jsonl`
- Ostatni poprawny dry-run raportu i szkicu PR ma stempe:
  - `dry_run_report_20260422T191422Z.md`
  - `summary_20260422T191422Z.md`
  - `pr_preview_20260422T191422Z.md`
- Ostatni rekord `Run` i `Artifact` dla dry-runu ma stempe:
  - `run-project13-kaggle-enrichment-dry-run-local-20260422T191422Z.json`
  - `artifact-project13-kaggle-enrichment-dry-run-local-20260422T191422Z.json`
- Notebook nie robi juz recznie `rebuild + summary + git add + push`, tylko wywoluje:
  - `python3 PROJEKTY/13_baza_czesci_recykling/scripts/finalize_execution_pack_run.py --fork-owner <login> --git-mode push`
- Po prawdziwym runie notebook powinien wypisac:
  - `run_id`
  - `run_ref`
  - `run_record_ref`
- Po otwarciu PR `Artifact` dopina sie przez:
  - `python3 PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py --run-id <run-id-z-logu-notebooka> --pr-url https://github.com/StrazPrzyszlosci/STRAZ_PRZYSZLOSCI/pull/<numer>`
- Helper wspiera tez autodiscovery:
  - `python3 PROJEKTY/13_baza_czesci_recykling/scripts/attach_pr_artifact_record.py --fork-owner <login> --pr-url https://github.com/StrazPrzyszlosci/STRAZ_PRZYSZLOSCI/pull/<numer>`
- Helper zostal sprawdzony lokalnie:
  - wariant z jawnym `run_id`
  - wariant autodiscovery po `fork_owner`
- Poprawna walidacja katalogu dla `Project 13` jest pod sciezka:
  - `python3 PROJEKTY/13_baza_czesci_recykling/scripts/build_catalog_artifacts.py validate`
  - nie `python3 pipelines/build_catalog_artifacts.py validate`

## 5. Ryzyka i zjawiska niekorzystne

- Ryzyka nepotyzmu:
  - review i approval moga z czasem skupic sie w zbyt waskiej grupie osob, jesli nie powstana jawne zasady reviewer roles i rotacji review
- Ryzyka korupcji:
  - przy przyszlych deploymentach hardware i alokacji zasobow moze pojawic sie niejawne uprzywilejowanie wybranych partnerow albo operatorow
- Ryzyka zawlaszczenia wspolnych efektow pracy:
  - najwazniejsze ryzyko obecnie to prywatne przechwycenie wynikow wolontariuszy uruchamiajacych notebooki Kaggle lub ich niewidoczne przekierowanie poza wspolny fork/PR flow
- Ryzyka centralizacji lub ukrytych przywilejow:
  - jesli przyszle workflowy dostana ukryte sciezki pushu, deployu albo bypassu review, cala logika dobra wspolnego zostanie oslabiona
- Ryzyka vendor lock-in:
  - na razie `Kaggle` jest traktowane pragmatycznie jako zasob wolontariacki, ale nie powinno stac sie jedynym execution surface
- Ryzyka heurystyk rebuilda:
  - obecny filtr odrzuca placeholdery, designator-listy i oczywiste frazy tekstowe, ale pierwszy prawdziwy publiczny run nadal powinien sprawdzic, czy heurystyki nie sa zbyt agresywne albo zbyt lagodne
- Ryzyka provenance po PR:
  - `Run record` jest juz automatyczny, a dopiecie `Artifact` ma juz helper lokalny, ale nadal nie jest to jeszcze w pelni automatyczne przez GitHub API / CI

## 6. Co zostalo otwarte

- Niezamkniete decyzje:
  - czy po pierwszym publicznym runie od razu zautomatyzowac rowniez zapis `Artifact` przez GitHub API / CI po utworzeniu PR, czy zostawic jeszcze jeden etap polautomatyczny z helperem `attach_pr_artifact_record.py`
  - czy kolejne execution packi rozbijac od razu na `verification chain`, `enrichment chain` i `export chain`, czy najpierw ustabilizowac tylko pierwszy pack end-to-end
- Blokery:
  - brak jeszcze pierwszego publicznego PR od wolontariusza uruchamiajacego nowy pack
  - brak jeszcze skryptu projekcyjnego, ktory syncuje rekordy `organization_agent_v1` do nowych tabel `D1` lub `SQLite`
  - brak jeszcze pelnej automatyzacji dopiecia `Artifact` po poznaniu URL-a prawdziwego PR
- Brakujace dane:
  - brak benchmarkow runtime, kosztu i skutecznosci dla kolejnych uruchomien packa
  - brak porownan promptow i modeli na tej samej probce filmow
  - brak danych, jak heurystyki rebuilda zachowaja sie na swiezym snapshotcie z prawdziwego Kaggle runu
- Brakujace execution packi:
  - brak nadal osobnego packa `curation chain`
  - pack `verification` jest jeszcze `draft` i wymaga realnego execution surface
- Brakujace review lub integrity review:
  - pack ma juz wlasny `IntegrityRiskAssessment`, ale brakuje jeszcze realnego review pierwszego PR przechodzacego cala checklista

## 7. Najlepszy kolejny krok

- Jeden najwyzszy priorytet:
  - rozdysponowac i potem odebrac wyniki zadan priorytetu `A` z `docs/AGENTY_PODWYKONAWCZE/PORTFEL_10_ZLECEN_DLA_PODWYKONAWCOW.md`, zaczynajac od `01`, `02` i `03`
- Dlaczego wlasnie ten:
  - portfel `10` zlecen pozwala naprawde uruchomic prace rownolegla zamiast jednego liniowego watku
  - zadania `01`, `02` i `03` odblokowuja najwiecej kolejnych ruchow: pamiec organizacji, provenance `Run -> Artifact` i realny verification chain
  - glowny agent ma teraz gotowa strukture do odbioru wynikow zamiast samemu implementowac wszystko po kolei
- Czemu ten krok sluzy wyzszemu celowi organizacji:
  - zamienia inicjatywe w realna organizacje agentowa z delegowaniem, odbiorem i rownolegla praca zamiast pojedynczego strumienia wykonawczego
- Co trzeba przeczytac najpierw:
  - `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
  - `docs/MAPOWANIE_ENCJI_ORGANIZACJI_DO_D1_I_SQLITE.md`
  - `docs/ENCJE_I_WORKFLOWY_ORGANIZACJI_AGENTOWEJ.md`
  - `docs/AGENTY_PODWYKONAWCZE/PORTFEL_10_ZLECEN_DLA_PODWYKONAWCOW.md`
  - `docs/AGENTY_PODWYKONAWCZE/INSTRUKCJA_DLA_AGENTA_PODWYKONAWCZEGO.md`
  - `docs/AGENTY_PODWYKONAWCZE/ZLECENIE_GLOWNE_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`
  - `docs/AGENTY_PODWYKONAWCZE/CHECKLISTA_ODBIORU_ZLECENIA_GLOWNEGO_01_SYNC_ENCJI_ORGANIZACJI_DO_D1_SQLITE.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/CHAIN_MAP.md`
  - `PROJEKTY/13_baza_czesci_recykling/README.md`
  - `PROJEKTY/13_baza_czesci_recykling/docs/MODEL_WOLONTARIACKICH_NOTEBOOKOW_KAGGLE.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/RUNBOOK.md`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/manifest.json`
  - `PROJEKTY/13_baza_czesci_recykling/execution_packs/pack-project13-kaggle-enrichment-01/dry_runs/dry_run_report_20260422T191422Z.md`
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/rebuild_autonomous_outputs_report.md`
  - `PROJEKTY/13_baza_czesci_recykling/autonomous_test/reports/rebuild_autonomous_outputs_skipped.jsonl`
  - `docs/ARCHITEKTURA_ORGANIZACJI_AGENTOWEJ.md`
- Jakie pliki najprawdopodobniej beda dotkniete:
  - `docs/AGENTY_PODWYKONAWCZE/PORTFEL_10_ZLECEN_DLA_PODWYKONAWCOW.md`
  - odpowiednie pliki `ZLECENIE_GLOWNE_0X_*.md`
  - wynikowe pliki podwykonawcow w `pipelines/`, `docs/` i `PROJEKTY/13_baza_czesci_recykling/`
  - po odbiorze: odpowiednie checklisty i handoff

## 8. Kolejnosc startu dla nastepnego agenta

1. Przeczytaj:
   - `docs/INSTRUKCJA_ROZWOJOWA_DLA_AGENTA.md`
   - `docs/HANDOFF_DLA_NASTEPNEGO_AGENTA_2026-04-22.md`
   - `docs/ENCJE_I_WORKFLOWY_ORGANIZACJI_AGENTOWEJ.md`
2. Zweryfikuj:
   - `schemas/organization_agent_v1.yaml`
   - wszystkie `data/sample/organization_*.json`
   - aktualny stan `Project 13`
   - najnowszy dry-run `191422Z`
   - nowy finalizer notebooka, helper `attach_pr_artifact_record.py` i tryb `artifact-only` w `create_execution_records.py`
3. Nie ruszaj jeszcze:
   - ciezszej orkiestracji wieloagentowej
   - zaawansowanej samooptymalizacji promptow i kodu
   - deploymentow hardware bez bardziej konkretnego workflowu
4. Zacznij od:
   - przeczytania `docs/AGENTY_PODWYKONAWCZE/PORTFEL_10_ZLECEN_DLA_PODWYKONAWCOW.md`
   - rozdysponowania zadan `01`, `02` i `03`
   - odbierania wynikow wzgledem acceptance criteria z odpowiednich plikow zlecen
   - aktualizacji handoffu po kazdym przyjetym albo odrzuconym wyniku

## 9. Uwagi koncowe

- Czego nie wolno zgubic:
  - `Project 13` ma pozostac pierwszym realnym poligonem produkcyjnym
  - `Project 13` nie jest celem samym w sobie, tylko pilotem budowy reusable capability i wolontariackiej warstwy wykonawczej
  - organizacja ma szukac zasobow, nie tylko wykonywac zadania
  - integrity/public-interest review jest czescia architektury, nie dodatkiem
  - wolontariusz z agentem AI ma byc traktowany jako podstawowa warstwa wykonawcza
  - zlozone zadanie dla podwykonawcy ma miec osobny plik poza handoffem, a handoff ma kazac sprawdzic wynik tej pracy
  - glowny agent ma odbierac `zadanie 1`, a nie robic go za podwykonawce
  - portfel podwykonawcow ma byc realnie uzywany do pracy rownoleglej, a nie tylko istnieć jako dokumentacja
- Co okazalo sie szczegolnie wartosciowe:
  - wprowadzenie kanonicznych encji bardzo porzadkuje rozmowe i kolejne decyzje
  - polaczenie Kaggle, wolontariuszy i `Project 13` daje najbardziej realistyczny pierwszy loop
  - deterministyczny rebuild outputow review-ready bardzo zmniejsza ryzyko, ze pack zostanie uznany za "gotowy", a faktycznie bedzie miec puste lub niejawne outputy
  - automatyczny finalizer notebooka usuwa jedno z najwazniejszych miejsc, w ktorych provenance moglo sie rozjechac albo zostac pominiete
  - prosty helper do dopiecia `Artifact` bardzo obniza ryzyko, ze pierwszy publiczny PR utkwi tylko dlatego, ze `Run` i `Artifact` nie zostana ze soba poprawnie powiazane
  - rozdzielenie handoffu glownego agenta od osobnego zlecenia dla podwykonawcy oraz checklisty odbioru bardzo porzadkuje odpowiedzialnosc i review
  - rozpisanie pelnego portfela `10` zlecen bardzo ulatwia rozkladanie pracy na wiele agentow bez gubienia priorytetow i zaleznosci
