# Officina supervisor and control-channel amendment — v2.1.10.1 pre-review correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.
Layer prefix: **§V21101**.

> ## WHAT THIS LAYER REPAIRS, STATED FIRST
>
> v2.1.10 contains seven literal or architectural defects that the author found
> before requesting independent review. **No independent review of v2.1.10 was
> requested and none is claimed.** This layer corrects them; v2.1.10 is not
> edited and stands as immutable evidence.
>
> **B1** — v2.1.10 said the bootstrap imports *four* modules with `fcntl`
> excluded **and** *five* modules with `fcntl` included. Not single-valued.
> **Resolved:** exactly **`{os, sys, _signal, time, fcntl}`**, using the
> **built-in `_signal`** module rather than the Python `signal` wrapper — which
> removes `signal → functools → _thread` from the closure and makes the signal
> primitives genuine built-ins. v2.1.10's single universal identity predicate
> would have **rejected the genuine `signal.signal`**; it is replaced by an
> exact per-primitive table.
>
> **B2** — `readlink("/proc/self/fd/<n>")` returns a *pathname*; passing it to
> the interpreter re-resolves it. **The "same inode" claim is deleted.** The
> source and the interpreter are now object-bound: both stay open on pinned
> descriptors and are named `/proc/self/fd/<N>`, which the kernel resolves to
> the held object, not to a re-walked path.
>
> **B3** — `subprocess.Popen` has no general fd-remapping argument, so
> v2.1.10's "the caller `dup2()`s onto 3…6 in the pre-exec child" with
> `preexec_fn=None` was impossible, and `cwd="/"` is not expressible by the
> chosen API. **Replaced** by `os.posix_spawn` with an exact, ordered
> `file_actions` sequence, and by a locally bound `_chdir("/")` inside the
> bootstrap.
>
> **B4** — the launcher runs in a caller declared to have "ANY runtime state".
> **The required property is now stated as a disjunction and discharged where it
> can be**: the caller either constructs the exact isolated process through
> genuine primitives, **or no authorized bootstrap comes into existence**. The
> launcher's own identity checks are explicitly **diagnostic, not the safety
> mechanism**; safety is the bootstrap's own preflight, executed where the
> caller cannot reach.
>
> **B5** — "a hostile caller can make the bootstrap exec an arbitrary
> supervisor" is **withdrawn as an accepted route.** fd 6 and fd 7 are bound to
> each other by `(st_dev, st_ino)`, the role image is opened `O_NOFOLLOW` under
> fd 6 and re-verified by the role's own entry, and the byte-provenance division
> between run-time object identity and the signed manifest is stated exactly.
>
> **B6** — the supervisor's own `Popen`/`waitpid`/`kill`/`killpg`/watchdog-fork
> defect is **no longer deferred**. Route 2 is unavailable by inspection, so
> **route 1 is taken**: all process authority moves behind one clean
> process-control instance, and **the supervisor is given handles, never PIDs**,
> which removes PID-reuse sensitivity from it structurally.
>
> **B7** — every totality detail is re-derived against the corrected topology,
> and every "the caller may kill or misreport" case is routed through the
> **signed invalidity / fail-closed semantics**, never through "its own user".
>
> **Zero new resource values, timeouts, K1 ceilings, E1/E2/E3 values, T bands,
> scientific estimands, or author-choice cells.**

**Authorship.** Written by **Claude Code Opus 5 acting only as the specification
author**, because Claude Code Fable 5 was unavailable. The same author line
wrote v2.1 through v2.1.10. This is **not** an X-line or Y-line review of its
own bytes and must never be counted as one
(`reviews/officina_supervisor_v2_1_authorship_note.md`). Every author closure in
the chain, including this layer's, is an untrusted self-assessment.

**Review state.** v2.1.9 was revised by **both** independent lines (Y: C219-1,
M219-1, M219-2, m219-1; X: F1, F2). v2.1.10 answered those findings and **has
received no independent review**. This layer is a **pre-review author
correction** over v2.1.10. The bytes that must eventually be reviewed are
v2.1.10 **as corrected by this layer**; both a fresh X-line and a fresh Y-line
review are required, and no earlier confirmation, conditional or otherwise,
survives or transfers.

This is a **bounded correction layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md`,
which layers over v2.1.9 … v2 — all twelve preserved unedited as evidence.
**Everything not named in the §V21101.0 replacement index carries forward
verbatim**, including v2.1.10's architectural core: the constructed clean
runtime, the isolated new root, the process-boundary reaping proof, the closure
theorem's shape, the `STRUCTURAL_VIOLATION` classifier, the non-circular
`B-CONTRADICTED` exclusion, and the pinned platform.

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

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
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
4cc19fc914f5908f069cb7b8aa09297dece424943f8a876974105e575d09c47d  reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
f49dcbf9900c0d3fe2e45abbc28193d8b4b4c20c8640dfab508aff15dcc90984  reviews/opus_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
1970986325c75e8f4c2dd72e57e0640ae88b165f3556920e85cae7efc8cc93be  reviews/sol_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
746bcf3694a67d04eacaec66190cf68cb92ac0070ec3d8cb24abf6eb22efee0c  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

`verification.py` is recorded **unamended**;
`scripts/officina_process_control_bootstrap.py` **does not exist**. Neither is
created or edited here.

---

## V21101.0. Literal v2.1.10 → v2.1.10.1 replacement index

**Nothing else moves.** Everything in v2.1.10 and every layer it carries — in
particular §V2110.2.2's process tree *shape*, §V2110.2.3's process-boundary
reaping proof, §V2110.3.3's operation inventory, §V2110.3.5–§V2110.3.8,
§V2110.4 in full, §V2110.6 in full, §V219.3, §V218.2.2, §V218.3, §V218.4.1–.4,
§V218.5, §V217.1, §V217.4, and the entire carried chain — carries forward
verbatim except at the rows below.

| # | v2.1.10 (or carried) locus, quoted | Action |
|---|---|---|
| 1 | Engineering-constants sentence "Modules the bootstrap imports: **`os`, `sys`, `signal`, `time` — and nothing else.** `json`, `hashlib`, `re`, `pathlib`, `enum`, `dataclasses`, `subprocess`, `fcntl`… are all **excluded from the bootstrap**" | **replaced** by §V21101.1.1 |
| 2 | §V2110.3.2's paragraph "`fcntl` is required for `flock`. It is **not** imported by the bootstrap: … so the bootstrap **does** import `fcntl` as a fifth module. Its permitted set is therefore exactly **`{os, sys, signal, time, fcntl}`**" | **replaced** by §V21101.1.1 — the contradiction is resolved in favour of a five-module set that uses `_signal`, not `signal` |
| 3 | §V2110.3.2's module table row for `signal` and the whole **"The `_thread` note"** block | **replaced** by §V21101.1.2 — `_signal` is a built-in with an empty Python closure, so `functools`/`_thread` leave the closure entirely |
| 4 | §V2110.3.4's import-derived binding lines `_sigsignal = signal.signal`, `_getsignal = signal.getsignal`, `_SIGCHLD = signal.SIGCHLD`, `_SIG_DFL = signal.SIG_DFL` | **replaced** by §V21101.1.3 (`_signal.` sources) |
| 5 | §V2110.3.4's **Identity validation** block ("for every bound CALLABLE above: require `type(f).__name__ == \"builtin_function_or_method\"` …") | **replaced** by §V21101.1.4 — one universal predicate is invalid; an exact per-primitive table replaces it |
| 6 | §V2110.2.1's argv line "`argv[0] = <the caller's own sys.executable>            # absolute, kernel-supplied`" | **replaced** by §V21101.2.3 — `sys.executable` is a mutable string and is **not** kernel-supplied; the interpreter is object-bound instead |
| 7 | §V2110.2.1's argv line 5 clause "resolved by the caller with `os.open(..., O_RDONLY\|O_NOFOLLOW\|O_CLOEXEC)` and `os.readlink(\"/proc/self/fd/<n>\")`, **so the exec target is the SAME inode the caller opened**, not a name re-resolved by `execve`" | **deleted as false**, replaced by §V21101.2.1–§V21101.2.2 |
| 8 | §V2110.2.1's launch block lines `cwd = "/"`, `close_fds = True`, `pass_fds = …`, `preexec_fn = None`, and its `shell=False` line | **replaced** by §V21101.3 (a `posix_spawn` launch with an exact `file_actions` sequence); `cwd` moves to §V21101.3.6 |
| 9 | §V2110.2.6's sentence "The caller `dup2()`s its ends onto exactly these numbers **in the pre-exec child** and clears `O_CLOEXEC` on exactly these four. Every other descriptor is closed by `close_fds=True`." | **deleted as impossible under the stated API**, replaced by §V21101.3.3 |
| 10 | §V2110.2.6's four-entry descriptor block and D-4's four constants | **replaced** by §V21101.3.2's six-entry table (`T_PCB_FD_SOURCE = 7`, `T_PCB_FD_INTERPRETER = 8` added) and §V21101.6.4's role-side table |
| 11 | §V2110.2.2's edge row "`[0]→[1]` … `execve` from a `fork`/`posix_spawn` inside the caller" | **replaced** by §V21101.3.1 (`posix_spawn` only; no `fork`, no `Popen`, no `preexec_fn`) |
| 12 | §V2110.2.7's `g0''` block clause "the interpreter is the bootstrap's own `sys.executable` (a runtime fact, never a request field); the package root is `os.readlink(\"/proc/self/fd/6\")`" | **replaced** by §V21101.5.3 (fd-bound interpreter and fd-bound package root) |
| 13 | §V2110.2.4's paragraph "**What a hostile caller can still do**, stated honestly: … and it can misreport the reply to its own user." | **replaced** by §V21101.7.5 — every such case is routed through the signed invalidity semantics, not through "its own user" |
| 14 | §V2110.2.7's **Scope note** ("This correction therefore does not claim to have repaired supervisor-side reaping") and §V2110.11 weakest-point 4 | **replaced** by §V21101.6 — the defect is repaired, not scoped away |
| 15 | §V2110.11 weakest-point 3 ("The bootstrap cannot attest the reviewed-ness of the role image it `execve`s … A hostile caller can therefore make the bootstrap launch a supervisor of the caller's choosing") | **replaced** by §V21101.5 |
| 16 | §V2110.3.9's CHANGE 2 map entry `"scripts/officina_process_control_bootstrap.py": frozenset({"os", "sys", "signal", "time", "fcntl"})` and CHANGE 3's `S-1`, `S-5`, `S-7`, `S-9` | **replaced** by §V21101.8.1 (`_signal`; the per-primitive attribute sets; the widened forbidden-symbol list) |
| 17 | §V2110.3.8's premise-5 phrase "the five-module closure of §V2110.3.2" | **retained**, with the closure now being the one of §V21101.1.1 |
| 18 | §V2110.7.4 test rows **273**, **276**, **277**, **279**, **293**, **297** | **replaced** by §V21101.8.2; rows 313–352 added |
| 19 | §V2110.10's edit-surface table | **extended** by §V21101.9.3 |
| 20 | §V2110.9's supersession table | **extended** by §V21101.10 rows 28–36 |

