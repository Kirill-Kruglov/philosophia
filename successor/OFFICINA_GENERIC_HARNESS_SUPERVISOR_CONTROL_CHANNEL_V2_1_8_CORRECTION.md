# Officina supervisor and control-channel amendment — v2.1.8 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

> ## THIS LAYER AMENDS A SIGNED ENGINEERING SURFACE
>
> **`ALLOWED_ABSOLUTE_IMPORTS` gains exactly one member: `signal`.**
>
> Every prior layer of this chain asserted a **zero import-allowlist delta**.
> **That claim is superseded and must not survive into v2.1.8.** It was correct
> for v2 through v2.1.7 and it is **false for v2.1.8**. The delta is one module,
> named here, used at exactly one site, for exactly one purpose: mechanically
> normalizing the CLI's `SIGCHLD` disposition and `SA_NOCLDWAIT` flag to the
> default before the first `os.fork` of every attempt, so that this process's
> own child cannot be auto-reaped and its PID cannot be recycled underneath a
> pending kill. §V218.1 states the delta, its containment, and every prior
> sentence whose "zero delta" or "`signal` is outside the allowlist" wording is
> replaced by it. No other module is added. No relative-import allowlist changes.
> This is an **engineering** amendment; **no scientific author cell is reopened
> and no new author-choice token is proposed.**

**Authorship and provenance, stated literally.** This correction was written
by **Claude Code Opus 5 acting only as the specification author**, because
Claude Code Fable 5 was unavailable. The same author line wrote v2.1 through
v2.1.7. It is **not** an independent X-line or Y-line review of its own bytes
and must never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every author
closure in the chain — including v2.1.7's, and including this layer's own
closure `reviews/opus5_officina_supervisor_control_channel_v2_1_8_closure.md` —
is an untrusted self-assessment; none of their claims is used as evidence here.

**Review state of v2.1.7, recorded exactly.** **Both** independent lines
returned `REVISE_OFFICINA_SUPERVISOR_V2_1_7`. The Y line raised C217-1
(Critical), M217-1 (Major) and m217-1 (Minor); the X line raised X217-M1
(Major) and X217-m1 (Minor). The findings are complementary and **all govern**.
There is no v2.1.7 confirmation of any kind. **v2.1.8 requires a fresh X-line
review and a fresh Y-line review of its own bytes**; no earlier confirmation of
any version carries across, and the allowlist delta above makes a fresh review
strictly mandatory rather than merely procedural.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md`
(v2.1.7), which layers over v2.1.6, v2.1.5, v2.1.4, v2.1.3, v2.1.2, v2.1.1,
v2.1, and v2 — all nine preserved unedited as review evidence. **Everything not
named in the §V218.0 replacement index carries forward verbatim.**

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Frozen closures carried forward unchanged** (§V218.9 audits them one by one):
v2.1.7's object-bound observation record and both revalidation barriers
(§V217.1, confirmed closed by **both** lines); the A3 residual honesty of
§V217.1.5; the complete bound-language replacement of §V217.4 (confirmed closed
by **both** lines); the `CLOSE_OWNED` primitive at every close site including
both lock closes (§V216.2); `MALFORMED` physical-presence dominance and the rule
ordering (§V216.1.2's rule structure); §V216.1.3's sub-routing and cross-product;
the three branch bodies `B-P`/`B-QM`/`B-QN`; §N2.3's P1–P7 custody proof and
§V214.2.4's custody/accounting reconciliation; K1's five constants and one-release
accounting; death-before-unlink for every record naming a process other than the
CLI (§V216.3, §V217.3.1's table); the corrected `boot_w` EOF provenance and the
eight-end audit (§V216.5); the narrowed pipe-only bootstrap invariant (§V216.4.1);
the nonblocking channels and bounded helpers; the GC order with `accepted.json`
last and `D6`; the lock-first preflight and non-mutating stuck-holder route; the
total watchdog partition; and the whole carried §V217/§V216/§V215/§V214/§U/§N/§Z/§W/§V2
chain.

Author token candidate, still **not signable**, and not made signable here:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, test, contract, signature, review,
prompt, or runtime artifact — in particular it does **not** edit
`src/philosophia/officina/verification.py`, whose future one-line amendment it
only specifies. Starts no process, endpoint, pipe, FIFO, journal, watchdog,
worker, adapter, or transport. Creates no entropy, activation, capability,
world, learner, candidate, datum, Q/C object, capacity artifact, custody
disposition, result manifest, or outcome. Authorizes no implementation. T
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

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
2e4bee2305bafb5825a6ac1cca4d131dcbdf730aa048f29c7023cf679c9936e6  reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
5c82f7c1894d3e76239ee26a611731d102a2891486a9c2d667ce9738956d533b  reviews/sol_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

The last line is new to this chain's hash block. It is present because
`verification.py` holds the literal `ALLOWED_ABSOLUTE_IMPORTS` set that
§V218.1's delta will one day amend. The digest records the **unamended** file as
of these bytes; **this correction does not modify it**, and no reviewer should
expect it to differ.

## Engineering constants (replaces v2.1.7's "Engineering constants")

**Zero new constants, durable objects, paths, durable schemas, schema keys,
wire enum tokens, refusal or `INVALID` tokens, public commands, signed events,
resource values, roots, or archival-set changes.** The selector observation
record of §V217.1 remains **in-memory only**. The syscall-result enums of
§V217.2/§V218.3, the `OWNERSHIP` label of §V218.3.1, the `CLOSE_OWNED` outcome
labels, and the terminal labels `T1`/`T2`/`B` are internal control-plane labels:
never persisted, never transmitted, never a durable schema, never a wire token.
§V218.4 installs no new record class — it reuses the already-signed
`SPAWNING_MIDDLE.json`.

**Exactly one import-allowlist delta: `signal` is added** (§V218.1). This layer
otherwise uses only `os.close`, `os.open`, `os.stat`, `os.fstat`, `os.pread`,
`os.read`, `os.listdir`, `os.kill`, `os.waitpid`, `os.fork`, `os.getpid`,
`os.unlink`, `os.fsync`, `time.clock_gettime_ns`, `hashlib`, and `json` — all
inside already-allowlisted modules — plus exactly four members of `signal`
(§V218.1.2). `select`, `selectors`, `ctypes`, `sys`, `socket`, `threading`, and
`multiprocessing` remain **outside** the allowlist and are not added.

---

## V218.0. Exact replacement index (v2.1.7 → v2.1.8)

**Nothing else moves.** Everything in v2.1.7 and in every layer it carries — in
particular **§V217.1 in full** (the object-bound observation record, the nine-step
`OBSERVE`, the predicates, both revalidation barriers, the A3 residual, and the
mutation-cut table), **§V217.4 in full** (the bound-language replacement, the
declared search terms, the ten stale loci, the retained-statement table, and the
revised row 86), §V217.3.1's death-proved-only boundary **table**, §V216.1.2's
rule structure and `MALFORMED` dominance, §V216.1.3's sub-routing and
cross-product, §V216.2 in full, §V216.4.1, §V216.5 in full, and the entire
carried §V215/§V214/§U/§N/§Z/§W/§V2 chain — carries forward verbatim except at
the rows below.

| v2.1.7 (or carried) locus (exact sentence / clause / block / table row) | Action in v2.1.8 |
|---|---|
| v2.1.7 "Engineering constants" sentence "**Zero new constants, … Zero import-allowlist delta.**" and its closing clause "`select`, `selectors`, `signal`, `ctypes`, and `sys` remain outside" | **replaced** by this layer's "Engineering constants" section and §V218.1 (`signal` added; everything else unchanged) |
| v2.1.7 §V217.7 sentence "The import-allowlist delta remains **none**." | **replaced** by §V218.1.1 |
| carried v2.1.6 §V216 constants sentence "…all inside allowlisted modules; `select`, `selectors`, `signal`, `ctypes`, and `sys` remain outside." | **replaced** by §V218.1.1 |
| carried v2.1.5 §V215, v2.1.4 §V214, v2.1.3 §U, v2.1.2 §N, and v2.1.1 §Z zero-delta sentences (the recurring "`select`, `selectors`, `signal`, `ctypes`, and `sys` remain outside it" / "the import allowlist delta remains **none**" wording) | **replaced** by §V218.1.1's single governing statement; §V218.1.4 enumerates each locus |
| carried v1 draft §S5 clause "No `socket`, `select`, `signal`, `sys`, `threading`, `multiprocessing`, or any new module is imported; **no `verification.py` change and no allowlist delta is required**, and none is smuggled: this claim is itself a §S7 probe" | **replaced** by §V218.1.3 (the delta is required, named, contained, and is itself the §S7 probe's new obligation; nothing is smuggled) |
| carried v2.1 §W2.6 parenthetical "(the `signal` module is outside `ALLOWED_ABSOLUTE_IMPORTS`; `SIGSTOP` disposition cannot be changed and `SIGCONT`'s default is what is required)" | **replaced** by §V218.1.2's containment rule; §W2.6's **claim** (the adapter entry installs no signal disposition) is retained unchanged and becomes directly asserted and statically testable |
| carried v2.1 §W6.4 parenthetical "(`signal`/`ctypes` are outside `ALLOWED_ABSOLUTE_IMPORTS`)" | **replaced** by §V218.1.2 (`ctypes` alone; `prctl(2)` remains unreachable, so the escaped-children conclusion is unchanged) |
| carried v1 draft §S0 parenthetical "Integer Linux signal numbers used (no `signal` import)" | **replaced** by §V218.1.2 (the integer literals are retained everywhere; `signal.SIGCHLD` is used at exactly one site) |
| carried v2.1.3 §U2.2 step list `c1`–`c8` | **extended** by §V218.2.1 (step `c3n`, between `c3` and `c4`; installs nothing durable, adds no constant) |
| carried v2.1.3 §U2.5 failure routes and §U6.1 P3's "reap if own child" | **extended** by §V218.2.6 (the sole-reaper contract and the closed table of permitted wait sites; no route's behaviour changes) |
| §V217.2.2's `IDENTITY_SAFE` block in full | **replaced** by §V218.3.4 (a total decision table including the `ppid` mismatch, the reaped state, and the contradiction state) |
| §V217.2.3's `SIGNAL_ATTEMPT` clause "`ESRCH ⇒ GONE` — … Proceed to WAIT_PROVE." | **replaced** by §V218.3.5 (`ESRCH` under an owned, unreaped child contradicts the pinned premise) |
| §V217.2.3's SIGTERM→SIGKILL schedule block | **replaced** by §V218.3.6 (ownership-gated, extended into the §V218.4.2 automaton; the `D/2` / `D` edges and the `≥` rule are preserved verbatim) |
| §V217.2.4's `WAIT_PROVE` block line "`ECHILD ⇒ PROVED_DEAD`" | **replaced** by §V218.3.3 (`ECHILD ⇒ INCONCLUSIVE_ECHILD`) |
| §V217.2.4's "**Why these two outcomes prove death, exactly**" bullets, in particular "This contract installs **no signal disposition** anywhere (`signal` is outside `ALLOWED_ABSOLUTE_IMPORTS`), so `SIGCHLD` keeps its default disposition and children are **never** auto-reaped; the only reaper is this route. `ECHILD` therefore means this route already reaped it, and the child is dead." | **replaced** by §V218.3.3 (proof only on a returned `pid_mid`; the false universal and its non-sequitur premise are **deleted**) |
| §V217.2.4's "**PID reuse.**" paragraph | **replaced** by §V218.3.2 (the fork-ownership PID-reuse proof, resting on the mechanically normalized and verified disposition of §V218.2, not on an assumed default) |
| §V217.2.5's `c5`/`c6`/`c7` cut-mapping table | **replaced** by §V218.3.7 |
| §V217.3.1's "**Two-supervisor safety, proved.**" paragraph (the `m5`/`rel2`/EOF argument) | **replaced** by §V218.5.1 (the actual `c5`–`c7` trace: no `c8` byte, middle at `m0`, `rel1_w` writer copy, fork-shared lock) |
| §V217.3.1's sentence "**The abandoning CLI therefore always removes its own `SPAWNING.json`, on every route, while still holding `SPAWN.lock`.**" | **replaced** by §V218.4.3 (scoped to every **returning** terminal; the non-returning state has not abandoned the attempt and retains the record) |
| §V217.3.2's terminal block `T1`/`T2`/`T3` in full | **replaced** by §V218.4.2 (`T1`, `T2`, and the non-returning `B` state; **`T3` is deleted**, including its "install NOTHING … remove ONLY `SPAWNING.json` … return" body and its contradictory "or `DENIED` signals" membership clause) |
| §V217.3.3's forward-progress table | **replaced** by §V218.4.4 (plus the §U6.1/§U2.5 totality proof for the surviving `SPAWNING_MIDDLE.json`) |
| §V217.3.4's named residual paragraph | **replaced** by §V218.4.5 (three named residuals, including the new unreaped-zombie residual this layer itself creates) |
| §V217.3.5's crash-and-cut table rows for `waitpid ECHILD`, `signal ESRCH`, `signal EPERM`, `/proc unreadable or unparsable`, PID-reuse, and every `T3` row | **replaced** by §V218.6 |
| §V217.5's crash-cut rows `waitpid ECHILD`, `kill ESRCH`, `kill EPERM or other error`, `T3 at c5/c6`, `a deliberately stopped middle child in T3`, and `T2 with a live middle child` | **replaced** by §V218.6 |
| §V217.6 test rows **198**, **199**, **200**, **203**, **205**, **207**, **208** | **replaced** by §V218.7 |
| §V217.6 test rows 185–197, 201, 202, 204, 206, 209–212 and every carried row | **unchanged**; §V218.7 adds rows **213–240** |
| §V217.7's "Two-implementer determinacy" and "Compatibility classification" paragraphs | **replaced** by §V218.9 |

---

## V218.1. The import-allowlist delta, stated loudly (R1)

### V218.1.1 The delta, exactly

The literal set in `src/philosophia/officina/verification.py` today is

```text
ALLOWED_ABSOLUTE_IMPORTS = {
    "__future__", "ast", "dataclasses", "datetime", "enum", "fcntl",
    "hashlib", "hmac", "json", "os", "pathlib", "re", "subprocess", "time",
    "typing", "weakref",
}
```

— sixteen members, digest `327b1bb2…`. The **only** change this amendment will
ever require of that file is the addition of the single string `"signal"`,
producing seventeen members. Nothing else in `verification.py` changes; the
`ALLOWED_RELATIVE_IMPORTS` set, the dynamic-import rules, the random-device
rules, and the production-manifest rules are untouched.

> **Governing statement, replacing every "zero import-allowlist delta" sentence
> in this chain (v1 draft §S5, v2.1 §W11, v2.1.1, v2.1.2, v2.1.3, v2.1.4,
> v2.1.5, v2.1.6, and v2.1.7 in both its Engineering-Constants and §V217.7
> paragraphs):**
>
> The Officina supervisor/control-channel amendment requires **exactly one**
> import-allowlist delta: the module `signal` is added to
> `ALLOWED_ABSOLUTE_IMPORTS`. It is required because the CLI must, before its
> first `os.fork`, replace whatever `SIGCHLD` disposition and `sa_flags` it
> inherited with the default, and no already-allowlisted module can perform
> that replacement. No other module is added; `select`, `selectors`, `ctypes`,
> `sys`, `socket`, `threading`, and `multiprocessing` remain outside. This delta
> is **named, not smuggled**: it is stated here, contained by §V218.1.2, carried
> into the §S7 probe obligation by §V218.1.3, and gated on a fresh independent
> X-line and Y-line review of these exact bytes.

### V218.1.2 Containment: the exact permitted `signal` surface

The delta is a permission to import, not a permission to use freely. The
following restriction is normative and statically testable:

```text
PERMITTED SIGNAL SURFACE
  Importing module      : the CLI bootstrap module only — the module that
                          implements c1–c18 of §U2.2/§U2.4.
  Permitted members     : signal.SIGCHLD, signal.SIG_DFL, signal.signal,
                          signal.getsignal — and no others.
  Permitted call sites  : NORMALIZE_REAPING_STATE and VERIFY_REAPING_STATE of
                          §V218.2.2/§V218.2.3, both executed only at step c3n,
                          and nowhere else.
  Forbidden, explicitly : any Python-level handler callable; signal.SIG_IGN;
                          signal.siginterrupt; signal.pthread_sigmask;
                          signal.pthread_kill; signal.sigwait / sigwaitinfo /
                          sigtimedwait; signal.set_wakeup_fd; signal.alarm;
                          signal.setitimer / getitimer; signal.raise_signal;
                          signal.pidfd_send_signal; signal.strsignal;
                          signal.valid_signals; every other member.
  Forbidden importers   : the supervisor serve module, the watchdog module, the
                          controller adapter entry, the worker entry, the
                          generic harness, the batch-settlement modules, and
                          every other module in the tree.
