# Officina supervisor and control-channel amendment — v2.1.10 architectural correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

> ## WHAT THIS LAYER CHANGES, STATED FIRST AND LOUDLY
>
> **The clean runtime is now CONSTRUCTED, never inferred.** v2.1.9 tried to
> prove that the process running `generic_harness.py` had a clean executor set,
> from `/proc/self/cmdline` plus a repository AST walk. Both independent lines
> rejected that, correctly. **v2.1.10 abandons that theorem entirely** and does
> not repair it with another observation or stronger prose.
>
> **1. A new, fourth executable root.**
> `scripts/officina_process_control_bootstrap.py` — a minimal, standalone,
> site-free process-control bootstrap, executed by a **fresh interpreter** with
> the exact isolation flags `-I -S -E -P` and an **absolute, object-bound script
> path**. `PRODUCTION_ROOTS` goes from **three to four** entries. This is a
> **loud engineering amendment to a signed control surface**; §V2110.9 names
> every affected sentence.
>
> **2. The process-control state machine moves into that root.** The lock, the
> four channels, the singleton records, the first fork, stage M, and every
> `wait`/`kill`/`signal` primitive live in the isolated bootstrap. It **never
> calls back into `generic_harness.py`**. `generic_harness.py` stops being the
> sole executable root and stops being the `signal` importer; it becomes the
> **contaminated caller**, which is now explicitly assumed dirty.
>
> **3. The reaping proof becomes a process-boundary proof.** `pid_mid` is a
> **direct child of the isolated bootstrap and of nothing else**. `wait`-family
> calls reap only direct children. A competing waiter inside the contaminated
> caller can reap at most the *bootstrap*, never `pid_mid`. The proof no longer
> depends on knowing what code the caller runs.
>
> **4. Two further named import-allowlist deltas and a new verifier mechanism.**
> `sys` joins `signal` in the allowlist, and the flat global allowlist is
> replaced by a **per-root module-scoped allowlist**, so the bootstrap's import
> set is `{os, sys, signal, time}` and **nothing else**, while
> `generic_harness.py` loses `signal` again. `json`, `hashlib` and `re` are
> deliberately kept **out** of the bootstrap.
>
> **5. The supervisor grandchild now `execve`s a reviewed role** across the
> custody boundary, re-introducing exactly **one** private argv entry surface,
> refusal-first, in the §Z3.3 style. §W2.1's "no `exec`, no new argv" for the
> supervisor is superseded and named.
>
> **6. The platform is pinned to `Linux x86_64, CPython 3.12.3`.** The false
> all-Linux 16-digit claim is withdrawn; MIPS is **explicitly unsupported** and
> refuses before fork.
>
> **New control-plane constants: four descriptor indices, of exactly the
> §Z-declared `T_CTRL_FD_LOW`/`T_CTRL_FD_HIGH` class. Zero new resource values,
> timeouts, K1 ceilings, E1/E2/E3 values, schemas beyond the one wire record,
> scientific estimands, or author-choice cells.**

**Authorship and provenance, stated literally.** This correction was written by
**Claude Code Opus 5 acting only as the specification author**, because Claude
Code Fable 5 was unavailable. The same author line wrote v2.1 through v2.1.9.
It is **not** an independent X-line or Y-line review of its own bytes and must
never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every author
closure in the chain — including this layer's — is an untrusted self-assessment.

**Review state of v2.1.9, recorded exactly.** **Both** independent lines
returned `REVISE_OFFICINA_SUPERVISOR_V2_1_9`. Y raised C219-1 (Critical),
M219-1, M219-2 (Major) and m219-1 (Minor); X raised F1 (Critical) and F2
(Major). **Their union governs, and where the lines differ the stricter
disposition is taken** — in particular X judged `m218-1`/the mask rule closed
while Y proved the 16-digit claim false on MIPS, so **Y's stricter disposition
governs** and §V2110.6 narrows the platform. v2.1.10 requires a **fresh**
independent X-line review and a **fresh** independent Y-line review of its own
bytes; no earlier confirmation, conditional or otherwise, survives or transfers.

This is an **architectural replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md`
(v2.1.9), which layers over v2.1.8 … v2 — all eleven preserved unedited as
review evidence. **Everything not named in the §V2110.0 replacement index
carries forward verbatim.**

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Accepted progress carried forward byte-for-byte** (§V2110.8 audits each): the
abstract `WAIT_ONE` W-1…W-5 automaton and its result × site product; the
resolved sole-importer contradiction (now re-expressed for the new topology);
the short-mask rejection *principle*; the `SIGCHLD` full-disposition reset and
its `sigaction`/`execve`/`fork` provenance analysis; `ECHILD` and `ESRCH` never
proving death; the ten-row identity table I-1…I-10; ownership-gated signals; the
deletion of `T3`; the stage-M `m0`/`rel1`/fork-shared-lock proof; §V217.1's
object-bound observation and both revalidation barriers; §V217.4's bound-language
sweep; A3/B1/C1/D1/K1; and every scientific and resource boundary of the signed
harness and batch-settlement composites.

Author token candidate, still **not signable**, and not made signable here:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, verifier, manifest, test, contract,
signature, review, prompt, or runtime artifact. Starts no process. Creates no
entropy, activation, capability, world, learner, candidate, datum, Q/C object,
capacity artifact, custody disposition, result manifest, or outcome. Authorizes
no implementation. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes (recomputed for this correction)

```text
746bcf3694a67d04eacaec66190cf68cb92ac0070ec3d8cb24abf6eb22efee0c  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
2e4bee2305bafb5825a6ac1cca4d131dcbdf730aa048f29c7023cf679c9936e6  reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
5c82f7c1894d3e76239ee26a611731d102a2891486a9c2d667ce9738956d533b  reviews/sol_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
e879b39cf6e22c93bcf309ed4a15a7a1f56e00fbcc17fd8cfc2398b04aec099a  reviews/opus_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
663184378fc6fa48c5d83e96cf659d2d9eb58f67a18fd8c7ba0efcb528caea34  reviews/sol_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
f49dcbf9900c0d3fe2e45abbc28193d8b4b4c20c8640dfab508aff15dcc90984  reviews/opus_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
1970986325c75e8f4c2dd72e57e0640ae88b165f3556920e85cae7efc8cc93be  reviews/sol_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

`verification.py` is recorded **unamended**; this correction does not edit it,
and `scripts/officina_process_control_bootstrap.py` **does not exist** — it is
specified here, not created.

## Engineering constants and the complete delta inventory

**Zero new resource values, timeouts, K1 ceilings, E1/E2/E3 values, T bands,
roots-of-trust, archival-set changes, public commands, signed events, refusal or
`INVALID` tokens, or scientific estimands. Zero new author-choice cells.**

Named deltas, all engineering, each superseding a signed sentence enumerated in
§V2110.9:

| # | Delta | Class |
|---|---|---|
| D-1 | `PRODUCTION_ROOTS` gains a fourth entry: `scripts/officina_process_control_bootstrap.py` | executable root |
| D-2 | `ALLOWED_ABSOLUTE_IMPORTS` gains `sys` (it already gains `signal` from v2.1.8, unchanged) | import allowlist |
| D-3 | a **module-scoped** import allowlist replaces the flat global one, so each root has an exact permitted set | verifier mechanism |
| D-4 | four control-plane descriptor indices `T_PCB_FD_REQUEST_R = 3`, `T_PCB_FD_REPLY_W = 4`, `T_PCB_FD_RUNTIME_ROOT = 5`, `T_PCB_FD_PACKAGE_ROOT = 6` — exactly the class §Z declared for `T_CTRL_FD_LOW = 3` / `T_CTRL_FD_HIGH = 4`: control-plane bounds, **not** scientific estimands, resource envelopes, E1/E2/E3 values, or K1 ceilings | control-plane constant |
| D-5 | one private argv entry token `--officina-supervisor-role`, refusal-first, in the §Z3.3 style | private entry surface |
| D-6 | one canonical wire record `philosophia.officina.t-process-control-request.v1` and its reply `…-reply.v1`, in-flight only over a sealed pipe — **never persisted, never a durable object, never an archival member** | wire schema |
| D-7 | the supported platform is pinned to `Linux x86_64, CPython 3.12.3` for **this engineering process-control bootstrap only** | platform scope |

Modules the bootstrap imports: **`os`, `sys`, `signal`, `time` — and nothing
else.** `json`, `hashlib`, `re`, `pathlib`, `enum`, `dataclasses`, `subprocess`,
`fcntl`… are all **excluded from the bootstrap** (`fcntl` is required for
`flock` and is treated in §V2110.3.2). `select`, `selectors`, `ctypes`,
`socket`, `threading`, `_thread`, `multiprocessing`, `concurrent`, `asyncio`,
`atexit`, and `gc` remain outside every allowlist and are not added.

---

## V2110.0. Literal v2.1.9 → v2.1.10 replacement index

**Nothing else moves.** Everything in v2.1.9 and in every layer it carries — in
particular **§V219.3 in full** (the `WAIT_ONE` classifier, the five site
instantiations, the exclusivity proof, the result × site product), **§V218.2.2**
(the `SIGCHLD` full-disposition replacement and its whole analysis),
**§V218.3 in full**, **§V218.4.1–§V218.4.4**, **§V218.5 in full**, **§V217.1 in
full**, **§V217.4 in full**, §V216.2, §V216.4.1, §V216.5, and the entire carried
chain — carries forward verbatim except at the rows below.