---

## V21101.1. B1 — one exact import inventory and a valid identity rule

### V21101.1.1 The single-valued import inventory

> **The bootstrap root imports exactly five modules, and no others, anywhere in
> the file, at module scope, unaliased, with no conditional, deferred, or
> dynamic import:**
>
> ```text
> import os
> import sys
> import _signal
> import time
> import fcntl
> ```
>
> **`{os, sys, _signal, time, fcntl}`** is the complete and only permitted set.
> Every earlier sentence in this chain that gives a different set — v2.1.10's
> "four modules … `fcntl` … excluded", v2.1.10's "`{os, sys, signal, time,
> fcntl}`", and every v2.1.8/v2.1.9 sentence naming `signal` as the bootstrap's
> importer — is **superseded** (§V21101.10 rows 28–29). `json`, `hashlib`, `re`,
> `pathlib`, `enum`, `dataclasses`, `subprocess`, `signal` (the Python wrapper),
> `select`, `selectors`, `ctypes`, `socket`, `threading`, `_thread`,
> `multiprocessing`, `concurrent`, `asyncio`, `atexit`, and `gc` are all
> **excluded from the bootstrap**, and the last nine remain outside every
> allowlist.

`fcntl` is in the set because `flock` is required by the carried `c1`
acquisition. That was v2.1.10's actual intent; only its two sentences
contradicted each other.

### V21101.1.2 Why `_signal` rather than `signal`, and the resulting closure

`signal` is a **pure-Python wrapper** over the built-in `_signal`. It imports
`enum` and `functools`, and `functools` does `from _thread import RLock`. Using
`_signal` directly deletes that whole sub-closure. It also makes the two signal
primitives **genuine built-ins**, which is what makes a uniform identity rule
expressible at all (§V21101.1.4).

| Module | Kind | Transitive Python import closure | Starts a task? | Registers an at-fork callback? | Installs a handler/hook? |
|---|---|---|---|---|---|
| `os` | Python wrapper over built-in `posix` | `sys`, `abc` (→`_abc`), `stat` (→`_stat`), `_collections_abc`, `posixpath`, `genericpath` | no | no — it *defines* `register_at_fork`, never calls it | no |
| `sys` | built-in | none | no | no | no |
| **`_signal`** | **built-in** | **none** | no | no | no; it *defines* `signal()` but installs nothing at import |
| `time` | built-in | none | no | no | no |
| `fcntl` | built-in | none | no | no | no |

> **`_thread`, `functools`, `enum`, `reprlib`, `collections`, `operator`, and
> `types` are no longer in the closure at all.** v2.1.10's "`_thread` note" and
> the weakest-point that accompanied it are therefore **withdrawn**, not merely
> mitigated. The only remaining pure-Python modules in the closure are the six
> pulled in by `os`, none of which imports any threading, subprocess, signal, or
> hook facility.

**Behavioural consequences of using `_signal`, pinned:** `_signal.SIG_DFL` and
`_signal.SIGCHLD` are plain `int`s, not `IntEnum` members; `_signal.getsignal`
returns the module's own `SIG_DFL` object (an `int`) for a default disposition,
`SIG_IGN` (an `int`) for an ignored one, or a callable. The carried `V-9`
corroboration therefore becomes `type(_getsignal(_SIGCHLD)) is int and
_getsignal(_SIGCHLD) == _SIG_DFL`, which is a **stronger** check than the
enum-identity form it replaces, because it also excludes a callable.

### V21101.1.3 The corrected binding block

§V2110.3.4's block is carried with exactly four lines changed and two added:

```text
… every `os.`, `fcntl.`, `time.` and `sys.` line of §V2110.3.4, unchanged …
_sigsignal   = _signal.signal        _getsignal = _signal.getsignal
_SIGCHLD     = _signal.SIGCHLD       _SIG_DFL   = _signal.SIG_DFL
_chdir       = os.chdir              _dup       = os.dup            # §V21101.3
```

### V21101.1.4 The per-primitive identity table (replacing the invalid universal rule)

v2.1.10 required, of **every** bound callable, that
`type(f).__name__ == "builtin_function_or_method"`. Under v2.1.10's own
`signal`-wrapper inventory that predicate **rejects the genuine
`signal.signal`**, which is a Python function. The rule is replaced by an exact
table with three kinds and no universal clause.

**Type anchor.** `_BUILTIN = type(len)` is captured once, before any other
statement, and every "built-in callable" row compares `type(f) is _BUILTIN` — an
**object-identity** test on the type, never a name comparison. `len` is used
only for this and is never called.

| Bound name(s) | Source module | Kind | `type(x) is` | `__self__.__name__` | `__qualname__` | Value requirement |
|---|---|---|---|---|---|---|
| `_fork`, `_waitpid`, `_kill`, `_killpg`, `_getpid`, `_getppid`, `_open`, `_read`, `_write`, `_close`, `_fstat`, `_stat`, `_listdir`, `_unlink`, `_fsync`, `_rename`, `_pipe2`, `_dup2`, `_dup`, `_execve`, `_setsid`, `_exit_`, `_uname`, `_chdir`, `_get_inheritable` | `os` (re-exported from built-in `posix`) | built-in callable | `_BUILTIN` | `"posix"` | the exact bare name (`"fork"`, `"waitpid"`, …; `_exit_` expects `"_exit"`) | — |
| `_flock` | `fcntl` | built-in callable | `_BUILTIN` | `"fcntl"` | `"flock"` | — |
| `_clock` | `time` | built-in callable | `_BUILTIN` | `"time"` | `"clock_gettime_ns"` | — |
| `_sigsignal`, `_getsignal` | `_signal` | built-in callable | `_BUILTIN` | `"_signal"` | `"signal"` / `"getsignal"` | — |
| `_SIGCHLD` | `_signal` | integer constant | `int` | — | — | `== 17` (pinned platform, §V2110.6) |
| `_SIG_DFL` | `_signal` | integer constant | `int` | — | — | `== 0` |
| `_WNOHANG`, `_CLOCK_MONOTONIC`, `_O_RDONLY`, `_O_DIRECTORY`, `_O_NOFOLLOW`, `_O_CLOEXEC`, `_O_NONBLOCK`, `_O_WRONLY`, `_O_CREAT`, `_O_EXCL`, `_LOCK_EX`, `_LOCK_NB` | `os` / `fcntl` / `time` | integer constants | `int` | — | — | pairwise distinct where the carried text requires it; each equal to the value recorded in the implementation review for the pinned build |
| `_devnull` | `os` | string constant | `str` | — | — | `== "/dev/null"` |
| `_flags`, `_version_info`, `_implementation` | `sys` | value objects | — | — | — | consumed **only** by the `P-b` field comparisons of §V2110.3.1; no identity claim is made about the objects themselves, because `P-b` compares the fields, not the container |

```text
IDENTITY_CHECK():
  for each row above, in the table's order, apply exactly that row's
  requirements to the bound name.
  ANY failure ⇒ PRIMITIVE_NOT_GENUINE ⇒ fail-closed refusal, NO fork,
                NO lock acquisition, NO record installed.
  No exception may escape; an escaping exception takes the same route.
```

**Why every genuine binding passes.** All twenty-five `os` names in row 1 are
re-exported from the built-in `posix` module, so each is a
`builtin_function_or_method` whose `__self__` is the `posix` module object;
`fcntl.flock`, `time.clock_gettime_ns`, `_signal.signal` and `_signal.getsignal`
are built-ins of their own built-in modules. **No pure-Python wrapper remains in
the bound set**, which is precisely the property `_signal` buys.

**Why every stated substitution fails, without trusting mutable caller state.**
A Python-level replacement of any bound name is a plain `function`, whose type
is not `_BUILTIN`. A `functools.partial`, a bound method, a class instance with
`__call__`, or a `types.MethodType` likewise fails the type test. A built-in
stolen from another module fails the `__self__.__name__` test. A built-in of the
right module under the wrong name fails `__qualname__`. A substituted integer or
string fails its value requirement. And — decisively — **none of these can have
happened**, because §V2110.3.8's premise 1 (no user code ran before the module
body, read back from `sys.flags`) holds in the bootstrap; the table is a
**positive corroboration inside an already-clean process**, not a defence
against a contaminated one. That distinction is stated so no reader mistakes it
for a sandbox.

---

## V21101.2. B2 — object-bound bootstrap source and interpreter

### V21101.2.1 The false claim, deleted

> **Deleted:** "resolved by the caller with `os.open(..., O_RDONLY|O_NOFOLLOW|O_CLOEXEC)`
> and `os.readlink("/proc/self/fd/<n>")`, **so the exec target is the SAME inode
> the caller opened**, not a name re-resolved by `execve`."
>
> `readlink` on `/proc/self/fd/<n>` returns a **pathname string**. Handing that
> string to the interpreter makes the kernel walk the path again at open time,
> so the file may be unlinked, renamed, or replaced between the caller's
> `fstat` and the interpreter's `open`. The claim was false and is withdrawn in
> full. No sentence in this chain may again derive object identity from a
> `readlink` result.

### V21101.2.2 The real fd-bound mechanism

```text
CALLER SIDE
  the bootstrap source is opened once:
      src_fd := _open(<deployment's path to the bootstrap source>,
                      _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC)
  it is NEVER readlink'ed, and its pathname is never used again. It is mapped by
  POSIX_SPAWN_DUP2 onto T_PCB_FD_SOURCE (§V21101.3.3), which clears close-on-exec
  on the destination, so it is open in the spawned process.

INTERPRETER ARGUMENT
  the script argument handed to the interpreter is the LITERAL byte string
      "/proc/self/fd/7"                       (7 == T_PCB_FD_SOURCE)
  and never a readlink result. On Linux, opening /proc/self/fd/<N> for a regular
  file re-opens the OBJECT the descriptor refers to; it is not a re-walk of the
  original name. The interpreter therefore executes the same file object the
  caller opened, even if that name has since been unlinked, renamed, or replaced.

BOOTSTRAP SIDE — new preflight step P-s, placed between P-b and P-c
  P-s1. st := _fstat(T_PCB_FD_SOURCE)
          any OSError                          ⇒ SOURCE_FD_UNUSABLE
  P-s2. require S_ISREG(st.st_mode)            ⇒ else SOURCE_NOT_REGULAR
  P-s3. require st.st_uid equals _getuid()'s value and (st.st_mode & 0o022) == 0
          — not writable by group or other      ⇒ else SOURCE_WRITABLE
  P-s4. record (st.st_dev, st.st_ino) as SOURCE_IDENTITY, used by §V21101.5.2
  P-s5. require the descriptor's file-status access mode is read-only, by
        _fcntl-free means: a _read of zero bytes must succeed and a _write must
        raise OSError                          ⇒ else SOURCE_NOT_READONLY