```

Three carried consequences, each preserved rather than weakened:

- **§W2.6 is unchanged in substance.** The reviewed controller adapter entry
  still **installs no signal disposition** before its `os.kill(os.getpid(),
  SIGSTOP)`. What changes is only the *justification*: that property was
  previously argued from "the `signal` module is outside
  `ALLOWED_ABSOLUTE_IMPORTS`", which is no longer available as an argument. It
  is now a **directly asserted restriction** with a static test (row 216) —
  which is a stronger form of the same guarantee, because the old argument
  never covered `os`-level or inherited state at all.
- **§W6.4 is unchanged in substance.** "No cgroup, PID namespace, or
  `PR_SET_CHILD_SUBREAPER` is available" still holds: `prctl(2)` is reachable
  only through `ctypes`, which remains outside the allowlist. Only the
  parenthetical's mention of `signal` is removed. The escaped-children A3
  procedural residual and the fail-closed quiescence scan are untouched.
- **The integer signal literals stay.** `SIGKILL = 9`, `SIGTERM = 15`,
  `SIGCONT = 18`, `SIGSTOP = 19` and the liveness probe `0` remain integer
  literals at every existing site, exactly as v1 draft §S0 pins them; this
  layer changes no `os.kill` / `os.killpg` argument anywhere. The **only**
  symbolic use is `signal.SIGCHLD` at `c3n`, and it is symbolic deliberately:
  `SIGCHLD`'s number is not uniform across Linux architectures, so a literal
  would introduce a platform assumption that the symbol does not. (The
  architecture-specificity of the *carried* `18`/`19` literals is a pre-existing
  pin of the reviewed Linux host and is **not reopened here**.)

### V218.1.3 The §S7 probe obligation, restated

v1 draft §S5 claimed no `verification.py` change was required and offered that
claim as a §S7 probe (a quarantine verifier over the implementation). That claim
is **false for v2.1.8** and is replaced:

> A `verification.py` change **is** required: the addition of `"signal"` to
> `ALLOWED_ABSOLUTE_IMPORTS`, and nothing else. The §S7 probe obligation is
> correspondingly replaced: the quarantine verifier must assert that the set
> equals the sixteen previously pinned members **plus exactly `"signal"`**, that
> `ALLOWED_RELATIVE_IMPORTS` is unchanged, that `signal` is imported by the CLI
> bootstrap module and by no other module in the tree, and that only the four
> members of §V218.1.2 are referenced. A verifier that merely tolerates the new
> member without pinning its containment does not discharge this obligation.

### V218.1.4 Every superseded zero-delta locus

| # | Locus | Superseded wording | Governed by |
|---|---|---|---|
| 1 | v1 draft §S5 "Import/allowlist proof (no delta)" | "no `verification.py` change and no allowlist delta is required, and none is smuggled" | §V218.1.1, §V218.1.3 |
| 2 | v1 draft §S0 | "Integer Linux signal numbers used (no `signal` import)" | §V218.1.2 (literals retained; one symbolic site) |
| 3 | v2.1 §W2.1 | "`os.fork` is inside the already-allowlisted `os`; the allowlist delta remains **none**." | §V218.1.1 (the `os.fork` half is still true) |
| 4 | v2.1 §W2.6 parenthetical | "the `signal` module is outside `ALLOWED_ABSOLUTE_IMPORTS`" | §V218.1.2 |
| 5 | v2.1 §W6.4 parenthetical | "(`signal`/`ctypes` are outside `ALLOWED_ABSOLUTE_IMPORTS`)" | §V218.1.2 (`ctypes` alone) |
| 6 | v2.1.1 §Z compatibility paragraph | "the import allowlist delta remains **none** … `signal`, `ctypes`, and `sys` remain outside it" | §V218.1.1 |
| 7 | v2.1.2 §N constants paragraph | "…`signal`, `ctypes`, and `sys` remain outside" | §V218.1.1 |
| 8 | v2.1.3 §U constants paragraph | "…`signal`, `ctypes`, and `sys` remain outside" | §V218.1.1 |
| 9 | v2.1.4 §V214 constants paragraph | "…`signal`, `ctypes`, and `sys` remain outside it." | §V218.1.1 |
| 10 | v2.1.5 §V215 constants paragraph | "…`signal`, `ctypes`, and `sys` remain outside" | §V218.1.1 |
| 11 | v2.1.6 §V216 constants paragraph | "…`signal`, `ctypes`, and `sys` remain outside." | §V218.1.1 |
| 12 | v2.1.7 Engineering constants | "**Zero import-allowlist delta.**" and "…`signal`, `ctypes`, and `sys` remain outside" | §V218.1.1 |
| 13 | v2.1.7 §V217.7 | "The import-allowlist delta remains **none**." | §V218.1.1 |
| 14 | v2.1.7 §V217.2.4 / test row 199 | "`signal` is outside `ALLOWED_ABSOLUTE_IMPORTS`, so `SIGCHLD` keeps its default disposition" | §V218.3.3, §V218.7 (row 199 replaced) |

**Not superseded, and deliberately so:** the **signed** generic-harness contract
(§9 of `OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md`) states that *the
harness* "uses no `signal`/`threading`/`multiprocessing`/backend import" and
that any change "requires a reviewed amendment to that allowlist". Both remain
true and are **honoured, not contradicted**: the harness still imports no
`signal` (§V218.1.2 forbids it), and this layer *is* the reviewed amendment that
sentence anticipates, submitted for exactly the review it demands. **There is no
contract conflict with the signed harness composite or with the signed
batch-settlement amendment**, and none is asserted.

---

## V218.2. Mechanical pre-fork normalization of child-reaping state (R1)

Closes Sol **C217-1** and Opus **X217-M1** at their root. The defect was not a
wrong sentence about `ECHILD`; it was that the whole stage-M kill/death
machinery rested on an **inherited** process property that the contract neither
set, nor read, nor could read. This section sets it and reads back what is
readable, before any fork, on every attempt.

### V218.2.1 Placement: step `c3n`, before every first fork

§U2.2's step list is **extended** by exactly one step, inserted between `c3` and
`c4`:

```text
c3n. NORMALIZE_REAPING_STATE()  then  VERIFY_REAPING_STATE()          (§V218.2.2,
                                                                      §V218.2.3)
       NORMALIZED   ⇒ proceed to c4
       otherwise    ⇒ PRE_FORK_FAIL_CLOSED                            (§V218.2.5)
```

Pinned properties of the placement, each load-bearing:

- **Before the first `os.fork` of the attempt.** `c4` is the only fork the CLI
  performs; `c3n` immediately precedes it, so the disposition that governs
  `pid_mid`'s termination is the normalized one from the child's first instant.
- **Under the signed lock and state.** `c1` has acquired `SPAWN.lock`, `c2` has
  installed `SPAWNING.json`, and `c3` has created the four channels. The CLI
  therefore owns its signed lock and its own attempt record while it
  normalizes, so no other contract actor can be in its bootstrap concurrently.
- **In the CLI main thread of the main interpreter.** See §V218.2.4.
- **On every attempt, never inherited from process startup.** A single CLI
  process may make more than one attempt (§U6.2's "retry the install exactly
  once", §U2.5's `s2`–`s4` "retry the bounded acquisition exactly once"). Each
  attempt executes its own `c3n`. **No attempt may skip `c3n` because an earlier
  attempt in the same process performed it**, and no cached "already normalized"
  flag may be consulted: the state is re-established and re-verified every time.
- **Nothing durable is created, changed, or removed by `c3n`**, and it consumes
  no constant, no deadline, and no resource. It is not a record, not a schema,
  not an event, and not an author choice.

**No fork may occur if normalization or verification is anything other than
`NORMALIZED`.** This is the fail-closed premise on which every later ownership
claim rests; §V218.3.1 states it as a precondition of `OWNERSHIP := OWNED`.

### V218.2.2 `NORMALIZE_REAPING_STATE` — the exact operation

```text
NORMALIZE_REAPING_STATE() → NORMALIZE_OK | NORMALIZE_INCONCLUSIVE

  the single operation is exactly:

      previous := signal.signal(signal.SIGCHLD, signal.SIG_DFL)

  return handling:
      returns normally ⇒ NORMALIZE_OK.
        `previous` is CPython's record of the Python-level handler it believed
        was installed. It is DIAGNOSTIC ONLY: it may be logged in memory for a
        refusal detail, and it is NEVER used as a safety premise, never routes,
        and never contributes to any death, identity, or ownership conclusion
        (§V218.2.4 states why it cannot be trusted as a kernel read).
      raises ValueError  ⇒ NORMALIZE_INCONCLUSIVE
        (raised by CPython when the caller is not the main thread of the main
         interpreter, or the signal number is rejected)
      raises RuntimeError ⇒ NORMALIZE_INCONCLUSIVE
        (raised under a sub-interpreter)
      raises OSError      ⇒ NORMALIZE_INCONCLUSIVE
        (the underlying sigaction failed)
      raises anything else ⇒ NORMALIZE_INCONCLUSIVE
  No exception may escape this function. An escaping exception is a contract
  violation, not a route.
```

**What that one call performs on the pinned Linux/CPython stack.**
`signal.signal(sig, SIG_DFL)` calls CPython's `PyOS_setsig(sig, SIG_DFL)`,
which on any platform with `sigaction(2)` — Linux always — performs **one
`sigaction(SIGCHLD, &act, &oldact)`** with a fully initialized `act`:

```text
act.sa_handler = SIG_DFL
sigemptyset(&act.sa_mask)
act.sa_flags   = a value that contains NEITHER SA_NOCLDWAIT NOR SA_NOCLDSTOP
                 (CPython >= 3.11 sets SA_ONSTACK; earlier CPython sets 0;
                  the project pins requires-python >= 3.11, and neither value
                  includes either NOCLD flag)