| v2.1.9 (or carried) locus | Action in v2.1.10 |
|---|---|
| §V219.2.1's **SUPPORTED PRODUCTION TOPOLOGY** block, premises **P-1** and **P-3**, and its `execve` paragraph | **replaced** by §V2110.2 (the topology is *constructed* by an isolated `execve` of a new root, not asserted of `generic_harness.py`) |
| §V219.2.2's **executor-set theorem** in full, especially step 4's identification of `C(t₀)` with the statically walked source set, and its corollary | **deleted and replaced** by §V2110.3.8 (a closure theorem whose premises follow from the construction) and §V2110.2.3 (the process-boundary reaping proof). **The v2.1.9 theorem is withdrawn in its entirety and is not repaired.** |
| §V219.2.3's `TOPOLOGY_GATE` step **`G-1`** (`/proc/self/cmdline` as program-image evidence) and the sentence "this is a KERNEL fact … it names the program image actually loaded" | **deleted.** Replaced by §V2110.3.1's `sys.flags` / interpreter-identity / platform readback. **No layer of this contract henceforth treats argv as evidence of a clean image, of a fresh `execve`, or of the executor set.** |
| §V219.2.3's `G-2`/`G-3`/`G-4` | **retained**, re-sited into the bootstrap's preflight (§V2110.3.1 `P-a`…`P-h`), and demoted from "the proof" to "corroboration inside a constructed clean process" |
| §V219.2.4 `N-1`/`N-2`, §V219.2.5 `V-1`…`V-10` | **retained byte-for-byte in substance**, re-sited into the bootstrap; `V-6`'s ignored-disposition invariance and `N-2`'s unconditional `SIGCHLD` write are unchanged |
| §V219.2.6's verifier-as-mechanism section and rules `R-a`…`R-e` | **replaced** by §V2110.3.9 (an exact verifier algorithm with AST/manifest invariants, alias and data-flow rules, prohibited syntax, and a fail-closed result per violation). **The claim that the *existing* signed verifier already proves a runtime executor theorem is withdrawn as false**, exactly as M219-1 states |
| §V219.2.7's entry-point table, in particular its `sitecustomize`/`faulthandler` rows and its in-process row | **replaced** by §V2110.3.7 (only the constructed bootstrap has process authority; every other entry has none, by construction rather than by gate) |
| §V219.2.8, §V219.2.9 | **replaced** by §V2110.2.8 and §V2110.7.2 |
| §V219.4.1's **PERMITTED SIGNAL SURFACE** block (`generic_harness.py` as sole root **and** sole `signal` importer) | **replaced** by §V2110.3.2 (the bootstrap is the sole `signal` importer; `generic_harness.py` imports `signal` **not at all**). The *resolution* of the v2.1.8 importer contradiction is preserved — there is still exactly one real importer topology and no unnamed module |
| §V219.4.2's supersession rows 15–18 | **retained**, and **extended** by §V2110.9's rows 19–27 |
| §V219.4.3's §S7 obligations 1–7 | **replaced** by §V2110.3.9's exact verifier algorithm and manifest invariants |
| §V219.3.1's `WAIT_ONE` result enum | **extended** by §V2110.4.1 (a sixth result, `STRUCTURAL_VIOLATION`, covering every unexpected returned object and every `BaseException`) |
| §V219.3.2's five site tables and §V219.3.4's product | **retained**, and **bound** by §V2110.4.2 to the locally held genuine primitives; §V2110.4.3 re-proves W-5 with a middle stopped between `m8` and `m9` |
| §V219.5.1's exclusion of contradiction source (a) "by §V219.2.2's corollary" | **replaced** by §V2110.4.5 (a non-circular process-boundary argument) |
| §V219.5.2's `B-CONTRADICTED` classification | **retained**, now resting on §V2110.4.5 instead of on the withdrawn theorem |
| §V219.6's `W-b` (`d == 16`), its "Architecture behaviour" paragraph, its `_NSIG = 128` table row, and the sentence "Linux renders a sigset_t … on every supported architecture, 32-bit and 64-bit alike" | **replaced** by §V2110.6 (platform pinned to `Linux x86_64`; the all-Linux claim is **withdrawn as false**; MIPS is explicitly unsupported and refuses) |
| §V219.8 test rows **241**, **242**, **243**, **249**, **250**, **252**, **253**, **255**, **264**, **265**, **270**, **271** | **replaced** by §V2110.7.4; rows 273–312 added there |
| §V219.10's edit-surface table | **replaced** by §V2110.10 |
| §V219.11's determinacy and compatibility paragraphs | **replaced** by §V2110.11 |
| carried §W2.1 bullet "**Supervisor:** … the grandchild **calls the serve function in-process** (no `exec`, no new argv)" and its sentence "There is no private argv entry surface to guard." (as already narrowed by §Z3.3) | **replaced** by §V2110.2.7 (the grandchild `execve`s the reviewed supervisor role through exactly one new refusal-first private token) |
| carried §W2.2 parenthetical "The fd is deliberately **not** `O_CLOEXEC` for the grandchild — which is safe precisely because §W2.1 removed the grandchild's `exec`." | **replaced** by §V2110.2.6 (the non-`O_CLOEXEC` property is retained and becomes **load-bearing**, since the grandchild now execs) |
| carried §V2.10 "Sole root: `src/philosophia/officina/generic_harness.py`" and its frozen-file/edit-surface clauses | **replaced** by §V2110.9 rows 19–22 (four roots; the new bootstrap file; `verification.py`'s exact amendment) |
| carried signed harness §9 sentence "**No additional `scripts/*.py` entry point is introduced** … since adding one would require a reviewed amendment to the immutable-control file `verification.py`, which this contract does not authorize." | **superseded** by §V2110.9 row 19 — one additional `scripts/*.py` entry point **is** introduced, and this layer **is** the reviewed amendment that sentence names as the prerequisite |

---

## V2110.1. One-to-one disposition of both lines' findings

| Finding | Line(s) | Disposition in v2.1.10 |
|---|---|---|
| **C219-1 / F1 (Critical)** — argv is not clean-exec or runtime-executor evidence; `.pth`, site/user customization, at-fork/audit/import/trace hooks, monkeypatching, retained callables and native extensions survive every gate | Y + X | **`G-1` is deleted; the theorem is withdrawn.** The clean runtime is **constructed**: a new root exec'd `-I -S -E -P` (so `site`, `.pth`, `sitecustomize`, `usercustomize`, `PYTHON*` env and path injection cannot run at all), importing four stdlib modules and **no project package**, binding genuine primitives at module scope from that clean import state, and containing the whole process-control machine. The isolation flags are **read back from `sys.flags`**, not inferred from argv. Independently, the reaping proof is now a **process-boundary** proof: `pid_mid` is a direct child of the bootstrap and of nothing else (§V2110.2.3). Both counterexamples are replayed in §V2110.7.2 — the `os.register_at_fork` wrapper and the monkeypatched `os.fork`/`os.waitpid` both live in the **caller**, which no longer holds process authority and is no longer `pid_mid`'s parent |
| **M219-1 (Major)** — the current/future verifier does not establish a closed runtime executor or call-target theorem | Y | **The claim is withdrawn.** §V219.2.6's "the signed verifier already enforces this" is deleted as false. §V2110.3.9 gives an **exact** verifier algorithm — module-scoped import allowlist, an import-graph closure rule, a closed AST grammar for the bootstrap root, alias/data-flow and rebinding rules, prohibited syntax, manifest invariants including a source hash, and a fail-closed result per violation — and §V2110.3.8 states precisely which premises are *statically decided*, which are *bound by the construction*, and which are *runtime preflight*. Nothing is claimed for the existing bytes |
| **M219-2 / F2 (Major)** — `WAIT_ONE` totality and `B-CONTRADICTED` unreachability depend on the failed premise; unexpected callable results/exceptions are not total | Y + X | Primitives are locally bound from the clean import state and identity-validated (§V2110.3.4), and a sixth `WAIT_ONE` result, `STRUCTURAL_VIOLATION`, covers **every** unexpected returned object and **every** `BaseException` — wrong arity/type, wrong positive pid, negative value, malformed status, `SystemExit`, `KeyboardInterrupt`, and anything else — with one safe continuation at all five sites (§V2110.4.1). `B-CONTRADICTED` unreachability is re-proved **without citing any executor theorem**, from direct-child ownership alone (§V2110.4.5) |
| **m219-1 (Minor)** — 16 hex digits are false over the stated Linux scope; MIPS `_NSIG = 128` renders 32 digits | Y (stricter; X had judged this closed) | **Y governs.** The all-Linux claim is withdrawn. §V2110.6 pins the bootstrap to `Linux x86_64, CPython 3.12.3`, verified by `os.uname()` and `sys.version_info`/`sys.implementation`, and justifies `d == 16` **only inside that scope**. MIPS and every other architecture route to a pre-fork refusal with an explicit unsupported-platform detail |

---

## V2110.2. A1 — the constructed clean runtime

### V2110.2.1 The new root: canonical path, owner, and byte-exact invocation

```text
canonical path : scripts/officina_process_control_bootstrap.py
owner          : Cursor (mechanical, from this contract), exactly as the signed
                 harness §9 owner column records for generic_harness.py
role           : the ONLY process-control surface. It owns SPAWN.lock, the four
                 bootstrap channels, the four singleton records, the first fork,
                 stage M, and every wait/kill/signal primitive.
NOT a public command. It has no public CLI, appears in no `--help`, and is
never invoked by an operator.
```

The **contaminated caller** — `generic_harness.py`'s `__main__`, running one of
the six carried public commands — launches it exactly so, and in no other way:

```text
argv[0] = <the caller's own sys.executable>            # absolute, kernel-supplied
argv[1] = "-I"        # isolated: implies -E and -s; no cwd/user-site on sys.path
argv[2] = "-S"        # do NOT import `site`: no .pth lines, no sitecustomize,
                      #                       no usercustomize
argv[3] = "-E"        # ignore every PYTHON* environment variable
argv[4] = "-P"        # do not prepend a potentially unsafe path to sys.path
argv[5] = <ABSOLUTE, object-bound path of the bootstrap script>
          — resolved by the caller with os.open(..., O_RDONLY|O_NOFOLLOW|O_CLOEXEC)
            and os.readlink("/proc/self/fd/<n>"), so the exec target is the
            SAME inode the caller opened, not a name re-resolved by execve
(no further argv element: the bootstrap takes NO argv parameters at all)

env      = {}                     # exactly empty
cwd      = "/"                    # pinned, so no relative resolution can matter
close_fds= True
pass_fds = exactly the four descriptors of §V2110.2.6
shell    = False
preexec_fn = None                 # pinned: no pre-exec Python callback
start_new_session = False         # the bootstrap must stay in the caller's
                                  # session so an operator SIGINT reaches it
```

**`-I -S -E -P` is the pinned minimum.** A strictly stronger reviewed invocation
(for example adding `-B`, or a future flag that removes further startup work)
may be substituted only through a fresh reviewed amendment; a **weaker** one is
a contract violation, and the bootstrap refuses at `P-b` (§V2110.3.1) if the
flags it reads back are not at least these four.

**Why the flags, one line each, since each answers a named counterexample:**

| Flag | Removes | Counterexample it answers |
|---|---|---|
| `-S` | `site` import ⇒ no `.pth` executable lines, no `sitecustomize`, no `usercustomize` | Y Trace 2, X Attack 2: the entire startup-contamination channel |
| `-I` | user site-packages, cwd/script-dir on `sys.path`; implies `-E`, `-s` | a `sitecustomize`/module shadowing the stdlib from a user directory |
| `-E` | `PYTHONSTARTUP`, `PYTHONPATH`, `PYTHONFAULTHANDLER`, `PYTHONWARNINGS`, `PYTHONBREAKPOINT`, `PYTHONPROFILEIMPORTTIME`, every `PYTHON*` | X Attack 2's `faulthandler` row and env-injected import paths |
| `-P` | prepending the script's directory to `sys.path` | a module dropped beside the script shadowing a stdlib name |

**The dirty caller may launch the bootstrap, and nothing of the caller crosses
`execve`.** `execve` replaces the entire address space and terminates every
other task in the caller's thread group *in the exec'd image*; every Python
object, monkeypatch, retained callable, at-fork registration, audit hook, import
hook, trace/profile function, and native extension of the caller is destroyed in
the new image. What survives `execve` is exactly: file descriptors (controlled
by `close_fds=True` + the four `pass_fds`), `SIG_IGN` dispositions (handled by
`N-1`/`N-2`, carried), the pid and its session/group, `rlimits`, and the cwd
(pinned to `/`). **Nothing else crosses**, and this is the whole point of the
architectural change: the bootstrap does not have to *know* what the caller
contained.

### V2110.2.2 The exact process tree, with direct-child and reaper ownership at every edge

```text
[0] contaminated caller — generic_harness.py __main__, ANY runtime state
     │   holds: no lock, no singleton record, no bootstrap channel, no pid_mid
     │   may contain: helper threads, monkeypatched os.*, at-fork handlers,
     │                audit/import/trace hooks, native extensions — ALL IRRELEVANT
     │
     │ direct child, created by exec of the pinned invocation
     ▼
[1] isolated process-control bootstrap — scripts/officina_process_control_bootstrap.py
     │   parent   : [0]
     │   reaper   : [0] (or a competing waiter inside [0]) — see §V2110.2.4
     │   holds    : SPAWN.lock, SPAWNING.json, the four channels, pid_mid
     │   task set : exactly one (guaranteed by execve, verified at P-c/P-d)
     │
     │ direct child, created by the bootstrap's own os.fork at c4
     ▼
[2] middle child (pid_mid)
     │   parent   : [1] and ONLY [1]
     │   reaper   : [1] and ONLY [1] — this is the safety property
     │   holds    : a fork-shared SPAWN.lock reference; its own rel1_w copy
     │   executes : m0…m9 (carried §U2.3, unchanged)
     │
     │ direct child, created by the middle's os.fork at m7
     ▼
[3] grandchild → execve of the reviewed supervisor role
         parent   : [2] until [2] exits at m9, then re-parented to init (pid 1)
         reaper   : init. [2] never waits; [1] never waits on it
         holds    : the retained non-CLOEXEC SPAWN.lock fd until g3
```

| Edge | Creator | Direct child of | Who may `wait` on it | Who may signal it |
|---|---|---|---|---|
| [0]→[1] | `execve` from a `fork`/`posix_spawn` inside the caller | [0] | **[0] only** (including any competing waiter inside [0]) | [0] only — and this contract forbids [0] to signal it (§V2110.2.4) |
| [1]→[2] | `os.fork` at `c4`, in the bootstrap | **[1] only** | **[1] only** — the entire W-1…W-5 surface | [1] only, ownership-gated (§V218.3, carried) |
| [2]→[3] | `os.fork` at `m7`, in the middle | [2] until `m9` | nobody: [2] never waits; after `m9`, init reaps | the carried stage-2/`killpg` routes, unchanged |

### V2110.2.3 Why a competing waiter in the caller cannot reap `pid_mid`

> **Process-boundary reaping proof.** On Linux, `wait`, `waitpid`, `wait3`,
> `wait4`, and `waitid` — in every form, including the wildcard forms
> `waitpid(-1, …)` and `waitid(P_ALL, …)` — can reap **only a direct child of
> the calling process's thread group**. A wildcard wait issued by any task of
> process [0] therefore ranges over [0]'s children, which is the set
> `{[1], …}` and **never contains `pid_mid`**, because `pid_mid` is the child of
> [1], not of [0]. `pid_mid` becomes reapable by another process only if [1]
> dies and `pid_mid` is re-parented to `init`, at which point [1] no longer
> exists and asserts nothing. Therefore **no code in the contaminated caller —
> no helper thread, no at-fork handler, no monkeypatched `os.waitpid`, no audit
> hook, no native extension — can reap `pid_mid`, regardless of what it
> contains.** ∎
>
> **This proof cites no property of the caller.** It does not need the caller to
> be single-tasked, callback-free, unpatched, or reviewed. That is the exact
> difference from v2.1.9, whose theorem needed the *same* process to be clean.
>
> **The remaining reaper set is inside [1] alone**, and [1] is clean **by
> construction** (§V2110.3.8), not by inference. Its complete wait surface is
> the carried W-1…W-5 (§V219.3, unchanged), bound to genuine primitives
> (§V2110.3.4).

### V2110.2.4 The caller side: launch, request, reply, and the never-signal rule

The caller is assumed dirty. Its whole permitted interaction is four steps:

```text
L-1. create two anonymous pipes with os.pipe2(O_CLOEXEC): the REQUEST pipe and
     the REPLY pipe. Open the runtime-root and package-root directories with
     os.open(O_RDONLY|O_DIRECTORY|O_CLOEXEC).
L-2. spawn the pinned invocation of §V2110.2.1, passing exactly the four
     descriptors of §V2110.2.6 (the spawn clears O_CLOEXEC on those four only).
     Close the caller's copies of the four passed ends immediately afterwards.
L-3. write EXACTLY ONE canonical request line (§V2110.2.5) on the request pipe;
     close the request write end.
L-4. read the reply pipe to EOF; parse exactly one canonical reply line; close
     the reply read end.

FORBIDDEN to the caller, normatively:
 - sending ANY signal to the bootstrap pid, ever, for any reason;
 - relying on the bootstrap's exit status for any decision;
 - performing ANY wait whose result changes a decision.
```

> **Why the reply travels on a pipe and not in an exit status.** A competing
> waiter inside the caller may reap the bootstrap before the caller's own wait
> runs, in which case the caller's `waitpid` yields `ECHILD` and the status is
> lost. The **pipe reply is therefore the sole authoritative result**, and the
> exit status is advisory diagnostics only. A stolen reap costs the caller a
> status field and costs the contract nothing.
>
> **Why the caller may never signal the bootstrap.** Once a competing waiter has
> reaped the bootstrap, its pid may be recycled — and the caller has no way to
> know. Forbidding the signal outright removes that entire class without
> requiring the caller to be clean. A caller that violates this rule can harm an
> unrelated process **in its own process's name**; it cannot make the bootstrap
> mis-reap, mis-signal, or mis-record anything, because the bootstrap's own
> custody is unaffected. This is stated rather than concealed.
>
> **What a hostile caller can still do**, stated honestly: it can decline to
> launch the bootstrap; it can kill the bootstrap (a liveness effect —
> §V2110.7.3 shows every such cut is safe: kernel release of the lock and fds,
> the middle exits at its own `m0` bound, no record is removed without proof);
> it can lie in the request (constrained to the closed grammar of §V2110.2.5,
> which cannot name code, modules, callbacks, primitives, or out-of-set paths);
> and it can misreport the reply to its own user. **None of these can corrupt
> `pid_mid`'s custody, produce a false death proof, cause a wrong-PID signal, or
> remove a record naming a live process.**

### V2110.2.5 The canonical request and reply schema

One line each, `\n`-terminated, ASCII, no NUL, ≤ `T_CONTROL_FRAME_MAX_BYTES`
(carried constant). Parsed with `bytes.split(b" ")` only — **no `json`, no
`re`, no `hashlib`**, so none of those modules and none of their transitive
closures (`functools`, `enum`, `_locale`, `_hashlib`/OpenSSL) enters the
bootstrap.

```text
REQUEST   schema philosophia.officina.t-process-control-request.v1
  field 0  b"philosophia.officina.t-process-control-request.v1"   (literal)
  field 1  protocol version, the literal b"1"
  field 2  operation, from the CLOSED one-element enum { b"SPAWN_SUPERVISOR" }
  field 3  spawning_id_nonce: exactly 64 bytes from [0-9a-f]
  field 4  caller_pid: decimal, 1..7 digits, no leading zero
  field 5  caller_start_identity: decimal, 1..20 digits
  exactly six fields, exactly one b"\n", nothing after it.

REPLY     schema philosophia.officina.t-process-control-reply.v1
  field 0  b"philosophia.officina.t-process-control-reply.v1"
  field 1  b"1"
  field 2  outcome, from the CLOSED enum
           { b"SUPERVISOR_LIVE", b"REFUSED", b"BLOCKED" }
  field 3  detail token, from the CLOSED enum of carried refusal details plus
           the pre-fork details of §V2110.3.1 — every element a fixed
           [A-Z_]{1,64} literal
  field 4  retryable, b"0" or b"1"
  exactly five fields, exactly one b"\n".
```

**Closure properties, each required by A1 item 5 and each checkable by reading
the grammar above:** no field is a path, a module name, a symbol, a callable, a
signal number, a pid to signal, a file descriptor, a timeout, a resource value,
or a format string. The only free values are a hex nonce and two decimal
integers describing the caller itself. **The request cannot name code, modules,
callbacks, paths outside the pinned set, or process primitives**, because the
grammar admits no field capable of carrying one. Any deviation — wrong field
count, wrong literal, wrong length, a byte outside the field's character class,
a second line, a missing terminator, or more than
`T_CONTROL_FRAME_MAX_BYTES` — is `REQUEST_MALFORMED` and takes the pre-fork
refusal of §V2110.3.1 with no fork.

**Neither record is ever persisted**, transmitted off-host, archived, hashed
into any signed set, or given a durable path. They are in-flight control-plane
frames on a sealed anonymous pipe.

### V2110.2.6 Descriptors, close-on-exec, lock, records, and handshake

```text
Passed from the caller to the bootstrap, at these pinned numbers, and NOTHING
else (close_fds=True):

  T_PCB_FD_REQUEST_R    = 3   request pipe, READ end
  T_PCB_FD_REPLY_W      = 4   reply pipe, WRITE end
  T_PCB_FD_RUNTIME_ROOT = 5   O_DIRECTORY fd of the runtime root
  T_PCB_FD_PACKAGE_ROOT = 6   O_DIRECTORY fd of the package root

The caller dup2()s its ends onto exactly these numbers in the pre-exec child and
clears O_CLOEXEC on exactly these four. Every other descriptor is closed by
close_fds=True.
```

- **Why directory descriptors instead of path strings.** No filesystem path
  crosses the wire at all, so the request grammar cannot name a path, and
  disposable-root testing works by passing a different `dirfd`. Every later
  `os.open`/`os.stat`/`os.unlink`/`os.fsync` in the bootstrap is `dir_fd=`-relative
  to fd 5, exactly as §V217.1's observation algorithm already uses
  `dir_fd=op_dirfd`.
- **Bootstrap-side preflight of the four descriptors** (part of §V2110.3.1):
  `os.fstat` each; fd 3 and 4 must be `S_ISFIFO`, fd 5 and 6 must be `S_ISDIR`;
  `os.get_inheritable` must be true for exactly these four; and `os.listdir("/proc/self/fd")`
  must contain exactly `{0,1,2,3,4,5,6}` plus the transient listing descriptor.
  Any deviation is a pre-fork refusal.
- **`SPAWN.lock`** is acquired by the **bootstrap** at `c1` (`flock(LOCK_EX|LOCK_NB)`
  with the carried bounded retry), `dir_fd=5`-relative, and is **not**
  `O_CLOEXEC`, because the grandchild must retain it across its `execve` — see
  §V2110.9 row 24. It is `CLOSE_OWNED` at `c18` exactly as carried.
- **The four singleton records** (`SPAWNING.json`, `SPAWNING_MIDDLE.json`,
  `SPAWNING_GROUP.json`, `SPAWNING_CHILD.json`), their key sets, atomic
  no-replace installs, `§U6.3` removal order, `§U6.1` P0–P3 preflight, and
  `§U6.2` `EEXIST` discipline are **carried byte-for-byte** and are now written
  by the bootstrap. `cli_pid`/`cli_start_identity` are the **bootstrap's** pid
  and start identity, since the bootstrap is the process that holds the lock —
  this is a re-binding of who "the CLI" is, not a schema change; §V2110.9
  row 25 names it.
- **The four bootstrap channels** `rel1`, `rel2`, `rel3`, `boot` are created by
  the bootstrap at `c3` with `os.pipe2(O_NONBLOCK|O_CLOEXEC)` and the carried
  §U2.1 ownership table is unchanged, with the bootstrap in the row previously
  labelled "CLI".
- **Handshake.** The bootstrap reads the request to EOF **before** `c1`; it
  writes exactly one reply line and closes fd 4 as its last action on every
  route, including every refusal and including the non-returning `B` states
  (which write **no** reply — see §V2110.4.5 — and are therefore observed by the
  caller as EOF without a reply line, which the caller must treat as
  `BLOCKED`/no-progress and never as success).

### V2110.2.7 Crossing the custody boundary: the grandchild `execve`s the reviewed role

The bootstrap does not contain the supervisor. At `m7` the middle forks the
grandchild, and the grandchild — **after** the custody/fork boundary — becomes
the reviewed supervisor by `execve`:

```text
g0'. (grandchild, before any other action) dup2 the retained descriptors onto
     the pinned numbers, clear O_CLOEXEC on exactly those, scrub every other
     inherited descriptor through the carried §W2.2/§Z3.5 discipline, and
     redirect stdio to os.devnull — all carried, unchanged.
g0''. os.execve(<interpreter>, [
        <interpreter>, "-P", "-m", "philosophia.officina.generic_harness",
        "--officina-supervisor-role",
        "--officina-ctrl-fds", "<low>,<high>",
        "--officina-spawning-id", "<64 hex>",
      ], {"PYTHONPATH": <package root>})
     — the interpreter is the bootstrap's own sys.executable (a runtime fact,
       never a request field); the package root is os.readlink("/proc/self/fd/6"),
       i.e. read back from the kernel for a descriptor the caller opened.
     — `-S`/`-I`/`-E` are DELIBERATELY NOT used here: the supervisor legitimately
       needs the project package and site-packages. See the scope note below.
g1.  the supervisor role entry is REFUSAL-FIRST, in the exact §Z3.3 style: it
     verifies the fixed index layout, the fd numbers and their types, the
     spawning id against SPAWNING_MIDDLE/GROUP.json, its own getppid()/session,
     and every inherited token BEFORE any behaviour; any mismatch ⇒ os._exit(3)
     with nothing written and nothing unlinked.
```

**This re-introduces exactly one private argv entry surface**, `--officina-supervisor-role`,
superseding §W2.1's deletion of `--supervisor-serve` and §Z3.3's sentence "the
supervisor and watchdog have no argv entry surface (they are in-process forks)".
X-M1 — the finding that deletion originally closed — is re-closed by the same
mechanism §Z3.3 already uses and both lines already accepted for controllers and
workers: a refusal-first entry that verifies every inherited token before acting.
The token is **not** added to §Z3.2's signed `t-spawn-intent.v1` role enum, which
stays `CONTROLLER|WORKER` and is untouched; this is an argv grammar only.

> **Scope note, stated because it limits what this layer proves.** The
> **supervisor's own** child management — §W2.5's `Popen` + `waitpid(WUNTRACED)`
> handshake for controllers and workers, and its in-process watchdog fork — runs
> in the supervisor's process, which is **not** isolated and is **not** claimed
> clean by this layer. No finding from any line raised it, and it is outside
> C219-1's scope, which is `pid_mid`'s custody. **This correction therefore does
> not claim to have repaired supervisor-side reaping**, and §V2110.11 records it
> as a disclosed follow-on surface. Claiming otherwise would be exactly the kind
> of over-reach both lines have been rejecting.

### V2110.2.8 Crash, restart, and the second launcher

| Cut | Continuation |
|---|---|
| the caller dies before `L-2` | nothing exists; no lock, no record, no child |
| the caller dies after `L-2`, before `L-3` | the bootstrap reads EOF on fd 3 without a complete request ⇒ `REQUEST_TRUNCATED` ⇒ pre-fork refusal; it holds no lock yet; it exits |
| the caller dies while the bootstrap holds the lock | the bootstrap is **unaffected**: it is not the caller's child in any custody sense, it holds its own lock reference, and its reply write to a closed pipe yields `EPIPE`, which it treats as "reply undeliverable" and which changes **no** record, custody, or terminal decision. It completes its own route, releases the lock, and exits |
| the caller kills the bootstrap mid-route | the kernel releases the bootstrap's descriptors and its lock reference; **no record is removed without an authoritative reap or a signed §U6.1 P3 death proof**; `pid_mid` is re-parented to `init`, which reaps it; the middle exits at its own `m0` bound; the next attempt's §U6.1 P0–P3 preflight governs. Carried §V218.6 rows, unchanged |
| a competing waiter in the caller reaps the bootstrap | the caller loses only the exit status; the pipe reply is authoritative; the contract is unaffected (§V2110.2.4) |
| a **second launcher** starts concurrently | it spawns its own bootstrap; both bootstraps contend for `SPAWN.lock` under the carried bounded acquisition and the `s1`–`s5` stuck-holder route; the singleton property is unchanged, because it was always the lock and the records, never the process identity of the caller |
| bootstrap crash between any ordered unlink and its `fsync` | carried §V218.6/§U6.3 rows, `ENOENT`-tolerant, unchanged |
| restart before / after the middle's `m0` bound | carried §V218.6 rows, unchanged |

---

## V2110.3. A2 — the closed primitive and runtime theorem

### V2110.3.1 Interpreter identity, isolation readback, and the complete pre-fork preflight

The bootstrap's first executable statements after its four imports and its
primitive binding (§V2110.3.4). Every step's failure is **fail-closed with no
fork**; the detail token is written on the reply pipe and the process exits.

```text
P-a  PLATFORM (§V2110.6):
       u := _uname()
       require u.sysname == "Linux" and u.machine == "x86_64"
         otherwise ⇒ PLATFORM_UNSUPPORTED
P-b  INTERPRETER IDENTITY AND ISOLATION READBACK:
       require _implementation.name == "cpython"
       require _version_info[:3] == (3, 12, 3)
       require _flags.isolated           is truthy      # -I
       require _flags.no_site            is truthy      # -S
       require _flags.ignore_environment is truthy      # -E
       require _flags.safe_path          is truthy      # -P
       require _flags.no_user_site       is truthy      # implied by -I
         any failure ⇒ INTERPRETER_UNSUPPORTED / ISOLATION_NOT_PINNED
       — this is a READBACK OF EFFECT, not of argv. argv is read nowhere in this
         bootstrap and is never evidence of anything.
P-c  SINGLE TASK, first readback:
       _listdir("/proc/self/task") == exactly [str(_getpid())]
         otherwise ⇒ TOPOLOGY_MULTITASK
P-d  SINGLE TASK, second independent readback:
       /proc/self/status "Threads:" == "1"          otherwise ⇒ TOPOLOGY_MULTITASK
P-e  NO INHERITED CHILDREN:
       the ONE permitted wildcard wait in this contract, at exactly this place,
       before any fork:  _waitpid(-1, WNOHANG)
         raises OSError with errno ECHILD ⇒ correct: this process has no children
         returns ANY value                ⇒ INHERITED_CHILD ⇒ refuse
         any other error                  ⇒ PREFLIGHT_INCONCLUSIVE ⇒ refuse
       — permitted here and nowhere else because (i) it precedes every fork, so
         it cannot steal a reap from any W-site, and (ii) its ONLY accepted
         outcome is the exception. If it did return a pid it would have reaped an
         inherited child, which is why the route immediately refuses.
P-f  DESCRIPTOR PREFLIGHT (§V2110.2.6): fstat and inheritability of fds 3–6;
       /proc/self/fd contains exactly {0,1,2,3,4,5,6} plus the transient listing
       descriptor                                    otherwise ⇒ FD_TOPOLOGY
P-g  SIGNAL STATE — carried §V219.2.4/§V219.2.5 byte-for-byte in substance:
       G-4 mask capture (under §V2110.6's grammar) → N-1 derived-mask reset pass
       → N-2 unconditional signal.signal(SIGCHLD, SIG_DFL) → V-4 SigCgt == 0
       → V-5 SIGCHLD not ignored → V-6 no other ignored bit moved
       → V-7/V-8 single task again → V-9 getsignal corroboration
P-h  REQUEST: read fd 3 to EOF; validate against §V2110.2.5's closed grammar
         any deviation ⇒ REQUEST_MALFORMED / REQUEST_TRUNCATED
⇒ only now may c1 acquire SPAWN.lock, and only then c2, c3, c4.
```

### V2110.3.2 The exact import closure: what is imported, native or pure, and what each can do

The bootstrap's own import statements are exactly four, at module top, with no
conditional, deferred, or dynamic import anywhere:

```text
import os
import sys
import signal
import time
```

`fcntl` is required for `flock`. It is **not** imported by the bootstrap:
`os.open` + the carried `flock` acquisition is expressed through
`fcntl.flock` in the signed text, so the bootstrap **does** import `fcntl` as a
fifth module. Its permitted set is therefore exactly
**`{os, sys, signal, time, fcntl}`**, and §V2110.3.9's module-scoped allowlist
pins that five-element set literally.

| Module | Native / pure | Transitive Python closure at import | Starts a task? | Registers an at-fork callback? | Installs a handler/hook? |
|---|---|---|---|---|---|
| `os` | Python wrapper over the built-in `posix` C module | `sys`, `abc` (→`_abc` C), `stat` (→`_stat` C), `_collections_abc`, `posixpath`, `genericpath` | no | no — it *defines* `register_at_fork` but never calls it | no |
| `sys` | built-in C | none | no | no | no |
| `signal` | Python wrapper over the built-in `_signal` C module | `enum` (→`types`, `operator`), `functools` (→`types`, `collections`, `reprlib`, **`_thread`**) | **no** — see the note below | no | no; it *defines* `signal()` but installs nothing at import |
| `time` | built-in C | none | no | no | no |
| `fcntl` | built-in C | none | no | no | no |

> **The `_thread` note, stated because a reviewer will find it.** CPython's
> `signal.py` imports `functools`, which does `from _thread import RLock`.
> **Importing `_thread` binds a module; it creates no task.** The
> only way a task comes into existence is a call to
> `_thread.start_new_thread` (or an equivalent native call), and §V2110.3.9's
> AST grammar makes the *name* `_thread`, the attribute `start_new_thread`, and
> every other task-creating symbol **syntactically unreachable in the bootstrap
> root**. `P-c`/`P-d` independently confirm the task count is one at preflight,
> and §V2110.3.8 explains why it cannot change afterwards. This is disclosed
> rather than hidden: the import closure is not empty of threading machinery,
> and the argument is about calls, not about imports.

**No project package, no `philosophia`, no `numpy`, no `scipy`, no `torch`, no
backend, no adapter, and no C extension beyond the five built-ins above is
imported.** With `-S` there is no `site-packages` on `sys.path` at all, so a
project or third-party import would fail rather than silently succeed.

### V2110.3.3 Every operation before the first child

Exhaustive, in execution order. The column that matters is the last two.

| # | Operation | Can register an at-fork callback? | Can create a native task? |
|---|---|---|---|
| 1 | CPython startup with `-I -S -E -P` | no `site`, no `.pth`, no `sitecustomize`, no `usercustomize`, no `PYTHON*` env, no cwd/user-site path ⇒ **no user code runs at all** | no |
| 2 | the five imports of §V2110.3.2 | no (table above) | no (table above) |
| 3 | primitive binding (§V2110.3.4) — attribute reads and identity comparisons | no | no |
| 4 | `P-a`/`P-b` — `os.uname`, `sys.flags`/`version_info`/`implementation` reads | no | no |
| 5 | `P-c`…`P-f` — `os.listdir`, `os.open`/`read`/`close`, `os.fstat`, `os.get_inheritable`, one `waitpid(-1, WNOHANG)` | no | no |
| 6 | `P-g` — `signal.signal(n, SIG_DFL)` × k, `signal.getsignal`, `/proc` reads | no | no |
| 7 | `P-h` — `os.read`, `bytes.split`, literal comparisons, `int()` | no | no |
| 8 | `c1` — `fcntl.flock`, `time.clock_gettime_ns`, `os.open` | no | no |
| 9 | `c2` — atomic no-replace install: `os.open`, `os.write`, `os.fsync`, `os.rename`, `os.unlink` | no | no |
| 10 | `c3` — `os.pipe2` × 4 | no | no |
| 11 | `c4` — `os.fork` | it **runs** any registered callback; **none is registered**, by rows 1–10 | it is the fork itself |

**Nothing in rows 1–10 can register an at-fork callback or create a task.** That
is the substance of the closure theorem, and it is a property of the
*construction* — an isolated interpreter plus five audited imports plus a closed
list of operations — not of a static walk over a repository.

### V2110.3.4 Genuine primitive binding, identity validation, and the no-rebinding rule

Immediately after the five imports, at module scope, before any other statement:

```text
_fork        = os.fork          _waitpid  = os.waitpid     _kill    = os.kill
_killpg      = os.killpg        _getpid   = os.getpid      _getppid = os.getppid
_open        = os.open          _read     = os.read        _write   = os.write
_close       = os.close         _fstat    = os.fstat       _stat    = os.stat
_listdir     = os.listdir       _unlink   = os.unlink      _fsync   = os.fsync
_rename      = os.rename        _pipe2    = os.pipe2       _dup2    = os.dup2
_execve      = os.execve        _setsid   = os.setsid      _exit_   = os._exit
_uname       = os.uname         _devnull  = os.devnull
_flock       = fcntl.flock      _clock    = time.clock_gettime_ns
_sigsignal   = signal.signal    _getsignal = signal.getsignal
_SIGCHLD     = signal.SIGCHLD   _SIG_DFL  = signal.SIG_DFL
_flags = sys.flags ; _version_info = sys.version_info
_implementation = sys.implementation ; _executable = sys.executable
```

**Identity validation**, executed once, immediately after the binding:

```text
for every bound CALLABLE above:
    require type(f).__name__ == "builtin_function_or_method"
    require getattr(f, "__self__", None) is not None
    require f.__self__.__name__ in {"posix", "fcntl", "time", "_signal"}
    require f.__qualname__ == the expected bare name
  any failure ⇒ PRIMITIVE_NOT_GENUINE ⇒ fail-closed, no fork
```

**The no-rebinding rule**, three parts, each enforced by §V2110.3.9's grammar:

1. **Every later use goes through the local name.** The strings `os.`, `signal.`,
   `fcntl.`, `time.`, `sys.` appear in the bootstrap **only** in the binding
   block above. Any other attribute access on those module objects is a
   syntactic violation.
2. **No rebinding of the local names.** Each `_name` is assigned exactly once,
   at module scope; a second assignment, an `AugAssign`, a `del`, a `global`
   statement naming it, a `setattr` targeting it, or its appearance as a
   function parameter or comprehension variable is a syntactic violation.
3. **No indirection.** `getattr`, `setattr`, `delattr`, `vars`, `globals`,
   `locals`, `eval`, `exec`, `compile`, `__import__`, `importlib`, subscripted
   call targets, and calls to expressions that are not a plain `Name` are all
   syntactic violations.

**Why this is stronger than v2.1.9's claim.** v2.1.9 asserted that the textual
`os.waitpid(...)` in the source would invoke CPython's genuine callable; X
Attack 2 showed that a startup monkeypatch defeats it. Here (i) nothing can have
monkeypatched anything, because with `-I -S` no user code ran before the module
body; (ii) the binding happens on the **first** statements after import, before
any other operation; and (iii) the identity check is a positive test on the
bound object, not an assumption. All three are needed; none alone would do.

### V2110.3.5 CPython's own internal at-fork callbacks

`os.fork()` calls `PyOS_BeforeFork()` → fork → `PyOS_AfterFork_Parent()` /
`PyOS_AfterFork_Child()`. Their work is: take and release the import lock and
the runtime's internal locks; reinitialize the interpreter's thread state,
locks, and — in the child — the GIL and the single remaining thread state; run
the Python callables registered through `os.register_at_fork`. **None of that
creates a process, reaps a process, or sends a signal**, and the third item is
empty by §V2110.3.3 row 11. There is no enumeration API for registered
callbacks, which is exactly why v2.1.9's "no gate can even detect them" (X
Attack 2, case 1) was fatal there and is irrelevant here: **the bootstrap does
not detect them; its construction makes their registration impossible.**

