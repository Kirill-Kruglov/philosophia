Both pre-signature probes completed on `workbench` (MS-S1 MAX). Status remains `DEV_PROBE_ONLY__NO_SIGNATURE_AUTHORIZED`.

### Probe A — tension resolved
`not_e` has **no** `#forward`/`#backward` annotation, but it **is** enumerable both ways (`c not_e` and `a not_e`), and its hand fixture types, compiles, and replays to an empty goal. The feasibility note about terminated traces was the correct fact; missing annotation does **not** remove it from the action space. Choice C’s `NOT_ELIM` family is not silently empty.

| premise | annotation | forward | backward | replay_empty |
|---|---|---|---|---|
| and_i | `#backward` | no | yes | yes |
| and_el / and_er | `#forward` | yes | no | yes |
| or_il / or_ir / or_e | `#backward` | no | yes | yes |
| not_i | `#backward` | no | yes | yes |
| **not_e** | **ABSENT** | **yes** | **yes** | **yes** |
| exfalso | `#backward` | no | yes | yes |

### Probe B — outcome: **realizable**
Depth-1 and depth-3 ambient-arrow instances under grammar A type-check, compile to primitive Peano actions, and fresh-process replay to an empty goal. Depth grading is checkable. Section 9 stands as written; A and the positive-control family are compatible.

### Artifacts
- Script (133 lines): `successor/dev/phase2_stageb_presignature_probes_20.py`
- Report: `successor/dev/PHASE2_STAGEB_PRESIGNATURE_PROBES_20.md`
- JSON: `successor/dev/phase2_stageb_presignature_probes_20_results.json`
- Log (Legion exclusion recorded): `successor/dev/phase2_stageb_presignature_probes_20_run.log`

Hashes (identical in report and JSON): script `ace82c257a4551dfecb58930886cedfec4c39450781452b75926fff129de2ec8`; theory `2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507`. Two fresh executions agreed byte-for-byte. PRF domain `philosophia.stageb-presignature-probe.v1`; 11 disposable roots permanently excluded. No calibration numbers.

---

1. Should those 11 excluded roots also be appended to a durable exclusions JSON (alongside L01/L2), or is the results JSON enough until signature?
2. For signature strength on E: worth one extra disposable pass over depths 1..8 (still no Spearman threshold) so depth grading is fully witnessed before signing?