```

Because `sigaction` **replaces the entire disposition record** for the signal —
handler, mask, and flags together — this single call clears, in one atomic
kernel operation and regardless of provenance:

1. an inherited `SIGCHLD == SIG_IGN` disposition (replaced by `SIG_DFL`); and
2. an inherited `SA_NOCLDWAIT` flag (the new `sa_flags` does not contain it).

Both are the Linux mechanisms that cause a terminating child to be **auto-reaped
without becoming a zombie** (`do_notify_parent()` auto-reaps when the parent's
`SIGCHLD` handler is `SIG_IGN` **or** its action carries `SA_NOCLDWAIT`). After
this call, and for every child forked after it, the parent's action is `SIG_DFL`
with neither flag, so a terminating child **becomes and remains `EXIT_ZOMBIE`
until this process reaps it**.

**Why both provenances must be handled, and why `execve` is not enough.** At
`execve` Linux's `flush_signal_handlers()` resets every caught handler to
`SIG_DFL`, **preserves** `SIG_IGN` dispositions, and clears `sa_flags` to `0`
for every signal. So an exec'd CLI can inherit `SIG_IGN` but not
`SA_NOCLDWAIT`. A CLI entered **without** an intervening `execve` — a launcher,
test harness, or supervisor process that `os.fork`s and calls the CLI entry
in-process — inherits **both**, because `fork` copies the disposition table
wholesale. This contract must not assume it was exec'd, so it clears both. This
is exactly the case Sol C217-1 named and the case a "cleared by exec" argument
would have missed.

**No handler is installed.** `SIG_DFL` is the *absence* of a handler: CPython
sets the kernel disposition directly and does not register its own C
trampoline for `SIGCHLD`, so no Python-level callback exists, no `EINTR` storm
is introduced, no wakeup fd is touched, and the carried invariant "this contract
installs no signal **handler** anywhere" is preserved exactly. What v2.1.7 wrote
as "installs no signal **disposition**" is what changes: this contract now
installs precisely one, the default.

### V218.2.3 `VERIFY_REAPING_STATE` — the readback, and its exact limits

```text
VERIFY_REAPING_STATE() → NORMALIZED | VERIFY_FAILED | VERIFY_INCONCLUSIVE

 V1. n := int(signal.SIGCHLD)                       # symbolic, not a literal
 V2. read /proc/self/status in full with os.open/os.read/os.close
       any OSError                       ⇒ VERIFY_INCONCLUSIVE
 V3. locate the lines beginning exactly "SigIgn:" and "SigCgt:"
       either line missing, duplicated, or its value not a non-empty string of
       hexadecimal digits                ⇒ VERIFY_INCONCLUSIVE
 V4. ign := int(SigIgn_value, 16) ; cgt := int(SigCgt_value, 16)
       (these are 1-based signal bitmasks: signal k occupies bit k-1)
 V5. require ((ign >> (n - 1)) & 1) == 0        # SIGCHLD is not ignored
       and   ((cgt >> (n - 1)) & 1) == 0        # SIGCHLD is not caught
       either bit set                    ⇒ VERIFY_FAILED
 V6. require signal.getsignal(signal.SIGCHLD) is signal.SIG_DFL
       otherwise                         ⇒ VERIFY_INCONCLUSIVE
 V7. ⇒ NORMALIZED
 No exception may escape. An escaping exception is a contract violation.