### V2110.3.6 Asynchronous entries and signal dispositions

The **only** asynchronous entry into a task is a signal handler. After `P-g`,
`SigCgt == 0` is read back from the kernel, so no signal in this process has a
catching handler and no Python-level callback can be dispatched. Every
deliverable signal takes its default action — terminate, ignore, stop, or
continue — and none of those executes process code. `SIGPIPE` remains `SIG_IGN`
(CPython's startup default, untouched by `N-1` because an ignored signal carries
no `SigCgt` bit, mechanically proved by `V-6`); the carried §U2.3 `m4`/`m8`
`EPIPE` route is therefore preserved. `KeyboardInterrupt` no longer exists in
this process: a `SIGINT` terminates the bootstrap by default action, which the
crash rows of §V2110.2.8 already cover safely. Because `start_new_session=False`,
an operator's terminal `SIGINT` still reaches the bootstrap — deliberate, so a
stuck bootstrap remains interruptible by the ordinary means.

### V2110.3.7 Every entry point, and why only the constructed bootstrap has process authority

| Entry | Has process authority? | Why |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` exec'd with the pinned `-I -S -E -P` invocation and the four fds | **yes, and only this** | it is the only code that acquires `SPAWN.lock`, installs the singleton records, and calls `_fork` |
| the same script exec'd with weaker flags | **no** | `P-b`'s `sys.flags` readback fails ⇒ refusal, no fork |
| the same script `import`ed as a module by anything | **no** | it takes no argv and does nothing on import; its process-control body runs only under `if __name__ == "__main__":`, and `P-b`…`P-f` would fail in any host anyway |
| `generic_harness.py`'s six public commands | **no** | they hold no lock, install no record, and call no fork/wait/kill primitive; their entire process-control interaction is `L-1`…`L-4` |
| `--officina-bootstrap` (§Z3.3, controller/worker adapter) | **no** | unchanged, refusal-first, and it is a role image, not a process-control surface |
| `--officina-supervisor-role` (new, §V2110.2.7) | **no** | it is the *target* of an `execve` performed by the grandchild; it acquires no lock and forks no middle child. Refusal-first |
| any test | **no in-process authority** | fork-path tests spawn a real bootstrap process with the pinned invocation into a disposable root and observe it from outside |

> **The key structural difference from v2.1.9.** v2.1.9 gave process authority to
> a program that could be entered many ways and then tried to *gate* the bad
> ways. v2.1.10 gives process authority to a program that **can only come into
> existence one way**, and the one way is an `execve` whose isolation is read
> back from the interpreter itself.

### V2110.3.8 The closure theorem, with premises that follow from the construction

> **Theorem.** In the bootstrap process, from the completion of `P-h` until the
> process exits, (i) exactly one task exists, (ii) no asynchronous callback can
> execute, (iii) the only code that executes is the bootstrap root plus the
> five-module import closure of §V2110.3.2, and (iv) `pid_mid` can be reaped by
> no entity other than this task.
>
> **Premises, and where each comes from:**
>
> | # | Premise | Source | Kind |
> |---|---|---|---|
> | 1 | no user code ran before the module body | `-I -S -E -P`, **read back** at `P-b` from `sys.flags` | constructed + runtime readback |
> | 2 | exactly one task at `P-h` | `execve` terminates every other task; `P-c` and `P-d` confirm | constructed + two runtime readbacks |
> | 3 | no catching handler at `P-h` | `N-1` reset pass; `V-4` reads `SigCgt == 0` | constructed + runtime readback |
> | 4 | no at-fork callback is registered | §V2110.3.3 rows 1–10: no operation that could register one has executed | constructed (enumerated) |
> | 5 | the executed code is exactly the root plus the five-module closure | premise 1 removes every other source; there is no project package on `sys.path`; §V2110.3.9 pins the root's bytes by hash and its imports by a module-scoped allowlist | constructed + statically verified |
> | 6 | the root contains no task-creating call, no wildcard wait after `P-e`, no handler installation, and no indirection | §V2110.3.9's closed AST grammar over **one small file** | statically decided |
> | 7 | `pid_mid` is a direct child of this process only | `c4`'s `os.fork` in this process | constructed |
>
> **Proof.** (i) A task joins a thread group only via `clone(CLONE_THREAD)`
> issued by a task already in it; by premise 2 the only such task is this one;
> by premises 5 and 6 the code it executes contains no task-creating call; by
> premises 3 and 4 no other code can be dispatched onto it. (ii) is premise 3.
> (iii) is premises 1 and 5. (iv) By premise 7 and the Linux rule that a `wait`
> reaps only direct children, the reaper set of `pid_mid` is the task set of this
> process, which by (i) is this task, whose wait calls are exactly W-1…W-5. ∎
>
> **What is claimed for each premise, exactly.** Premises 1–3 are **read back
> from the kernel or the interpreter at runtime**. Premise 4 is an
> **enumeration** over a closed list of operations. Premises 5 and 6 are
> **statically decided over one small file** whose bytes are pinned by hash —
> which is a decidable problem, unlike v2.1.9's attempt to decide it over an
> arbitrary Python process. Premise 7 is a **construction**. **No premise is
> inferred from argv, and none asserts that a repository AST equals a runtime
> executor set.**
>
> **What is *not* claimed.** That the CPython 3.12.3 build is itself reviewed
> byte-for-byte (it is a pinned, reviewed *identity*, checked at `P-b`, not a
> hashed artifact); that the *caller* is clean (it is assumed dirty); that the
> *supervisor* process is clean (§V2110.2.7's scope note); or that the
> filesystem is protected against a same-UID actor (the A3 residual is untouched).

### V2110.3.9 The exact future verifier algorithm and manifest changes

Replaces §V219.2.6, §V219.4.3, and the claim that today's `verification.py`
already proves any of this. **The existing bytes prove none of it**; what
follows is the exact amendment a later implementation review must make.

```text
CHANGE 1 — roots
  PRODUCTION_ROOTS = (
      "scripts/officina_activate_t.py",
      "scripts/verify_officina_active.py",
      "src/philosophia/officina/generic_harness.py",
      "scripts/officina_process_control_bootstrap.py",          # ADDED
  )

