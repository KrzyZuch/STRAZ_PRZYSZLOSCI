# Review Checklist Dla Pack Project13 Kaggle Verification 01

- [ ] PR wskazuje `pack_id`, input snapshot i provenance uruchomienia
- [ ] `test_db_verified.jsonl` nie miesza potwierdzonych rekordow z rekordami spornymi bez jawnego statusu
- [ ] `verification_report.md` wyjasnia counts, kryteria potwierdzenia i znane ograniczenia
- [ ] `verification_disagreements.jsonl` pozwala przejrzec trudne przypadki zamiast ukrywac je w agregacie
- [ ] diff nie zawiera sekretow, plikow tymczasowych ani pobranych materialow binarnych
- [ ] pack nie wykonuje przy okazji downstream exportu do `ecoEDA`, `InvenTree` ani `D1`
- [ ] reviewer moze odroznic, co jest gotowe do dalszej kuracji, a co nadal wymaga pracy