```

`st_nlink` is deliberately **not** constrained: a hardlink to the reviewed file
is the *same inode* and is harmless; the discriminator is `(st_dev, st_ino)`
equality, established in §V21101.5.2, not the link count.

### V21101.2.3 The interpreter is object-bound too

> **Deleted:** "`argv[0] = <the caller's own sys.executable>  # absolute,
> kernel-supplied`". `sys.executable` is an ordinary mutable `str` attribute of
> a mutable module; it is **not** kernel-supplied and this chain must never
> again describe it that way.

```text
CALLER SIDE
  interp_fd := _open(<deployment's path to the interpreter>,
                     _O_RDONLY | _O_CLOEXEC)
  mapped by POSIX_SPAWN_DUP2 onto T_PCB_FD_INTERPRETER (8).

SPAWN TARGET
  the posix_spawn `path` argument is the LITERAL byte string "/proc/self/fd/8".
  File actions run in the child before the exec, so fd 8 exists when the kernel
  resolves that name; executing /proc/self/fd/<N> is Linux's supported
  fexecve equivalent and binds the exec to the held object.

BOOTSTRAP SIDE — P-s6
  require _fstat(T_PCB_FD_INTERPRETER) is a regular file, not group- or
  other-writable, and its (st_dev, st_ino) is recorded as INTERPRETER_IDENTITY;
  the SAME descriptor, still open and non-close-on-exec, is what every later
  exec in this process tree uses (§V21101.5.3). sys.executable is recorded as a
  diagnostic string and is used for NOTHING.
```

**The narrower trust premise, stated exactly.** Object-binding the interpreter
proves that every process in the tree executes **the same interpreter object**
the deployment opened. It does **not** prove that object is a reviewed CPython
build; that remains the pinned-identity check of `P-b` plus the deployment's
integrity, exactly as §V2110.11 weakest-point 1 already states and this layer
does not weaken.

### V21101.2.4 Unlink, rename, hardlink, symlink, and every spawn cut

| Event | Effect on the exec target | Contract behaviour |
|---|---|---|
| source unlinked after the caller's `open`, before the spawn | none — the inode is held by `src_fd` | proceeds; `P-s` sees the same inode |
| source renamed | none | proceeds |
| source replaced by a new file at the same name | none — `/proc/self/fd/7` still names the **old** inode | proceeds on the reviewed object; §V21101.5.2's cross-check then **fails**, because `openat(fd 6, canonical)` now yields the new inode ⇒ `ROOT_SOURCE_MISMATCH` ⇒ refusal before any authority |
| the name was a symlink at `open` time | `O_NOFOLLOW` makes the caller's `open` fail with `ELOOP` ⇒ no spawn | no bootstrap comes into existence |
| a symlink is installed at the name afterwards | irrelevant; the fd is bound | proceeds |
| a hardlink to the reviewed inode is used | same inode ⇒ `(st_dev, st_ino)` equal | proceeds; this is not an attack |
| source truncated to zero after `open` | the interpreter executes an empty file ⇒ it exits 0 having done nothing; **no lock, no record, no fork, no reply** | the caller reads EOF without a reply line ⇒ §V21101.7.5's `NO_REPLY` route |
| source content rewritten in place after `open`, before the interpreter reads | the interpreter may execute mixed bytes; the file is required to be non-group/other-writable, so this requires the owning UID | the signed **A3 same-UID procedural residual**, unchanged and not claimed impossible; byte provenance is the manifest's job (§V21101.5.4) |
| `posix_spawn` fails (`ENOENT`, `EACCES`, `ENOMEM`, `EAGAIN`, any errno) | no child exists | the launcher refuses (§V21101.3.5); no authorized bootstrap comes into existence |
| the spawned interpreter cannot open `/proc/self/fd/7` (fd missing, `/proc` unmounted) | the interpreter exits non-zero with no reply | `NO_REPLY` route |
| the interpreter starts but `P-b` fails (wrong flags/version) | reply written, then exit; **no lock, no record, no fork** | ordinary refusal |

---

## V21101.3. B3 — the exact `posix_spawn` launcher

### V21101.3.1 The launch mechanism, single-valued

> **`os.posix_spawn` is the one and only launch mechanism.** No
> `subprocess.Popen`, no `subprocess` object of any kind, no `os.fork`, no
> `preexec_fn`, no shell, no `os.system`, no `os.exec*` in the caller. The
> caller performs **no fork**, so no Python at-fork callback of the caller can
> run on the launch path at all.

**Does `posix_spawn` invoke user Python at-fork callbacks?** Pinned answer:
**no.** CPython's `os.posix_spawn` calls libc `posix_spawn(3)` directly and does
not enter `PyOS_BeforeFork`/`PyOS_AfterFork_Parent`, unlike
`_posixsubprocess.fork_exec`, which enters them only when `preexec_fn` is used;
glibc implements `posix_spawn` with `clone(CLONE_VM|CLONE_VFORK)` and does not
run `pthread_atfork` handlers. **This is recorded as a reviewer-verifiable
platform fact, and the repair does not rest on it**: even if a parent-side
callback did run, it would run in the **contaminated caller**, which holds no
process authority and is not `pid_mid`'s parent (§V2110.2.3, carried), so
nothing about the bootstrap's custody would change. Both statements are made so
that no unsupported assumption carries the repair.

### V21101.3.2 The complete descriptor table

Six descriptors in the spawned bootstrap; **nothing else may be open**.

| Constant | # | Contents | Opened by the caller as | Checked at `P-f`/`P-s` |
|---|---|---|---|---|
| `T_PCB_FD_REQUEST_R` | 3 | request pipe, read end | `os.pipe2(0)` read end | `S_ISFIFO` |
| `T_PCB_FD_REPLY_W` | 4 | reply pipe, write end | `os.pipe2(0)` write end | `S_ISFIFO` |
| `T_PCB_FD_RUNTIME_ROOT` | 5 | runtime root directory | `_O_RDONLY\|_O_DIRECTORY\|_O_CLOEXEC` | `S_ISDIR` |
| `T_PCB_FD_PACKAGE_ROOT` | 6 | package/repository root directory | `_O_RDONLY\|_O_DIRECTORY\|_O_CLOEXEC` | `S_ISDIR` |
| `T_PCB_FD_SOURCE` | 7 | the bootstrap source file | `_O_RDONLY\|_O_NOFOLLOW\|_O_CLOEXEC` | `S_ISREG`, mode, `P-s1`–`P-s5` |
| `T_PCB_FD_INTERPRETER` | 8 | the interpreter binary | `_O_RDONLY\|_O_CLOEXEC` | `S_ISREG`, mode, `P-s6` |

`T_PCB_FD_SOURCE` and `T_PCB_FD_INTERPRETER` are the **two added**
control-plane descriptor indices; with v2.1.10's four they make six, all of
exactly the §Z-declared `T_CTRL_FD_LOW`/`T_CTRL_FD_HIGH` class — control-plane
bounds, **not** scientific estimands, resource envelopes, E1/E2/E3 values, or K1
ceilings. `P-f` is amended to require `/proc/self/fd` to contain exactly
`{0,1,2,3,4,5,6,7,8}` plus the transient listing descriptor.

### V21101.3.3 The hoist, the file actions, and their exact ordering

The caller's six descriptors are at arbitrary numbers and may collide with the
targets `3…8`. The mapping is therefore two-phase and deterministic.

```text
PHASE 1 — HOIST (in the caller, before building file_actions)
  for each logical descriptor L in the fixed order
        (REQUEST_R, REPLY_W, RUNTIME_ROOT, PACKAGE_ROOT, SOURCE, INTERPRETER):
      h[L] := the caller's current descriptor for L
      while h[L] <= 8:
          n := _dup(h[L])          # returns the LOWEST free descriptor
          keep the previous h[L] OPEN for now (so _dup cannot return it again)
          h[L] := n
      # every intermediate opened during the loop is recorded in a close-list
  after all six are hoisted, close every recorded intermediate and every
  original descriptor whose number is <= 8.
  POSTCONDITION, asserted before continuing:
      h[L] >= 9 for all six, and the six values are pairwise distinct.
      Violation ⇒ LAUNCH_FD_HOIST_FAILED ⇒ NO SPAWN.

PHASE 2 — FILE ACTIONS, in exactly this order, twelve entries
  ( _POSIX_SPAWN_DUP2, h[REQUEST_R],    3 )
  ( _POSIX_SPAWN_DUP2, h[REPLY_W],      4 )
  ( _POSIX_SPAWN_DUP2, h[RUNTIME_ROOT], 5 )
  ( _POSIX_SPAWN_DUP2, h[PACKAGE_ROOT], 6 )
  ( _POSIX_SPAWN_DUP2, h[SOURCE],       7 )
  ( _POSIX_SPAWN_DUP2, h[INTERPRETER],  8 )
  ( _POSIX_SPAWN_CLOSE, h[REQUEST_R] )
  ( _POSIX_SPAWN_CLOSE, h[REPLY_W] )
  ( _POSIX_SPAWN_CLOSE, h[RUNTIME_ROOT] )
  ( _POSIX_SPAWN_CLOSE, h[PACKAGE_ROOT] )
  ( _POSIX_SPAWN_CLOSE, h[SOURCE] )
  ( _POSIX_SPAWN_CLOSE, h[INTERPRETER] )
```

**Why this ordering is collision-free and total.**

- Every **source** is `>= 9`; every **destination** is in `3…8`. No `DUP2`
  destination can therefore overwrite a descriptor that a later action still
  needs to read. Alias collisions are impossible by the postcondition of
  Phase 1 (pairwise distinct sources) and by the disjointness of the source and
  destination ranges.
- The six `CLOSE` actions run **after** all six `DUP2`s, so no source is closed
  before it is duplicated.
- `POSIX_SPAWN_DUP2` has `dup2(2)` semantics: it **clears close-on-exec on the
  destination**. That is why the caller opens every descriptor `O_CLOEXEC` and
  never calls `set_inheritable`: the six targets become inheritable exactly and
  only by the file actions, and every *other* caller descriptor that is
  `O_CLOEXEC` is closed by the exec itself.
- A caller descriptor that is **not** `O_CLOEXEC` leaks into the child. The
  contract does not try to prevent that in the caller; the **bootstrap refuses**
  at `P-f`, which is the B4 disjunction working as designed.
- If a `DUP2` source has been closed, or a destination is invalid, `posix_spawn`
  fails and the child exits with status 127 without executing anything;
  §V21101.3.5 routes it.

### V21101.3.4 The complete spawn call

```text
_posix_spawn(
    b"/proc/self/fd/8",                       # object-bound interpreter
    [ b"/proc/self/fd/8",                     # argv[0]
      b"-I", b"-S", b"-E", b"-P",
      b"/proc/self/fd/7" ],                   # object-bound script; no argv
                                              # parameters follow
    {},                                       # EXACTLY the empty environment
    file_actions = the twelve entries of §V21101.3.3,
    setsigmask   = (),                        # empty signal mask in the child
)
```

`setpgroup`, `resetids`, `setsid`, `scheduler`, and `setsigdef` are **not**
passed. `setsid` is omitted deliberately, so the bootstrap remains in the
caller's session and an operator's terminal `SIGINT` still reaches it (carried
from §V2110.3.6). `setsigdef` is omitted because the carried `N-1` derived-mask
reset is strictly stronger — it reads the kernel's own `SigCgt` and resets
exactly what is set. `setsigmask=()` is passed **and** the bootstrap
independently verifies `SigBlk == 0` at `P-g` (§V21101.7.1), the verification
being the load-bearing half.

**Constant validation, before the call:**

```text
require type(_POSIX_SPAWN_OPEN)  is int
    and type(_POSIX_SPAWN_CLOSE) is int
    and type(_POSIX_SPAWN_DUP2)  is int