CHANGE 2 — module-scoped absolute-import allowlist (replaces the flat global set
           for the named files; the flat set remains the default for the rest)
  ALLOWED_ABSOLUTE_IMPORTS = { …the sixteen signed members, UNCHANGED… }
  MODULE_SCOPED_ABSOLUTE_IMPORTS = {
      "scripts/officina_process_control_bootstrap.py":
          frozenset({"os", "sys", "signal", "time", "fcntl"}),
      "src/philosophia/officina/generic_harness.py":
          ALLOWED_ABSOLUTE_IMPORTS,        # NOTE: `signal` is NOT a member here
  }
  Rule: for a file with an entry, its permitted set is EXACTLY that entry — not
  the union with the default. `sys` is added to ALLOWED_ABSOLUTE_IMPORTS so the
  scoped set is expressible; no file without a scoped entry gains `sys`, because
  CHANGE 3's rule S-7 forbids `sys` outside the scoped map.

CHANGE 3 — the closed AST grammar for the bootstrap root, checked over its
           module AST. Each violation is FAIL-CLOSED with the named result.
  S-1  imports: exactly five `ast.Import` nodes, exactly the five names, at
       module scope, none aliased, no `ImportFrom`, no import inside any
       function/class/conditional        ⇒ "bootstrap import shape differs"
  S-2  no `ast.Global`, `ast.Nonlocal`, `ast.AsyncFunctionDef`, `ast.Await`,
       `ast.Yield`, `ast.YieldFrom`, `ast.Lambda`, `ast.ClassDef`,
       `ast.With`/`AsyncWith` whose context expression is not a pinned form,
       `ast.Try` whose handler binds a name it then calls, decorators, or
       `ast.Starred` in a call to a bound primitive
                                          ⇒ "bootstrap prohibited syntax"
  S-3  binding block: the exact assignment list of §V2110.3.4, in that order,
       at module scope, each target a plain `Name`, each value an
       `Attribute(Name(module), attr)` with module in the five and attr in the
       pinned per-module attribute set  ⇒ "bootstrap primitive binding differs"
  S-4  single assignment: every `_name` from S-3 appears exactly once as a
       store target in the whole file; never as an `AugAssign` target, a `del`
       target, a parameter, a comprehension target, an `as` target, or a
       `setattr` first argument         ⇒ "bootstrap primitive rebound"
  S-5  module-attribute access: the names `os`, `sys`, `signal`, `time`,
       `fcntl` appear as an `Attribute` value ONLY inside the S-3 block
                                          ⇒ "bootstrap module attribute escape"
  S-6  call targets: every `ast.Call.func` is a plain `Name`, a bound `_name`,
       or a whitelisted builtin from the closed set
       {len,int,str,bytes,range,enumerate,sorted,min,max,abs,tuple,list,dict,
        set,frozenset,isinstance,type,repr,ord,chr,divmod,bool}; never a
       `Subscript`, never an `Attribute` other than the pinned bytes/str/int
       methods, never an arbitrary expression
                                          ⇒ "bootstrap indirect call target"
  S-7  forbidden names anywhere in the file, as `Name`, `Attribute`, or string
       literal used as a name: `_thread`, `threading`, `multiprocessing`,
       `concurrent`, `asyncio`, `ctypes`, `subprocess`, `atexit`, `gc`,
       `register_at_fork`, `start_new_thread`, `settrace`, `setprofile`,
       `addaudithook`, `set_wakeup_fd`, `pthread_sigmask`, `pthread_kill`,
       `siginterrupt`, `alarm`, `setitimer`, `pidfd_send_signal`, `SIG_IGN`,
       `getattr`, `setattr`, `delattr`, `vars`, `globals`, `locals`, `eval`,
       `exec`, `compile`, `__import__`, `importlib`, `open` (the builtin)
                                          ⇒ "bootstrap forbidden symbol"
  S-8  wait forms: every call to `_waitpid` has a first argument that is either
       the literal `-1` (permitted at exactly ONE call site, whose enclosing
       function is the `P-e` preflight and which is lexically before every
       `_fork` call site) or a plain `Name` bound from a `_fork` return; no
       `_wait`, `_wait3`, `_wait4`, `_waitid` binding exists at all
                                          ⇒ "bootstrap wait form differs"
  S-9  signal calls: every `_sigsignal` call's second argument is `_SIG_DFL`;
       every `_getsignal` call's argument is `_SIGCHLD`
                                          ⇒ "bootstrap signal argument differs"
  S-10 no `__del__`, no `weakref`, no finalizer, no context manager whose exit
       calls a bound primitive           ⇒ "bootstrap finalizer present"

