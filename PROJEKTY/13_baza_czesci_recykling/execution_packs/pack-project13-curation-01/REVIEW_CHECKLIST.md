# Review Checklist Dla Pack Project13 Curation 01

- [ ] PR wskazuje pack, wejsciowy verification report i provenance kuracji
- [ ] `curation_decisions.jsonl` zawiera jawne decyzje accept/defer/reject z rationale
- [ ] `curation_report.md` wyjasnia counts, najwazniejsze przypadki i provenance do verification
- [ ] rekordy dodane do `devices.jsonl`, `parts_master.jsonl` i `device_parts.jsonl` sa zgodne z kanonicznymi schematami
- [ ] nie ma duplikatow rekordow w kanonicznym katalogu
- [ ] diff nie zawiera sekretow, plikow tymczasowych ani pobranych materialow binarnych
- [ ] pack nie wykonuje przy okazji downstream exportu do `ecoEDA`, `InvenTree` ani `D1`
- [ ] reviewer moze odroznic, co jest gotowe do katalogu, a co nadal wymaga dalszej kuracji
- [ ] audit trail decyzji kuracyjnych jest kompletny i spojny z verification reportem