require the three are pairwise distinct
require {_POSIX_SPAWN_OPEN, _POSIX_SPAWN_CLOSE, _POSIX_SPAWN_DUP2} == {0, 1, 2}
require each equals the value recorded in the implementation review for the
        pinned CPython 3.12.3 build
  any failure ⇒ LAUNCH_CONSTANT_MISMATCH ⇒ NO SPAWN
```

The set-equality form is used so the check is a real invariant rather than an
author assertion about which constant holds which value; the review record fixes
the assignment, and reviewers verify it against the pinned build.

### V21101.3.5 Return, failure, and cleanup

```text
r := the value returned by _posix_spawn
  type(r) is not int  ⇒ LAUNCH_STRUCTURAL ⇒ no authorized bootstrap
  r <= 0              ⇒ LAUNCH_STRUCTURAL ⇒ no authorized bootstrap
  OSError (any errno) ⇒ LAUNCH_SPAWN_FAILED ⇒ no authorized bootstrap
  any other BaseException ⇒ LAUNCH_STRUCTURAL ⇒ no authorized bootstrap
CLEANUP, on every path including success:
  close every hoisted descriptor and every original the caller still holds for
  the six logical roles; keep only the request WRITE end and the reply READ end.
  Then: write the request, close the request write end, read the reply to EOF,
  close the reply read end (§V2110.2.4's L-3/L-4, carried).
An interpreter that exits before writing a reply is the NO_REPLY route
(§V21101.7.5). The caller NEVER signals the spawned pid and NEVER lets a wait
result change a decision (carried, unchanged).
```

### V21101.3.6 `cwd` — the false launcher claim removed

> **Deleted:** the launch-block line `cwd = "/"`. `os.posix_spawn` exposes no
> `cwd` parameter and no `POSIX_SPAWN_CHDIR` file action in CPython, so the
> claim was unimplementable under the chosen API.

Replaced by a bootstrap-side step, executed immediately after `IDENTITY_CHECK()`
and before **any** name is opened:

```text
P-cwd.  _chdir("/")
          OSError ⇒ CHDIR_FAILED ⇒ fail-closed refusal, no fork
```

**Why the inherited cwd is irrelevant either way.** Every filesystem operation
the bootstrap performs is one of: a `dir_fd`-relative call against
`T_PCB_FD_RUNTIME_ROOT` or `T_PCB_FD_PACKAGE_ROOT`; an `fstat`/`read` on an
already-open descriptor; or an absolute `/proc/...` name. **No relative name is
ever resolved against the process cwd.** `_chdir("/")` is therefore defence in
depth — it additionally releases a possibly-unlinked inherited cwd reference and
makes any future relative resolution deterministic — and no safety property
depends on it.

---

## V21101.4. B4 — launcher authority, narrowed and mechanized

### V21101.4.1 The property, stated as a disjunction

> **LAUNCHER PROPERTY.** For any caller, in any runtime state:
> either (a) the caller constructs **exactly** the isolated process of
> §V21101.3.4 through genuine primitives, or (b) **no authorized bootstrap comes
> into existence**.
>
> This contract makes **no claim** that a hostile or arbitrarily monkeypatched
> caller must succeed in launching. It claims only that it cannot produce
> something that *is* an authorized bootstrap while not being one.

**Disjunct (b) is discharged by the bootstrap, not by the caller.** Whatever a
contaminated caller does, one of the following holds:

| Caller behaviour | Outcome |
|---|---|
| does not launch | no bootstrap; no lock, no record, no child |
| launches a **different program** | that program is not the reviewed bootstrap. It acquires no authority *from this contract*; it can do only what the caller could already do in its own process. No new authority is created. Its `SPAWN.lock` contention, if any, is the ordinary singleton discipline |
| launches the reviewed bootstrap with **weaker isolation flags** | `P-b` reads `sys.flags` back and refuses ⇒ no lock, no record, no fork |
| launches it with a **leaked or missing descriptor** | `P-f` refuses |
| launches it with a **non-empty environment** | `-I`/`-E` neutralize `PYTHON*`; anything else is unread by a five-module bootstrap; `P-b` still governs |
| launches it with a **substituted source or interpreter object** | `P-s` and §V21101.5.2's cross-check refuse |
| launches it with a **malformed request** | `P-h` refuses |
| launches it **correctly**, but is itself full of hooks, threads, monkeypatches | the bootstrap is clean by `execve` (§V2110.2.1, carried); the caller's contamination is confined to the caller |

### V21101.4.2 Launcher-side primitive binding, and what it is for

The caller binds and checks, before use, the same way and with the same table as
§V21101.1.4: `_posix_spawn`, `_open`, `_close`, `_pipe2`, `_dup`, `_fstat`,
`_read`, `_write`, and the `_O_*` / `_POSIX_SPAWN_*` / `_LOCK_*` constants. Any
failure is `LAUNCH_PRIMITIVE_NOT_GENUINE` and **no spawn occurs**. No mutable
high-level wrapper — `subprocess`, `shutil`, `pathlib`, `tempfile` — is used on
the launch path.

> **These checks are diagnostic, not the safety mechanism, and this is stated so
> that no reviewer mistakes them for a sandbox.** A caller that has rebound
> `builtins.len`, the `os` module object, or the checking code itself can defeat
> them; that is unavoidable and it is *why* the property in §V21101.4.1 is a
> disjunction. Their purpose is to convert an **honest but contaminated**
> caller's mis-launch into a loud pre-spawn refusal instead of a silent wrong
> launch. All load-bearing safety is in the bootstrap's own preflight, executed
> in a process the caller cannot reach.

### V21101.4.3 Contamination made harmless by `execve` vs. contamination that refuses

| Caller contamination | Disposition |
|---|---|
| `.pth` / `sitecustomize` / `usercustomize` code, audit hooks, import hooks, trace/profile functions, `__del__`s, retained callables, native extensions, helper threads, `os.register_at_fork` handlers | **made harmless by `execve`**: none of it exists in the spawned image, because `-I -S -E -P` prevent the new interpreter from running any of it and `execve` destroyed the old address space |
| a monkeypatched `os.posix_spawn`, `os.open`, `os.pipe2`, `os.dup`, or a rebound `_POSIX_SPAWN_*` constant | **refuses before spawn** if the launcher checks are themselves intact; otherwise it produces a process that is not the reviewed bootstrap, which the bootstrap's own preflight then does not certify — disjunct (b) |
| a caller helper thread doing `waitpid(-1, WNOHANG)` | harmless: it can reap only the bootstrap, never `pid_mid` (§V2110.2.3, carried). The reply pipe is the sole authoritative result |
| a caller that kills the bootstrap | a liveness event routed through §V21101.7.5's invalidity semantics; no record is removed without proof |
| a caller that lies in the request | constrained to the closed six-field grammar, which cannot name code, modules, callbacks, primitives, fds, timeouts, or out-of-set paths |

### V21101.4.4 The three counterexamples replayed against this launcher

| Counterexample | Result |
|---|---|
| **`.pth` / `sitecustomize`** installs anything at all | it runs in the **caller**. The spawned interpreter runs with `-S`, so `site` is never imported and no `.pth`, `sitecustomize`, or `usercustomize` executes there; `-I -E` remove user-site and every `PYTHON*` vector. `P-b` reads the flags back. **Nothing crosses.** |
| **`os.register_at_fork(after_in_parent=…)`** starting a wildcard reaper | the launch path performs **no fork**: `posix_spawn` is used, and by the pinned fact it runs no Python at-fork callback. Even if it did, the callback runs in the caller, whose helper can reap only the bootstrap. `pid_mid` is unreachable to it. |
| **monkeypatched `os.fork` / `os.waitpid`** in the caller | the caller never forks and never waits on `pid_mid`. Inside the bootstrap, `_fork` and `_waitpid` are bound at module scope from a clean import state and pass the §V21101.1.4 table; and a structurally impossible result at any W site is `STRUCTURAL_VIOLATION` (§V2110.4.1, carried), which is never death and forbids every further signal. |

---

## V21101.5. B5 — package and role provenance

### V21101.5.1 The withdrawn admission

> **Withdrawn:** "A hostile caller can therefore make the bootstrap launch a
> supervisor of the caller's choosing." That is no longer an accepted supported
> route.

### V21101.5.2 Binding fd 6 to fd 7 — the mutual object check

```text
P-p1. self_fd := _open("scripts/officina_process_control_bootstrap.py",
                       _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC,
                       dir_fd = T_PCB_FD_PACKAGE_ROOT)
         OSError ENOENT/ELOOP/EACCES/any ⇒ ROOT_CANONICAL_UNREADABLE ⇒ refuse
P-p2. require (_fstat(self_fd).st_dev, _fstat(self_fd).st_ino)
              == SOURCE_IDENTITY                       (from P-s4)
         mismatch ⇒ ROOT_SOURCE_MISMATCH ⇒ refuse, NO fork, NO lock
P-p3. close self_fd.
```

**What this establishes.** The directory named by fd 6 **contains, at the
canonical relative path, the very inode that is currently executing**.
Therefore a caller cannot combine the reviewed bootstrap with an unrelated
package root: the two must be consistent. `O_NOFOLLOW` on the final component
rejects a symlink swap at that name.

**What it does not establish, stated plainly.** A caller that supplies a *wholly
fabricated* tree — a fake bootstrap **and** a matching fake root — is not
running the reviewed bootstrap at all, so it holds none of this contract's
guarantees and creates no new authority (§V21101.4.1, disjunct (b)). Code
provenance of the launched file is established by the immutable-control verifier
and the deployment, per §V21101.5.4.

### V21101.5.3 The role image: object-bound resolution and a re-verified exec

```text
BOOTSTRAP SIDE, before the c4 fork, so a mismatch refuses before any authority:
 P-p4. role_fd := _open("src/philosophia/officina/generic_harness.py",
                        _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC,
                        dir_fd = T_PCB_FD_PACKAGE_ROOT)
          any OSError ⇒ ROLE_SOURCE_UNREADABLE ⇒ refuse
 P-p5. require S_ISREG and not group/other writable; record
       ROLE_IDENTITY := (st_dev, st_ino)
 P-p6. src_dir_fd := _open("src", _O_RDONLY|_O_DIRECTORY|_O_CLOEXEC,
                           dir_fd = T_PCB_FD_PACKAGE_ROOT)
          any OSError ⇒ ROLE_PATH_UNREADABLE ⇒ refuse

GRANDCHILD SIDE, at g0' (replacing §V2110.2.7's g0'' env/interpreter clauses):
   dup2 role_fd     → T_ROLE_FD_SOURCE      (5)
   dup2 src_dir_fd  → T_ROLE_FD_SRCDIR      (8)
   dup2 T_PCB_FD_INTERPRETER → T_ROLE_FD_INTERP (9)
   … plus the carried lock/boot/PCS descriptors of §V21101.6.4 …
   _execve(b"/proc/self/fd/9",
           [ b"/proc/self/fd/9", b"-P",
             b"-m", b"philosophia.officina.generic_harness",
             b"--officina-supervisor-role",
             b"--officina-role-fds", b"<pinned list>",
             b"--officina-spawning-id", b"<64 hex>" ],
           { b"PYTHONPATH": b"/proc/self/fd/8" })