```

**Stated exactly, so no reviewer must infer it — what this verifies and what it
does not.**

| Property | Established by | Independent kernel readback? |
|---|---|---|
| `SIGCHLD` is not `SIG_IGN` | `V5`'s `SigIgn` bit test | **Yes** — `/proc/self/status` is written by the kernel from the live `sighand` table |
| `SIGCHLD` has no catching handler | `V5`'s `SigCgt` bit test | **Yes** |
| `SA_NOCLDWAIT` is clear | the `sigaction` **write** of §V218.2.2, which sets `sa_flags` without it | **No.** Linux exposes no `SA_NOCLDWAIT` bit in `/proc/<pid>/status` or anywhere else readable from `os`; it is not observable without `ctypes`, which stays outside the allowlist |
| CPython's own view agrees | `V6`'s `getsignal` | **No** — `getsignal` reads CPython's cached table, not the kernel |

The `SA_NOCLDWAIT` row is the one premise that rests on the **semantics of the
write** rather than on a readback. That is materially different from v2.1.7's
defect: v2.1.7 rested on an *unperformed* and *unobservable* assumption about
inherited state; v2.1.8 rests on a *performed*, fully specified `sigaction` whose
`sa_flags` argument is pinned in this document. **Independent reviewers must
verify, as a platform fact, that `PyOS_setsig` on the pinned CPython (≥ 3.11)
issues a `sigaction` whose `sa_flags` contains neither `SA_NOCLDWAIT` nor
`SA_NOCLDSTOP`, and that Linux's auto-reap condition is exactly
`SIG_IGN ∨ SA_NOCLDWAIT`.** This contract asserts those two facts and marks them
as reviewer-verifiable rather than author-asserted.

**A rejected stronger verification, recorded.** A direct empirical check —
fork a throwaway child, let it exit, and assert `waitpid` returns its pid rather
than `ECHILD` — would observe the property end-to-end. It is **rejected**: it
requires an additional fork before the attempt's own fork, creates a process the
contract does not otherwise account for, and would need a new timing decision.
No such probe is specified, and none may be added without a fresh author
decision.

**Residual risk if the unverifiable premise is nonetheless violated.** If
`SA_NOCLDWAIT` somehow survived, the child could be auto-reaped. That case is
**not** left to inference: §V218.3 catches it three ways — `waitpid` returns
`ECHILD` (⇒ `INCONCLUSIVE_ECHILD`, never `PROVED_DEAD`), `os.kill` returns
`ESRCH` for an unreaped owned child (⇒ contradiction), and a `/proc` read
showing `ppid ≠ os.getpid()` (⇒ contradiction). Each irreversibly forbids every
further signal to `pid_mid`. This is the defence in depth Sol C217-1 required:
the safety property no longer depends on the subtle premise alone.

### V218.2.4 The main-thread premise, stated as a premise

CPython's `signal.signal()` raises `ValueError` unless it is called from the
**main thread of the main interpreter**. The contract therefore pins:

> `c3n` executes in the CLI process's **main thread of the main interpreter**.
> The CLI creates no thread (`threading` is outside the allowlist and is not
> added) and runs no sub-interpreter. If a host embeds the CLI entry point off
> the main thread, `signal.signal` raises `ValueError`, `c3n` returns
> `NORMALIZE_INCONCLUSIVE`, and **no fork occurs** — the CLI refuses rather than
> forking a child it could not have normalized for. This is a premise the
> contract **enforces mechanically by its own failure**, not one it assumes.

The value returned by `signal.signal` is likewise treated as a premise-free
diagnostic: CPython initializes its handler table by reading the kernel
dispositions at `signal`-module import, and returns from that table, so the
value reflects the state **at module import**, which a C-level actor could have
changed since. The *write* is unconditional and authoritative regardless; only
the *reported previous value* is untrustworthy, and nothing depends on it.

### V218.2.5 `PRE_FORK_FAIL_CLOSED` — the exact refusal route

Reached from `c3n` on `NORMALIZE_INCONCLUSIVE`, `VERIFY_FAILED`, or
`VERIFY_INCONCLUSIVE`. At this instant **no fork has occurred**, so no child of
this attempt exists and no record naming another process exists.

```text
PRE_FORK_FAIL_CLOSED(reason ∈ {NORMALIZE_INCONCLUSIVE, VERIFY_FAILED,
                               VERIFY_INCONCLUSIVE}):
  F1. execute NO os.fork. The attempt has no child and can never acquire one.
  F2. BOOTSTRAP_FD_CLEANUP(CLI) over the eight bootstrap ends created at c3,
      through CLOSE_OWNED (§V216.2.2), every outcome CONTINUE.
  F3. remove ONLY SPAWNING.json — this attempt's sole durable record, and one
      that names ONLY this CLI (§V217.3.1's table, carried unchanged) — with its
      fsync(T_SUPERVISOR/), ENOENT tolerated, WHILE STILL HOLDING SPAWN.lock.
      No other singleton record of this attempt exists; any record present from
      another attempt is NEVER touched here.
  F4. CLOSE_OWNED(CLI, spawn_lock_fd, "lock-release")
  F5. return REFUSED / BOOTSTRAP, retryable = FALSE, with the explicitly named
      terminal "bootstrap refused; child-reaping state not normalizable", and
      the reason label from above as its detail.
```

`retryable = false` is deliberate: an unnormalizable reaping state is a property
of the launching environment or the interpreter embedding, not a transient
condition, and a retryable refusal would spin. This introduces **no new refusal
or `INVALID` token**: `REFUSED`/`BOOTSTRAP` and its `retryable` field are the
already-signed shape, and the terminal name is a detail string, exactly as
v2.1.7's non-retryable terminal was.

**Two-supervisor safety at this route is trivial:** no fork happened, so no
middle child, no group, and no grandchild ever existed, and the fork-shared
lock reference set is `{CLI}` alone, released at `F4`.

### V218.2.6 The sole-reaper contract and every permitted wait site

The pinned premise of §V218.3.2 is not only "the disposition is `SIG_DFL`" but
also "**this route is the only reaper of `pid_mid`**". That is now a normative
contract with an enumerated surface rather than an assumption:

> **SOLE-REAPER CONTRACT for `pid_mid`.** Within the CLI process, from `c4`'s
> fork return until `pid_mid` is authoritatively reaped, **no signal handler,
> no `subprocess` object, no helper thread, no `atexit` hook, no library
> finalizer, no other `wait`-family call, and no external component may reap or
> attempt to reap `pid_mid`.** Concretely:
>
> - **No `wait`-family call in the CLI may be a wildcard.** `os.wait()`,
>   `os.wait3()`, `os.waitid(P_ALL, …)`, `os.waitpid(-1, …)`, `os.waitpid(0, …)`
>   and any negative-pgid form are **forbidden in the CLI**, because a wildcard
>   wait could reap `pid_mid` from a site that does not own the death
>   conclusion. Every CLI wait targets one explicit positive pid.
> - **The CLI creates no `subprocess` object.** `subprocess` remains
>   allowlisted and is used by the **supervisor** for controllers and workers
>   (§W2.5), which is a different process; the CLI's own bootstrap is `os.fork`
>   only (§W2.1, §U2.2). A `Popen` object in the CLI would install a process
>   reaper CPython manages on its own schedule, and is forbidden.
> - **The CLI creates no thread and installs no handler**, per §V218.2.4 and
>   §V218.1.2.
> - **Client takeover phase 1 (§W2.9) reaps nothing.** It runs under
>   `SPAWN.lock` **before any fork**, so the CLI has no children at all at that
>   point; its §W2.4 discovery predicate kills stale processes from *earlier*
>   generations, which are not this CLI's children, and its "`os.waitpid` only
>   for own-generation children" clause therefore selects the empty set. This is
>   stated so that the enumeration below is demonstrably complete rather than
>   merely asserted.

**The closed table of permitted wait sites for `pid_mid` in the CLI.** Every one
is a targeted `os.waitpid(pid_mid, …)`; there are no others, and an
implementation containing another is in violation, not on a route.

| # | Site | Carried from | Form | When it may execute |
|---|---|---|---|---|
| W-1 | `WAIT_PROVE` inside the stage-M route and the §V218.4.2 automaton | §V217.2.4, replaced by §V218.3.3 | `os.waitpid(pid_mid, WNOHANG)` | after `c4`, on a `c5`/`c6`/`c7` abandonment |
| W-2 | §U2.5 **stage-1 route** death proof (`c9`/`c10` failure) | §U2.5, unchanged | `os.waitpid(pid_mid, WNOHANG)` | after `c8`, before a verified group |
| W-3 | §U2.5 **stage-2 route** own-generation reap (`c13`/`c14`/`c17` failure) | §U2.5, unchanged | `os.waitpid(pid_mid, WNOHANG)` | after `c11` |
| W-4 | §U6.1 **P3**'s "reap if own child", when a later attempt **in this same CLI process** resolves a record naming a child this process forked | §U6.1, unchanged | `os.waitpid(pid_mid, WNOHANG)` | at a later attempt's preflight |
| W-5 | the **success-path** reap of the middle child, which §W2.1 states as "the middle child `os._exit(0)`s and is reaped by the CLI" | §W2.1, unchanged | `os.waitpid(pid_mid, WNOHANG)` | after `c13`'s bootstrap line proves `m8` completed |

W-1 through W-5 are **mutually exclusive per attempt**: exactly one of the
stage-M route, the stage-1 route, the stage-2 route, and the success path
executes for a given `pid_mid`, and W-4 can only observe a `pid_mid` that an
earlier attempt in this process left unreaped (which only §V218.4.5's named
zombie residual produces). No site may execute after `OWNERSHIP == REAPED`.

**The middle child and the grandchild need no premise of their own.** The middle
child's `m0`–`m9` list contains **no `wait`-family call at all**: it forks the
grandchild at `m7` and `_exit(0)`s at `m9` without waiting, and the grandchild is
reparented to `init`. The normalized `SIG_DFL` disposition is inherited across
`c4`'s fork by the middle and across `m7`'s fork by the grandchild (fork copies
the disposition table), which is a **fact**, not a new obligation: **this layer
states no new claim about, and imposes no new obligation on, the supervisor's own
§W2.5 handshake, its watchdog reap, or any other post-`m9` reaping.** Those
surfaces are carried unchanged.

---

## V218.3. Fork ownership, PID pinning, and the total identity/signal/wait tables (R2)

Closes Sol **C217-1**'s signal half and Opus **X217-m1**. §V217.2.1's
`STAT_OBSERVE` five-result enum is carried **verbatim** — `ABSENT`,
`PRESENT_VALID`, `UNREADABLE`, `UNPARSABLE`, `ERROR`, with `EINTR` bounded-retry
and the `/proc` parse rules unchanged. What is replaced is what those results
are allowed to authorize.

### V218.3.1 `OWNERSHIP` — the primary identity authority

```text
OWNERSHIP(pid_mid) ∈ { OWNED, CONTRADICTED, REAPED }

  OWNED
    set at exactly one place: c4's os.fork() returning a value > 0 in the
    parent, in an attempt whose c3n returned NORMALIZED.
    MEANING: pid_mid denotes this CLI's own child — running, stopped, or
    zombie — or nothing at all; it can denote NO OTHER PROCESS.
    AUTHORIZES: os.kill(pid_mid, …) and os.waitpid(pid_mid, …), with no
    /proc corroboration required.

  CONTRADICTED
    set IRREVERSIBLY on the FIRST of:
      (a) WAIT_PROVE returns INCONCLUSIVE_ECHILD                (§V218.3.3)
      (b) SIGNAL_ATTEMPT returns GONE (ESRCH)                    (§V218.3.5)
      (c) STAT_OBSERVE returns PRESENT_VALID, no start identity has been
          captured, and s.ppid != os.getpid()                    (§V218.3.4)
      (d) STAT_OBSERVE returns PRESENT_VALID and a previously captured start
          identity MISMATCHES                                    (§V218.3.4)
    MEANING: the pinned premise is contradicted by the kernel. The route no
    longer knows that pid_mid denotes its child.
    AUTHORIZES: os.waitpid(pid_mid, WNOHANG) only. NO SIGNAL, EVER AGAIN, of
    any number, to pid_mid. No start identity may be captured after this point.

  REAPED
    set at exactly one place: os.waitpid(pid_mid, …) returning pid_mid.
    AUTHORIZES: nothing. The route NEVER signals, stats, or waits on pid_mid
    again; the pid may now be reused by the kernel.

The transitions OWNED → CONTRADICTED, OWNED → REAPED are the only ones. There
is no transition out of CONTRADICTED except to REAPED, and none out of REAPED.
```

> **`os.kill(pid_mid, …)` is executed if and only if `OWNERSHIP == OWNED`.**
> This single rule discharges the required prohibition — *no branch may signal a
> PID after authoritative reap or under an inconclusive ownership premise* —
> without needing any per-branch reasoning, and it is statically checkable
> (row 222).

### V218.3.2 The fork-ownership PID-reuse proof

> **Claim.** Let the CLI's `c3n` have returned `NORMALIZED` and let `c4`'s
> `os.fork()` return `pid_mid > 0` in the parent. Then, until this process
> obtains `os.waitpid(pid_mid, …) == pid_mid`, the kernel cannot assign
> `pid_mid` to any other process.
>
> **Proof.** Linux allocates a pid only when no task currently holds it in its
> pid namespace. The child created by `c4` holds `pid_mid` from the moment
> `fork` returns. When it terminates, the kernel calls `do_notify_parent()`,
> which auto-reaps the task **only** if the parent's `SIGCHLD` action is
> `SIG_IGN` or carries `SA_NOCLDWAIT`. By §V218.2.2, executed **before** the
> fork, the parent's action is `SIG_DFL` with neither flag, and §V218.2.3
> verified the `SIG_IGN`/handler half against the kernel's own
> `/proc/self/status`. The task therefore enters `EXIT_ZOMBIE` and **continues
> to hold `pid_mid`**. A zombie is released only by a `wait`-family call from
> its parent (or by the parent's own exit, at which point this CLI is gone and
> makes no further claim). By §V218.2.6 the only such call in this process is a
> targeted `os.waitpid(pid_mid, …)` from the five enumerated sites, and it is
> the return of `pid_mid` from one of them that ends the guarantee — at which
> instant `OWNERSHIP := REAPED` forbids every further use of the pid. ∎
>
> **Corollary — the capture-to-signal race is closed by ownership, not by
> `/proc`.** In v2.1.7 the interval between an identity-safe `STAT_OBSERVE` and
> the following `os.kill` was protected only by an asserted zombie reservation
> that had no mechanical basis. It is now protected by a property established
> **before the child existed**. Consequently `/proc` identity is **not required
> to signal the still-owned child**: it is required only to construct a
> *durable handoff* record (`SPAWNING_MIDDLE.json`, whose
> `middle_child_start_identity` must be a truthfully observed value) and to
> support the `T2` continuation. An unreadable, unparsable, or erroring `/proc`
> therefore no longer blocks termination of an owned child — which is precisely
> what R3's elimination of the returning live-child terminal depends on.
>
> **What the proof does not claim.** It does not claim the premise cannot be
> violated; §V218.2.3 names the one unverifiable component. It claims that if
> the premise is violated, §V218.3.1's `CONTRADICTED` transitions (a)–(d) fire
> before or instead of any harmful action, and that the route then signals
> nothing. It makes **no** claim about filesystem exclusion, about same-UID
> actors, or about any security boundary; the A3 procedural residual is
> untouched (§V218.8).

### V218.3.3 `WAIT_PROVE` — proof only on a returned `pid_mid`

```text
WAIT_PROVE(pid_mid) → PROVED_DEAD | NOT_YET | INCONCLUSIVE_ECHILD
                    | INCONCLUSIVE_OTHER
  precondition: OWNERSHIP != REAPED (an evaluation after REAPED is a contract
                violation, not a route)
  os.waitpid(pid_mid, WNOHANG)
    returns (pid_mid, status) ⇒ PROVED_DEAD ; OWNERSHIP := REAPED
    returns (0, 0)            ⇒ NOT_YET — the child exists and has not
                                terminated (running or stopped)
    ECHILD                    ⇒ INCONCLUSIVE_ECHILD ; OWNERSHIP := CONTRADICTED
    EINTR                     ⇒ bounded retry at T_SUPERVISOR_POLL_INTERVAL_NS
                                until the step's existing signed deadline; on
                                expiry ⇒ INCONCLUSIVE_OTHER
    any other OSError         ⇒ INCONCLUSIVE_OTHER
  returns (pid_mid, status) where WIFSTOPPED(status) is IMPOSSIBLE here: WNOHANG
    without WUNTRACED never reports a stop. A stopped child yields (0, 0), and
    §V218.3.6 SIGKILLs it.
```

**`PROVED_DEAD` has exactly one source: `waitpid` returning `pid_mid`.** That is
the strongest possible proof — the child terminated and the kernel reaped it in
this call — and it is the **only** proof that authorizes `T1`.

**`ECHILD` is INCONCLUSIVE, never `PROVED_DEAD`.** v2.1.7's contrary rule and
its justifying paragraph are **deleted**. The reasoning, stated as the contract's
own:

- Under the normalized premise, an own child that terminated is a zombie and
  `waitpid` returns its pid. So `ECHILD` means **either** the premise was
  violated (an inherited `SA_NOCLDWAIT` the readback cannot see, or an
  auto-reap this contract failed to prevent) **or** the sole-reaper contract of
  §V218.2.6 was violated (a handler, a `subprocess` object, a thread, or an
  external component reaped it) **or** this route already reaped it, which
  `OWNERSHIP == REAPED` forbids reaching.
- In **every** one of those cases the safety property that made a pending signal
  safe — the PID reservation — is exactly what is absent. Concluding
  `PROVED_DEAD` would let the route remove records and free the singleton on the
  strength of the very premise the `ECHILD` disproves.
- Mapping it to `INCONCLUSIVE_ECHILD` + `CONTRADICTED` is therefore not
  conservatism for its own sake: it converts the one observation that falsifies
  the premise into an irreversible prohibition on the one action (signalling)
  that the premise was protecting.

**Every prose and test row asserting `ECHILD ⇒ PROVED_DEAD`, or pinning a zombie
without the mechanically established scope, is deleted**: §V217.2.4's bullet,
§V217.3.5's `waitpid ECHILD` row, §V217.5's `waitpid ECHILD` row, §V217.2.4's
`PID reuse` paragraph, and test rows 198/199/200 (§V218.7). The zombie pin
survives **only** in §V218.3.2, where it is scoped to a child forked after a
verified `c3n` and bounded by this route's own reap.

### V218.3.4 `IDENTITY_SAFE` — the total decision table

`IDENTITY_SAFE` no longer gates *signalling* (ownership does, §V218.3.1). It
decides two separate things: whether a **start identity may be captured** (which
is what makes `T2`'s durable record truthfully constructible), and whether the
observation **contradicts** ownership. The table is total over the Cartesian
product of `STAT_OBSERVE`'s five results, the presence or absence of a captured
identity, the `ppid` comparison, and the `OWNERSHIP` state.

```text
IDENTITY_OBSERVE(pid_mid) :
  if OWNERSHIP == REAPED ⇒ the call is a CONTRACT VIOLATION, not a route; the
     pinned continuation for an implementation that reaches it anyway is: send
     no signal, capture nothing, take T1 (the reap already happened).
  if OWNERSHIP == CONTRADICTED ⇒ capture NOTHING regardless of the result; the
     observation is recorded for the refusal detail only and can never restore
     OWNED nor produce a capturable identity.
  otherwise (OWNERSHIP == OWNED):
     s := STAT_OBSERVE(pid_mid)
```

| # | `STAT_OBSERVE` result | Captured identity | `ppid` vs `os.getpid()` | Verdict | Capture? | Ownership after | Continuation |
|---|---|---|---|---|---|---|---|
| I-1 | `PRESENT_VALID` | present | *not consulted* | **MATCHES** ⇒ identity confirmed | no (already held) | `OWNED` | signal per §V218.3.6; `T2` remains available |
| I-2 | `PRESENT_VALID` | present | *not consulted* | **MISMATCHES** ⇒ contradiction (d) | no | **`CONTRADICTED`** | no further signal; the **earlier** capture stays valid, so `T2` remains available (§V218.4.2) |
| I-3 | `PRESENT_VALID` | absent | `==` | identity confirmed by parentage | **yes** — capture `s.start_identity` | `OWNED` | signal per §V218.3.6; `T2` becomes available |
| I-4 | `PRESENT_VALID` | absent | `≠` | **contradiction (c)** — an owned, unreaped child necessarily has `ppid == getpid()`; this is the last line of defence against a failed normalization | **no** — capturing here would fabricate another process's identity into a durable record | **`CONTRADICTED`** | no further signal, ever; no capture; `T2` unavailable ⇒ `B` |
| I-5 | `ABSENT` | either | — | not identity-bearing; **absence alone is never death** (carried verbatim from §V217.2.2) | no | unchanged | `WAIT_PROVE` decides; a subsequent `ECHILD` sets `CONTRADICTED` |
| I-6 | `UNREADABLE` | either | — | not identity-bearing | no | unchanged | **ownership still authorizes the signal** (§V218.3.2's corollary) and the reaper loop continues; only `T2` is affected |
| I-7 | `UNPARSABLE` | either | — | identical to I-6 | no | unchanged | identical to I-6 |
| I-8 | `ERROR` | either | — | identical to I-6 | no | unchanged | identical to I-6 |
| I-9 | any | either | — | `OWNERSHIP == REAPED` on entry | no | `REAPED` | contract violation; no signal; `T1` |
| I-10 | any | either | — | `OWNERSHIP == CONTRADICTED` on entry (including after `ECHILD`) | **no** | `CONTRADICTED` | no signal; `T2` if an identity was captured **before** the contradiction, else `B` |

**The difference from v2.1.7, in one line per row that changed.** Rows I-4 and
I-10 did not exist (I-4 is Opus X217-m1's exact gap; I-10 is Sol C217-1's
contract-violation state). Rows I-6/I-7/I-8 previously routed to a terminal that
could **return while the child lived**; they now merely withhold the durable
identity, because ownership carries the kill. Row I-2 previously read "PID
reuse ⇒ no kill"; under the ownership premise PID reuse before the reap is
impossible, so the same observation is now correctly labelled a **premise
contradiction**, with the identical no-kill consequence and a strictly better
continuation (`T2`, because a truthful identity was captured earlier).

### V218.3.5 `SIGNAL_ATTEMPT` — ownership-gated, every result pinned

```text
SIGNAL_ATTEMPT(pid_mid, sig) → SENT | GONE | INTERRUPTED | DENIED | ERROR
  PRECONDITION: OWNERSHIP == OWNED. Called in any other state, the call is a
  CONTRACT VIOLATION; the pinned continuation is that no signal is sent.
  sig ∈ {15 (SIGTERM), 9 (SIGKILL)} — integer literals, as carried. killpg is
  NEVER used at stage M (no verified group exists before c11).
  os.kill(pid_mid, sig)
    success           ⇒ SENT — delivered to this child, or discarded because it
                        is already a zombie. Signalling a zombie is a no-op and
                        is SAFE, because an unreaped zombie still holds the pid.
                        SENT alone NEVER proves anything about death.
    ESRCH             ⇒ GONE. Under OWNERSHIP == OWNED this is a CONTRADICTION,
                        not an ordinary race: an owned, unreaped child is a task
                        in some state and kill(2) would succeed. ESRCH therefore
                        means the task no longer exists, i.e. it was reaped by
                        someone other than this route.
                        ⇒ OWNERSHIP := CONTRADICTED ; send no further signal.
    EINTR             ⇒ INTERRUPTED ⇒ retry the SAME signal at
                        T_SUPERVISOR_POLL_INTERVAL_NS within the step's existing
                        signed deadline; on expiry ⇒ ERROR
    EPERM             ⇒ DENIED ⇒ send no further signal of this attempt's
                        schedule; ownership is NOT contradicted (EPERM says
                        nothing about identity); the reaper loop continues to
                        wait. Unreachable for an own child at the same UID on
                        the pinned host; enumerated because the enum must be
                        closed.
    any other OSError ⇒ ERROR ⇒ same continuation as DENIED
  No exception may escape. An escaping exception is a contract violation.
```

The change from §V217.2.3 is exactly the `ESRCH` row: v2.1.7 routed it to
"`WAIT_PROVE` decides", which under a violated premise could be followed by
another signal to a possibly-recycled pid. It now terminates the signalling
authority immediately.

### V218.3.6 The SIGTERM → SIGKILL schedule (carried, ownership-gated)

Inside the one existing signed deadline, with **no new constant**:

```text
t0 := the step's monotonic start ; D := T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
 1. if OWNERSHIP == OWNED: SIGNAL_ATTEMPT(pid_mid, 15)
 2. poll WAIT_PROVE at T_SUPERVISOR_POLL_INTERVAL_NS until t0 + D/2
 3. if not PROVED_DEAD by t0 + D/2 and OWNERSHIP == OWNED:
        SIGNAL_ATTEMPT(pid_mid, 9)
 4. poll WAIT_PROVE until t0 + D
 5. at t0 + D without PROVED_DEAD ⇒ §V218.4.2's terminal selection
Deadline edge: a poll whose sample is exactly t0 + D/2 or exactly t0 + D is
treated as EXPIRED (the comparison is >=), so no edge is ambiguous.
Early exit: if OWNERSHIP becomes CONTRADICTED via INCONCLUSIVE_ECHILD, leave
the loop immediately — no later wait on this pid can return pid_mid — and go to
terminal selection. A contradiction via ESRCH or via a ppid/identity mismatch
does NOT exit early: waitpid may still return pid_mid, which is the outcome the
route most wants.
```

**A stopped child is reached.** `SIGKILL` (9) cannot be caught, blocked, or
ignored and terminates a `SIGSTOP`ed process; the terminated task becomes a
zombie under the normalized disposition and step 4's next poll returns
`PROVED_DEAD`. This is the mechanism by which "a stopped child must be
SIGKILLed and reaped" is satisfied **even when `/proc` is entirely unreadable**,
because step 3 is gated on `OWNERSHIP`, not on `STAT_OBSERVE`.

### V218.3.7 The `c5`/`c6`/`c7` cut mapping (replacing §V217.2.5)

| Cut | `STAT_OBSERVE` result | Ownership effect | Continuation |
|---|---|---|---|
| `c5`, `c6`, or `c7` abandonment | `ABSENT` | none | no identity captured; `OWNED` still authorizes the schedule; `WAIT_PROVE` decides |
| any | `PRESENT_VALID`, captured identity matches (I-1) | none | schedule, then `WAIT_PROVE`; `T2` available |
| any | `PRESENT_VALID`, no captured identity, `ppid == getpid()` (I-3) | none | capture; schedule; `T2` available |
| any | `PRESENT_VALID`, no captured identity, `ppid ≠ getpid()` (I-4) | **`CONTRADICTED`** | **no signal**; no capture; `T2` unavailable ⇒ `B` (this is Opus X217-m1's exact gap, now the premise-failure detector) |
| any | `PRESENT_VALID`, captured identity mismatches (I-2) | **`CONTRADICTED`** | no signal; the earlier capture stands ⇒ `T2` |
| **`c6` unreadable stat** | `UNREADABLE` | none | **the child is still terminated and reaped by ownership**; only the durable identity is unavailable. This is the row that v2.1.7 sent to a returning live-child terminal and that Sol M217-1 rejected |
| **`c6` unparsable stat** | `UNPARSABLE` | none | identical |
| any host fault | `ERROR` | none | identical |
| any | any, after `INCONCLUSIVE_ECHILD` | **`CONTRADICTED`** | no signal; `T2` if an identity was captured earlier, else `B` |

---

## V218.4. Stage-M terminals: the returning live-child terminal is eliminated (R3)

Closes Sol **M217-1**. **`T3` is deleted.** Its "install nothing and return"
body, its removal of `SPAWNING.json` while the middle may be live, and its
contradictory "`or DENIED signals`" membership clause are gone from the
contract.

### V218.4.1 The no-discard invariant

> **No route may return, release `SPAWN.lock`, remove `SPAWNING.json`, or
> discard every durable and in-process handle on `pid_mid` while `pid_mid` may
> remain live and unreaped.**

"Handle" means either the durable `SPAWNING_MIDDLE.json` naming the child by pid
and start identity, or the in-process retention of `pid_mid` in a state that is
still actively terminating and reaping it. `T1` satisfies the invariant because
the child is reaped; `T2` satisfies it by installing the durable handle; `B`
satisfies it by not returning at all and retaining both the lock and the
in-process handle. There is no fourth exit.

### V218.4.2 The stage-M automaton (replacing §V217.3.2)

```text
STAGE_M(cut ∈ {c5, c6, c7}):

 M0. PRECONDITION, both parts required:
       (i)  this attempt's c3n returned NORMALIZED (§V218.2.1); and
       (ii) c4's os.fork() returned pid_mid > 0 in the parent.
     ⇒ OWNERSHIP := OWNED.  captured := the start identity from c6/c7 if one
       was captured, else ⊥.
     If (i) does not hold, no fork occurred and STAGE_M is unreachable
     (§V218.2.5); if (ii) does not hold, see §V218.6's fork-failure row.

 M1. t0 := time.clock_gettime_ns(CLOCK_MONOTONIC) ; D :=
     T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS

 M2. IDENTITY_OBSERVE(pid_mid)                                    (§V218.3.4)

 M3. if OWNERSHIP == OWNED: SIGNAL_ATTEMPT(pid_mid, 15)           (§V218.3.5)

 M4. REAPER LOOP, paced at T_SUPERVISOR_POLL_INTERVAL_NS:
       a. WAIT_PROVE(pid_mid)                                     (§V218.3.3)
            PROVED_DEAD          ⇒ leave the loop (OWNERSHIP == REAPED)
            NOT_YET              ⇒ continue
            INCONCLUSIVE_ECHILD  ⇒ leave the loop immediately
            INCONCLUSIVE_OTHER   ⇒ continue
       b. if OWNERSHIP == OWNED and now >= t0 + D/2:
              SIGNAL_ATTEMPT(pid_mid, 9)
       c. if captured == ⊥ and OWNERSHIP == OWNED:
              IDENTITY_OBSERVE(pid_mid)     # at most once per poll interval
       d. if now >= t0 + D: leave the loop

 M5. TERMINAL SELECTION — total, and the three predicates are pairwise
     disjoint by construction:
       OWNERSHIP == REAPED              ⇒ T1
       OWNERSHIP != REAPED and captured != ⊥   ⇒ T2
       OWNERSHIP != REAPED and captured == ⊥   ⇒ B   (does not return)

────────────────────────────────────────────────────────────────────────────
T1  — AUTHORITATIVE REAP.  Entered only after os.waitpid(pid_mid, …) returned
      pid_mid.  ECHILD NEVER enters T1.
    1. S1: CLOSE_OWNED cleanup of the CLI's bootstrap ends (§V216.2.2)
    2. ordered removal of ALL FOUR of this attempt's records in the §U6.3
       order SPAWNING_CHILD → SPAWNING_GROUP → SPAWNING_MIDDLE → SPAWNING,
       each unlink followed by fsync(T_SUPERVISOR/), ENOENT tolerated, matched
       by spawning_id, while still holding SPAWN.lock
    3. CLOSE_OWNED(spawn_lock_fd); return REFUSED / BOOTSTRAP, retryable = true
    ⇒ no record survives; the child is dead and reaped, so no fork-shared lock
      reference survives; the next attempt starts at §U6.1 P0.

T2  — TRUTHFUL DURABLE HANDOFF.  Entered when the child was not reaped and a
      start identity WAS captured while OWNERSHIP was OWNED (so every field is
      an observed value; nothing is fabricated).
    1. S1: CLOSE_OWNED cleanup of the CLI's bootstrap ends
    2. install SPAWNING_MIDDLE.json for this attempt if it is not already
       durable, with the already-signed §U2.2 c7 key set exactly — schema,
       scientific_outcome, spawning_id, cli_pid, cli_start_identity,
       middle_child_pid, middle_child_start_identity, boot_identity,
       created_utc — under the §U6.2 EEXIST discipline
    3. remove ONLY SPAWNING.json (§V218.4.3), with its fsync
    4. RETAIN pid_mid in memory as an unreaped own child of this process, so
       that a later attempt in this same process reaps it at §U6.1 P3 (wait
       site W-4). See §V218.4.5's zombie residual.
    5. CLOSE_OWNED(spawn_lock_fd); return REFUSED / BOOTSTRAP, retryable = true
    ⇒ the surviving handle is SPAWNING_MIDDLE.json, resolved by the EXISTING
      §U6.1/§U2.5 routes (§V218.4.4 proves that resolver total).

B   — HOST-FAULT / PREMISE-CONTRADICTION BLOCKED REAPER.  Entered when the
      child was not reaped and NO start identity was ever captured, so
      SPAWNING_MIDDLE.json is NOT truthfully constructible.
      B DOES NOT RETURN. It is an explicit non-returning state, not a terminal.
    B holds, for as long as it lasts:
      - SPAWN.lock                       (CLOSE_OWNED is NOT called)
      - SPAWNING.json                    (NOT removed — the attempt is not
                                          abandoned; §V218.4.3)
      - pid_mid in memory                (the in-process fork handle)
      - the CLI's bootstrap ends         (cleanup is deferred to the exit)
    B installs NOTHING: no record, no schema, no field, no event, no reply.
    B produces NO refusal, NO scientific statement, and NO resource statement.
    B loops, paced at T_SUPERVISOR_POLL_INTERVAL_NS, with no deadline:
       a. WAIT_PROVE(pid_mid)
            PROVED_DEAD          ⇒ exit B into T1's body (steps 1–3 above)
            NOT_YET              ⇒ continue
            INCONCLUSIVE_ECHILD  ⇒ OWNERSHIP := CONTRADICTED; continue
            INCONCLUSIVE_OTHER   ⇒ continue
       b. if OWNERSHIP == OWNED: SIGNAL_ATTEMPT(pid_mid, 9)
            — re-issuing SIGKILL each interval is provably harmless: under
              OWNED the pid denotes this child or a zombie of it and can denote
              nothing else, so no unrelated process can receive it.
       c. if OWNERSHIP == OWNED: IDENTITY_OBSERVE(pid_mid)
            PRESENT_VALID with a capture (I-3) ⇒ captured := s.start_identity
                                               ⇒ exit B into T2's body
            anything else ⇒ continue
    B's ONLY exits are (a)'s PROVED_DEAD into T1 and (c)'s capture into T2.
    Sub-modes, for the residual table:
      B-OWNED         : OWNERSHIP == OWNED — signals and re-observes
      B-CONTRADICTED  : OWNERSHIP == CONTRADICTED — waits only; sends no
                        signal; captures nothing; therefore its only exit is
                        WAIT_PROVE returning pid_mid
```

**Why `B` is preferred over inventing a new durable object.** R3 asks for the
no-new-object route when it is total, and `B` is total: every syscall in its
loop returns one of a closed enum with a pinned continuation, and every state of
the automaton has exactly one successor. It introduces no record class, no
schema, no tier, no path, and no resource decision. What it does **not** promise
is termination in every case; §V218.4.5 states exactly when it does not
terminate, and why that is the correct fail-closed behaviour rather than a
concealed defect.

**`B` introduces no new blocking syscall and no unsigned deadline.** Its wait is
`os.waitpid(pid_mid, WNOHANG)` — the same nonblocking primitive used everywhere
— paced by `time`; it adds no constant and reads no pipe. Its unbounded duration
contradicts nothing, because §V217.4.3 (carried unchanged) already withdrew
every fixed-total-CLI-lifetime and lock-hold claim and states plainly that the
CLI's total lifetime and total lock-hold are **not** fixed-bounded, with D1
resting on "no supervisor waits on `SPAWN.lock`". `B` is the first route to make
that withdrawal operationally visible; it does not reintroduce the contradiction
class Opus X216-M1 closed, and revised row 86 remains satisfiable (§V218.7).

### V218.4.3 `SPAWNING.json` removal, correctly scoped

§V217.3.1's table (which records that `SPAWNING.json` names **only** the CLI,
and that the other three records are protected by death-before-unlink) is
carried **unchanged**. Its concluding sentence is replaced:

> **Every *returning* terminal of stage M — `T1` and `T2` — removes the CLI's
> own `SPAWNING.json` while still holding `SPAWN.lock`.** The premise of that
> rule is that the CLI has *abandoned the attempt and will perform no further
> action in it*. The non-returning state `B` has **not** abandoned the attempt:
> it is still signalling and still reaping, so it **retains** `SPAWNING.json`,
> which truthfully continues to name the live CLI that is performing those
> actions. Removing it there would make the record's absence a lie about a CLI
> that is still acting, and would gain nothing, since `B` does not release the
> lock either.

The Y-line wedge remains closed at its root: **no returning route can leave
behind a `SPAWNING.json` naming a live long-lived CLI**, so no future attempt's
`§U6.1 P2b` can be triggered by one. The only surviving `SPAWNING.json` naming a
live CLI belongs to a process that is simultaneously holding `SPAWN.lock`, so no
other CLI can reach the preflight that would read it.

### V218.4.4 Forward progress, and the totality of the existing resolver

| Surviving state after stage M | Lock | Next attempt's behaviour | Bound |
|---|---|---|---|
| nothing (`T1`) | free once the CLI's fd closes; the child is reaped, so no fork-shared reference remains | §U6.1 P0 ⇒ install and proceed | immediate |
| `SPAWNING_MIDDLE.json`, recorded process live (`T2`) | the middle still holds a fork-shared reference, so acquisition fails until it exits | acquisition retries to `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS`; on acquire, §U6.1 P2b ⇒ `REFUSED`/`BOOTSTRAP` (retryable) with no unlink and no kill | the middle is at `m0` and exits at its own `m0` bound ≤ `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` unless deliberately stopped |
| `SPAWNING_MIDDLE.json`, recorded process live and aged | as above | the **existing** §U2.5 `s4` tier: `kill(middle_child_pid)` only (never `killpg`), after start-identity validation, then proved death, then one bounded retry of the acquisition; `c1`'s preflight P3 then removes the record under the acquired lock | `T_SPAWN_BOOTSTRAP_MAX_AGE_NS` + `s4`'s own bounds |
| `SPAWNING_MIDDLE.json`, recorded process not live (including state `Z` — the ordinary outcome once the `m0` bound fires) | free | §U6.1 P3 ⇒ death proved by `/proc` absence, state `Z` with matching identity, or start-identity mismatch ⇒ ordered removal ⇒ proceed | immediate |
| `SPAWNING.json` + `SPAWN.lock` held by a CLI in `B` | held | acquisition expires ⇒ `s1` (no `SUPERVISOR_IDENTITY.json`) ⇒ `s2`/`s3` (no child/group record) ⇒ `s4` (no middle record) ⇒ **`s5`** ⇒ `REFUSED`/`BOOTSTRAP` (retryable = true); **nothing is unlinked and nothing is killed** | none — see §V218.4.5 |

**Proof that the existing resolver is total for `T2`'s surviving record.** The
`SPAWNING_MIDDLE.json` that `T2` installs is well-formed by construction (the
signed `c7` key set, every field an observed value). A later attempt reading it
falls into exactly one of §U6.1's cases, and every case has a pinned
continuation that already exists in the signed text:

| §U6.1 case | Applies to `T2`'s record when | Continuation | New text needed? |
|---|---|---|---|
| P0 | it was already removed by a previous resolver | install and proceed | no |
| P1 (malformed) | **unreachable** — `T2` writes the signed key set atomically with no-replace and §3 durability | fail-closed refusal | no |
| P2a | a later attempt would install a byte-identical record with the same `spawning_id` — **unreachable across attempts**, since `spawning_id` is per-attempt | adopt | no |
| P2b | the recorded middle is live and not yet aged | retryable `BOOTSTRAP`; nothing unlinked, nothing killed | no |
| P3 | the recorded middle is absent, in state `Z`, or live with a different start identity | prove, remove per §U6.3, continue | no |
| `s4` | the record is aged past `T_SPAWN_BOOTSTRAP_MAX_AGE_NS` and its process is live by pid + start identity | `kill(middle_child_pid)`, prove death, remove per §U6.3, retry once | no |
| `s5` | none of `s1`–`s4` applies | retryable `BOOTSTRAP` | no |

Every branch is pinned and **no new tier, record, schema, resolver, or operator
step is introduced**. Two honest limits, stated rather than glossed: `s4`'s
death proof is `/proc`-based and is not available to a *different* process that
also cannot read `/proc` — under such a host fault the resolver refuses
retryably (`s5`) instead of acting unsafely, which is the correct fail-closed
behaviour; and `s4` cannot `waitpid` the middle, because the later CLI is not
its parent — it proves death by `/proc` absence or state `Z`, exactly as the
signed text already says, and the zombie left by §V218.4.5 satisfies the state-`Z`
branch precisely.

### V218.4.5 The three named residuals, stated not claimed away

**Residual 1 — the unreaped-zombie residual this layer itself creates (new).**
Normalizing `SIGCHLD` to `SIG_DFL` has a cost that must be named rather than
discovered by a reviewer: a middle child that terminates while the CLI has taken
`T2` becomes a **zombie**, and a long-lived CLI process that never makes another
attempt holds that zombie for its own lifetime. Its exact scope:

- **one** zombie per `T2`-terminated attempt, holding **one** pid slot;
- **no** file descriptors, therefore **no** `SPAWN.lock` reference — a zombie
  releases every descriptor at exit, so it never wedges the singleton;
- **no** durable object, no runtime evidence, no capacity, no custody, and no
  scientific artifact;
- reaped by wait site **W-4** (§U6.1 P3) at the next attempt in the same
  process, or by the CLI's exit, whichever comes first;
- **positively useful** to other processes: a zombie is `/proc` state `Z` with a
  matching start identity, which is exactly the §U6.1 P3 death proof, so a
  concurrent CLI resolves `T2`'s record faster than it could against a
  `/proc`-absent pid.

This residual did not exist in v2.1.7 because v2.1.7 (incorrectly) assumed
nothing about reaping. It is a **resource** residual of the A3 procedural class,
permanently non-citable, forbidden from selection, Q, C, C1–C6, any blinding
claim, and any scientific or resource interpretation.

**Residual 2 — `B-OWNED` non-termination requires a stopped child *and* a
persistent signal fault.** In `B-OWNED` the child is reached by `SIGKILL`
(§V218.3.6) without any `/proc` dependence, so it terminates and is reaped.
Even with **no** signal delivered at all, a middle child that is executing
normally is at `m0` and exits at its own signed bound
(`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` from `m0` entry), becoming a zombie that
`B`'s next poll reaps ⇒ `T1`. **`B-OWNED` therefore fails to terminate only when
the child is deliberately `SIGSTOP`ed by a same-UID actor *and* every
`SIGNAL_ATTEMPT` returns `DENIED`/`ERROR` — a same-UID interference conjoined
with a host fault that is unreachable for an own child at the same UID on the
pinned host.** (That sentence is a conditional statement about one state under
stated premises; it is **not** a total-CLI-lifetime or lock-hold bound, and
§V217.4.3's withdrawal of every such bound is unaffected.) This is the signed A3
procedural residual, the same class as §U2.7's stopped-CLI and stopped-middle
residuals, permanently non-citable, and **not** claimed impossible.

**Residual 3 — `B-CONTRADICTED` does not terminate, deliberately.** If the
premise is violated so that `pid_mid` was reaped by something other than this
route (`ECHILD`, or `ESRCH` on an owned unreaped child, or a `ppid` mismatch),
then `waitpid` can never return `pid_mid`, and `B-CONTRADICTED` loops
indefinitely while holding `SPAWN.lock` and `SPAWNING.json`. This is deliberate
and is stated in full:

- It **blocks future supervisor construction** for as long as it lasts. Later
  CLIs receive `s5`'s retryable `REFUSED`/`BOOTSTRAP` and nothing is unlinked or
  killed.
- It is **process control, not evidence**. It emits no refusal to a caller, no
  event, no ledger entry, no capacity or custody artifact, and nothing citable.
  It is **never** a resource-exhaustion result, **never** a scientific outcome,
  and **never** an invalidity cause. It must not be read as `T_PROCESS_INVALID`,
  as an E1/E2/E3 fact, or as any Q/C input.
- It **does not falsely free the singleton**: the alternative — returning while
  holding an inconclusive ownership premise — would either signal a possibly
  recycled pid or declare a possibly live child dead, and both are worse than a
  visible stall.
- It relies on **no** caller exit, garbage collection, finalizer, unstated
  operator, or invented deadline, and it picks **no** resource value. That the
  situation is one an operator will eventually notice is a *fact about the
  world*, not a step of this contract, and no route delegates to it.
- Reaching it requires a **violation of §V218.2.6's sole-reaper contract or of
  the §V218.2.2 normalization** — i.e. a contract violation — **conjoined with**
  a `/proc` fault severe enough that no start identity was ever captured. Under
  a conforming host and a conforming implementation it is unreachable.

D1 is unaffected by all three: no supervisor waits on `SPAWN.lock`, and a
running supervisor's lifetime never depends on any client.

---

## V218.5. The corrected stage-M causal proof (R4)

Closes Sol **m217-1**. v2.1.7's stage-M two-supervisor argument reasoned from
`m5` and `rel2`, which **no `c5`–`c7` schedule can reach**. The whole argument
is replaced by the actual trace, and the `m5`/`rel2` reasoning is removed from
every stage-M prose, table, test, and closure claim.

### V218.5.1 The actual `c5`/`c6`/`c7` trace

Execution order is `c1 → c2 → c3 → c3n → c4 → c5 → c6 → c7 → c8`, and the
stage-1 release byte is written **at `c8`** (§U2.2). Therefore, at any `c5`,
`c6`, or `c7` abandonment:

1. **No `c8` release byte was ever written on `rel1`.** `rel1` is a fresh pipe
   created at `c3` and the only writer that ever writes to it is `c8`, which has
   not executed. The pipe is empty; there is no queued or buffered byte, and
   none can appear, because the abandoning CLI never reaches `c8`.
2. **The middle child is at `m0`**, its literal first instruction — a bounded,
   `O_NONBLOCK`, poll-paced read of `rel1_r` that performs no filesystem write
   and changes no shared state (§U2.3, carried).
3. **The middle still owns its own inherited `rel1_w` copy**, which it does not
   close until `m1`. EOF on a pipe requires **every** writer to be closed, so
   **EOF at `m0` is impossible in principle** no matter what the CLI closes —
   §V216.3.1's finding, carried unchanged and now applied where it belongs.
4. **The middle's exit is controlled by exactly two things**: its own `m0` bound
   (`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, after which it `os._exit(3)`s), and the
   parent's ownership-authorized `SIGTERM`/`SIGKILL` and reap (§V218.3.6). A
   third path — reading a byte — cannot occur, since none was written; and were
   any other byte somehow present, `m0` maps it to `os._exit(3)`.
