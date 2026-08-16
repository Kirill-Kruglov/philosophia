**Addendum done.** Depths 1..8 all pass; durable registry is live. Status remains `DEV_PROBE_ONLY__NO_SIGNATURE_AUTHORIZED`.

### Item 1 — depth 1..8
| depth | grammar_A | typed | compile | replay | size |
|---:|---|---|---|---|---:|
| 1..8 | True | True | True | True | 78…358 |

`first_failure: None` — no expressibility or size failure.

### Item 2 — registry
`successor/dev/phase2_disposable_identity_registry.jsonl` — **78** entries (L01 + L2 + probe A + depth 1..8 roots + prior B roots 100/101). Fail-closed: `refuse_if_registered(...)` (self-checked).

### Signature facts recorded
1. `not_e` wider footprint than every annotated premise.  
2. Positive control realizable at 1..8 under A → choice A no longer blocked by §9.

### Provenance (raw = lf)
- script `6ee8bcfa4a9bb0ae057e708697691730cb211e7b189013a1ad538ad0ee499de6`
- theory `2056deaf…`, L01 `31e319bd…`, L2 `a1f907ad…`
- two fresh worker execs byte-identical; +78 lines (≤80); Legion excluded in log

**Questions**
1. Should `refuse_if_registered` also refuse on `raw_ascii_sequent_sha256` aliases when a later generator only has a sequent string (not a theorem object)?
2. For signature quality: pin the `not_e` dual-direction cost asymmetry as a named band covariate before `B*` calibration, rather than discovering it post hoc?