ROLE SIDE, refusal-first, before ANY behaviour:
   R-1. fstat fd 5 and fstat the module's own loaded file; require
        (st_dev, st_ino) EQUAL. Mismatch ⇒ os._exit(3), nothing written,
        nothing unlinked.
   R-2. verify every inherited token, descriptor number and type, the spawning
        id against SPAWNING_MIDDLE/GROUP.json, and its own parentage, exactly as
        §Z3.3's adapter already does.
```

`R-1` is the substantive addition: it closes the window between the bootstrap's
`P-p4` check and the interpreter's own `-m` name resolution under
`PYTHONPATH=/proc/self/fd/8`. The directory is object-bound; the components
below it are name-resolved, and `R-1` proves the module actually loaded is the
inode the bootstrap checked.

> **The residual, assigned to its existing owner.** Path components resolved
> *below* an object-bound directory descriptor remain subject to the **signed A3
> same-UID procedural residual**. This layer does not close it, does not claim
> to, and invents no filesystem-exclusion mechanism. `R-1` narrows it to the
> instant between the role's own `fstat` and its import completion.

### V21101.5.4 The byte-provenance division, stated exactly

| Property | Established by | When |
|---|---|---|
| the executing bootstrap and the package root are the same tree | `P-p1`–`P-p3` `(st_dev, st_ino)` cross-check | **run time**, before any authority |
| the role image loaded is the inode the bootstrap checked | `P-p4`–`P-p5` + role-side `R-1` | **run time** |
| the **bytes** of every production root equal the reviewed bytes | the signed immutable-control verifier plus the production manifest's `root_source_sha256` field (§V2110.3.9 CHANGE 5, carried) | **deploy / review time** |

> **Why the hash is not recomputed inside the bootstrap.** Doing so would
> require a hashing facility. `hashlib` pulls `_hashlib` and OpenSSL — a large
> native surface that would defeat the five-module closure this layer just made
> exact. Implementing SHA-256 in the bootstrap root instead is possible but adds
> a substantial body of arithmetic to a file whose entire value is that it is
> small enough to decide statically. **The chosen division is therefore: object
> identity at run time, byte provenance by the signed manifest at deploy
> time.** Its limit is stated without softening: **a deployment that ships
> unverified bytes gets no run-time rescue from this contract.** That is a
> deployment-integrity requirement, and it is exactly the requirement the
> immutable-control verifier already exists to discharge.

---

## V21101.6. B6 — the supervisor's process authority, resolved

### V21101.6.1 Route 2 is unavailable, by inspection

The prompt's route 2 requires proving the supervisor holds no
PID-reuse-sensitive authority. It does not:

| Signed locus | Primitive the supervisor issues | Result-bearing? |
|---|---|---|
| §W2.5 controller/worker bootstrap handshake | `subprocess.Popen`, `os.waitpid(pid, WNOHANG\|WUNTRACED)` | **yes** — the durable `t-process-claim.v1`, the lease, and every later operation depend on it |
| §W2.1 watchdog creation | `os.fork()` | **yes** — C1's freeze evidence |
| §W2.4 discovery predicate; §U2.5 stage-1/2 routes | `os.kill`, `os.killpg`, `os.waitpid` | **yes** — death proofs feeding §U6.3 removals and §4c/§4d settlement |
| §W3.3 freeze | `killpg(SIGSTOP/SIGCONT)`-class group control | **yes** — quiescence, overrun, invalidity |

**Route 2 is therefore unavailable and route 1 is taken.** The v2.1.10 scope
note and weakest-point 4 are withdrawn (§V21101.0 row 14).

### V21101.6.2 Route 1 — the Process-Control Server, and the handle model

> **The reviewed bootstrap does not exit after the supervisor is live. It
> becomes the Process-Control Server (PCS): the single clean process that
> performs every child creation, every numeric signal, every wait, and the
> watchdog creation, for the whole generation.**
>
> **The supervisor is given opaque handles and is never told a PID.** A handle
> is a monotonically increasing decimal integer the PCS assigns; it names an
> entry in the PCS's private table `handle → (pid, start_identity, pgid,
> state)`. The supervisor's wire vocabulary contains **no pid field**, so the
> supervisor **cannot express** a signal to a numeric pid. PID-reuse sensitivity
> is removed from the supervisor **structurally**, not by discipline.

**The bounding principle, stated so the amendment stays reviewable:** this is a
**relocation of the primitive, not a change of semantics.** Every carried rule —
§W2.5's self-stop handshake and its `WIFSTOPPED` requirement, §Z3.3's adapter
argv layout and refusal-first duties, §W2.4's discovery predicate, §W3.3's
freeze and quiescence proof, §U2.5's tier discipline and `killpg` prohibition
before a verified group, §U6.1/§U6.3's record rules, C1's watchdog role — keeps
its exact meaning. What changes is **which process issues the syscall** and
**what the supervisor is allowed to name**.

### V21101.6.3 The PCS operation set

Added to the already-introduced closed wire enum of §V2110.2.5; the record
grammar, field character classes, and framing are unchanged.

| Operation | Supervisor supplies | PCS does | PCS returns |
|---|---|---|---|
| `SPAWN_SUPERVISOR` | (the caller's original request) | the carried `c1`–`c18` | `SUPERVISOR_LIVE` / `REFUSED` / `BLOCKED` |
| `SPAWN_ROLE` | role token (`CONTROLLER`\|`WORKER`), argv-template handle, ctrl-fd pair, spawn-intent id | builds §Z3.3's exact thirteen-element argv, `posix_spawn`s it in a new session, records the child | a **handle** |
| `AWAIT_STOP` | handle | the carried §W2.5 bounded `waitpid(WNOHANG\|WUNTRACED)` loop | `STOPPED` + start identity + pgid, or `EXITED`, or `TIMEOUT` |
| `SIGNAL_ROLE` | handle, signal token from a closed enum (`CONT`,`TERM`,`KILL`,`STOP`,`PROBE`) | validates the handle's state, then `kill` on the recorded pid | `SENT` / `GONE` / `DENIED` / `STRUCTURAL_VIOLATION` |
| `SIGNAL_GROUP` | handle, signal token | validates that a **verified** group exists for the handle (§U2.5's tier rule, unchanged), then `killpg` | as above |
| `REAP_ROLE` | handle | `WAIT_ONE` on the recorded pid | the carried six-result classification |
| `SPAWN_WATCHDOG` | sealed update/ack pipe descriptors | creates the watchdog (§V21101.6.5) | a **handle** |
| `RELEASE_HANDLE` | handle | requires the entry to be `REAPED`; drops the table entry | `RELEASED` |
| `SHUTDOWN` | — | refuses if any handle is not `REAPED`; otherwise exits | `SHUTDOWN_OK` / `HANDLES_LIVE` |

**Invariants of the handle table, each carrying a carried rule forward:**

1. A handle is never reused. A `REAPED` handle can be `RELEASE`d but its integer
   is never issued again.
2. `SIGNAL_ROLE` / `SIGNAL_GROUP` are refused unless the entry's state is
   `OWNED` — the carried §V218.3.1 single-kill precondition, now enforced on the
   PCS side where the pid actually lives.
3. `SIGNAL_GROUP` is refused unless the entry records a **kernel-verified**
   group, which is §U2.5's "`killpg` is forbidden before verified `setsid`",
   unchanged.
4. Every PCS-created process is a **direct child of the PCS**, so §V2110.2.3's
   process-boundary reaping proof extends to all of them verbatim: no task in
   the supervisor's contaminated interpreter can reap any of them.
5. The PCS's own wait surface remains W-1…W-5 plus one instantiation per handle,
   all governed by the carried `WAIT_ONE` classifier including
   `STRUCTURAL_VIOLATION`.

### V21101.6.4 The role-side descriptor table

| Constant | # | Contents |
|---|---|---|
| `T_ROLE_FD_LOCK` | 3 | the retained non-close-on-exec `SPAWN.lock` descriptor |
| `T_ROLE_FD_BOOT_W` | 4 | the sealed `boot` write end |
| `T_ROLE_FD_SOURCE` | 5 | the role source file, for `R-1` |
| `T_ROLE_FD_PCS_REQ_W` | 6 | request write end to the PCS |
| `T_ROLE_FD_PCS_REP_R` | 7 | reply read end from the PCS |
| `T_ROLE_FD_SRCDIR` | 8 | the object-bound `src` directory, for `PYTHONPATH` |
| `T_ROLE_FD_INTERP` | 9 | the object-bound interpreter, for descendant execs |

These are role-process indices and are independent of §Z3.3's
`T_CTRL_FD_LOW = 3` / `T_CTRL_FD_HIGH = 4`, which are **controller/worker**
indices in a different process and are carried byte-unchanged.

### V21101.6.5 The watchdog

The watchdog moves from an in-process `fork` by the supervisor to a PCS-created,
`execve`'d role with its own refusal-first private token
`--officina-watchdog-role`, receiving its sealed update/ack pipes at pinned
numbers.

> **This strengthens C1 rather than weakening it.** §W2.1's justification for the
> in-process fork was that the watchdog is created "before any
> `RealTCapability` exists, so the inherited address space contains no
> capability." An `execve`'d watchdog has a **fresh address space**, so it
> contains no capability **by construction** rather than by an ordering
> argument. Every other C1 property — witness/freezer role, holds no lock or
> capability, writes nothing under `runtime/`, appends no ledger, settles
> nothing, `getppid()`-and-identity verification, sealed pipes only — is carried
> byte-for-byte. Its `getppid()` check is re-pointed at the **PCS**, which is
> now its parent, and the supervisor identity it verifies is read from
> `SUPERVISOR_IDENTITY.json` exactly as carried.

### V21101.6.6 The complete call/ownership table after route 1

| Process | Creates | Signals | Waits | Names PIDs? |
|---|---|---|---|---|
| contaminated caller | the PCS, by `posix_spawn` | **nothing** (forbidden) | may reap only the PCS; result irrelevant | its own children only |
| **PCS (clean)** | middle child; controllers; workers; watchdog — all by `posix_spawn`/`fork` it issues itself | every `kill`/`killpg` in the system | every `wait` in the system | **yes, and only it** |
| supervisor (contaminated) | **nothing** | **nothing** — it cannot express a pid | **nothing** | **no** — handles only |
| watchdog (exec'd role) | nothing | nothing | nothing | no |
| controller / worker | per the carried adapter and role contracts, unchanged | unchanged | unchanged | unchanged |

> **Consequence.** Every PID-reuse-sensitive authority in the system is held by a
> process constructed exactly as §V2110.2–§V2110.3 specify. The supervisor's
> contamination can still corrupt the supervisor's *own* bookkeeping — which is
> what the signed B1 journal, the custody proof, and the invalidity semantics
> already govern — but it can no longer cause a signal to a recycled PID, a
> false death proof, or a stolen reap anywhere in the tree.

---

## V21101.7. B7 — totality reconciled with the corrected topology

### V21101.7.1 `P-g` amended: the blocked-signal mask

The carried `MASK_FIELD` grammar and width rule (§V2110.6.2) now also parse
`SigBlk`, with the identical grammar and the identical `W-a`/`W-b` width
conjuncts:

```text
P-g0.  require SigBlk == 0
         non-zero ⇒ SIGNAL_MASK_INHERITED ⇒ fail-closed refusal, no fork
