# Level 0 anchor source audit

Inspected 2026-07-11 before any outcome implementation or run.

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