CHANGE 4 — the harness root loses `signal`
  `src/philosophia/officina/generic_harness.py` must contain NO `import signal`
  and no `signal.` attribute anywhere                ⇒ "harness imports signal"

CHANGE 5 — manifest invariants, in the existing
           `philosophia.officina.production-call-graph.v1` record
  manifest["roots"] == list(PRODUCTION_ROOTS)                    (four entries)
  manifest["reachable_sources"] == sorted(reachable)             (unchanged rule)
  manifest["import_edges"] == the computed closure                (unchanged rule)
  manifest["dynamic_resolution"] is False                         (unchanged)
  AND the manifest gains ONE field, `root_source_sha256`, a mapping from each
  root's repository-relative path to the SHA-256 of its exact bytes, which the
  verifier recomputes and compares. A mismatch ⇒ "production root bytes differ".
  This is the ONLY schema addition, and the manifest is a control artifact, not
  a scientific or archival object.

RUNTIME PREFLIGHT — the properties that CANNOT be decided statically, bound
  instead by the construction and checked at run time, each fail-closed with no
  fork: P-a platform, P-b interpreter identity and the four isolation flags,
  P-c/P-d single task, P-e no inherited children, P-f descriptor topology,
  P-g SigCgt == 0 and the SIGCHLD disposition, P-h request grammar, and the
  §V2110.3.4 primitive identity validation.
```

**Two-implementer determinacy.** S-1…S-10 are decidable syntactic predicates
over one file's AST; CHANGE 5 pins that file's bytes by hash; the runtime
preflight is a fixed list of readbacks with fixed comparisons. There is no
"probe", no discretionary analysis, and no place where two conforming
implementers could accept different runtime executor sets.

---

## V2110.4. A3 — total process primitives and `WAIT_ONE`

### V2110.4.1 The structural classifier, added to `WAIT_ONE`

§V219.3.1's five results are carried; a **sixth** is added, and it is evaluated
**first**, before any errno mapping.

```text
WAIT_ONE(pid_mid, site) → REAPED_POSITIVE | NOT_YET | CONTRADICTED_ECHILD
                        | RETRY_EINTR | INCONCLUSIVE_OTHER
                        | STRUCTURAL_VIOLATION            ← new

  PRECONDITION (carried): OWNERSHIP(pid_mid) != REAPED.

  r := _waitpid(pid_mid, WNOHANG)          # the LOCALLY BOUND genuine primitive

  STRUCTURAL CLASSIFICATION of the returned object, in this order:
    not a tuple                                  ⇒ STRUCTURAL_VIOLATION
    len(r) != 2                                  ⇒ STRUCTURAL_VIOLATION
    type(r[0]) is not int or type(r[1]) is not int
                                                 ⇒ STRUCTURAL_VIOLATION
      (bool is rejected: `type(x) is int`, not isinstance)
    r[0] < 0                                     ⇒ STRUCTURAL_VIOLATION
    r[0] != 0 and r[0] != pid_mid                ⇒ STRUCTURAL_VIOLATION
    r[0] == 0 and r[1] != 0                      ⇒ STRUCTURAL_VIOLATION
    r[1] < 0 or r[1] > 0xFFFF                    ⇒ STRUCTURAL_VIOLATION
    r == (pid_mid, status)                       ⇒ REAPED_POSITIVE; OWNERSHIP := REAPED
    r == (0, 0)                                  ⇒ NOT_YET

  EXCEPTION CLASSIFICATION — every BaseException, with no bare re-raise:
    OSError with errno ECHILD                    ⇒ CONTRADICTED_ECHILD
    OSError with errno EINTR                     ⇒ RETRY_EINTR
    OSError, any other errno                     ⇒ INCONCLUSIVE_OTHER
    OSError with errno None or a non-int errno   ⇒ STRUCTURAL_VIOLATION
    SystemExit                                   ⇒ STRUCTURAL_VIOLATION
    KeyboardInterrupt                            ⇒ STRUCTURAL_VIOLATION
    GeneratorExit                                ⇒ STRUCTURAL_VIOLATION
    MemoryError, RecursionError                  ⇒ STRUCTURAL_VIOLATION
    ANY other BaseException                      ⇒ STRUCTURAL_VIOLATION
  Nothing escapes: the handler is `except BaseException`, and the classifier is
  total over the union of "returned object" and "raised object".
```

> **The single safe continuation of `STRUCTURAL_VIOLATION`, at every site.**
> A structurally impossible result means the running primitive is **not** the
> genuine `posix.waitpid`, i.e. premise 5 or 6 of §V2110.3.8 has failed and the
> process is not the reviewed program.
>
> ```text
> STRUCTURAL_VIOLATION ⇒
>   1. it is NEVER death and NEVER sets REAPED;
>   2. OWNERSHIP := CONTRADICTED, irreversibly ⇒ no further signal to any pid,
>      ever, at any site (the carried §V218.3.1 single kill precondition);
>   3. no record is installed, modified, or removed;
>   4. the site's continuation is the same as CONTRADICTED_ECHILD's at that site
>      (§V219.3.4, carried), so the terminal selection is unchanged and total;
>   5. the detail token STRUCTURAL_VIOLATION is carried into the reply when a
>      reply is written.
> ```
>
> The same six-way classification is applied to `_kill`/`_killpg` (return value
> must be `None`; any other object or any `BaseException` outside the carried
> `SIGNAL_ATTEMPT` errno set ⇒ `STRUCTURAL_VIOLATION` ⇒ `CONTRADICTED`, no
> further signal) and to `_fork` (return must be an `int ≥ 0`; a negative value,
> a non-`int`, or any `BaseException` ⇒ pre-fork/ownership-never-established
> refusal, since ownership is set only on a strictly positive return).

### V2110.4.2 The carried W-1…W-5 tables, bound to the genuine primitives

§V219.3.2's five site instantiations, §V219.3.3's mutual-exclusivity proof, and
§V219.3.4's result × site product are carried **byte-for-byte**, with exactly two
changes: every `os.waitpid` is `_waitpid` (§V2110.3.4), and every site's product
row gains the `STRUCTURAL_VIOLATION` column, whose entry at every site is
"`CONTRADICTED`; no signal; the site's `CONTRADICTED_ECHILD` continuation".
Restated for completeness:

| Result | W-1 | W-2 | W-3 | W-4 | W-5 |
|---|---|---|---|---|---|
| `REAPED_POSITIVE` | `REAPED`; `T1` | `REAPED`; §U6.3 removal; refuse | `REAPED`; per-member proof then §U6.3; refuse | `REAPED`; P3 continues | `REAPED`; attempt continues |
| `NOT_YET` | poll to `t0+D` | poll to `t0+D` | poll to `t0+D` | poll to `t0+D` | attempt continues; ≤2 tries |
| `RETRY_EINTR` | re-issue within deadline | re-issue | re-issue | re-issue | re-issue once, then `NOT_YET` |
| `CONTRADICTED_ECHILD` | `CONTRADICTED`; `T2`/`B` | `CONTRADICTED`; identity known ⇒ `T2`-shaped | as W-2 | `CONTRADICTED`; **P3 unaffected** | `CONTRADICTED`; attempt continues |
| `INCONCLUSIVE_OTHER` | poll, then terminal selection | poll, then selection | poll, then selection | **P3 unaffected** | attempt continues |
| **`STRUCTURAL_VIOLATION`** | `CONTRADICTED`; no signal; `T2`/`B` | `CONTRADICTED`; no signal; `T2`-shaped | `CONTRADICTED`; no signal; `T2`-shaped | `CONTRADICTED`; no signal; **P3 unaffected** | `CONTRADICTED`; no signal; attempt continues |
| invoked after `REAPED` | contract violation: no syscall, no signal | " | " | " | " |
| stop / continue status | impossible (`WNOHANG` without `WUNTRACED`) | " | " | " | " |

### V2110.4.3 W-5 re-proved with a middle stopped between `m8` and `m9`

| Sub-case | Trace | Result |
|---|---|---|
| middle running, has not reached `m9` | first `WNOHANG` ⇒ `(0,0)` ⇒ `NOT_YET`; the bootstrap continues `c14`–`c17`; the second `WNOHANG` before `c18` ⇒ `REAPED_POSITIVE` or `NOT_YET` | **bootstrap succeeds** either way |
| middle **`SIGSTOP`ed** between `m8` and `m9` | `WNOHANG` without `WUNTRACED` **cannot report a stop**, so both attempts return `(0,0)` ⇒ `NOT_YET` | **bootstrap succeeds.** W-5 sends **no signal**, so the stopped middle is not disturbed. It holds a fork-shared `SPAWN.lock` reference, so the singleton is not free until it dies — which is the **carried** A3 stopped-middle residual (§U2.7 residual 2), not a new defect, and is disclosed as such |
| middle exits between the two attempts | second attempt ⇒ `REAPED_POSITIVE` | success; no zombie |
| both attempts `NOT_YET`, bootstrap then exits | the middle is re-parented to `init`, which reaps it | success; the carried zombie residual is bounded by the bootstrap's own short lifetime — **strictly narrower than v2.1.9**, where a long-lived CLI could hold the zombie indefinitely |
| `ECHILD` at either attempt | `CONTRADICTED`; **no signal**; the attempt still succeeds, because W-5's outcome never gates the bootstrap's success | success |
| `STRUCTURAL_VIOLATION` at either attempt | `CONTRADICTED`; no signal; success unchanged | success |
| **deadline cuts** | W-5 has **no deadline** and at most two non-blocking attempts, so there is no deadline cut to analyse — this is why it was specified that way | — |
| the bootstrap dies at any point during W-5 | kernel releases its fds and lock reference; the middle exits at `m9` or its bound; the grandchild is already `execve`d and holds the lock until `g3`; carried §V218.6 rows govern | safe |

### V2110.4.4 `T1`/`T2`/`B`, the zombie/P3 route, restart, and the second launcher

All carried from §V218.4 and §V219.3–§V219.5, re-proved under the new topology:

- **`T1`** — entered only on `REAPED_POSITIVE` from the bootstrap's own targeted
  wait. Ordered §U6.3 removal of all four records under the held lock, then
  release, then a retryable refusal written on the reply pipe.
- **`T2`** — a truthful `SPAWNING_MIDDLE.json` from an identity captured while
  `OWNERSHIP == OWNED`; only `SPAWNING.json` removed; `pid_mid` retained in
  memory for W-4; lock released; retryable refusal. Resolved by the **existing**
  §U6.1 P0–P3 and §U2.5 `s4`/`s5` routes, unchanged.
- **the zombie/P3 route** — a zombie holds no descriptor and no lock reference,
  is `/proc` state `Z` with a matching start identity, and therefore satisfies
  §U6.1 P3's death proof precisely for any other process; W-4 reaps it on a
  later attempt in the same bootstrap process, and otherwise `init` does when
  the bootstrap exits. **Because the bootstrap is short-lived by construction,
  the residual is bounded by one process lifetime**, which is a strict
  improvement on v2.1.9's long-lived-CLI case.
- **`B-OWNED`** — unchanged in substance: non-returning, retains lock, record,
  handle and bootstrap ends, installs nothing, writes **no** reply, and exits
  only via `REAPED_POSITIVE ⇒ T1` or a capture `⇒ T2`. Ordinarily terminates:
  `SIGKILL` is ownership-authorized and needs no `/proc`, and even with every
  signal suppressed the middle exits at its own `m0` bound and is reaped.
- **restart / second launcher** — §V2110.2.8, unchanged in outcome from the
  carried rows.

### V2110.4.5 `B-CONTRADICTED` is outside supported history — proved without circularity

v2.1.9 excluded contradiction source (a) by citing its own executor-set
corollary; X F2 correctly called that circular. The replacement cites **no
theorem about the caller and no theorem about repository source**:

| Source of `CONTRADICTED` | What it requires | Excluded by |
|---|---|---|
| (a) `CONTRADICTED_ECHILD` | some entity other than this task reaped `pid_mid`, or the kernel auto-reaped it | **Process boundary** (§V2110.2.3): only a task of the bootstrap process can reap its direct child, and the bootstrap has exactly one task (`P-c`, `P-d`, two independent kernel readbacks, plus `execve`'s guarantee) whose only wait calls are W-1…W-5, none of which runs after `REAPED`. Auto-reaping is excluded by `N-2`'s unconditional `sigaction` write, with the `SIG_IGN`/handler half read back at `V-4`/`V-5`. **No premise here is about the caller.** |
| (b) `ESRCH` on an owned unreaped child | the task named by `pid_mid` does not exist although it was forked and not reaped | same as (a): an unreaped own child is a task in some state, and `kill(2)` on a zombie succeeds |
| (c) `PRESENT_VALID`, uncaptured, `ppid ≠ getpid()` | `/proc` reports a parent for our own unreaped child that is not us | a kernel contradiction |
| (d) captured start identity mismatches | the kernel start identity of our unreaped child changed | a kernel contradiction |
| (e) `STRUCTURAL_VIOLATION` (new) | `_waitpid` is not the genuine primitive | premises 5–6 of §V2110.3.8, i.e. the bootstrap root's bytes or its AST grammar are not the reviewed ones — an **implementation-contract** contradiction |

> **Result.** In every supported execution `OWNERSHIP` never becomes
> `CONTRADICTED`, so `B-CONTRADICTED` is never entered. It is reachable only
> after (i) a platform contradiction — the pinned CPython `PyOS_setsig`
> `sigaction` semantics or the Linux `SIG_IGN ∨ SA_NOCLDWAIT` auto-reap
> condition not holding; (ii) a kernel contradiction; or (iii) an
> implementation-contract contradiction — a bootstrap whose bytes or AST are not
> the reviewed ones, which CHANGE 5's `root_source_sha256` and CHANGE 3's
> grammar reject before it can be shipped.
>
> **It therefore remains classified as a non-returning safety sink outside
> supported history** (§V219.5.2, carried): it holds `SPAWN.lock`,
> `SPAWNING.json`, the in-process handle and the bootstrap ends; signals
> nothing; installs, removes and modifies nothing; **writes no reply**; and
> emits no refusal, event, ledger entry, capacity artifact, custody disposition,
> or anything citable. `s5` at a later launcher is a **consequence**, explicitly
> **not** a resolver, and no operator notice, caller exit, GC, finalizer, or
> indefinite retry is offered as one. **This is not a liveness route**: every
> supported execution reaches `T1` or `T2` (or `B-OWNED`, which ordinarily
> reaches `T1`).

---

## V2110.5. The carried identity, ownership, and signal surface

Unchanged and re-stated only to record that it is unchanged: §V218.3.1's
three-valued `OWNERSHIP` with `os.kill` executed **iff** `OWNED`; §V218.3.2's
fork-ownership PID-reuse proof, whose exclusivity premise is now supplied by
§V2110.2.3 and §V2110.3.8 instead of by the withdrawn theorem; §V218.3.3's
`WAIT_PROVE`/`ECHILD` rules; §V218.3.4's ten-row identity table I-1…I-10 including
the `ppid`-mismatch row I-4; §V218.3.5's `SIGNAL_ATTEMPT` with `ESRCH` as a
contradiction; §V218.3.6's ownership-gated `SIGTERM → SIGKILL` schedule with the
`D/2`, `D` and `≥` edge rules; and §V218.5's stage-M `m0`/`rel1`/fork-shared-lock
causal proof with `m5`/`rel2` retained only for cuts at or after `c8`. Every
`os.` primitive in those sections is the corresponding `_name` of §V2110.3.4.

---

## V2110.6. A4 — honest platform scope and mask width

**The all-Linux 16-digit claim of §V219.6 is withdrawn as false.** Y proved it:
Linux MIPS defines `_NSIG = 128`, and `render_sigset_t` emits one hex digit per
four signal positions, so a valid MIPS mask is 32 digits, which v2.1.9's `W-b`
rejects as malformed. X judged this closed; **Y's stricter disposition governs.**

### V2110.6.1 The pinned platform

```text
SUPPORTED PLATFORM for the process-control bootstrap, checked at P-a/P-b:
    os.uname().sysname   == "Linux"
    os.uname().machine   == "x86_64"
    sys.implementation.name == "cpython"
    sys.version_info[:3]    == (3, 12, 3)
    plus the exact reviewed build identity recorded in the implementation
    review (sys.version string and the distribution build tag), checked once at
    review time, not hashed at run time.
