# Level 0 anchor source audit

Initial pass 2026-07-11; materially updated 2026-07-12 before any outcome run.
See COMPANION_SOURCE_AUDIT.md. Lock is blocked on source reconciliation.

## Paper

Nanda et al., Progress Measures for Grokking via Mechanistic Interpretability:
https://arxiv.org/abs/2301.05217

## Linked repository

- URL: https://github.com/neelnanda-io/Grokking
- Commit: dfbd38f7d23e09aaa5e5c9bd0483b69ca533e580
- Commit date: 2022-09-26T04:00:31-07:00
- Subject: Graphs!

The README calls the repository a dump of saved weights and loss curves for a
Colab notebook. At the inspected revision:

- grokking.py and Streamlit pages are analysis/visualization code;
- p = 113 is explicit;
- modular-addition artifacts are loaded from saved_runs;
- no complete training loop for the anchor run was found;
- no LICENSE file was present.

## Consequence

This is not a source-complete, licensed training implementation. Philosophia
will not vendor its code or weights unless licensing is clarified.

Before lock:

1. archive paper and linked Colab identifiers/hashes where permitted;
2. extract a cited line-by-line configuration table;
3. independently implement from that specification;
4. list unresolved and modern-PyTorch deviations;
5. review whether the positive arm remains faithful.

If traceability remains insufficient, switch to a published anchor with complete
licensed code and record that change before preregistration.

## 2026-07-12 companion-source correction

The paper's official companion repository,
mechanistic-interpretability-grokking/progress-measures-paper, was subsequently
identified. Its README explicitly names transformers.py as training code, and
its training source predates arXiv v1. This corrects the earlier operational
premise that no complete anchor training loop was available.

The companion repository has no detected license, so its implementation is not
vendored. Its executable facts are nevertheless primary provenance evidence.
They reopen initialization, split, learning-rate warmup, and training-class
semantics. Full hashes and the discrepancy matrix are in
COMPANION_SOURCE_AUDIT.md.

The previous independent choices remain useful as a reviewed v1 reconstruction,
but they cannot be locked as the closest source-fidelity arm until the new
evidence is reconciled.