5. **The middle can never reach `m1`**, hence never `m2` (`setsid`), never `m4`
   (the group report), never `m5` (the stage-2 gate), and never `m7` (the second
   fork). **No grandchild is ever created and no `SUPERVISOR_IDENTITY.json` is
   ever installed.** That — not any `rel2` EOF — is the reason no `c5`–`c7`
   abandonment can yield a second supervisor.
6. **The fork-shared `SPAWN.lock` reference is what serializes the next CLI.**
   The middle holds a reference to the same open file description, so the
   `flock` persists until that reference is closed at the middle's exit. A new
   CLI therefore cannot acquire `SPAWN.lock` until the middle exits — which is
   the true statement of when the singleton becomes free, replacing v2.1.7's
   `rel2`-based account.

The sentence "the middle closed its own `rel2_w` copy at `m1`, making the CLI
the sole remaining writer, so `m5` observes EOF" is **deleted from stage M**. It
was not merely imprecise; at `c5`–`c7` the middle has not executed `m1` at all,
so it has not closed any `rel2_w` copy, and the reasoning describes a state the
cut cannot produce.

### V218.5.2 The five re-run schedules

| Schedule | Trace under §V218.5.1 | Outcome |
|---|---|---|
| **stopped / resumed middle** | `SIGSTOP` at or before `m0`. `SIGKILL` from `M4.b` or `B-OWNED.b` is ownership-authorized and cannot be blocked ⇒ the child terminates while stopped ⇒ zombie ⇒ reaped | `T1`. If instead it is resumed without being killed, its `m0` bound is measured from `m0` entry against the monotonic clock and has elapsed during the stop, so the next loop iteration exits it ⇒ `os._exit(3)` ⇒ zombie ⇒ reaped ⇒ `T1` |
| **queued byte** | none can exist: `c8` never executed, and `rel1` had no other writer | no `m1` transition is reachable; the `m0` "any other byte ⇒ `_exit(3)`" branch is unreachable in fact and harmless if reached |
| **writer copy** | the middle's own `rel1_w` copy is open until `m1`; the CLI's `rel1_w` is closed only at `c8` or at `BOOTSTRAP_FD_CLEANUP` | no EOF at `m0` in either case; the `m0` bound, not EOF, governs — exactly §V216.3.1's carried finding |
| **timeout** | the `m0` bound fires ≤ `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` after `m0` entry ⇒ `os._exit(3)` ⇒ zombie (normalized disposition) ⇒ the next `WAIT_PROVE` poll returns `pid_mid` | `T1`, **including from inside `B-OWNED` with `/proc` entirely unreadable** — the case v2.1.7 sent to a returning live-child terminal |
| **immediate new CLI** | `T1`: records gone, no fork-shared reference remains ⇒ the new CLI acquires and starts at P0. `T2`: `SPAWNING.json` gone, `SPAWNING_MIDDLE.json` durable, the middle still holds the lock reference ⇒ acquisition retries until the middle exits, then P2b/P3/`s4` per §V218.4.4. `B`: the lock is retained ⇒ acquisition expires ⇒ `s1`–`s5` ⇒ `s5` retryable refusal, nothing unlinked, nothing killed | no schedule yields two supervisors, and none removes a record naming a possibly live process |