```

An inherited blocked mask cannot affect `WNOHANG` waits, but it can make the
bootstrap unresponsive to default-action termination, so it is refused rather
than tolerated. `setsigmask=()` in the spawn makes this the expected state; the
readback is what makes it a fact.

### V21101.7.2 The eight required reconciliations

| Case | Disposition under the corrected topology |
|---|---|
| **caller helper reaps the PCS** | it may. The reply pipe is the sole authoritative result and the exit status is advisory (carried). The PCS's own custody, records and lock are untouched. If the PCS is *reaped after exiting*, everything it owned has already been released by the kernel |
| **caller dies / stops reading / closes the reply pipe early** | the reply write raises on `EPIPE` (`SIGPIPE` is `SIG_IGN`, carried). It is recorded and **changes no record, custody, ownership, or terminal decision**. The PCS completes its route, releases the lock, and exits |
| **caller lies in the request** | the six-field closed grammar admits no field that can name code, a module, a callback, a primitive, a path, an fd, or a timeout. A lie is confined to a hex nonce and two integers describing the caller itself, both of which are recorded, not trusted |
| **caller misreports the reply to its user** | §V21101.7.5 |
| **operator `SIGINT` at every cut** | no handler exists after `N-1` (`SigCgt == 0`), so the default action terminates the PCS. Before `c1`: nothing exists. Between `c1` and `c4`: kernel releases the lock and fds; `SPAWNING.json` names a dead process; the next attempt's §U6.1 P3 removes it. After `c4`: `pid_mid` is re-parented to `init`, which reaps it; the middle exits at its own `m0` bound; no record was removed without proof. Identical for a role or watchdog process |
| **`P-e` wildcard wait and its inherited-child side effect** | unchanged and carried: one call, pre-fork, at one site, whose only accepted outcome is `ECHILD`. If it returns a pid it has reaped an inherited child, and the route refuses immediately with `INHERITED_CHILD`. The side effect is stated, not avoided; it can only occur in a process that was already outside the supported construction |
| **W-5 with the middle stopped after `m8`** | carried verbatim from §V2110.4.3: `WNOHANG` without `WUNTRACED` cannot report a stop, so both attempts return `(0,0)`, **no signal is sent**, the bootstrap **succeeds**, and the stopped middle holding a fork-shared lock reference is the **carried §U2.7 A3 stopped-middle residual** |
| **`STRUCTURAL_VIOLATION` at every W site** | carried verbatim from §V2110.4.1–§V2110.4.2, and now additionally at every PCS handle site: never death, `CONTRADICTED` set irreversibly, no signal ever again, no record touched, the site's `CONTRADICTED_ECHILD` continuation |
| **PCS dies and `init` adopts its descendants** | `pid_mid`, roles and the watchdog are re-parented to `init`, which reaps them. **No surviving process holds a wait authority this contract relies on**, because every route that needed one has already failed closed. Records naming those processes are resolved by the next attempt's §U6.1 P0–P3 (`/proc` absence or state `Z`), unchanged. The supervisor, holding only handles, can issue nothing: its PCS reply pipe reaches EOF, which it must treat as loss of process authority and route through §V21101.7.5 |
| **locks / records / fds across every exec and failure** | `SPAWN.lock` is non-close-on-exec and survives the grandchild's `execve` (now load-bearing, §V2110.9 row 24, carried); every other descriptor is either `O_CLOEXEC` or explicitly `dup2`'d to a pinned number; a failed `execve` yields `os._exit(3)` with nothing written and nothing unlinked; the four singleton records, their key sets, `§U6.2` `EEXIST`, `§U6.1` P0–P3 and `§U6.3` order are byte-unchanged |

### V21101.7.3 The `NO_REPLY` route

Any case in which the caller reads the reply pipe to EOF **without** a complete
canonical reply line — a truncated interpreter, a `P-s`/`P-b` failure before the
reply is written, a killed PCS, or a `B-OWNED`/`B-CONTRADICTED` state, which by
construction write no reply — is exactly one control-plane outcome:

```text
NO_REPLY  ⇒  the caller learned NOTHING about the attempt's outcome.
             It MUST NOT infer success, failure, retryability, or liveness.
             It routes to §V21101.7.5.
```

### V21101.7.4 Added crash and cut rows

Every §V2110.7.1 row not listed here carries forward unchanged.

| Cut | Single continuation |
|---|---|
| `P-s1`–`P-s6` any failure (source or interpreter object unusable, not regular, writable, not read-only) | reply if the pipe is usable, else `NO_REPLY`; **no lock, no record, no fork** |
| `P-p1`–`P-p3` package-root/source mismatch | `ROOT_SOURCE_MISMATCH`; no lock, no record, no fork |
| `P-p4`–`P-p6` role image unreadable or not regular | `ROLE_SOURCE_UNREADABLE`; no fork |
| `P-cwd` `chdir("/")` fails | `CHDIR_FAILED`; no fork |
| `P-g0` `SigBlk != 0` | `SIGNAL_MASK_INHERITED`; no fork |
| hoist postcondition violated in the caller | `LAUNCH_FD_HOIST_FAILED`; **no spawn** |
| a `_POSIX_SPAWN_*` constant fails validation | `LAUNCH_CONSTANT_MISMATCH`; **no spawn** |
| `posix_spawn` raises, or returns a non-`int` or `<= 0` | `LAUNCH_SPAWN_FAILED` / `LAUNCH_STRUCTURAL`; no authorized bootstrap |
| a file action fails in the child (bad source fd, invalid destination) | the child exits 127 having executed nothing; no reply ⇒ `NO_REPLY` |
| the interpreter cannot open `/proc/self/fd/7` | exits non-zero, no reply ⇒ `NO_REPLY` |
| role-side `R-1` `(st_dev, st_ino)` mismatch | `os._exit(3)`, nothing written, nothing unlinked; `c13` reads EOF on `boot` ⇒ carried §U2.5 stage-2 route |
| supervisor's PCS reply pipe reaches EOF | the supervisor has lost process authority; it may create, signal, or wait on nothing; it routes to §V21101.7.5 and stops admitting |
| `SHUTDOWN` requested with a live handle | `HANDLES_LIVE`; the PCS does not exit; nothing is released |

### V21101.7.5 Caller misbehaviour routed through the signed invalidity semantics

> **Replacing** §V2110.2.4's clause "it can misreport the reply to its own user".
>
> A control-plane outcome that is unknown, lost, or misreported is **never** a
> scientific or resource result and is **never** silently absorbed. Every such
> case is routed through the already-signed semantics:
>
> 1. **`NO_REPLY`, a killed PCS, or a lost supervisor channel** is a
>    **process** fact. Any operation whose control outcome cannot be established
>    settles through the signed `T_PROCESS_INVALID` recovery disposition and the
>    §4c(c)/§4d **unknowable** route, with invalidity dominance applying exactly
>    as carried. It is never `T_PROCESS_CLOSED`, never a completion, never a
>    capacity or custody fact, and never a Q/C input.
> 2. **A caller that misreports a truthful reply** changes nothing durable: the
>    durable record set, the journal, the capacity ledger, and the custody
>    dispositions are written by processes the caller does not control, and the
>    signed B1 idempotency/acknowledgement rules make a retry converge on the
>    recorded truth rather than on the caller's account of it.
> 3. **No route anywhere may treat "the caller's own user was misinformed" as a
>    disposition.** The phrase is withdrawn from this chain.
> 4. **A caller that kills the PCS** produces exactly rule 1's outcome, plus the
>    carried crash continuations: no record naming a live process is removed, no
>    death is proved, and the next attempt's §U6.1 preflight governs.
>
> The general rule, carried and re-stated: **process invalidity, resource
> exhaustion, and missing evidence are infrastructure facts and are nowhere
> treated as scientific evidence.**

---

## V21101.8. Future verifier algorithm and tests

### V21101.8.1 Amendments to §V2110.3.9

```text
CHANGE 2 (amended) — module-scoped absolute-import allowlist
  MODULE_SCOPED_ABSOLUTE_IMPORTS = {
      "scripts/officina_process_control_bootstrap.py":
          frozenset({"os", "sys", "_signal", "time", "fcntl"}),     # _signal
      "src/philosophia/officina/generic_harness.py":
          ALLOWED_ABSOLUTE_IMPORTS,      # contains neither `signal` nor `_signal`
  }
  ALLOWED_ABSOLUTE_IMPORTS gains `sys` and `_signal`; it does NOT gain `signal`.
  Rule S-7 forbids `sys` and `_signal` in any file without a scoped entry.

