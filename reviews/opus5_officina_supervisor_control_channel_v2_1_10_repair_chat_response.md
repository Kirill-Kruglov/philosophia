I'll verify the pinned hashes and ancestry, then read both v2.1.9 reviews.

All three hashes verify. Reading both v2.1.9 reviews.

I referenced test-obligation rows in §V2110.7 but only wrote the crash matrix there. Adding the missing subsection.

Now the closure.

Custody verified: exactly two new files, pre-existing dirty/untracked paths byte-identical, `verification.py` unmodified at `327b1bb2…`, and the specified bootstrap script correctly does **not** exist.

## Done — v2.1.10 architectural repair

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md) | `2b4f9cad…0dc8` |
| [opus5_officina_supervisor_control_channel_v2_1_10_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md) | `4cc19fc9…c47d` |

All three pinned hashes verified. Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_FINAL_XY_CONFIRMATION`.

**The theorem is withdrawn, not repaired.** `G-1` and §V219.2.2 are deleted outright. A new fourth root, `scripts/officina_process_control_bootstrap.py`, is `execve`'d with `-I -S -E -P` from an absolute object-bound path with `env={}` — so `site`, `.pth`, `sitecustomize`, `usercustomize` and `PYTHON*` cannot run at all — imports five audited stdlib modules and no project package, binds and identity-validates the genuine primitives at module scope, and contains the whole process-control machine. Isolation is read back from `sys.flags`; argv is evidence of nothing.

**The reaping proof is now a process boundary.** `pid_mid` is a direct child of the bootstrap and of nothing else; a `wait` reaps only direct children; so the caller's helper thread, at-fork handler, monkeypatch or native extension can reach at most the *bootstrap*. This cites no property of the caller — which is the whole structural difference from v2.1.9. Both counterexamples are replayed step-by-step and fail at their load-bearing step. The caller's reply travels on a pipe, never an exit status, so a stolen reap costs nothing; the caller may never signal the bootstrap.

**M219-1**: the "existing verifier already proves this" claim is withdrawn as false; CHANGES 1–5 give the exact algorithm — fourth root, module-scoped allowlist (bootstrap gets exactly `{os, sys, signal, time, fcntl}`, not a union), a ten-predicate closed AST grammar, `generic_harness.py` losing `signal`, and `root_source_sha256` in the manifest. **M219-2**: a sixth `WAIT_ONE` result, `STRUCTURAL_VIOLATION`, is total over every returned object and every `BaseException`, with one safe continuation at all five sites; `B-CONTRADICTED` is re-excluded from direct-child ownership alone. **m219-1**: Y's stricter disposition governs — platform pinned to `Linux x86_64, CPython 3.12.3`, MIPS refused at `P-a` *before* any mask parse.

Nine signed sentences are superseded and individually quoted (§V2110.9), including harness §9's no-additional-`scripts/*.py` rule — which names this very amendment as its prerequisite — and §W2.1's in-process supervisor entry, now an `execve` through one refusal-first private token.

Eight weakest points are stated against myself, chief among them that the CPython build is a pinned *identity* not a hashed artifact, that `signal`→`functools`→`_thread` is in the import closure, and that **the supervisor process is still not isolated** — the same class of defect, explicitly not claimed repaired.

T `NOT_ACTIVATED`; claim `OPEN`; token unavailable pending fresh X/Y confirmation of digest `2b4f9cad…`.