### V218.5.3 Where the `m5`/`rel2` argument is retained

It is **correct and retained** only for routes that can actually reach `m5` —
i.e. cuts at or after `c8`, where the middle has passed `m0`, executed `m1`
(closing its `rel1` ends and its `rel2_w`/`rel3_w` copies), and is waiting at the
`m5` stage-2 gate:

- §U2.6's rows "after `c8`, before `m2`", "after `m4`, before `c11`", "after
  `c11`, before `c12`", and "after `c12`, before `m7`" — carried unchanged;
- §U2.5's stage-1 and stage-2 routes — carried unchanged;
- §V216/§V217's statements about the grandchild gate `rel3` — carried unchanged.

No stage-M sentence, table cell, test row, or closure claim may cite `m5`,
`rel2`, or a `rel2` EOF. Test row **207** is replaced accordingly (§V218.7), and
this correction's own closure states the `m0`/`rel1`/lock trace and not the
`rel2` one.

---

## V218.6. Crash and cut matrix (replacing the named §V217.3.5 and §V217.5 rows)

Every §V217.3.5 and §V217.5 row not listed in §V218.0 carries forward
unchanged — in particular every §V217.1 selector/barrier row, every
`OBSERVATION_INCONCLUSIVE` row, and every bound-language row.

| Cut / scenario | Single continuation |
|---|---|
| `c3n` normalization raises `ValueError` (not the main thread) | `PRE_FORK_FAIL_CLOSED`; **no fork**; only `SPAWNING.json` removed; non-retryable refusal |
| `c3n` normalization raises `OSError`/`RuntimeError`/anything else | identical |
| `c3n` verification finds the `SigIgn` or `SigCgt` bit set | `VERIFY_FAILED` ⇒ `PRE_FORK_FAIL_CLOSED`; **no fork** |
| `c3n` verification cannot read or parse `/proc/self/status` | `VERIFY_INCONCLUSIVE` ⇒ `PRE_FORK_FAIL_CLOSED`; **no fork** |
| `c3n` succeeds, `c4`'s `os.fork` raises `OSError` | no child exists; ownership is never established; the `PRE_FORK_FAIL_CLOSED` body applies unchanged (its `F1` is already satisfied) |
| crash between `c3n` and `c4` | no child; `SPAWNING.json` survives naming a **crashed** CLI; the next attempt's §U6.1 P3 proves its death by absence and removes it |
| a second attempt in the same CLI process | re-executes `c3n` in full; **no cached normalization is consulted** |
| `waitpid` returns `pid_mid` | `PROVED_DEAD`; `OWNERSHIP := REAPED`; `T1`; the route never touches the pid again |
| `waitpid` returns `0` | `NOT_YET` ⇒ continue polling |
| `waitpid` `ECHILD` | **`INCONCLUSIVE_ECHILD`; `OWNERSHIP := CONTRADICTED`; never `PROVED_DEAD`; never `T1`** ⇒ leave the deadline loop ⇒ `T2` if an identity was captured, else `B-CONTRADICTED` |
| `waitpid` `EINTR` | bounded retry within the existing deadline; on expiry `INCONCLUSIVE_OTHER` |
| `waitpid` any other error | `INCONCLUSIVE_OTHER` ⇒ continue polling ⇒ terminal selection at `t0 + D` |
| `kill` success on a live child | `SENT` ⇒ nothing is concluded about death |
| `kill` success on an unreaped zombie | `SENT` ⇒ harmless no-op; the pid is still reserved |
| `kill` `ESRCH` | **contradiction**: `OWNERSHIP := CONTRADICTED`; no further signal ⇒ `T2` or `B-CONTRADICTED` |
| `kill` `EINTR` | bounded retry of the same signal within the existing deadline |
| `kill` `EPERM` or other error | `DENIED`/`ERROR`; ownership **not** contradicted; no further signal in this schedule; the reaper loop continues |
| `/proc` stat `EACCES`/`EPERM`, parse failure, `EINTR`-expiry, or other error | `UNREADABLE`/`UNPARSABLE`/`ERROR`; **no capture**, but the ownership-authorized `SIGTERM`/`SIGKILL` and reap proceed; `T2` is unavailable from this observation |
| `/proc` stat `PRESENT_VALID`, no captured identity, `ppid ≠ getpid()` | **contradiction**; no signal; no capture ⇒ `B-CONTRADICTED` |
| `/proc` stat `PRESENT_VALID`, captured identity mismatches | **contradiction**; no signal; the earlier truthful capture stands ⇒ `T2` |
| SIGTERM sent, no reap by `t0 + D/2` | SIGKILL sent; polling continues to `t0 + D` |
| a poll sample exactly at `t0 + D/2` or `t0 + D` | treated as expired (`≥`); no ambiguous edge |
| **stopped middle child, `/proc` readable** | `SIGKILL` ⇒ terminates ⇒ zombie ⇒ `WAIT_PROVE` returns `pid_mid` ⇒ `T1` |
| **stopped middle child, `/proc` entirely unreadable** | ownership authorizes `SIGKILL` without any `/proc` read ⇒ `T1`. This is the row that had no safe continuation before this layer |
| middle exits **before** any signal | zombie ⇒ `WAIT_PROVE` ⇒ `PROVED_DEAD` ⇒ `T1` |
| middle exits **between** SIGTERM and SIGKILL | zombie ⇒ next poll ⇒ `T1` |
| middle at `m0` reaches its own bound while the CLI is in `B-OWNED` | `os._exit(3)` ⇒ zombie ⇒ next poll ⇒ `T1` |
| **long-lived CLI**, failure at `c5`/`c6`/`c7`, child reaped | `T1`: all four records removed; the CLI's own `SPAWNING.json` is gone; **no wedge** |
| **long-lived CLI**, child not reaped, identity known | `T2`: truthful `SPAWNING_MIDDLE.json` installed, `SPAWNING.json` removed, `pid_mid` retained in memory; `§U6.1`/`s4` resolve it; **no wedge**; one zombie residual (§V218.4.5) |
| **long-lived CLI**, child not reaped, identity never obtainable | `B`: **does not return**; lock and `SPAWNING.json` retained; the reaper continues; §V218.4.5 residuals 2 and 3 govern |
| a route attempts to signal after `PROVED_DEAD` | forbidden by `OWNERSHIP == REAPED`; an implementation that does so is in violation, not on a route |
| a route attempts to signal while `CONTRADICTED` | forbidden by §V218.3.1's single rule |
| a CLI containing `os.wait()`, `os.wait3()`, `os.waitpid(-1, …)`, `os.waitpid(0, …)`, `os.waitid(P_ALL, …)`, a `subprocess` object, a thread, or a signal handler | **contract violation**, not a route (§V218.2.6) |
| CLI crash anywhere inside `M4`, `B`, `T1`, or `T2` | the kernel releases the CLI's descriptors and its lock reference; any unreaped child is reparented to `init`, which reaps it; no record was removed without an authoritative reap; the next attempt's §U6.1 P0–P3 governs |
| crash after `T2`'s `SPAWNING_MIDDLE.json` install, before the `SPAWNING.json` unlink | both records exist; the next preflight applies P1/P2/P3 in the child→group→middle→spawning order; a live middle is P2b-refused then `s4`-resolved; the surviving `SPAWNING.json` names a **crashed** CLI, so P3 proves its death by absence and removes it |
| crash between any ordered unlink and its `fsync` | ENOENT-tolerant; `child → group → middle → spawning` resumes |
| crash after the final unlink, before the lock close | the crash releases the lock reference; no attempt state survives |
| restart **before** the middle's own `m0` bound | records of the attempt survive; the middle exits at its bound; the next attempt's P0–P3 governs |
| restart **after** the middle's own `m0` bound | the middle is gone (or is a zombie reparented to `init` and reaped); P3 proves death and removes the records |