CHANGE 3 (amended) — the closed AST grammar
  S-1  exactly five `ast.Import` nodes: os, sys, _signal, time, fcntl — module
       scope, unaliased, no `ImportFrom`, none conditional or nested
  S-3  the binding block is the §V2110.3.4 list as amended by §V21101.1.3, with
       `_signal.` sources for the four signal names and the added `_chdir`,
       `_dup`, `_get_inheritable`; each value an `Attribute(Name(m), attr)` with
       m in the five and attr in that module's pinned attribute set
  S-3b (new) the first executable statement of the module is
       `_BUILTIN = type(len)`; `len` appears nowhere else
  S-5  the names os, sys, _signal, time, fcntl appear as an `Attribute` value
       ONLY inside the S-3 block
  S-7  (widened) forbidden anywhere: `signal` (the wrapper), `functools`,
       `enum`, `_thread`, `threading`, `multiprocessing`, `concurrent`,
       `asyncio`, `ctypes`, `subprocess`, `atexit`, `gc`, `hashlib`, `json`,
       `re`, `register_at_fork`, `start_new_thread`, `settrace`, `setprofile`,
       `addaudithook`, `set_wakeup_fd`, `pthread_sigmask`, `pthread_kill`,
       `siginterrupt`, `alarm`, `setitimer`, `pidfd_send_signal`, `SIG_IGN`,
       `readlink`, `getattr`, `setattr`, `delattr`, `vars`, `globals`,
       `locals`, `eval`, `exec`, `compile`, `__import__`, `importlib`,
       `open` (the builtin)
       — `readlink` is newly forbidden so B2's defect cannot recur
  S-9  every `_sigsignal` call's second argument is `_SIG_DFL`; every
       `_getsignal` call's argument is `_SIGCHLD`
  S-11 (new) every `_posix_spawn` call in the LAUNCHER root passes exactly the
       argument shape of §V21101.3.4, with a `file_actions` literal of twelve
       tuples in the pinned order and no `preexec_fn`/`shell`/`cwd` keyword
  S-12 (new) `subprocess`, `Popen`, `fork`, and `system` appear nowhere on the
       launcher path of `generic_harness.py`
  S-13 (new) no string literal `/proc/self/fd/` is concatenated with a
       non-constant expression; the six literal fd paths are exact constants
Each violation is FAIL-CLOSED with the named result, as in v2.1.10.
```

### V21101.8.2 Replaced and added test rows

Rows **273**, **276**, **277**, **279**, **293**, **297** of §V2110.7.4 are
replaced by the corrected statements below; all other carried rows stand.

| # | Test | Covers |
|---|---|---|
| 273R | the spawn call is byte-exact: `path == b"/proc/self/fd/8"`, the six-element argv, `env == {}`, `setsigmask=()`, twelve file actions in the pinned order, **no** `preexec_fn`/`shell`/`cwd`/`close_fds`/`pass_fds` keyword anywhere | B3 |
| 276R | the bootstrap's import set is exactly `{os, sys, _signal, time, fcntl}`; `signal`, `functools`, `enum` and `_thread` are absent from the closure | B1 |
| 277R | every row of the §V21101.1.4 identity table passes for a genuine binding and fails for its stated substitution (Python function, `partial`, bound method, callable instance, foreign-module builtin, wrong `__qualname__`, wrong constant value) | B1 |
| 279R | `P-f` requires exactly `{0,1,2,3,4,5,6,7,8}`; a leaked non-`O_CLOEXEC` caller descriptor causes a refusal | B3, B4 |
| 293R | the grandchild execs `/proc/self/fd/<T_ROLE_FD_INTERP>` with `PYTHONPATH=/proc/self/fd/<T_ROLE_FD_SRCDIR>`; the `SPAWN.lock` fd is non-close-on-exec and survives; a failed `execve` writes and unlinks nothing | B2, B5 |
| 297R | the scoped map gives the bootstrap `{os, sys, _signal, time, fcntl}` and `generic_harness.py` a set with neither `signal` nor `_signal` | B1 |
| 313 | `readlink` appears nowhere in the bootstrap or on the launcher path; the exec targets are the two literal `/proc/self/fd/<N>` constants | B2 |
| 314 | source-object binding: unlink, rename, replace-at-name, truncate, hardlink, and symlink-at-name each behave as §V21101.2.4 tabulates | B2 |
| 315 | `P-s1`–`P-s6` reject a non-regular, group-writable, other-writable, or write-open source and interpreter | B2 |
| 316 | `sys.executable` is never used for any exec or decision; it appears only as a recorded diagnostic | B2 |
| 317 | the hoist algorithm terminates, yields six pairwise-distinct descriptors `>= 9`, and closes every intermediate; a forced collision is detected and refuses | B3 |
| 318 | the file-action sequence is collision-free for every arrangement of caller descriptors, including all six initially inside `3…8` | B3 |
| 319 | `POSIX_SPAWN_DUP2` clears close-on-exec on the destination; the six targets are inheritable and every other `O_CLOEXEC` descriptor is closed by the exec | B3 |
| 320 | the `_POSIX_SPAWN_*` set-equality and distinctness validation rejects a rebound constant | B3 |
| 321 | `posix_spawn` failure modes: raise, non-`int`, `<= 0`, and a failing file action each route as §V21101.3.5/§V21101.7.4 state | B3 |
| 322 | `_chdir("/")` runs before any name is opened; assert no relative name is resolved anywhere in the bootstrap | B3 |
| 323 | the launcher performs no `fork`, no `Popen`, no `preexec_fn`, no shell; static and dynamic | B3, B4 |
| 324 | the launcher primitive checks refuse before spawn on each injected rebinding; and a caller that defeats the checks produces a process the bootstrap's own preflight refuses | B4 |
| 325 | the three counterexamples of §V21101.4.4 each fail at their stated step | B4 |
| 326 | `P-p1`–`P-p3`: a mismatched package root refuses with `ROOT_SOURCE_MISMATCH` before any lock or fork | B5 |
| 327 | `P-p4`–`P-p6` and role-side `R-1`: a role image substituted between the bootstrap's check and the role's import is rejected by `R-1` | B5 |
| 328 | the byte-provenance division of §V21101.5.4 is asserted: the manifest check is a deploy-time obligation and the bootstrap makes no byte claim | B5 |
| 329 | the supervisor's wire vocabulary contains **no pid field**; static assertion over the schema and the role source | B6 |
| 330 | handles are never reused; `RELEASE_HANDLE` requires `REAPED`; `SHUTDOWN` refuses while a handle is live | B6 |
| 331 | `SIGNAL_ROLE` refuses unless the entry is `OWNED`; `SIGNAL_GROUP` refuses unless a kernel-verified group is recorded | B6 |
| 332 | every PCS-created process is a direct child of the PCS; a wildcard wait in the supervisor reaches none of them | B6 |
| 333 | §W2.5's self-stop handshake, §Z3.3's argv layout, §W2.4's discovery predicate, §W3.3's freeze, and §U2.5's tier rules keep their exact semantics under relocation | B6, no-regression |
| 334 | the exec'd watchdog satisfies every carried C1 property and holds no capability by construction | B6 |
| 335 | `P-g0` refuses a non-zero `SigBlk`; `setsigmask=()` makes zero the expected state | B7 |
| 336 | `NO_REPLY` is produced by a truncated source, a pre-reply refusal, a killed PCS, and both `B` states; the caller infers nothing from it | B7 |
| 337 | every §V21101.7.5 rule: an unknown control outcome settles through `T_PROCESS_INVALID` and the §4c(c)/§4d unknowable route, never as a completion | B7 |
| 338 | the phrase "its own user" as a disposition appears nowhere | B7 |
| 339 | PCS death with `init` adoption: descendants are reaped by `init`, no record naming a live process is removed, the supervisor's channel EOF removes its authority | B7 |
| 340 | W-5 stopped-middle, `STRUCTURAL_VIOLATION` at all sites, and `P-e`'s inherited-child side effect are unchanged from v2.1.10 | B7, no-regression |
| 341–352 | one row per §V21101.10 supersession (28–36) asserting its exact scope and that the paired untouched property still holds | governance |

---

## V21101.9. No-regression

### V21101.9.1 v2.1.10 surfaces preserved

| Surface | Status |
|---|---|
| the constructed clean runtime, the isolated root, `-I -S -E -P`, the `sys.flags` readback | **byte-for-byte** |
| §V2110.2.3's process-boundary reaping proof | **byte-for-byte**, and extended by §V21101.6.6 to every PCS-created process |
| §V2110.3.3's operation inventory, §V2110.3.5–§V2110.3.8's theorem and premise table | carried; premise 5's closure is now the smaller one of §V21101.1.1, which strictly strengthens it |
| §V2110.4 in full — `WAIT_ONE`, `STRUCTURAL_VIOLATION`, the site tables, the product, W-5, `T1`/`T2`/`B`, the non-circular `B-CONTRADICTED` exclusion | **byte-for-byte** |
| §V2110.6 in full — the pinned platform and the mask grammar/width | **byte-for-byte**, extended only to parse `SigBlk` with the identical rules |
| §V2110.9 rows 19–27 | carried, extended by §V21101.10 |

### V21101.9.2 Carried signed surfaces

`N-1`/`N-2`/`V-4`…`V-9`; `ECHILD`/`ESRCH` never death; the ten-row identity
table; ownership-gated signals and the fork-ownership proof; `T3` deleted; the
no-discard invariant; the stage-M `m0`/`rel1`/fork-shared-lock proof; §V217.1's
object-bound observation and both barriers; §V217.4's bound-language sweep;
`CLOSE_OWNED`; `MALFORMED` dominance and the branch bodies; §N2.3 P1–P7 custody;
K1's constants and one-release accounting; death-before-unlink; §U6.1 P0–P3,
§U6.2, §U6.3, `s1`–`s5`; §U2.1–§U2.4 and `m0`–`m9` including the `EPIPE` route
and `SIGPIPE = SIG_IGN`; §Z3.3's adapter layout and `T_CTRL_FD_LOW/HIGH`;
§Z3.2's signed `t-spawn-intent.v1` role enum; A3/B1/C1/D1/K1; the signed
generic-harness v2→v2.3.1 and batch-settlement v1→v1.1.1 composites; the nine
events; E1/E2/E3; invalidity dominance; the Q/C boundary; and T's inactivity —
**all unchanged**. The A3 same-UID filesystem residual is untouched, and nothing
here claims filesystem exclusion.

### V21101.9.3 Edit surface, extended

| Path | Permitted change | Status today |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` | the bootstrap **and** the PCS mode of §V21101.6 | **does not exist** |
| `src/philosophia/officina/verification.py` | v2.1.10's CHANGES 1–5 as amended by §V21101.8.1 | unmodified, `327b1bb2…` |
| `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json` | four roots, the closure, `root_source_sha256` | does not exist |
| `src/philosophia/officina/generic_harness.py` | the `posix_spawn` launcher; the `--officina-supervisor-role` and `--officina-watchdog-role` refusal-first entries; the PCS client; **removal** of every `Popen`/`fork`/`waitpid`/`kill`/`killpg` on a result-bearing path | **untracked Cursor work — preserved byte-for-byte** |
| `tests/test_officina_generic_harness.py` and a new bootstrap/PCS test module | §V2110.7.4 and §V21101.8.2 | untracked Cursor work — preserved |
| everything else | **no change** | byte-unchanged |

---

## V21101.10. Superseded sentences, named

v2.1.10 §V2110.9 rows 19–27 are carried. Nine more:

