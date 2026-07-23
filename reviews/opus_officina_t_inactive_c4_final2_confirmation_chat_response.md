Review complete. Verdict: **`OFFICINA_T_INACTIVE_C4_XLINE_CONFIRMED`**, written to `reviews/opus_officina_t_inactive_c4_final2_confirmation.md` (one new file, verdict token on the first line).

This is the follow-up to my `REVISE_OFFICINA_T_INACTIVE_C4_NAMESPACE`. The repair (`fbac493`, verifier-only) is exactly the bounded correction I requested: `_normalized_capability_name` now loops over both `"builtins."` and `"__builtins__."` prefixes, mapping the suffix to the bare declared member when it's in `BUILTIN_DYNAMIC_IMPORT_CALLS` — inventory unchanged, no capability or executable inspection added.

**All five required checks confirmed (static, nothing imported/executed):**
1. `__builtins__.eval`, `__builtins__.getattr`, and the `namespace = __builtins__; resolver = namespace.eval` hop all refuse in **both** verifiers; all five bare members (`__import__/compile/eval/exec/getattr`) via `__builtins__.` refuse in both. My reported residual is closed exactly.
2. Normalization restricted to the five existing bare members (`importlib.import_module` stays dotted); only a second literal prefix added.
3. Earlier refusals intact — `builtins.*`, `ImportFrom` entropy, cross-module entropy (sole failure), `/dev/urandom`, and reachability all still refuse.
4. Focused **75 passed**, full **279 passed** (+6, no regression); bootstrap regression added; `verify_officina_wp12` OK; `verify_officina_active` exits 1 only for absent authorization; tree pristine, no officina working changes.
5. Hunted ordinary name/attribute/assignment alias variants within the declared set (import-alias, from-import-as, double-hop, dunder-name primitive, mixed) — all refuse; no reproducible non-subscript bypass. Subscript reflection remains the agreed out-of-scope static-lint limitation for the harness gate.

I created only this one review file. The positive verdict **closes only the inactive production-boundary verifier gate** — no harness, manifest, activation, spend, entropy, or claim movement by implication. The real tree remains `NOT_ACTIVATED`.