**Death-before-unlink is preserved exactly.** In every row, no record naming the
grandchild, the group, or the middle child is removed without an authoritative
reap (`waitpid == pid_mid`) or one of §U6.1 P3's signed death proofs. The only
record ever removed without such a proof is `SPAWNING.json`, which names the CLI
performing the removal — and `B` does not even remove that.

---

## V218.7. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, commit, host change,
process, signature, activation, entropy, T/Q/C work, E1/E2/E3 spend, scientific
execution, or later gate is authorized. Obligations become due only after both
fresh independent v2.1.8 reviews confirm these bytes **and** the author signs
the amendment token.

§W10 rows 1–50, §Z12.2 rows 51–74, §N12 rows 75–85 and 87–96 (row **86**
replaced by §V217.4.4, carried), §U11 rows 97–120, §V214.10 rows 122–125 and
127–144, §V215.7 rows 145–149, 151–153, 155–156, 158–164, §V216.6 rows 165–180
and 182–183, and §V217.6 rows 185–197, 201, 202, 204, 206, 209–212 carry
forward. Replaced:

- **row 198 replaced:** `WAIT_PROVE` returns exactly one of four results for
  `pid_mid`, `0`, `ECHILD`, `EINTR`, and other errno; **only a returned
  `pid_mid` proves death**; `ECHILD` yields `INCONCLUSIVE_ECHILD` and sets
  `CONTRADICTED`; no path maps `ECHILD` to `PROVED_DEAD` or to `T1`.
- **row 199 replaced:** assert that `c3n` executes `signal.signal(signal.SIGCHLD,
  signal.SIG_DFL)` before the first `os.fork` of **every** attempt, that
  verification reads `/proc/self/status` and requires the `SigIgn` and `SigCgt`
  bits for `signal.SIGCHLD` to be clear, and that **no fork occurs** unless the
  result is `NORMALIZED`. The old row's premise — "no signal disposition is
  installed anywhere, so `SIGCHLD` keeps its default" — is **deleted as false**.
- **row 200 replaced:** after `OWNERSHIP == REAPED` the route never signals,
  stats, or waits on `pid_mid` again; **and** after `OWNERSHIP ==
  CONTRADICTED` it never signals it again; both are enforced by the single
  `os.kill` precondition and are statically checkable.
- **row 203 replaced:** the Y-line wedge over the **surviving** terminals: for a
  long-lived CLI failing at `c5`/`c6`/`c7`, every **returning** terminal (`T1`,
  `T2`) removes the CLI's own `SPAWNING.json`, and the non-returning `B` state
  retains it while retaining the lock; assert no future attempt is P2b-refused
  because of a `SPAWNING.json` naming a live CLI that has returned.
- **row 205 replaced:** **`T3` no longer exists.** Assert that no route
  installs nothing, removes `SPAWNING.json`, releases the lock, and returns
  while `pid_mid` may be live and unreaped; assert the terminal predicates
  `REAPED` / (`¬REAPED` ∧ captured) / (`¬REAPED` ∧ ¬captured) are pairwise
  disjoint and exhaustive.
- **row 207 replaced:** the stage-M no-second-supervisor proof is the
  `m0`/`rel1`/lock trace of §V218.5.1 — no `c8` byte was written, the middle is
  at `m0` and owns its own `rel1_w`, EOF at `m0` is impossible, `m1`/`m5`/`m7`
  are unreachable, and the fork-shared lock serializes the next CLI; assert that
  **no** stage-M text, table, or test cites `m5`, `rel2`, or a `rel2` EOF.
- **row 208 replaced:** every row of §V218.6 has exactly one continuation, and
  no row removes a record naming a possibly live process or discards every
  handle on a possibly live child.

Added:

| # | Test | Covers |
|---|---|---|
| 213 | **inherited `SIG_IGN` fixture**: a parent process sets `SIGCHLD` to `SIG_IGN`, then `execve`s the CLI entry; assert `/proc/self/status` shows the `SigIgn` bit set **before** `c3n` and clear **after**, and that a child forked afterwards becomes a zombie observable by `waitpid` | R1, C217-1, X217-M1 |
| 214 | **inherited `SA_NOCLDWAIT` fixture**: a parent installs `sigaction(SIGCHLD, {SIG_DFL, SA_NOCLDWAIT})` — the fixture may use `ctypes`, which the runtime allowlist forbids but which does not govern test fixtures — and then **forks without exec** into the CLI entry, so both the disposition table and the flags are inherited; assert that after `c3n` a forked child becomes a zombie and `waitpid` returns its pid rather than `ECHILD` | R1, C217-1 |
| 215 | the negative control: with `c3n` disabled and `SIGCHLD == SIG_IGN` inherited, assert `waitpid` yields `ECHILD`, that the route maps it to `INCONCLUSIVE_ECHILD`, that it never reaches `T1`, and that no signal is sent after the contradiction | R1, R2 |
| 216 | **allowlist containment**: `ALLOWED_ABSOLUTE_IMPORTS` equals the sixteen previously pinned members plus exactly `"signal"`; `ALLOWED_RELATIVE_IMPORTS` is unchanged; `signal` is imported by the CLI bootstrap module and by **no** other module; only `SIGCHLD`, `SIG_DFL`, `signal`, and `getsignal` are referenced; no handler callable, no `SIG_IGN`, no `set_wakeup_fd`, no `pthread_sigmask`, no `pidfd_send_signal` | R1, §V218.1.2 |
| 217 | §W2.6's property survives the delta: the controller adapter entry installs no signal disposition and calls `os.kill(os.getpid(), SIGSTOP)` before any input read, thread, backend, or controller logic — now asserted directly rather than argued from the allowlist | R1, no-regression |
| 218 | §W6.4's conclusion survives: no cgroup, PID namespace, or `PR_SET_CHILD_SUBREAPER` is used; `ctypes` remains unimported anywhere in the runtime tree | R1, no-regression |
| 219 | `NORMALIZE_REAPING_STATE` returns exactly one of two results for each injected condition (`ValueError` off the main thread, `RuntimeError`, `OSError`, success); no exception escapes; the returned previous handler is never consulted by any predicate | R1 |
| 220 | `VERIFY_REAPING_STATE` returns exactly one of three results for each injected `/proc/self/status` condition (absent, unreadable, missing line, duplicated line, non-hex value, bit set, all clear); the bit index is computed from `int(signal.SIGCHLD) - 1`, not a literal | R1 |
| 221 | **no fork on a non-`NORMALIZED` result**: for each of the three failure results, assert `os.fork` is never called, only `SPAWNING.json` is removed, the lock is released, and the non-retryable named terminal is returned | R1 |
| 222 | **the single kill precondition**: every `os.kill(pid_mid, …)` in the CLI is guarded by `OWNERSHIP == OWNED`; injected `REAPED` and `CONTRADICTED` states make every signal site unreachable | R2 |
| 223 | **sole-reaper static assertion**: the CLI contains no `os.wait()`, `os.wait3()`, `os.wait4()`, `os.waitid()`, `os.waitpid(-1, …)`, `os.waitpid(0, …)`, or negative-pgid wait; no `subprocess` object; no thread; no signal handler; every wait targets one explicit positive pid | R1, R2 |
| 224 | **wait-site enumeration**: the five permitted sites W-1…W-5 are exactly the wait sites present; W-1…W-3 and W-5 are mutually exclusive per attempt; no site executes after `OWNERSHIP == REAPED` | R1 |
| 225 | **per-attempt reset**: a CLI process making two attempts executes `c3n` twice; a cached "already normalized" flag is absent; the second attempt's fork is preceded by its own verification | R1 |
| 226 | `IDENTITY_OBSERVE` is total over the product of the five `STAT_OBSERVE` results × captured/uncaptured × `ppid` equal/unequal × the three ownership states; every cell matches §V218.3.4 | R2, X217-m1 |
| 227 | the `ppid ≠ getpid()` branch (I-4) captures nothing, sends no signal, and routes to `B`; assert no durable record is ever written from an observation taken under a contradicted premise | R2, X217-m1 |
| 228 | the captured-identity mismatch branch (I-2) sends no further signal but retains the **earlier** truthful capture and reaches `T2` | R2 |
| 229 | `SIGNAL_ATTEMPT` returns exactly one of five results for success, `ESRCH`, `EINTR`, `EPERM`, and other errno; `ESRCH` under `OWNED` sets `CONTRADICTED`; `EPERM` does not | R2 |
| 230 | **the PID-reuse window**: with the normalization in place, inject a child exit at every instruction boundary between `STAT_OBSERVE` and `os.kill`; assert the pid is never reassigned before the route's own reap, and that no signal is delivered to any process other than `pid_mid`'s task | R2, C217-1, X217-M1 |
| 231 | **`/proc` fully unreadable, live child**: the route still terminates and authoritatively reaps its own child; assert `T1` is reached with no `/proc` read having succeeded | R2, R3 |
| 232 | **`/proc` fully unreadable, stopped child**: `SIGKILL` is issued under ownership alone, the child dies, is reaped, and `T1` is reached | R3, M217-1 |
| 233 | the `B` state does not return, does not release the lock, does not remove `SPAWNING.json`, installs nothing, and emits no refusal, event, or artifact; its only exits are `PROVED_DEAD` ⇒ `T1` and a capture ⇒ `T2` | R3 |
| 234 | `B-OWNED` terminates via the middle's own `m0` bound when every signal is suppressed, and via `SIGKILL` when signals succeed; `B-CONTRADICTED` sends no signal and its non-termination under an injected external reaper is asserted as the **named** residual, with nothing citable produced | R3 |
| 235 | `T2` writes the signed `c7` key set with every field an observed value; no field is fabricated; assert the record is well-formed against §U6.1 P1 and resolvable by P2b/P3/`s4` | R3 |
| 236 | **the zombie residual**: after `T2`, exactly one zombie exists, it holds no descriptor and no lock reference, `/proc` reports state `Z` with a matching start identity, a concurrent CLI resolves the record through P3, and a later attempt in the same process reaps it at W-4 | R1, R3 |
| 237 | **long-lived-CLI crash/restart traces**: for each of `T1`, `T2`, and `B`, inject a CLI crash at every instruction boundary and assert a single continuation, no record naming a live process removed, and no handle discarded while the child may act | R3 |
| 238 | **the corrected causal trace**: at `c5`, `c6`, and `c7`, assert no `c8` byte was written, the middle is at `m0`, it owns its `rel1_w`, EOF at `m0` never occurs, `m1`/`m2`/`m4`/`m5`/`m7` are never reached, no grandchild is forked, no `SUPERVISOR_IDENTITY.json` is installed, and the next CLI cannot acquire `SPAWN.lock` until the middle exits | R4, m217-1 |
| 239 | the five §V218.5.2 schedules — stopped/resumed, queued byte, writer copy, timeout, immediate new CLI — each behave as tabulated, and none is analyzed through `m5` or `rel2` | R4 |
| 240 | **no-regression sweep**: diff every non-replaced section body of v2.1.7 and every carried layer against the text this correction claims to carry, including §V217.1 in full, §V217.4 in full, §V216.1.2's rule structure, §V216.2, §V216.3.1, §V216.5, the three branch bodies, K1's accounting, the GC order, the watchdog partition, and the batch-settlement and generic-harness composites; assert the reaper repair changes no selector, custody, capacity, or filesystem rule | R5 |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object. Fixtures 213–215 fork and signal only their own throwaway
children inside a disposable process tree.

