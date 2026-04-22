# Review Checklist Dla Pack Project13 Catalog Export 01

- [ ] PR wskazuje pack, komende exportu i zrodlo reviewowanego katalogu
- [ ] `build_catalog_artifacts.py validate` przeszlo na tym samym stanie repo
- [ ] diff dotyczy tylko downstream artefaktow i nie miesza discovery albo OCR
- [ ] `inventory.csv`, `recycled_parts_seed.sql`, `mcp_reuse_catalog.json` i `inventree_import.jsonl` sa spojne z kanonicznym katalogiem
- [ ] wygenerowane pliki nie wygladaja na recznie edytowane po eksporcie
- [ ] reviewer moze odtworzyc wynik z jednego polecenia bez tajnych krokow