Any mismatch ⇒ PLATFORM_UNSUPPORTED or INTERPRETER_UNSUPPORTED ⇒ reply written,
NO fork, NO lock acquisition, NO record installed.
```

Inside that scope, and **only** inside it, `_NSIG == 64` holds, so
`render_sigset_t` emits exactly `64 / 4 = 16` hexadecimal digits and the carried
`MASK_FIELD` grammar's width rule is justified.

### V2110.6.2 The mask rule and the platform table

`MASK_FIELD`'s grammar (single occurrence, mandatory whitespace, maximal hex run
to end of line, no `0x` prefix, no sign, no internal whitespace, no trailing
byte) is carried **byte-for-byte** from §V219.6. Its width rule becomes:

```text
 W-a (architecture-independent, mandatory, carried):  4 * d >= int(_SIGCHLD)
 W-b (pinned-platform exact width, replacing the false all-Linux claim):
       d == 16, valid because P-a/P-b already required Linux x86_64 with
       _NSIG == 64. W-b is evaluated ONLY after P-a and P-b have passed, so it
       is never applied to a platform whose width it does not describe.
```

| Platform | `_NSIG` | `SIGCHLD` | Valid mask digits | This contract |
|---|---|---|---|---|
| **Linux x86_64** | 64 | 17 | 16 | **supported**; `W-a` (`64 ≥ 17`) and `W-b` (`16`) both pass |
| Linux i386 / ARM / ARM64 | 64 | 17 | 16 | **not supported** by `P-a` (`machine != "x86_64"`) — refused, even though the width rule would have been correct. Narrowing is deliberate: one reviewed platform, not a family |
| **Linux MIPS** | **128** | 18 | **32** | **explicitly unsupported.** `P-a` refuses at `machine`, **before** any mask is parsed, so the false `W-b` rejection Y found can no longer arise. Recorded here so the exclusion is visible rather than accidental |
| Linux Alpha / SPARC | 64 | 20 | 16 | not supported by `P-a` |
| a future Linux widening `_NSIG` on x86_64 | >64 | 17 | >16 | `W-b` fails ⇒ `VERIFY_INCONCLUSIVE` ⇒ no fork. Fail-closed on a rendering this contract has not reviewed |
| non-Linux | — | — | — | `P-a` refuses at `sysname` |

**`signal.NSIG` is deliberately not used**, and no architecture is silently
added: the permitted `signal` surface stays at the four carried names
(`signal`, `getsignal`, `SIG_DFL`, `SIGCHLD`). The width is not derived at run
time; it is **pinned inside a verified platform scope**, which is the smaller
and more auditable of the two repairs Y offered.

### V2110.6.3 Why this narrows an engineering surface only

The pin says: *the Officina supervisor's process-control bootstrap is reviewed
and supported on Linux x86_64 with CPython 3.12.3.* It is a statement about
which **host** may run the control plane. It is **not** a statement about
scientific devices, adapters, or off-CPU compute: the signed harness's off-CPU
device policy, its adapter admission rules, and every E1/E2/E3 and K1 boundary
are untouched, and on the present x86_64 host they are unaffected in fact as
well as in form. No scientific estimand, resource envelope, capacity ceiling,
custody rule, or Q/C boundary moves. Should the programme ever need another
control-plane architecture, the correct route is a fresh reviewed amendment that
extends `P-a` and states that architecture's `_NSIG` — not a silent widening.

---

## V2110.7. Crash/cut matrix and replay of both counterexamples

### V2110.7.1 Added and replaced crash/cut rows

Every §V218.6 and §V219.7.3 row not listed here carries forward unchanged.

| Cut / scenario | Single continuation |
|---|---|
| `P-a` platform or `P-b` interpreter/isolation mismatch | reply `REFUSED`/`PLATFORM_UNSUPPORTED`\|`INTERPRETER_UNSUPPORTED`\|`ISOLATION_NOT_PINNED`; **no lock, no record, no fork** |
| `P-c`/`P-d` more than one task | reply `REFUSED`/`TOPOLOGY_MULTITASK`; no fork |
| `P-e` returns a pid instead of raising `ECHILD` | reply `REFUSED`/`INHERITED_CHILD`; no fork. (The inherited child has been reaped by that call; the route refuses precisely because it must not proceed in a process it does not understand) |
| `P-f` descriptor topology differs | reply `REFUSED`/`FD_TOPOLOGY`; no fork |
| `P-g` any of `N-1`/`V-4`/`V-5`/`V-6`/`V-7`/`V-8`/`V-9` fails | carried §V219.7.3 rows; no fork |
| `P-h` request malformed or truncated | reply `REFUSED`/`REQUEST_MALFORMED`\|`REQUEST_TRUNCATED`; no lock, no fork |
| the reply pipe is closed early (caller died) | the reply write yields `EPIPE`, which `SIGPIPE = SIG_IGN` turns into an exception rather than death; it is recorded and **changes no record, custody, terminal, or ownership decision** |
| a bound primitive fails identity validation | reply `REFUSED`/`PRIMITIVE_NOT_GENUINE`; no fork |
| `_waitpid` returns a structurally impossible object at any W site | `STRUCTURAL_VIOLATION` ⇒ `CONTRADICTED` ⇒ no signal ⇒ that site's `CONTRADICTED_ECHILD` continuation (§V2110.4.1) |
| `_waitpid` raises `SystemExit` / `KeyboardInterrupt` / any other `BaseException` | identical |
| `_kill` returns a non-`None` object, or raises outside the carried errno set | `STRUCTURAL_VIOLATION` ⇒ `CONTRADICTED` ⇒ no further signal |
| `_fork` returns a non-`int` or a negative value, or raises | ownership is **never** established (it is set only on a strictly positive `int`); the pre-fork fail-closed body applies |
| the caller kills the bootstrap mid-route | §V2110.2.8 row: kernel release; no record removed without proof; middle exits at its `m0` bound; `init` reaps |
| a competing waiter in the caller reaps the bootstrap | the caller loses the exit status only; the pipe reply is authoritative |
| the grandchild's `execve` fails | the grandchild `os._exit(3)` with nothing written and nothing unlinked; `c13` reads EOF on `boot` ⇒ the carried §U2.5 stage-2 route governs |
| the supervisor role's refusal-first entry rejects any inherited token | `os._exit(3)`, nothing written, nothing unlinked; identical continuation |
| a second launcher runs concurrently | both bootstraps contend for `SPAWN.lock`; carried acquisition and `s1`–`s5`; the singleton property is the lock and the records, never the caller's identity |

### V2110.7.2 Replay of both v2.1.9 counterexamples

**Y Trace 1 / X F1 — the `.pth`/`sitecustomize` wrapper that rebinds `os.fork`
and starts a wildcard-reaping helper.**

| Step | v2.1.9 | v2.1.10 |
|---|---|---|
| 1. startup customization stores and wraps `os.fork`, prepares a helper | ran in the **process that would fork `pid_mid`** | runs in the **caller** only. The bootstrap is a **separate process** whose `execve` with `-S` means `site` is never imported, so `.pth`, `sitecustomize` and `usercustomize` **cannot run in it at all**, and with `-E`/`-I` no environment or user path can inject one |
| 2. every gate passes | true, and fatal | in the bootstrap there is nothing to pass: no customization ran. `P-b` reads the four isolation flags back from `sys.flags`, so a weaker invocation refuses |
| 3. `c4` resolves the rebound `os.fork`; the wrapper starts a helper, then forks | the helper is created **in `pid_mid`'s parent** | `c4` is `_fork`, bound at module scope from a clean import state and identity-validated. Nothing could have rebound it, because no user code ran. Even if the **caller's** `os.fork` is wrapped, the caller's helper is created in the **caller**, which is **not** `pid_mid`'s parent |
| 4. the helper polls `waitpid(-1, WNOHANG)` and reaps `pid_mid` | the harm | **impossible.** A wildcard wait in the caller ranges over the caller's direct children — the bootstrap — and can never reach `pid_mid` (§V2110.2.3). The worst it achieves is reaping the bootstrap, which costs an exit status the contract does not use |
| 5. the pid is reused while `OWNERSHIP == OWNED` | followed from 4 | **unreachable**: `pid_mid` stays `EXIT_ZOMBIE` until the bootstrap's own targeted `_waitpid` returns it |
| 6. the next `os.kill(pid_mid, …)` hits an unrelated process | the harm | **unreachable** |

**X Attack 2 case 2 / Y Trace 5 — a monkeypatched `os.waitpid` returning an
unmapped value, with no thread and no handler.**

| Step | v2.1.9 | v2.1.10 |
|---|---|---|
| a startup hook rebinds `os.waitpid` | invisible to every gate; the reviewed source's textual call invoked the patch | **cannot occur in the bootstrap**: no startup hook can run under `-I -S -E`. `_waitpid` is bound at module scope from the clean import state and identity-validated (`builtin_function_or_method`, `__self__` is `posix`, `__qualname__ == "waitpid"`), and §V2110.3.9's S-4/S-5 make rebinding it a syntactic violation of the reviewed root |
| it returns `(pid_mid + 1, status)`, `(0, nonzero)`, a non-tuple, or raises a non-`OSError` | **no continuation existed** | every one of those is now classified: `STRUCTURAL_VIOLATION` ⇒ never death, `OWNERSHIP := CONTRADICTED`, no signal ever again, no record touched, and the site's carried `CONTRADICTED_ECHILD` continuation (§V2110.4.1). **Totality no longer depends on the premise holding** — it is a defence that works even if it does |
| the process reaches an undefined W site | the finding | **unreachable**: `WAIT_ONE` is total over the union of every returned object and every raised object |

### V2110.7.3 The `B-CONTRADICTED` wedge trace of Y Trace 6

Y's six-step wedge began with "the `c4` wrapper from Trace 1 creates the helper
after `V-8`". Under §V2110.2.3 that helper cannot reap `pid_mid` no matter when
it is created or by whom, so step 3 ("the helper wildcard-reaps it") never
occurs, step 4's genuine `ECHILD` never arises, and the sink is not entered. The
exclusion argument cites the **process boundary and the bootstrap's own task
count**, never the withdrawn executor-set theorem — which is precisely what
F2 required.

### V2110.7.4 Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, verifier edit,
manifest, commit, host change, process, signature, activation, entropy, T/Q/C
work, E1/E2/E3 spend, or later gate. Obligations become due only after both
fresh independent v2.1.10 reviews confirm these bytes **and** the author signs
the amendment token.

All carried rows through §V219.8's 272 remain, except:

- **row 241 replaced:** the eight-step preflight `P-a`…`P-h` returns exactly one
  named result per step; no exception escapes; every non-`OK` result writes its
  reply token and reaches the pre-fork refusal with **no `os.fork`**, **no lock
  acquisition**, and **no record installed**.
- **rows 242/243 replaced:** the C219-1 replay is now a *process-tree* test —
  launch the bootstrap from a caller that has a wildcard-reaping helper thread
  and a monkeypatched `os.fork`/`os.waitpid`, and assert (i) the bootstrap
  refuses nothing on that account, (ii) `pid_mid` is never reaped by the caller,
  and (iii) the caller's helper observes only the bootstrap pid.
- **rows 249/250 replaced:** no in-process caller has process authority; every
  fork-path test spawns a real bootstrap process with the pinned invocation into
  a disposable root and observes it from outside.
- **rows 252/253 replaced:** `PYTHONFAULTHANDLER`, `-X dev`, `sitecustomize`,
  `usercustomize`, and a `.pth` executable line are each installed in the
  **caller's** environment and each asserted to have **no effect inside the
  bootstrap**, because `-I -S -E` prevent them from running there at all.
- **row 255 replaced:** `WAIT_ONE` is total over the union of every returned
  object and every raised object, including `STRUCTURAL_VIOLATION`.
- **rows 264/265 replaced:** the verifier assertions are CHANGES 1–5 of
  §V2110.3.9, not the withdrawn prose obligations.
- **rows 270/271 replaced:** the mask width rule is asserted only inside the
  pinned platform, and the v2.1.9-vs-v2.1.10 discrimination test is the
  process-tree replay above.

Added:

| # | Test | Covers |
|---|---|---|
| 273 | the pinned invocation is byte-exact: `argv` is the seven elements of §V2110.2.1, `env == {}`, `cwd == "/"`, `close_fds=True`, `preexec_fn=None`, `shell=False`, and the exec target is the inode the caller opened (`/proc/self/fd` readback), not a re-resolved name | A1 |
| 274 | `P-b` refuses when any one of `-I`, `-S`, `-E`, `-P` is dropped; assert the refusal is read back from `sys.flags` and that argv is never consulted anywhere in the bootstrap | A1, C219-1 |
| 275 | with `-S`, a `.pth` executable line, a `sitecustomize`, and a `usercustomize` present on the host each execute in the caller and **not** in the bootstrap; assert by observing that the module they would have installed is absent from the bootstrap's behaviour | A1, C219-1 |
| 276 | the bootstrap's import set is exactly `{os, sys, signal, time, fcntl}`; assert `json`, `hashlib`, `re`, `subprocess`, `pathlib`, `enum`, `dataclasses`, and every project package are absent, and that a project import would fail under `-S` rather than silently succeed | A1, A2 |
| 277 | the primitive binding block matches §V2110.3.4 exactly and the identity validation rejects a substituted callable (`builtin_function_or_method`, `__self__` module name, `__qualname__`) | A2, M219-2 |
| 278 | `P-e`'s single wildcard wait raises `ECHILD` in a correctly launched bootstrap; a fixture that hands the bootstrap an inherited child makes it return, and the route then refuses with `INHERITED_CHILD` and no fork | A2 |
| 279 | `P-f` descriptor topology: exactly `{0,1,2,3,4,5,6}`, fds 3/4 FIFO, fds 5/6 directory, inheritability as pinned; each deviation refuses | A1 |
| 280 | the request grammar rejects wrong field count, wrong literal, wrong length, an out-of-class byte, a second line, a missing terminator, and an over-long frame; assert **no** field can carry a path, module, symbol, callable, signal number, fd, or timeout | A1 item 5 |
| 281 | the reply is the sole authoritative result: a fixture that reaps the bootstrap from the caller before the caller's own wait still yields the correct outcome from the pipe | A1, §V2110.2.4 |
| 282 | the caller never signals the bootstrap: static assertion over `generic_harness.py`'s launcher path | A1 |
| 283 | **the process-boundary property**: a wildcard `waitpid(-1, WNOHANG)` in the caller never returns `pid_mid`; assert across the whole stage-M window with the middle exiting at every injected instant | A1, C219-1, F1 |
| 284 | `WAIT_ONE` structural rows: non-tuple, wrong arity, `bool` elements, negative pid, wrong positive pid, `(0, nonzero)`, out-of-range status — each `STRUCTURAL_VIOLATION`, never `REAPED` | A3, M219-2 |
| 285 | `WAIT_ONE` exception rows: `ECHILD`, `EINTR`, other errno, `errno is None`, `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`, `MemoryError`, `RecursionError`, an arbitrary `BaseException` — each classified, none escaping | A3, M219-2 |
| 286 | `STRUCTURAL_VIOLATION`'s continuation at all five sites: never death, `CONTRADICTED` set, no signal ever again, no record touched, the site's `CONTRADICTED_ECHILD` continuation taken | A3 |
| 287 | `_kill` and `_fork` structural classifiers behave as §V2110.4.1 states; ownership is set only on a strictly positive `int` fork return | A3 |
| 288 | W-5 with the middle `SIGSTOP`ed between `m8` and `m9`: both attempts return `(0,0)`, **no signal is sent**, the bootstrap **succeeds**, and the carried stopped-middle A3 residual is the only consequence | A3 |
| 289 | every W-5 sub-case of §V2110.4.3, including `ECHILD`, `STRUCTURAL_VIOLATION`, bootstrap death mid-W-5, and the `init`-reaps-the-zombie case | A3 |
| 290 | `T1`/`T2`/`B` selection, the zombie/P3/W-4 route, restart, and a concurrent second launcher all behave as §V2110.4.4 states | A3 |
| 291 | **`B-CONTRADICTED` unreachability**: enumerate sources (a)–(e) and assert each requires a platform, kernel, or implementation-contract contradiction; assert the argument nowhere cites an executor-set theorem or any property of the caller | A3, M219-2, F2 |
| 292 | when a contradiction is injected, the sink signals nothing, installs nothing, removes nothing, **writes no reply**, and emits nothing citable; assert `s5` is nowhere described as its resolver | A3 |
| 293 | the grandchild `execve`s the reviewed role; the retained `SPAWN.lock` fd is **not** `O_CLOEXEC` and survives; every other descriptor is scrubbed; a failed `execve` yields `os._exit(3)` with nothing written | A1 item 6 |
| 294 | the `--officina-supervisor-role` entry is refusal-first: every inherited token, fd number and type, spawning id, and parentage is verified before any behaviour; each mismatch exits with nothing written and nothing unlinked | A1, §V2110.9 row 23 |
| 295 | §Z3.3's controller/worker layout, `--officina-bootstrap`, `T_CTRL_FD_LOW/HIGH`, and §Z3.2's `t-spawn-intent.v1` role enum are **byte-unchanged** | no-regression |
| 296 | verifier CHANGE 1: `PRODUCTION_ROOTS` has exactly the four entries; the manifest's `roots` matches | A2 |
| 297 | verifier CHANGE 2: the module-scoped map gives the bootstrap exactly `{os, sys, signal, time, fcntl}` and `generic_harness.py` a set **without** `signal`; a file with a scoped entry does **not** get the union with the default | A2, M219-1 |
| 298 | verifier CHANGE 3: each of S-1…S-10 rejects a bit-exact negative fixture and accepts a bit-exact positive one | A2, M219-1 |
| 299 | verifier CHANGE 4: `generic_harness.py` contains no `import signal` and no `signal.` attribute | A2 |
| 300 | verifier CHANGE 5: `root_source_sha256` is recomputed and compared for all four roots; a one-byte change to the bootstrap fails the manifest | A2 |
| 301 | the platform table of §V2110.6.2: x86_64 accepted; MIPS, ARM64, i386, Alpha, SPARC and non-Linux each refused **at `P-a`, before any mask is parsed** | A4, m219-1 |
| 302 | `MASK_FIELD` still rejects empty, `0`, `0000`, 13-digit, 20-digit, `0x`-prefixed, signed, internally spaced, trailing-byte, duplicate, and missing values, and `W-b` is evaluated only after `P-a`/`P-b` pass | A4 |
| 303 | `signal.NSIG` is referenced nowhere; the permitted `signal` surface is exactly the four carried names | A4 |
| 304 | the reply pipe closing early yields `EPIPE` that changes no record, custody, terminal, or ownership decision | A1 item 7 |
| 305 | the caller killing the bootstrap at every injected instant: kernel release, no record removed without proof, middle exits at its `m0` bound, `init` reaps | A1 item 7 |
| 306 | `SIGPIPE = SIG_IGN` survives `N-1` and `V-6` proves no ignored disposition moved; the carried `m4`/`m8` `EPIPE` route is unchanged | no-regression |
| 307 | `N-1`/`N-2`/`V-4`…`V-9` behave exactly as carried, re-sited into the bootstrap, on every attempt | no-regression |
| 308 | the four singleton records, their key sets, §U6.2 `EEXIST`, §U6.1 P0–P3, and §U6.3 order are byte-unchanged, with the bootstrap as writer | no-regression |
| 309 | §V217.1's object-bound observation and both revalidation barriers are unchanged and operate `dir_fd`-relative to fd 5 | no-regression |
| 310 | §V218.3's ownership, identity table, `SIGNAL_ATTEMPT`, and TERM→KILL schedule are byte-unchanged with `_name` primitives | no-regression |
| 311 | §V218.5's stage-M `m0`/`rel1`/lock proof is unchanged and no stage-M text cites `m5`/`rel2` | no-regression |
| 312 | **whole-chain no-regression sweep**: diff every non-replaced section body of v2.1.9 and every carried layer against the text this correction claims to carry; assert the architectural repair changes no selector, custody, capacity, filesystem, event, E1/E2/E3, Q/C, or scientific rule | no-regression |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object. Contamination fixtures (rows 275, 283) install their hooks in
the **caller**, which is exactly where the architecture now says they are
harmless.

---

## V2110.8. No-regression over every carried signed surface

| Carried surface | Status under v2.1.10 |
|---|---|
| **Abstract `WAIT_ONE` W-1…W-5 automaton**, five site tables, exclusivity proof, result × site product (§V219.3) | carried **byte-for-byte**, extended by one column (`STRUCTURAL_VIOLATION`) and re-bound to `_waitpid` |
| **Resolved sole-importer contradiction** (§V219.4) | preserved in substance: still exactly **one** real importer topology, no unnamed module, no undeclared dependency. The importer moves from `generic_harness.py` to the new bootstrap root, and `generic_harness.py` loses `signal` entirely |
| **Short-mask rejection principle** (§V219.6's `MASK_FIELD` grammar) | carried byte-for-byte; only the width *justification* is re-scoped to the pinned platform |
| **`SIGCHLD` full-disposition reset** (§V218.2.2, `N-1`/`N-2`) and its `sigaction`/`execve`/`fork` provenance analysis | carried byte-for-byte, re-sited into the bootstrap |
| **`ECHILD`/`ESRCH` never death** | carried at all five sites and in `SIGNAL_ATTEMPT` |
| **Ten-row identity table I-1…I-10** | carried byte-for-byte |
| **Ownership-gated signals** and the fork-ownership PID-reuse proof | carried byte-for-byte; the exclusivity premise now comes from the process boundary |
| **Deletion of `T3`; `T1`/`T2`/`B` no-discard invariant** | carried; no returning route abandons a possibly live child |
| **Stage-M `m0`/`rel1` proof and the fork-shared lock** | carried byte-for-byte; `m5`/`rel2` still scoped to cuts at or after `c8` |
| **§V217.1 object-bound observation and both revalidation barriers** | carried, untouched. The bootstrap's `dir_fd`-relative operations are exactly the style §V217.1 already uses |
| **§V217.4 bound-language sweep**, revised row 86, D1's ground | carried; `B`'s unbounded loop remains consistent with the withdrawn fixed-total claims |
| **`CLOSE_OWNED`, `MALFORMED` dominance, §V216.1.2/.1.3, the three branch bodies `B-P`/`B-QM`/`B-QN`, §N2.3 P1–P7 custody, §V214.2.4 reconciliation, K1 constants and one-release accounting** | carried byte-for-byte |
| **Death-before-unlink, §U6.1 P0–P3, §U6.2 `EEXIST`, §U6.3 order, `s1`–`s5`** | carried byte-for-byte; the writer is the bootstrap instead of the old CLI process, which changes no rule |
| **§U2.1–§U2.4 channels, `c1`–`c18`, `m0`–`m9`, the `m4`/`m8` `EPIPE` route, `SIGPIPE = SIG_IGN`** | carried; `V-6` still proves `N-1` disturbed no ignored disposition |
| **§Z3.3's controller/worker adapter, its fixed argv layout, `--officina-bootstrap`, `T_CTRL_FD_LOW/HIGH`** | carried byte-for-byte. The new `--officina-supervisor-role` is a **separate** token with its own layout, so §Z3.3's thirteen-element layout and its `argv_template_sha256` semantics are untouched |
| **§Z3.2's signed `t-spawn-intent.v1` role enum `CONTROLLER\|WORKER`** | **untouched.** The new argv token is not a spawn-intent role |
| **A3 / B1 / C1 / D1 / K1** | no scientific cell reopened. A3's residual set is unchanged in kind; the stopped-middle and zombie residuals are **narrower**, because the bootstrap is short-lived. D1 unaffected: no supervisor waits on `SPAWN.lock` |
| **Signed generic harness v2→v2.3.1 and batch settlement v1→v1.1.1** — §J1–§J3, §D1 head/cache completion, §D2 inline `meter_evidence`, fixed process order, prefix settlement, archival boundaries, two-token meanings | referenced unchanged. The only harness-text changes are §V2110.9's narrow supersessions of the `signal` conjunct and the no-additional-`scripts/*.py` sentence |
| **Nine events, E1/E2/E3, invalidity dominance, capacity/custody/result boundaries, Q/C, T** | unchanged; every fact added here is control-plane, T-development-only, non-citable. Neither `B-CONTRADICTED`, nor a `STRUCTURAL_VIOLATION`, nor a platform refusal is ever scientific or resource evidence |
| **The A3 filesystem boundary** | untouched. Nothing here proves same-UID filesystem exclusion, and no security boundary is invented |

---

## V2110.9. Every superseded signed sentence, named loudly

v2.1.9 §V219.4.2's rows 15–18 are carried. This layer supersedes nine more, each
quoted so a reviewer can check it literally, each with an exact scope.

| # | Locus | Superseded wording | Replaced by | Scope |
|---|---|---|---|---|
| 19 | **signed** harness contract §9 | "**No additional `scripts/*.py` entry point is introduced** — in particular no `scripts/officina_t_process.py` — since adding one would require a reviewed amendment to the immutable-control file `verification.py`, which this contract does not authorize." | §V2110.2.1, §V2110.3.9 CHANGE 1 | **exactly one** additional entry point, `scripts/officina_process_control_bootstrap.py`. The named counter-example `scripts/officina_t_process.py` is **still** forbidden. This layer **is** the reviewed amendment the sentence itself names as the prerequisite |
| 20 | carried §V2.10 | "Sole root: `src/philosophia/officina/generic_harness.py`." | §V2110.2.1 | four roots; `generic_harness.py` remains the sole root **of the public CLI**, and the bootstrap is the sole root of process control |
| 21 | carried §V2.10 | "Future edit surface after token+confirmation: `generic_harness.py`, its tests, signed accounting amendment surface only." | §V2110.10 | the surface gains the new bootstrap file, its tests, `verification.py`'s enumerated amendment, and the production manifest |
| 22 | carried §V2.10 | "Frozen files (byte-unchanged): … **`verification.py`** …" (already narrowed by v2.1.9 §V219.4.2 row 16) | §V2110.3.9 | the amendment is now CHANGES 1–5, not one string. `runtime.py`, `ledger.py`, `checkpoint.py`, `activation.py`, signed events/schemas/constants remain **byte-unchanged** |
| 23 | carried §W2.1 | "**Supervisor:** … the grandchild **calls the serve function in-process** (no `exec`, no new argv)" and §Z3.3's "the supervisor and watchdog have no argv entry surface (they are in-process forks)" | §V2110.2.7 | the **supervisor** grandchild now `execve`s through exactly one new refusal-first private token. The **watchdog** remains an in-process fork with **no** argv surface, unchanged |
| 24 | carried §W2.2 | "The fd is deliberately **not** `O_CLOEXEC` for the grandchild — which is safe precisely because §W2.1 removed the grandchild's `exec`." | §V2110.2.6 | the **property** (not `O_CLOEXEC`) is retained and becomes **load-bearing**; only the justifying clause is replaced |
| 25 | carried §W2.2 / §U2.2 | the `SPAWNING.json` / `SPAWNING_MIDDLE.json` field names `cli_pid` and `cli_start_identity`, read as naming the public CLI process | §V2110.2.6 | the **field names and the schema are unchanged**; they now denote the **bootstrap** process, which is the process that holds `SPAWN.lock` and performs the fork. This is a re-binding of the referent, not a schema change |
| 26 | v2.1.9 §V219.4.1 | `generic_harness.py` is "the exact and only permitted importer of `signal`" | §V2110.3.9 CHANGES 2 and 4 | `generic_harness.py` imports `signal` **not at all**; the bootstrap root is the sole importer |
| 27 | v2.1.9 §V219.2.6, §V219.4.3, §V219.10 | every sentence describing the **existing** signed verifier as already enforcing `R-a`…`R-e`, a runtime executor theorem, or a closed call-target theorem | §V2110.3.9 | **withdrawn as false**, exactly as M219-1 states. Nothing is claimed for the current bytes; CHANGES 1–5 are what a later review must make true |

---

## V2110.10. Exact future implementation edit surface

**This document changes none of it.**

| Path | Permitted change | Status today |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` | **new file**: the isolated process-control bootstrap of §V2110.2–§V2110.4 | **does not exist**; it is specified here, not created |
| `src/philosophia/officina/verification.py` | CHANGES 1–5 of §V2110.3.9, and nothing else | unmodified, digest `327b1bb2…` |
| `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json` | four roots, the new reachable/edge closure, and the added `root_source_sha256` field | does not exist; it is a future control artifact |
| `src/philosophia/officina/generic_harness.py` | remove any `signal` use; add the `L-1`…`L-4` launcher and the `--officina-supervisor-role` refusal-first entry; **remove** the process-control machine | **untracked Cursor work in progress — preserved byte-for-byte by this correction** |
| `tests/test_officina_generic_harness.py` and a new bootstrap test module | the rows of §V2110.7.4 | untracked Cursor work — preserved |
| everything else | **no change**: `runtime.py`, `ledger.py`, `checkpoint.py`, `activation.py`, signed events/schemas/constants, every other `scripts/*.py`, every contract, signature, and prior review | byte-unchanged |

The pre-existing dirty and untracked paths — `essay/OUTLINE.md`,
`src/philosophia/officina/generic_harness.py`,
`tests/test_officina_generic_harness.py`, the modified `accounting.py`,
`test_officina_accounting.py`, and the modified review/prompt files — are **not**
edited, staged, or committed here, and no obligation above is due before the
amendment token exists. The frozen runtime surfaces —
`successor/officina/runtime/` (only `T_RUNTIME.lock`), the absent
`successor/officina/runtime_control/`, and `successor/officina/T_ENVELOPE.json`
— are unchanged.

---

## V2110.11. Governance, weakest points, and negative space

**Weakest points, stated by the author against the author.** Reviewers should
attack these first.

1. **The CPython 3.12.3 build is a pinned identity, not a hashed artifact.**
   `P-b` checks `implementation.name` and `version_info`, which a hostile or
   patched interpreter could satisfy while behaving differently. The bootstrap
   cannot hash its own interpreter without importing `hashlib`, which was
   deliberately excluded. This is the sharpest remaining boundary between
   "verified at run time" and "reviewed once".
2. **The five-module import closure includes `_thread` via
   `signal` → `functools`.** No task is created, and every task-creating symbol
   is syntactically unreachable, but the closure is not free of threading
   machinery and the argument is about calls rather than imports.
3. **The bootstrap cannot attest the reviewed-ness of the role image it
   `execve`s.** The package root arrives as a caller-opened directory
   descriptor. The bootstrap guarantees *process-control custody*, not the code
   provenance of the supervisor, which remains the immutable-control verifier's
   and the deployment's responsibility. A hostile caller can therefore make the
   bootstrap launch a supervisor of the caller's choosing — while still being
   unable to corrupt `pid_mid`'s custody, force a false death proof, or cause a
   wrong-PID signal.
4. **The supervisor process is not isolated.** §W2.5's own `Popen` +
   `waitpid(WUNTRACED)` handshake and the in-process watchdog fork run in a
   contaminated interpreter. No finding raised it and it is outside C219-1's
   scope, but it is the same *class* of defect, and this layer explicitly does
   not claim to have repaired it.
5. **`P-e`'s single wildcard wait is a real exception to `R-a`.** It is
   pre-fork, its only accepted outcome is `ECHILD`, and it refuses on anything
   else — but it does reap an inherited child in the case where it returns, and
   that side effect is stated rather than avoided.
6. **`start_new_session=False`** keeps the bootstrap in the caller's session so
   an operator `SIGINT` reaches it. That also means the caller's process group
   can be signalled as a unit by a third party. Both directions are stated.
7. **The platform pin is narrow to the point of inconvenience**: Linux x86_64
   with one CPython patch version. Any other host refuses before fork. That is
   the intended fail-closed behaviour, but it is a real operational constraint.

**Two-implementer determinacy.** One canonical path, one byte-exact invocation
with four pinned flags and an empty environment, four pinned descriptor numbers,
a five-module import set, an ordered binding block with a positive identity
test, an eight-step preflight with a named refusal token each, a six-field
request grammar and a five-field reply grammar, a six-result wait classifier
total over returned objects and raised objects, five site instantiations carried
verbatim, ten syntactic verifier predicates, five verifier changes, and one
platform table. No clause resolves to "as reviewed", "as appropriate", or
implementer discretion; no design fork is left open; and no property is claimed
for bytes that do not yet exist.

**No author cell is reopened, and none is required.** Every delta in the
inventory is an engineering surface: an executable root, an import allowlist, a
verifier mechanism, four control-plane descriptor indices, one private argv
token, one in-flight wire record, and one platform scope. **No new resource
value, timeout, K1 ceiling, E1/E2/E3 value, T band, scientific estimand, or
policy cell is reached**, which is why no `BLOCKED_..._AUTHOR_CELL` verdict is
emitted. Both v2.1.9 reviewers independently reached the same author-cell
conclusion for the repairs they demanded.

**Compatibility classification.** An engineering/control amendment surface over
the signed harness composite. Protocol amendments: §W6.5's carried supersession
of harness §5a; v2.1.9's narrow supersession of harness §9's `signal` conjunct;
and this layer's rows 19–27. No signed archival set, event, runtime schema,
root-of-trust, resource value, T band, or Q/C boundary moves.

**Negative space.** This correction creates nothing executable and authorizes no
implementation, commit, host change, verifier edit, manifest, process,
supervisor, controller, worker, watchdog, adapter, middle child, endpoint, pipe,
FIFO, journal instance, spawn record, lease, capability, operation, framed
transport, result manifest, quarantine record, promoted object, capacity
artifact, custody disposition, freeze witness, entropy, E1/E2/E3 spend, world,
learner, candidate, Q attempt, Q/C object, datum, outcome, Proof, or claim
movement. It predicts no qualification and no C1–C6 outcome. Process
invalidity, resource exhaustion, missing evidence, a platform refusal, a
`STRUCTURAL_VIOLATION`, the `B-OWNED` residual, and the `B-CONTRADICTED` sink
remain infrastructure facts and are nowhere treated as scientific evidence. No
example in this document was written to any file.

---

## V2110.12. The bounded confirmation questions

At most three per line, focused as required on clean construction / runtime
closure, primitive / wait / `B` totality, and root / verifier / platform
containment. Both lines must recompute the digest of **this file** and of every
governing hash, and must treat this author's closure and both v2.1.9 reviews as
untrusted inputs rather than as support for these bytes.

### For the X line (Claude Opus 4.8, clean context)

> **X-Q1 — clean construction and runtime closure.** Is the clean runtime now
> *constructed* rather than inferred? Attack: that `-I -S -E -P` genuinely
> prevents `site`, `.pth`, `sitecustomize`, `usercustomize`, `PYTHON*` env and
> path injection from executing any code before the module body; that
> `sys.flags` is a readback of effect and not of argv; that the five-module
> import closure of §V2110.3.2 starts no task, registers no at-fork callback,
> and installs no hook (including the disclosed `signal` → `functools` →
> `_thread` edge); that §V2110.3.3's row list is exhaustive over everything that
> executes before `c4`; that §V2110.3.4's binding-plus-identity-validation
> defeats your own monkeypatch counterexample; and above all that
> §V2110.2.3's process-boundary argument is correct — that no `wait` form in the
> contaminated caller can reach `pid_mid`. Confirm or refute that your F1
> scenario and Y Trace 1 are now unreachable **without any premise about the
> caller**.
>
> **X-Q2 — primitive, wait, and `B` totality.** Is `WAIT_ONE` total over the
> union of every returned object and every raised object, and is
> `STRUCTURAL_VIOLATION`'s single continuation safe at all five sites? Attack
> the arity/type/bool/negative/wrong-pid/status-range rows, the
> `SystemExit`/`KeyboardInterrupt`/`MemoryError` rows, and the `_kill`/`_fork`
> classifiers. Then judge whether §V2110.4.5 excludes `B-CONTRADICTED` **without
> circularity** — i.e. whether the exclusion of `CONTRADICTED_ECHILD` now rests
> only on the process boundary and the bootstrap's own two task readbacks, and
> never on a claim about the caller or about repository source. Re-check W-5
> with a middle stopped between `m8` and `m9`.
>
> **X-Q3 — root, verifier, and platform containment.** Are §V2110.9's nine
> supersessions correctly and narrowly scoped, especially row 19 (one additional
> `scripts/*.py` entry point, against the signed harness sentence that forbids
> them and names this amendment as the prerequisite) and row 23 (the
> re-introduced private argv surface, and whether X-M1 is re-closed by §Z3.3's
> refusal-first mechanism)? Is §V2110.3.9's verifier algorithm exact enough that
> two implementers cannot accept different runtime executor sets — in particular
> S-3…S-8 and the `root_source_sha256` manifest invariant? Is the platform pin
> of §V2110.6 honest, and does the MIPS row correctly place the exclusion
> *before* any mask parse?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_X` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_10`. Static review only: no code, test,
> probe, fork/signal/subprocess experiment, or Officina process may run; no
> runtime or scientific artifact may be created; no existing file may be
> modified; create exactly one review file. Do not authorize
> `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, implementation, T
> activation, entropy, spend, or any later gate.

### For the Y line (GPT-5.6 Sol, clean context)

> **Y-Q1 — your C219-1, replayed.** Your counterexample was a startup
> customization that stores and wraps `os.fork` and creates a helper after the
> last readback. Under §V2110.2 and §V2110.3, can that schedule — or any variant
> using audit, import, trace, profile, at-fork, finalizer, monkeypatch, retained
> callable, or native-extension contamination — still cause a wrong-PID signal or
> a stolen reap of `pid_mid`? Judge specifically whether the repair genuinely
> *constructs* the clean runtime instead of inferring it, whether every premise
> of §V2110.3.8 follows from the construction rather than from an observation,
> and whether the boundary claims of §V2110.11 items 1–4 are stated honestly
> enough that no reader could mistake what has been proved.
>
> **Y-Q2 — your M219-2 and the `B` wedge.** Does the `STRUCTURAL_VIOLATION`
> classifier close the "rebound `os.waitpid` returns an unmapped value" gap at
> all five sites, and is its continuation safe rather than merely labelled? Then
> re-run your Trace 6 wedge: with the process boundary in place, can a genuine
> `ECHILD` arise before any truthful capture in a supported execution, and is
> `B-CONTRADICTED` now outside supported history for reasons that do not cite
> any executor-set theorem? If you judge it still reachable, say whether a
> durable resolver is required rather than a sink.
>
> **Y-Q3 — your M219-1 and m219-1.** Is §V2110.3.9 an exact verifier algorithm
> rather than a prose probe — module-scoped allowlist, closed AST grammar,
> alias/rebinding/data-flow rules, prohibited syntax, import graph, manifest
> invariants including `root_source_sha256`, and a fail-closed result for each
> violation — and is the withdrawal of v2.1.9's "the existing verifier already
> proves this" complete (§V2110.9 row 27)? Separately: does §V2110.6 close your
> MIPS finding by pinning `Linux x86_64, CPython 3.12.3` and refusing every other
> architecture **before** any mask is parsed, and is the claim that this narrows
> only an engineering process-control surface — leaving the signed off-CPU
> scientific device policy untouched on the present x86_64 host — correct?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_Y` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_10`. Static review only: no code, test,
> probe, fork/signal/subprocess experiment, or Officina process may run; no
> runtime or scientific artifact may be created; no existing file may be
> modified; create exactly one review file. Do not authorize
> `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, implementation, T
> activation, entropy, spend, or any later gate.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. Both lines revised v2.1.9; no
conditional authorization from any earlier round survives or transfers. The only
next authorization step is a **fresh independent X-line review and a fresh
independent Y-line review of the v2.1.10 bytes**.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