---

## V218.8. No-regression: every closed repair preserved (R5)

| Closed surface | Status under v2.1.8 |
|---|---|
| **§V217.1 object-bound observation** (the record, `OBSERVE` O1–O9, the seven inconclusive triggers, the predicates, `bytes_sha256` binding) | carried **byte-for-byte**; untouched by this layer |
| **§V217.1.4 both revalidation barriers** (`BRANCH_ENTRY`, `DISPOSITION`, `R-a`/`R-b`, the same-rule requirement) | carried byte-for-byte |
| **§V217.1.5 A3 residual honesty** and §V217.1.6's mutation-cut table | carried byte-for-byte. **The reaper repair proves nothing about filesystem exclusion**; `T_RUNTIME.lock` still serializes contract actors and is still not a same-UID filesystem exclusion mechanism; no security boundary is invented here |
| **§V217.4 complete bound-language replacement** (ten loci, eighteen search terms, the retained-statement table, revised row 86, D1's true ground) | carried byte-for-byte. `B`'s unbounded loop is *consistent with* that replacement, which already withdrew every fixed-total-CLI claim; it reintroduces none |
| **§V216.2 `CLOSE_OWNED`** at every site including both lock closes, the errno classification, the never-retry rule, the fork-ownership rule | carried byte-for-byte; `B` simply defers its cleanup to whichever terminal it exits into |
| **`MALFORMED` physical-presence dominance** and §V216.1.2's rule ordering, §V216.1.3's sub-routing and cross-product | carried byte-for-byte |
| **The three branch bodies** `B-P`/`B-QM`/`B-QN` (note: unrelated to this layer's `B` state, which is a stage-M control label and touches no branch) | carried byte-for-byte |
| **K1 custody and accounting**: five constants, one-write/one-hash, no replenishment, §N2.3 P1–P7, §V214.2.4's reconciliation | carried byte-for-byte |
| **Death-before-unlink** (§V216.3, §V217.3.1's table) | carried, and **strengthened**: the only unproved removal remains `SPAWNING.json`, and `B` does not even perform that |
| **§V216.5** `boot_w` EOF provenance and the eight-end audit; **§V216.4.1**'s narrowed pipe-only invariant | carried byte-for-byte |
| **Bootstrap, forks, gates, GC, watchdog, singleton preflight** | carried; the only additions are step `c3n` and the stage-M automaton |
| **A3 / B1 / C1 / D1 / K1** | no cell reopened, weakened, or reinterpreted. A3 gains one new *named* residual (the zombie of §V218.4.5) and one *narrowed* one (`B` replaces v2.1.7's every-`T3`-case exposure). B1: no journal, ack, frontier, prefix, GC, or classification rule changes. C1: the watchdog remains a witness/freezer holding no lock or capability. D1: no idle exit; its ground remains "no supervisor waits on `SPAWN.lock`". K1: unchanged |
| **Generic harness v2/v2.1/v2.2/v2.3/v2.3.1** and **batch settlement v1/v1.1/v1.1.1** (§J1–§J3, §D1 head/cache completion, §D2 inline `meter_evidence`) | referenced unchanged; §V218.1.4 shows the allowlist delta **honours** rather than contradicts the signed harness's own amendment clause |
| **Nine signed events, E1/E2/E3, invalidity dominance, Q/C boundary, T** | unchanged; every fact added here is control-plane, T-development-only, and non-citable |

---

## V218.9. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The CLI normalizes its
child-reaping state with one named `signal` call at one named step before every
first fork, verifies it against two named kernel bitmask fields, and refuses to
fork on any of three named failure results (§V218.2). Ownership of `pid_mid` is
a three-valued label with exactly two transitions, each set at exactly one
place, gating every `os.kill` by a single precondition (§V218.3.1). Identity
observation is a ten-row total table over the full product of stat result,
capture state, `ppid` comparison, and ownership (§V218.3.4). `waitpid` has four
results with `PROVED_DEAD` sourced from exactly one of them (§V218.3.3).
Stage M is a five-step automaton with three pairwise-disjoint, exhaustive
successors, one of which explicitly does not return (§V218.4.2). The causal
proof cites `m0`, `rel1`, and the fork-shared lock, and cites `m5`/`rel2`
nowhere (§V218.5). No clause resolves to "as reviewed", "as appropriate", or
implementer discretion.

**Compatibility classification.** An engineering/control amendment surface over
the signed harness composite, containing no protocol amendment except §W6.5's
explicitly named supersession of harness §5a's physical at-or-before-deadline
sentence. The signed generic-harness contract and the signed batch-settlement
amendment are referenced unchanged. No signed archival set, event, runtime
schema, root, constant, resource value, T band, or Q/C boundary moves.
**The import-allowlist delta is exactly one module, `signal` (§V218.1); every
prior "zero delta" statement in this chain is superseded and is enumerated in
§V218.1.4.** That delta is the reason a fresh X-line and Y-line review of these
exact bytes is mandatory.

**No author cell is reopened.** A3 is untouched and gains honesty:
§V218.4.5 names one new residual that this layer's own repair creates (the
unreaped zombie) and narrows the stopped-middle exposure to a conjunction of
same-UID interference and a host fault. B1, C1, D1, and K1 are untouched.
**No new author-choice token is proposed, and none was found to be
unavoidable**; both independent v2.1.7 reviews independently reached the same
conclusion, and the allowlist delta is an engineering artifact rather than a
scientific choice.

**Negative space.** This correction creates nothing executable and authorizes
no implementation, commit, host change, process, supervisor, controller,
worker, watchdog, adapter, middle child, endpoint, pipe, FIFO, journal
instance, tombstone, spawn record, lease, capability, operation, output bound,
framed transport, result manifest, quarantine record, promoted object, capacity
artifact, custody disposition, author decision file, freeze witness, fallback
witness, replacement-freeze record, entropy, E1/E2/E3 spend, world, learner,
candidate, Q attempt, Q/C object, datum, outcome, Proof, or claim movement. It
edits no code — in particular it does **not** add `"signal"` to
`ALLOWED_ABSOLUTE_IMPORTS` in `src/philosophia/officina/verification.py`; it
only specifies that future one-string amendment and its containment. It
predicts no qualification and no C1–C6 outcome. Process invalidity, resource
exhaustion, missing evidence, and the `B` blocked state remain infrastructure
facts and are nowhere treated as scientific evidence. No example in this
document was written to any file.

---

## V218.10. The two fresh bounded confirmation questions

Both lines must recompute the digest of **this file** and of every governing
hash above, and must treat this author's own closure
(`reviews/opus5_officina_supervisor_control_channel_v2_1_8_closure.md`) as an
untrusted self-assessment.

### For the X line (Claude Opus 4.8, clean context, adversarial Linux/CPython process semantics)

> Recompute the SHA-256 of
> `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md`
> and of every file in its governing-hash block, and read the complete v2 →
> v2.1.8 chain plus **both** v2.1.7 REVISE reviews. Then answer one question:
>
> **Does v2.1.8 mechanically establish, before every first fork, the exact
> process state its stage-M kill/reap machinery depends on — and does it name
> the resulting engineering delta truthfully?**
>
> Attack, at minimum: (1) that one `signal.signal(SIGCHLD, SIG_DFL)` really
> issues a `sigaction` on the pinned CPython (≥ 3.11) whose `sa_flags` contains
> neither `SA_NOCLDWAIT` nor `SA_NOCLDSTOP`, and that Linux's auto-reap
> condition is exactly `SIG_IGN ∨ SA_NOCLDWAIT`; (2) whether the
> `/proc/self/status` `SigIgn`/`SigCgt` readback, plus the honestly stated
> `SA_NOCLDWAIT` gap, is a sufficient verification given the three
> `CONTRADICTED` detectors that back it up; (3) whether the fork-ownership
> PID-reuse proof of §V218.3.2 holds at every instruction boundary between
> `STAT_OBSERVE` and `os.kill`, including for a stopped child and an unreaped
> zombie; (4) whether `IDENTITY_SAFE`'s replacement (§V218.3.4) is genuinely
> total over its stated product, and whether your own X217-m1 `ppid`-mismatch
> case is now closed in the *safe* direction; (5) whether **`T3` is truly gone**
> — that no route returns, releases the lock, removes `SPAWNING.json`, or
> discards every handle while `pid_mid` may be live and unreaped — and whether
> the non-returning `B` state is total, correctly refuses to free the singleton,
> and states its non-termination cases honestly rather than concealing them;
> (6) whether the allowlist delta is contained exactly as §V218.1.2 claims, and
> whether §W2.6's and §W6.4's carried properties survive losing their old
> justification; (7) whether the new unreaped-zombie residual is correctly and
> completely scoped; (8) whether any v2.1.7 closure — especially §V217.1's
> selector, both barriers, and §V217.4's bound-language replacement — regressed.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_X` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_8`. Static review only: no code, test, probe,
> or Officina process may run; no runtime or scientific artifact may be created;
> no existing file may be modified; create exactly one review file. Do not
> authorize `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`,
> implementation, T activation, entropy, spend, or any later gate.

### For the Y line (GPT-5.6 Sol, clean context, adversarial contract totality and forward progress)

> Recompute the SHA-256 of
> `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md`
> and of every file in its governing-hash block, and read the complete v2 →
> v2.1.8 chain plus **both** v2.1.7 REVISE reviews. Then answer one question:
>
> **Is every stage-M continuation now total, truthful, and free of any route
> that abandons a possibly live untracked child — and is the corrected causal
> proof the governing one?**
>
> Attack, at minimum: (1) your C217-1 counterexample end to end — inherit
> `SIGCHLD = SIG_IGN` **and** inherit `SA_NOCLDWAIT` through a fork-without-exec
> launcher, and determine whether §V218.2 defeats both, whether the three
> `CONTRADICTED` detectors catch a residual failure, and whether any surviving
> path can signal a recycled PID; (2) whether `ECHILD ⇒ INCONCLUSIVE` is applied
> everywhere, with **no** prose, table, or test row still asserting
> `ECHILD ⇒ PROVED_DEAD` or a zombie pin outside §V218.3.2's mechanically
> established scope; (3) your M217-1 case — every `/proc` observation fails,
> `waitpid` is inconclusive, and the middle is stopped at `m0` — and whether the
> automaton now terminates and reaps, whether `B` is an acceptable exact
> continuation given R3's two permitted options, and whether its
> non-termination cases are named rather than concealed; (4) whether `T1`/`T2`/`B`
> are pairwise disjoint and exhaustive, whether `T2`'s `SPAWNING_MIDDLE.json` is
> truthfully constructible in every case that selects it, and whether the
> **existing** §U6.1/§U2.5 resolver is total for it without any new tier, record,
> or operator step; (5) your m217-1 case — whether the `m0`/`rel1`/fork-shared-lock
> trace of §V218.5.1 is now the governing one and whether **any** stage-M
> sentence, table, test, or closure still cites `m5` or `rel2`; (6) whether the
> named `signal` allowlist delta is contained, whether it conflicts with the
> signed harness contract's own import-discipline clause, and whether the new
> zombie residual is fully scoped; (7) whether every v2.1.7 closure you
> confirmed — §V217.1 and §V217.4 in particular — is carried without regression,
> and whether the reaper repair is anywhere mistaken for a filesystem-exclusion
> proof.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_Y` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_8`. Static review only: no code, test, probe,
> or Officina process may run; no runtime or scientific artifact may be created;
> no existing file may be modified; create exactly one review file. Do not
> authorize `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`,
> implementation, T activation, entropy, spend, or any later gate.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. Its only next authorization step is a
**fresh independent X-line review and a fresh independent Y-line review of the
v2.1.8 bytes**; both lines revised v2.1.7, no earlier confirmation of any
version carries across, and the `signal` allowlist delta of §V218.1 makes an
independent review of these exact bytes strictly mandatory.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