| # | Locus | Superseded wording | Scope of the supersession |
|---|---|---|---|
| 28 | v2.1.10 Engineering constants | "Modules the bootstrap imports: **`os`, `sys`, `signal`, `time` — and nothing else.**" | replaced by the five-module `_signal` set; the exclusion list is retained and widened |
| 29 | v2.1.10 §V2110.3.2 | "the bootstrap **does** import `fcntl` as a fifth module. Its permitted set is therefore exactly **`{os, sys, signal, time, fcntl}`**" | replaced by `{os, sys, _signal, time, fcntl}`; `fcntl`'s membership is confirmed, `signal`'s is removed |
| 30 | v2.1.8 §V218.1.1 / v2.1.9 §V219.4.1 | "`ALLOWED_ABSOLUTE_IMPORTS` gains `signal`" and "the sole permitted importer of `signal`" | the allowlist gains `sys` and **`_signal`**, never the `signal` wrapper. The one-importer principle is unchanged |
| 31 | v2.1.10 §V2110.3.4 | the universal identity predicate "`type(f).__name__ == \"builtin_function_or_method\"` … for every bound CALLABLE" | replaced by the per-primitive table; the predicate is **invalid** as stated |
| 32 | v2.1.10 §V2110.2.1 | "so the exec target is the SAME inode the caller opened" and "`sys.executable` … absolute, kernel-supplied" | both **deleted as false** |
| 33 | v2.1.10 §V2110.2.1/§V2110.2.6 | "`cwd = \"/\"`", "`close_fds = True`", "`pass_fds = …`", "`preexec_fn = None`", and "The caller `dup2()`s its ends onto exactly these numbers in the pre-exec child" | replaced by the `posix_spawn` launcher; the `dup2`-in-pre-exec-child clause is **deleted as impossible** under the stated API |
| 34 | v2.1.10 §V2110.2.4 | "it can misreport the reply to its own user" | replaced by §V21101.7.5's invalidity routing; the phrase is withdrawn |
| 35 | v2.1.10 §V2110.2.7 scope note and §V2110.11 weakest-point 4 | "This correction therefore does not claim to have repaired supervisor-side reaping" | **withdrawn**; §V21101.6 repairs it |
| 36 | carried §W2.1 watchdog bullet | "the supervisor calls `os.fork()`; the child calls the watchdog function in-process" | replaced by §V21101.6.5's PCS-created, `execve`'d watchdog role. Every C1 property is carried; the address-space argument is **strengthened** |

---

## V21101.11. Weakest points, governance, negative space

**Weakest remaining points, stated against the author.**

1. **The interpreter is object-bound but not attested.** `/proc/self/fd/8` binds
   *which object* runs, not *that it is a reviewed CPython*. `P-b` checks a
   pinned identity a patched build could satisfy. This is the sharpest boundary
   in the whole design and it is unchanged from v2.1.10.
2. **Byte provenance is a deploy-time obligation.** The bootstrap proves object
   identity and consistency; it does not hash anything. A deployment that ships
   unverified bytes gets no run-time rescue. `hashlib` was excluded
   deliberately, and an in-root SHA-256 was rejected as too large for a file
   whose value is being statically decidable — a trade a reviewer may reject.
2b. **`/proc` must be mounted and unfaked.** Every object-bound path, the flag
   and mask readbacks, and the task-count checks route through `/proc`. A host
   with a substituted `/proc` defeats them, and nothing here detects that.
3. **B6 is the largest amendment in this chain.** It relocates every process
   primitive in the system and re-points the watchdog through an `execve`'d
   role. I have bounded it by "relocate the primitive, preserve the semantics"
   and by giving the supervisor handles instead of PIDs, but the surface is
   wide, it touches §W2.1, §W2.4, §W2.5, §W3.3, §Z3.3 and C1's creation path,
   and a reviewer may reasonably judge that it needs its own layer rather than a
   subsection of a pre-review correction.
4. **The handle model removes PID authority from the supervisor, not
   bookkeeping corruption.** A contaminated supervisor can still mis-order its
   own requests, mis-record its own journal, or mis-report to a client. Those
   are governed by the signed B1 idempotency rules, the custody proof, and the
   invalidity semantics — but this layer does not strengthen them and does not
   claim to.
5. **`P-e`'s single wildcard wait remains a real exception** to the
   no-wildcard rule, with a stated reaping side effect in the case where it
   returns.
6. **The launcher checks are defeatable by a fully hostile caller.** That is
   accepted and is why §V21101.4.1 is a disjunction; but it means the *loudness*
   of a mis-launch is not guaranteed, only its harmlessness.
7. **The `posix_spawn` at-fork fact is stated as reviewer-verifiable.** I have
   made it non-load-bearing, but if it were false *and* the process boundary
   argument were also wrong, the repair would fail; the two are independent, and
   I rely on the second.
8. **`_signal` is a private CPython module.** Its API is stable in practice and
   is what `signal` itself wraps, but depending on an underscore module is a
   deliberate trade of convention for a smaller, auditable closure.

**Governance.** No scientific author cell is reopened. Every delta is an
engineering surface: an import set, an identity table, two descriptor indices,
a launch mechanism, two provenance checks, a handle-based control protocol, one
further private argv token, and a mask check. **No resource value, timeout, K1
ceiling, E1/E2/E3 value, T band, scientific estimand, or policy cell is
reached**, which is why no `BLOCKED_..._AUTHOR_CELL` verdict is emitted.

**Negative space.** This correction creates nothing executable and authorizes no
implementation, commit, host change, verifier edit, manifest, process,
supervisor, controller, worker, watchdog, adapter, middle child, endpoint, pipe,
FIFO, journal instance, spawn record, lease, capability, operation, framed
transport, result manifest, quarantine record, promoted object, capacity
artifact, custody disposition, freeze witness, entropy, E1/E2/E3 spend, world,
learner, candidate, Q attempt, Q/C object, datum, outcome, Proof, or claim
movement. It predicts no qualification and no C1–C6 outcome. Process
invalidity, resource exhaustion, missing evidence, `NO_REPLY`, a
`STRUCTURAL_VIOLATION`, the `B-OWNED` residual, and the `B-CONTRADICTED` sink
remain infrastructure facts and are nowhere treated as scientific evidence. No
example in this document was written to any file.

---

## V21101.12. The final bounded questions

At most three per line. Both lines must recompute the digest of **this file**,
of v2.1.10, and of every governing hash, and must treat both author closures as
untrusted. **The bytes under review are v2.1.10 as corrected by this layer.**

### For the X line (Claude Opus 4.8, clean context)

> **X-Q1 — construction, binding, and primitives.** Is the corrected
> construction single-valued and does it hold? Attack: the five-module
> `_signal` closure (does using the private built-in genuinely remove
> `functools`/`_thread`, and does `_signal.getsignal` return an `int` for a
> default disposition?); the per-primitive identity table (does every genuine
> binding pass and every stated substitution fail, and is `type(len)` a sound
> anchor *inside* the isolated process?); and the object-binding of source and
> interpreter (does opening `/proc/self/fd/<N>` resolve to the held object
> rather than re-walking a path, does executing it work as `fexecve`, and is
> §V21101.2.4's cut table complete?).
>
> **X-Q2 — the launcher and the process boundary.** Is the `posix_spawn` route
> implementable exactly as written — the hoist postcondition, the twelve
> ordered file actions, the collision argument, `POSIX_SPAWN_DUP2`'s
> close-on-exec semantics, the constant validation, and the removal of `cwd`
> in favour of `_chdir("/")`? Is the pinned fact that `posix_spawn` runs no
> Python at-fork callback correct, and — more importantly — is the repair
> genuinely independent of it? Does §V21101.4.1's disjunction hold for every
> caller behaviour in §V21101.4.3?
>
> **X-Q3 — provenance and supervisor authority.** Do `P-p1`–`P-p3` and role-side
> `R-1` actually remove "hostile caller launches an arbitrary supervisor", and
> is the object-identity/manifest division of §V21101.5.4 honest about what it
> does not prove? Then judge B6: is route 2 correctly ruled unavailable; does
> the handle model structurally remove PID-reuse sensitivity from the
> supervisor; is "relocate the primitive, preserve the semantics" a sound
> bound; and is the `execve`'d watchdog genuinely a strengthening of C1 rather
> than a change to it? If you judge B6 too large for this layer, say so
> explicitly.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_1_X` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_10_1`. Static review only: no code, test,
> probe, spawn/fork/signal experiment, or Officina process may run; no runtime
> or scientific artifact may be created; no existing file may be modified;
> create exactly one review file. Do not authorize
> `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, implementation, T
> activation, entropy, spend, or any later gate.

### For the Y line (GPT-5.6 Sol, clean context)

> **Y-Q1 — single-valuedness and the identity rule.** Are all seven blockers now
> single-valued and implementable, with no sentence in the corrected composite
> contradicting another? Check specifically that exactly one import inventory
> survives anywhere in the chain, that the per-primitive identity table admits
> every genuine binding and rejects every substitution **without** trusting
> mutable caller state, and that the `readlink`, `sys.executable`, `cwd`,
> `close_fds`/`pass_fds` and pre-exec-`dup2` claims are deleted rather than
> merely re-worded.
>
> **Y-Q2 — authority, provenance, and the supervisor.** Does the launcher
> property "either the exact isolated process or no authorized bootstrap" hold
> mechanically, and is it correctly *not* a claim that a hostile caller must
> succeed? Do the fd 6 ↔ fd 7 binding and role-side `R-1` close B5 to the point
> where "hostile caller launches arbitrary supervisor" is no longer a supported
> route? And is B6's route 1 a genuine resolution — does the supervisor now hold
> **no** PID-reuse-sensitive authority, is every `Popen`/`fork`/`waitpid`/`kill`/
> `killpg` on a result-bearing path relocated to a clean process, and does the
> carried §W2.5/§W3.3/§Z3.3/C1 semantics survive relocation unchanged?
>
> **Y-Q3 — totality and the invalidity routing.** Are the eight B7
> reconciliations complete against the corrected topology — caller reaping the
> PCS, `NO_REPLY` in all its forms, operator `SIGINT` at every cut, `P-e`'s
> side effect, W-5's stopped middle, `STRUCTURAL_VIOLATION` at every site
> including the new PCS handle sites, `init` adoption after PCS death, and locks
> and records across every exec and failure? And is §V21101.7.5 a correct use of
> the **signed** invalidity semantics — `T_PROCESS_INVALID` plus the §4c(c)/§4d
> unknowable route with invalidity dominance — rather than a new disposition?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_1_Y` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_10_1`. Static review only: no code, test,
> probe, spawn/fork/signal experiment, or Officina process may run; no runtime
> or scientific artifact may be created; no existing file may be modified;
> create exactly one review file. Do not authorize
> `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, implementation, T
> activation, entropy, spend, or any later gate.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. No independent review of v2.1.10 was
requested, and none of v2.1.10.1 has occurred. The only next authorization step
is a **fresh independent X-line review and a fresh independent Y-line review of
v2.1.10 as corrected by these bytes**.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
