REVISE_STAGE_A_V4_3_1_X

1. Spec boundary: Confirmed. All 13 targeted invalid cases—including unhashable `dtype={}`, non-string dtype, invalid optimizer values/types, and `init_seed=2**63`—returned `IsolatedInvalidSpec` before multiprocessing context access. Validation order is correct at [phase2_spec.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/phase2_spec.py:171) and [phase2_isolated.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/phase2_isolated.py:302).

2. Learner construction: Confirmed for the CPU route. Identical specs produced identical model/optimizer hashes under ambient CPU and `meta` default devices and differing default dtypes. A forced `GPT2LMHeadModel` constructor exception after RNG/dtype/device scoping restored all caller state. The `finally` restoration is at [phase2_spec.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/phase2_spec.py:427).

3. Seed domain: Blocker reproduced. `2**63` is correctly typed-rejected, and the stated upper-half alias exists. However, `[0, 2**63-1]` is not canonical: accepted seeds `0`, `2**32`, and `2**62` generated identical CPU streams and byte-identical learner states while producing distinct spec hashes:

   - `state_dict_hash`, all three: `0fa58f6727b770644db32d456f39bbc94ebea232db350b4b09a0996830da7e94`
   - Spec hashes: distinct for every seed.

   The contradiction is in the claimed domain at [phase2_spec.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/phase2_spec.py:49) and its validator at [phase2_spec.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/phase2_spec.py:201). The regression at [test_phase2_spec.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/test_phase2_spec.py:208) checks only the `2**63` alias and misses accepted lower-domain aliases.

4. Preserved behavior: Confirmed. Zero-work evidence, separate entered-iteration/leaf-expansion accounting, faithful delayed terminal traversal, codec causal boundaries, and real budget-4 two-fresh-process replay all passed. Relevant implementation is at [phase2_search.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/phase2_search.py:89), with faithful traversal and replay evidence at [test_phase2_search.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/test_phase2_search.py:295) and [test_phase2_root.py](/tmp/minimo_stagea_v431_x_confirm_20260814/learning/test_phase2_root.py:963).

5. V4.3/V4.3.1 disposition: The dtype, ambient-construction, zero-work, accounting, codec, traversal, and replay findings are closed. The seed-identity finding is not closed because the revised accepted domain still assigns multiple spec identities to identical learner initialization.

Commands/counts:

- Patch SHA-256 matched `38afd423…e571`; fresh detached pinned tree, `git apply --check`, application, and `git diff --check` passed.
- Combined Stage-A gate: 125/125 passed in 49.141 seconds.
- Public pre-spawn counterexamples: 13/13 typed refusals; zero spawn requests.
- Constructor probes: 2/2 passed, including forced-exception restoration.
- Seed probes: three documented upper-half pairs confirmed; lower-domain and actual-learner probes reproduced the blocker above.

This review authorizes no training, carrier, SELF/YOKED execution, commit, or push.
