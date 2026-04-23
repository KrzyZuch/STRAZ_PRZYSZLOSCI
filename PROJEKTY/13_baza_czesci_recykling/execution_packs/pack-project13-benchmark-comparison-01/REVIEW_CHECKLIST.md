# Review Checklist Dla Pack Project13 Benchmark Comparison 01

- [ ] PR wskazuje pack, probke testowa i warianty do porownania
- [ ] `benchmark_sample.jsonl` definiuje stala probke z ground-truth labelami
- [ ] `benchmark_metrics.json` zawiera nazwane metryki dla kazdego wariantu
- [ ] `benchmark_report.md` wyjasnia probke, warianty, wyniki i wnioski
- [ ] metryki sa mierzalne i porownywalne miedzy wariantami
- [ ] diff nie zawiera sekretow, plikow tymczasowych ani pobranych materialow binarnych
- [ ] pack nie modyfikuje kanonicznego katalogu ani downstream artefaktow
- [ ] wyniki benchmarku nie sa promowane do katalogu bez oddzielnego etapu kuracji
- [ ] reviewer moze odtworzyc wyniki z tej samej probki i konfiguracji
