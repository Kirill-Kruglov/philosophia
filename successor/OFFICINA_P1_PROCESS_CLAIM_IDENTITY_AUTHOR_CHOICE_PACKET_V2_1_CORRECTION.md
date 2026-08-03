# Officina P1 process-claim identity — author choice packet v2.1 (bounded correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This correction selects nothing.** It
closes exactly two residual defects that two independent bounded confirmation
lines returned `REVISE` on, and changes nothing else.

**No token in this correction is signable.** Every token remains signable only
after a bounded independent X-line and Y-line confirmation round on identical
bytes. `T` is `NOT_ACTIVATED`; the programme claim is `OPEN`. This document
creates nothing executable and authorizes no implementation.

**Status.** v2.1 is a **bounded correction**, not a replacement. It carries
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
forward **verbatim** except for the two loci named in the replacement index at
§0.2. v2, v1, both v1 reviews and both v2 confirmations are preserved
byte-untouched as the evidentiary record. Where v2.1 and v2 differ, v2.1
governs; everywhere else v2's text is the operative text and is read as written.

**Bounded repair mandate.** Both confirmation lines returned `REVISE` and both
are treated here as **binding defect reports**:

```text
X-line, reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
        determination 2 — the residual under X M-2 and Y-C1: reflective,
        iteration-based and attribute-based reads of the restricted values are
        not foreclosed in src/philosophia/officina/generic_harness.py, the root
        where the governed code lives. Three concrete constructs pass
        S-25a..S-25h and reach a second sink.
Y-line, reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
        YV2-C1 — the canonical whole-claim SHA-256 that produces
        process_claim_sha256 is a signed fifth persistent consumer that the
        C-1..C-4 whitelist omits and that P-R1/P-R4 forbid.
```

**Nothing else is reopened.** The eight findings both lines confirmed closed
(`X M-1`, `X m-1`, `X m-2`, `X m-3`, `Y-C2`, `Y-M1`, `Y-M2`, `Y-m1`) are
untouched by this correction, and §7 lists them with the exact v2 loci that must
remain intact.

---

## §0. What v2.1 changes, and where

### §0.1 The two residual defects, in the reviewers' own terms

```text
RESIDUAL X — INDIRECT READS IN THE PEER ROOT.
  The occurrence count of §2.5 governs occurrences of the two NAMES. ACC-R1 and
  S-25d govern accesses whose KEY OPERAND is one of two string literals. A read
  that uses neither is invisible to both. S-25f/S-25g recognize a restricted
  value only by its whitelisted shapes, so they do not fire on a laundered
  shape. The composite bans locals/globals/vars/getattr/setattr/eval/exec/
  compile/__import__ and the builtin open only in "the PCS and role roots"
  (S-7, composite :2581); invariant 80 (:2749) names no wider scope for it; and
  generic_harness.py's 17-module allowlist (§P1-3.2) shows the S-1..S-24 grammar
  is the process-control-root grammar. So reflection, mapping iteration and
  attribute access are all available exactly where the governed code lives.

  The three demonstrated bypasses, verbatim from the X-line file:
      _vals = list(claim.values()); _leaked = _vals[5]
      _leaked = locals()["attested_pid"]
      _leaked = claim.controller_pid

RESIDUAL Y — THE OMITTED FIFTH CONSUMER (YV2-C1).
  The signed chain requires a canonical whole-claim SHA-256:
      OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:99-102 — the durable
        non-state-bearing T_PROCESS_STARTED event carries process_claim_sha256
        after the claim is durable and verified;
      OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:248-257 — the final
        process record's key set contains process_claim_sha256.
  The claim bytes that are hashed contain controller_pid and process_group_id
  (:231-238). The hash is therefore a persistent consumer of restricted values.
  It is omitted from C-1..C-4, forbidden by P-R1 and by P-R4's "any record class
  other than the claim and the lease", and it escapes ACC-R1/ACC-R2 because it
  binds neither key literal and neither integer. On the v2 bytes the whitelist
  is simultaneously required and forbidden by the signed chain.
```

Both statements were re-derived here from the committed contract bytes, not
accepted on the reviewers' authority. Both are correct. v2.1 accepts them
without reservation.

### §0.2 The exact replacement index — two rows, and no third

| # | v2 locus replaced | Replaced by | Closes |
|---|---|---|---|
| **1** | §2.6.3 `ACC-R1`..`ACC-R4`, and the §2.11 texts of `S-25d`, `S-25e`, `S-25g`, **as they bear on indirect reads** | **§2 of this correction**: the reflection lockdown `S-25i`, the pinned mapping representation and its position discipline `S-25j`, the carrier discipline `S-25k`, the approved call-site table `MS-1`..`MS-12`, and the amended rule texts at §4 | X-line determination 2; the residuals under `X M-2` and `Y-C1` |
| **2** | §2.6.2 `C-1`..`C-4` and `P-R1`/`P-R4`/`P-R5`, and §2.6.1's "there is no declassifying operation" | **§3 of this correction**: consumer `C-5`, accessors `ACC-4`/`ACC-5`, the classification rules `DC-1`..`DC-7`, the laundering analysis `WL-1`..`WL-4`, and the amended rule texts at §4 | `YV2-C1` |

**Everything else in v2 carries forward verbatim**, including §1 (the conflict
and the corrected `/proc` rationale), §2.1–§2.5 (the response grammar, the
pinned `PID_MAX_LIMIT`, the PCS proof obligation `A-P1`..`A-P6` with
`A-P4a`..`A-P4d`, the withdrawn sole-sink rule, and the whole immediate-use
occurrence whitelist `V-1`..`V-9` / `Z1-R1`..`Z1-R6` / `Z2-R1`..`Z2-R5`), §2.6.1
(the class, as amended only by the two additions at §3.3 and §3.5), §2.6.4–§2.6.7
(the recomputed schema-reader audit as extended by §5, the `SPAWNING_GROUP.json`
collision `NC-1`..`NC-3`, and the disposal of the admission-time membership
question), §2.7 (`A-R1`..`A-R8`), §2.8 (the `J4` vector and byte-identical
replay), §2.9, §2.10 (crash matrix, `EEXIST` `X-1`..`X-4`, invalidity dominance
`I-1`..`I-10`), §2.12 (the bounded weakening and its token), §3 (Option B and
its non-selectability), §4 (Option C rejected), §5 (the comparative audit, with
only the counts amended at §6), §6 (the orthogonal watchdog-freeze defect), §7
(the recommendation and the v1.3 handoff, with only the steps amended at §6.3),
§8, §9 and §10.

**No selection is made. Neither `A` nor `B` is chosen. The weakening token is
neither minted nor accepted.**

---

## §1. Binding inputs, on committed bytes

```text
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
```

The first two digests are the ones **both** confirmation lines independently
recomputed and declared as their targets, so the bytes v2.1 repairs are the
bytes the two `REVISE` verdicts were returned against. The governing-contract
digests are recomputed in the companion closure §2.2 and are unchanged from v2.

Two contracts are load-bearing for this correction and were read directly:

```text
…GENERIC_HARNESS_CONTRACT_V2_DRAFT.md         64b8d3f6…af71   §2c:99-106
    accepted as the governing harness contract "as corrected, in order, by
    v2.1, v2.2, v2.3, and v2.3.1" — OFFICINA_GENERIC_HARNESS_SIGNATURE.md,
    signed 2026-07-26. §2c carries forward verbatim; none of the four
    corrections touches it.
…T_ACTIVATION_PROTOCOL_V2_CORRECTION.md       cd106d7f…c40c   :231-238, :248-257
```

---

## §2. Repair 1 — closing indirect reads in `generic_harness.py`

**Design constraint, stated first.** This repair introduces **no taint
analysis, no call graph, no fixpoint and no soundness assumption about value
flow**. Every rule below is an occurrence count, a position match, a name match
or a node-type match over a single AST walk of the five production roots of
§P1-3.1. That is the property `X M-2` required and the property §2.5's design
already has; v2.1 extends the same discipline to the routes that did not go
through a governed Name or a key literal.

### §2.1 Why v2's rules did not reach these constructs

Recomputed from the composite's own bytes, not from the X line's summary:

```text
F-1  S-7's forbidden-name set — which contains locals, globals, vars, getattr,
     setattr, delattr, eval, exec, compile, __import__, importlib and the
     builtin open — is scoped by its own first line to "the PCS and role roots"
     (composite :2581). Where the framers mean every root they say so: S-23
     says "no production root" (:2626) and CHANGE 5 says "all five roots"
     (:2638). The two-root scope is deliberate, not an omission.
F-2  Invariant 80 (:2749) constrains generic_harness.py only by the five-root
     list, the scoped import map, and the absence of signal/_signal/sys. It
     imposes no reflective-name rule.
F-3  §P1-3.2 gives generic_harness.py a 17-module allowlist — including ast,
     dataclasses, json, re, typing and weakref — which S-1's "exactly six /
     exactly three Import nodes, no ImportFrom" cannot describe. The S-1..S-24
     grammar is therefore the process-control-root grammar.
F-4  v2's own A-T9 fixture 5 uses open() inside this scope, which is only
     coherent if S-7's ban on the builtin open does not reach it. v2 was
     internally consistent about the scope and simply did not close it.
F-5  CONSEQUENCE. In the root where every governed value actually lives,
     locals, vars, getattr, .values(), .items(), mapping iteration, **
     unpacking and attribute access were all available, and none of
     S-25a..S-25h fires on them, because none of them mentions a governed Name
     or a governed key literal.
```

`S-12` (`:2601`) independently bars `subprocess`, `Popen`, `fork`, `waitpid`,
`kill`, `killpg` and `system` from `generic_harness.py` on every path, so the
**control-plane** half of §2.12's amended sentence was never at risk. What was
at risk is the broader half — that the values reach no capacity, custody,
spend, selection, qualification, comparison, Q/C, datum, evidence, outcome or
Proof sink — and those sinks live in the peer layer. The X line's scoping of
the consequence is exact and is adopted here.

### §2.2 `S-25i` — the reflection and name-indirection lockdown

```text
S-25i  REFLECTIVE AND NAME-INDIRECTION LOCKDOWN, ALL FIVE PRODUCTION ROOTS.
       In every root of §P1-3.1 — src/philosophia/officina/generic_harness.py
       INCLUDED, and not only the PCS and role roots — none of the following
       may appear, in any syntactic position, at any depth:

  (i)  as a plain Name, or as the attr of any Attribute node:
         locals, globals, vars, dir, eval, exec, compile, __import__,
         importlib, getattr, setattr, delattr, hasattr, inspect, copy, pickle,
         marshal, operator, builtins, __builtins__, _getframe, f_locals,
         f_globals, f_back, gi_frame, tb_frame, cr_frame, __subclasses__,
         __mro__, __bases__, __globals__, __code__, __func__, __self__,
         __wrapped__, __reduce__, __reduce_ex__, __getstate__, __setstate__
  (ii) as an Attribute whose attr begins AND ends with two underscores —
         NO DUNDER ATTRIBUTE ACCESS OF ANY KIND, on any object, anywhere in the
         five roots. This closes x.__dict__, x.__class__,
         type(x).__mro__, obj.__getattribute__, cls.__slots__ and every future
         dunder route without enumerating them. The __future__ IMPORT is an
         Import node, not an Attribute, and is unaffected.
  (iii) as a qualified Attribute, these exact reflective forms:
         ast.literal_eval, ast.parse applied to any value other than a source
         string read at the manifest-verification site, dataclasses.asdict,
         dataclasses.astuple, dataclasses.fields, dataclasses.replace,
         typing.get_type_hints, json.JSONDecoder, json.JSONEncoder,
         re.sub / re.match / re.search applied to a governed mapping Name or a
         carrier Name (§2.3, §2.4)
  (iv) as a Call whose func is a Subscript, an Attribute of a Call, a Lambda
       (already banned by S-2), or any expression other than a plain Name, a
       bound name, or an approved qualified Attribute of §2.4's table

       ⇒ "S-25i: reflective or name-indirection construct in a production root"

S-25i-N1  WHAT S-25i DOES NOT ADD. The builtin open is NOT added to
          generic_harness.py's forbidden set. The peer layer's durable file I/O
          is signed and this packet does not withdraw it. The reload route that
          open() enables is closed by S-25j, at the mapping, not by removing the
          peer layer's ability to read its own records. v2's A-T9 fixture 5
          therefore remains exactly as written and still fires S-25d.
S-25i-N2  json, hashlib and hmac remain available. They are constrained only at
          the enumerated sites of §2.4 when their operand is a governed mapping
          or a carrier.
S-25i-N3  dataclasses remains available for every purpose EXCEPT representing a
          t-process-claim.v1 or t-active-lease.v1 object (§2.3 M-R1). The four
          reflective dataclasses entry points at (iii) are forbidden outright,
          because each converts an object into a positional or keyed view of its
          fields without naming any of them.
S-25i-N4  SCOPE HONESTY. S-25i is root-wide, which is broader than the two
          identity fields strictly need. A function-scoped lockdown would not be
          closed: a helper defined outside the scope could be called with a
          governed operand, and deciding that would need a call graph — exactly
          what M-2 forbids. The breadth is the price of decidability and is
          counted in the blast radius at §6.
```

**E2 disposition.** `locals()["attested_pid"]` names `locals`, which is
forbidden by `S-25i(i)` in `generic_harness.py`. It no longer matters that the
identifier `attested_pid` appears as a `str` Constant rather than a `Name`, and
no rule has to reason about what the reflective call returns.

### §2.3 `S-25j` — the pinned mapping representation and its position discipline

#### §2.3.1 Representation, pinned

```text
M-R1  REPRESENTATION. In the five production roots, a philosophia.officina.
      t-process-claim.v1 object and a philosophia.officina.t-active-lease.v1
      object are each represented in memory as a PLAIN MAPPING with str keys
      and no attribute surface. A dataclass, a class instance, a NamedTuple, a
      SimpleNamespace, an attribute-bearing wrapper, a subclass of dict, or any
      object exposing either key as an attribute MAY NOT represent either
      schema. A ClassDef is already banned outright by S-2 in the PCS and role
      roots; M-R1 bans this specific representation in all five.
M-R2  ATTRIBUTE FORM OF THE TWO KEYS, BANNED OUTRIGHT. No Attribute node whose
      attr is controller_pid or process_group_id appears anywhere in the five
      roots, on any object, in any position. This is a pure name match and
      needs no knowledge of what the object is.
```

`M-R1` and `M-R2` together close **E3** — `claim.controller_pid` — twice: the
object cannot have that attribute, and the syntax naming it is banned.

#### §2.3.2 The governed mapping Names — a closed set with closed producers

```text
M-R3  GOVERNED MAPPING NAMES, EXACTLY THREE:
          claim_mapping      a t-process-claim.v1 mapping
          lease_mapping      a t-active-lease.v1 mapping
          occupant_mapping   the EEXIST occupant's mapping (§2.10.3 X-2/X-3)
      Each is a plain Name, assigned exactly once, never rebound, deleted,
      parameterized outside the approved signatures of §2.4, used as a
      comprehension or for target, or passed to any construct not in §2.4's
      table. S-4's assign-once discipline composes with this and is not relied
      on in its place.
M-R4  CLOSED PRODUCERS. A governed mapping Name is bound ONLY by one of the
      producer sites MS-3, MS-4, MS-5 or MS-11 of §2.4, and by nothing else.
      No other expression in the five roots may yield a claim or lease mapping:
      every route from durable bytes to a mapping passes MS-2 -> MS-3, and
      every route from the wire to a mapping passes MS-4.
M-R5  CLOSED CONSUMERS. A governed mapping Name may occur ONLY as the single
      positional operand of an approved call of §2.4's table, and in no other
      syntactic position whatsoever. ANY OTHER OCCURRENCE IS A STATIC
      VIOLATION; absence from the table is sufficient for rejection, and no
      catalogue of prohibitions is required for the closure. This is the same
      occurrence discipline §2.5 already applies to the two parsed Names, moved
      up one level to the object that carries them.
```

#### §2.3.3 The rule

```text
S-25j  GOVERNED MAPPING DISCIPLINE, ALL FIVE PRODUCTION ROOTS.
       M-R1..M-R5 hold, and in particular, on a governed mapping Name:
         - no Attribute access of any kind, including but not limited to
           .values, .items, .keys, .get, .pop, .popitem, .copy, .setdefault,
           .update, .fromkeys, .clear
         - no iteration: no for-target, no comprehension or generator iterable,
           no iter/next/enumerate/zip/reversed/sorted/min/max/sum/any/all/len
           applied to it
         - no ** unpacking, in a Call keywords entry with arg None, in a Dict
           literal, or in any other position
         - no destructuring: it is never the value of a tuple/list Assign
           target, never Starred, never unpacked
         - no Subscript with a non-literal key operand, and no Subscript with a
           literal key operand outside ACC-2 and ACC-3
         - no membership test, comparison, boolean context, truth test, or
           equality against another mapping
         - no generic serialization or reflection — no json.dumps, json.dump,
           str, repr, format, f-string, encode, pickle or copy — outside the
           single ACC-4 site MS-6
         - no logging, diagnostic, frame, request-builder, journal-key,
           retry-key, handle-table, capacity, custody, spend, settlement,
           selection, qualification, comparison, blinding, Q, C, datum,
           evidence, outcome or Proof expression, at any distance
       ⇒ "S-25j: governed claim or lease mapping used outside its approved
          call sites"
```

**E1 disposition.** `list(claim.values())[5]` fails `S-25j` three separate
times: `.values` is an Attribute on a governed mapping Name; `list` is not an
approved call for that operand; and the result is bound to a Name that is not a
governed Name and has no approved producer. If the mapping were instead bound to
a Name outside `M-R3`, it would fail `M-R4` at its producer, because the only
expressions in the five roots that yield a claim or lease mapping are `MS-3`,
`MS-4`, `MS-5` and `MS-11`, each of which binds a governed Name.

**Scope note, so the rule is not read wider than it is.** `S-25j` constrains
**governed mapping Names only**. Ordinary peer-layer mappings — settlement
records, meter evidence, journal entries, configuration — are entirely
unaffected, and `.values()`, `.items()` and `**` remain available on them.
Only the claim and the lease are pinned.

### §2.4 The approved call-site table — exact sites, exact operands

This table is the whitelist that `M-R5` closes over. **A call site not in this
table, or a call in this table with a different operand, is a static violation
by absence.** No semantic clause such as "and equivalent operations are
forbidden" appears anywhere in this correction; the table, not a prohibition
list, is the closure.

| # | Enumerated function | Exact call it may contain | Operand | Result binds to |
|---|---|---|---|---|
| `MS-1` | `_claim_path(process_id)` | one path construction over the fixed constant `successor/officina/runtime/T_PROCESS_CLAIMS/` and the 64-hex `process_id` stem | `process_id` | `claim_path` |
| `MS-2` | `_read_claim_bytes(path)` | exactly one `open(path, "rb")` and exactly one `.read()` | `claim_path` **or** the occupant path, and nothing else | a carrier Name (§2.5) |
| `MS-3` | `_claim_mapping_from_bytes(carrier)` | exactly one `json.loads(carrier)` | one carrier Name | `claim_mapping` or `occupant_mapping` |
| `MS-4` | `_build_claim_mapping(...)` — **`C-1`** | exactly one Dict literal whose twenty keys are the twenty string literals of `:231-238`, with `controller_pid` and `process_group_id` taking the two §2.5 Zone 2 keyword positions and no other | the §2.5 Zone 2 Names, once each | `claim_mapping` |
| `MS-5` | `_lease_from_claim(claim_mapping)` — **`C-2`** | exactly one `dict(claim_mapping)` followed by exactly five literal-key assignments naming only the five lease-only keys of `:241-246` | `claim_mapping` | `lease_mapping` |
| `MS-6` | `_canonical_claim_bytes(mapping)` — **`ACC-4`** | exactly one canonical serialization of the whole mapping in the encoding the peer contract already fixes for durable records, and exactly one `.encode("ascii")`; **v2.1 invents no encoding** | `claim_mapping` **or** `occupant_mapping` | a carrier Name |
| `MS-7` | `_process_claim_sha256(carrier)` — **`ACC-5`** | exactly one `hashlib.sha256(carrier)` and exactly one `.hexdigest()` | one carrier Name | a 64-lowercase-hex `str` |
| `MS-8` | `_claim_identity_pair(claim_mapping)` — **`ACC-2`** | exactly two Subscripts, keys the string literals `"controller_pid"` and `"process_group_id"` | `claim_mapping` or `occupant_mapping` | a 2-tuple of `int` |
| `MS-9` | `_lease_identity_pair(lease_mapping)` — **`ACC-3`** | exactly two Subscripts, the same two literals | `lease_mapping` | a 2-tuple of `int` |
| `MS-10` | `_validate_claim_mapping(mapping)` | the schema validation of `X-2`: the twenty-key set, exact types, strict `int`, recursive scientific-field rejection. It reads keys **only** by literal subscript and binds **no** value of either identity key to a Name; the two identity keys are validated through `MS-8` and its boolean result alone | `claim_mapping` or `occupant_mapping` | a boolean |
| `MS-11` | the `EEXIST` occupant load (§2.10.3) | `MS-2` then `MS-3`, in that order, at exactly one site | the occupant path | `occupant_mapping` |
| `MS-12` | `_install_claim(claim_path, carrier)` — the `C-1` durable write | exactly one atomic no-replace write of the carrier bytes under `T_RUNTIME.lock` | `claim_path`, one carrier Name | none |

```text
MS-R1  Each function in this table is defined EXACTLY ONCE in the five roots
       and is called only at the sites enumerated in §2.5 and §3.3.
MS-R2  No function in this table has a default argument, a *args or **kwargs
       parameter, a fallback branch, a cache, an attribute assignment, or a
       second return shape.
MS-R3  No function in this table returns a governed mapping Name's value, a
       carrier's slice, or any individual field of either identity key. MS-8
       and MS-9 return the 2-tuple that ACC-R2 governs; every other row returns
       bytes, a boolean, a 64-hex str, a mapping, or nothing.
MS-R4  ACC-2 is permitted to accept occupant_mapping so that §2.10.3's X-3
       cross-field conjunct has an accessor. This is a bookkeeping precision
       inside the already-closed Y-M1 repair, not a new consumer: X-3 was
       already required by v2 §2.10.3, it produces a boolean only, and it falls
       inside C-3's operation class. ACC-R2 at §4 names its site explicitly so
       that it is single-valued rather than implied.
```

### §2.5 `S-25k` — the carrier discipline

The canonical byte string of a claim **contains** both restricted integers.
Reading it wholesale is therefore itself a route to them, and pinning the
mapping without pinning the bytes would leave the same defect one level down.

```text
CR-1  RESTRICTED_CLAIM_CANONICAL_BYTES is the class containing every byte
      string that is, or is derived from, the canonical serialization of a
      t-process-claim.v1 or t-active-lease.v1 object, however obtained — from
      MS-6, from a durable read at MS-2, from an archived copy, or from any
      future route. A read-then-reserialize does not launder it.
CR-2  CARRIER NAMES, EXACTLY THREE:
          canonical_bytes   the bytes MS-6 produces for the claim being installed
          claim_bytes       the bytes MS-2 reads from the durable claim path
          occupant_bytes    the bytes MS-2 reads from the EEXIST occupant path
      Each is assigned exactly once, never rebound, never deleted, never
      parameterized outside the approved signatures of §2.4.
CR-3  CARRIER POSITIONS, CLOSED. A carrier Name may occur ONLY as:
        (a) the single operand of MS-3;
        (b) the single operand of MS-7 (ACC-5);
        (c) the byte operand of MS-12, the atomic no-replace install;
        (d) one side of the single X-1 byte-equality comparison of §2.10.3,
            whose other side is the other carrier and whose result is a boolean.
      NOWHERE ELSE.
CR-4  ON A CARRIER, THESE ARE STATIC VIOLATIONS: any Subscript or slice; any
      index; decode, split, partition, strip, find, index, replace, startswith,
      endswith or any other bytes method; any regex application; any iteration,
      comprehension, unpacking or destructuring; any len, ord, int, str, repr,
      format or f-string; any second hash, second serialization, or alternate
      encoding; any logging, diagnostic or frame placement; any return other
      than the enumerated ones.

S-25k  CARRIER DISCIPLINE. CR-1..CR-4 hold over the five production roots, as
       an occurrence count and position match on exactly three Names.
       ⇒ "S-25k: canonical claim bytes bound or used outside the carrier
          positions"
```

### §2.6 One-to-one disposition of the three demonstrated bypasses

| X-line construct | Rule that fires | Why, mechanically |
|---|---|---|
| `_vals = list(claim.values()); _leaked = _vals[5]` | `S-25j` | `.values` is an Attribute on a governed mapping Name; `list` is not an approved call for that operand; `_vals` has no approved producer under `M-R4`. Three independent violations. |
| `_leaked = locals()["attested_pid"]` | `S-25i(i)` | `locals` is a forbidden Name in **all five** roots, `generic_harness.py` included. The string-Constant identifier is irrelevant. |
| `_leaked = claim.controller_pid` | `S-25j` via `M-R1` **and** `M-R2` | the object may not have an attribute surface for these schemas, and the Attribute `attr` `controller_pid` is a banned name match on its own. |

Variants, each rejected by the same three rules with no new clause:

```text
a, b, *rest = claim_mapping.values()          S-25j  (.values; destructuring)
for k, v in claim_mapping.items():            S-25j  (.items; for-target)
for k in claim_mapping:                       S-25j  (iteration)
{**claim_mapping}                             S-25j  (** unpacking)
dict(**claim_mapping)                         S-25j  (** unpacking)
f(**lease_mapping)                            S-25j  (** unpacking)
[claim_mapping[k] for k in claim_mapping]     S-25j  (non-literal key; iteration)
sorted(claim_mapping.values())[5]             S-25j  (.values; sorted)
next(iter(claim_mapping.values()))            S-25j  (.values; iter; next)
max(claim_mapping.values())                   S-25j  (.values; max)
json.dumps(claim_mapping)  outside MS-6       S-25j  (serialization off-site)
vars(claim_obj)                               S-25i  (vars)
getattr(claim_mapping, "controller_pid")      S-25i  (getattr) + M-R2
claim_obj.__dict__["controller_pid"]          S-25i  (dunder Attribute)
dataclasses.asdict(claim_obj)                 S-25i(iii) + M-R1
globals()["attested_pgid"]                    S-25i  (globals)
eval("attested_pid")                          S-25i  (eval)
canonical_bytes[40:47]                        S-25k  (CR-4 slice)
re.search(rb"\"controller_pid\": (\d+)", canonical_bytes)
                                              S-25k  (CR-4 regex) + S-25i(iii)
int(claim_bytes.decode().split(":")[6])       S-25k  (CR-4 decode, split)
```

**Every one of these is rejected by absence from an enumerated position, not by
presence in a prohibition list.** The catalogue above is illustrative and
normatively redundant, exactly as §2.5.4 is in v2.

### §2.7 Why the extended rule is still decidable

```text
D-5  S-25i is a NAME MATCH and a NODE-TYPE MATCH. No resolution, no import
     chain, no aliasing question: an identifier either appears in the parsed
     AST of a root or it does not, and an Attribute's attr either is a dunder
     or is not.
D-6  S-25j is an OCCURRENCE COUNT and POSITION MATCH over exactly three Names,
     plus a representation check that is a node-type match (no ClassDef, no
     dataclass decorator, no NamedTuple base for these two schemas) and a name
     match (M-R2).
D-7  S-25k is the same discipline over exactly three more Names.
D-8  M-R4's closure is decidable because the producer set is four enumerated
     call sites, and the durable-read route to a mapping is MS-2 -> MS-3 with
     both sites enumerated. §P1-13.7 (:2357-2368) already gives each durable
     artifact exactly one open site, which is what makes the anchor sound; NC-2
     of v2 §2.6.5 relies on the same property and is unchanged.
D-9  NO RULE ADDED HERE REQUIRES A SOUND TAINT ANALYSIS, A CALL GRAPH, OR A
     FIXPOINT. The whole of S-25a..S-25m remains a single AST walk over the
     five roots. This is the property X M-2 demanded and v2.1 does not spend it.
```

### §2.8 What Repair 1 preserves exactly

```text
P-1  The occurrence-count design for the two DIRECT PARSED NAMES is UNCHANGED.
     V-1..V-9, Z1-R1..Z1-R6, Z2-R1..Z2-R5, the exactly-three count of Z2-R4,
     the "absence is sufficient" closure of Z2-R5, the §2.5.4 redundant
     catalogue, and the §2.5.5 decidability argument all carry forward
     verbatim. The X line confirmed this part of the mechanism works; v2.1 adds
     to it and subtracts nothing.
P-2  S-25a, S-25b, S-25c, S-25f and S-25h are UNCHANGED in text.
P-3  A-T9's five fixtures are UNCHANGED, including fixture 5's use of open(),
     which still fires S-25d.
P-4  S-7's committed bytes are UNTOUCHED. S-25i states the wider scope as its
     own rule rather than editing a signed rule's text, so no existing
     composite rule changes shape.
```

---

## §3. Repair 2 — `C-5`, the canonical claim lineage digest

### §3.1 The finding, re-derived

```text
REQUIRED BY THE SIGNED CHAIN:
  …GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:99-102
     "T_PROCESS_STARTED (P1->P2): claim durable and verified. Durable: the
      non-state-bearing start event carrying process_claim_sha256."
     — governing, per OFFICINA_GENERIC_HARNESS_SIGNATURE.md: the second signed
       token accepts V2_DRAFT "as corrected, in order, by v2.1, v2.2, v2.3, and
       v2.3.1", and none of the four corrections touches §2c.
  …T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:248-257
     the final process record's key set contains process_claim_sha256.

FORBIDDEN BY v2 AS WRITTEN:
  §2.6.2   "Exactly four consumers exist."
  P-R1     "C-1..C-4 IS THE COMPLETE LIST."
  P-R4     "...or any record class other than the claim and the lease."
  §2.6.1   "THERE IS NO DECLASSIFYING OPERATION."

AND INVISIBLE TO THE ACCESSORS:
  the hash reads the whole canonical byte string. It binds neither integer and
  uses neither key literal, so ACC-R1 and ACC-R2 never fire on it — which is
  also, precisely, why it is safe once it is written down.

CONCLUSION. The Y line is right. On the v2 bytes the whitelist cannot be
implemented while preserving both its own rules and the signed lineage. Y-C1 is
not closed as dispositioned, and Option A is not selectable until it is.
```

### §3.2 `C-5`, stated exactly

```text
C-5  THE CANONICAL CLAIM LINEAGE DIGEST.

     PRECONDITION. The claim mapping has passed complete canonical validation
     at MS-10: the exact twenty-key set of :231-238, exact types, strict int,
     recursive scientific-field rejection, the process_id recomputation from
     its signed preimage (:296-299), scientific_outcome the literal false, and
     the §2.2 cross-field invariant on its identity keys. NO DIGEST IS COMPUTED
     OVER AN UNVALIDATED, PARTIAL, OR NON-CANONICAL MAPPING.

     OPERATION. EXACTLY ONE SHA-256, at MS-7 (ACC-5), over the COMPLETE
     canonical claim byte string produced at MS-6 (ACC-4), yielding
     process_claim_sha256 as 64 lowercase hex.

     KEYS READ INDIVIDUALLY AT THIS CONSUMER: NONE. The operand is the whole
     byte string and never a field, a subset, a projection, or a re-encoding.

     DESTINATIONS, EXACTLY TWO, BOTH ALREADY SIGNED:
       D-1  the durable non-state-bearing T_PROCESS_STARTED event
            (…GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:99-102)
       D-2  the t-process-record.v1 key process_claim_sha256
            (…T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:248-257)

     FORBIDDEN, EXPLICITLY AND WITHOUT EXCEPTION:
       - a hash over any partial field set, any single field, or any projection
       - a hash under any encoding other than the one canonical encoding the
         peer contract already fixes for durable records
       - a second digest, a secondary digest, a truncated digest, a keyed
         digest, an HMAC, or any digest of the identity fields alone
       - any derived numeric identity, index, ordinal, bucket, or shortening
         computed from the digest
       - any destination other than D-1 and D-2
       - any invocation before MS-10 returns true
```

**The one enumerated second invocation of `ACC-5`, so the count is
single-valued.** §2.10.3's `X-4` compares `SHA-256` of the occupant's canonical
bytes against the digest this install computed. That is a **second call of the
same accessor**, on `occupant_bytes`, whose result is consumed **inside the
`X-4` boolean conjunct and nowhere else**, and which reaches **neither** `D-1`
**nor** `D-2`. It produces no lineage value; it is a comparison value in the
`C-3`/`C-4` boolean class. `C-5`'s "exactly one" governs the digest that reaches
a destination; `ACC-5` has exactly two call sites and no third.

### §3.3 The centralized accessors

```text
ACC-4  _canonical_claim_bytes(mapping) -> bytes          [MS-6]
       the SOLE producer of a canonical claim or lease byte string in the five
       roots, and the SOLE generic-serialization site permitted on a governed
       mapping. It binds no field, reads no key, indexes nothing, and returns
       a carrier of §2.5.
ACC-5  _process_claim_sha256(carrier) -> str             [MS-7]
       the SOLE hash accessor over a carrier. Exactly one hashlib.sha256 call
       and exactly one .hexdigest(). Its parameter is one carrier Name and it
       has no second parameter, no default, no keyword, and no branch.

ACC-R5  NEITHER ACC-4 NOR ACC-5 MAY BIND, EXPOSE, ITERATE, LOG, RETURN, SLICE,
        DECODE, COMPARE, OR OTHERWISE SURFACE EITHER IDENTITY FIELD
        INDIVIDUALLY. Neither function body contains a Subscript, an Attribute
        other than the two enumerated method calls, a slice, a loop, a
        comprehension, a decode, a split, a regex, a format, or a conditional
        branch over its operand. This is checked as a node-type match by
        S-25k, not inferred.
```

`RESTRICTED_PROCESS_IDENTITY` gains one member, so that a value recovered by any
route re-enters the class rather than escaping it:

```text
§2.6.1 (f)  ADDED — any value of either identity key that is recovered,
            reconstructed, inferred, or otherwise obtained from a claim-lineage
            digest, from a carrier of RESTRICTED_CLAIM_CANONICAL_BYTES, or from
            any durable or archived form of either, by any route whatsoever.
            The moment such a value is bound it is class member (f) and every
            rule of §2.6 and §2.5 applies to it unchanged.
```

### §3.4 The one-way classification boundary

```text
DC-1  MODEL, SINGLE-VALUED. process_claim_sha256 is THE SOLE NAMED
      DECLASSIFICATION from RESTRICTED_PROCESS_IDENTITY and from
      RESTRICTED_CLAIM_CANONICAL_BYTES. There is exactly one, produced at
      exactly one site (MS-7) from exactly one operand shape (a validated
      complete canonical carrier), and there is never a second. The alternative
      model — a restricted derived class carrying two destinations — is
      REJECTED for the reason at §3.5.
DC-2  DECLASSIFIED IS NOT UNCONSTRAINED. Declassification means exactly that
      the digest is not a member of RESTRICTED_PROCESS_IDENTITY and does not
      inherit C-1..C-4's closure. It does NOT mean the digest is free. Its own
      positive classification is DC-3 and DC-4, and every deviation routes by
      P-R5.
DC-3  WHAT IT IS. An INTEGRITY AND LINEAGE IDENTIFIER of a validated durable
      record. It is never process identity, never process authority, never a
      handle, never a selector, and never a name of anything addressable.
DC-4  WHAT IT MAY NEVER FEED. The digest may not enter, at any distance and
      through any number of intermediate bindings: addressing or selection of
      any kind; signalling; waiting; any process-control primitive; any request
      builder for the nine opcodes; a handle-table key or a handle comparison;
      a journal key or a retry key; capacity observation; custody disposition;
      spend or settlement input; qualification, comparison, or blinding; a Q or
      C input; a scientific datum, observation, evidence, outcome, or Proof.
      Its ONLY destinations are D-1 and D-2.
DC-5  ONE-WAY. No route in the five production roots may invert, search,
      enumerate against, or otherwise attempt to recover a claim field from a
      digest. Constructing a candidate claim in order to compare digests
      requires binding both identity integers, which is a S-25c and S-25j
      violation BEFORE any hash is reached, so the attempt fails statically at
      its first line rather than at the hash.
DC-6  NO SECOND DIGEST. process_claim_sha256 is the only value derived from a
      carrier in the five roots. No other digest, checksum, fingerprint,
      shortened form, or numeric projection of a claim or lease exists.
DC-7  DEVIATION IS DOMINANT INVALIDITY. A digest computed over an unvalidated,
      partial, or non-canonical operand; a digest reaching any destination
      other than D-1 and D-2; and any access to either key or to a carrier
      outside ACC-1..ACC-5 are each routed RECORD-FIRST to the process-
      invalidity disposition of §P1-11.6 and §P1-13.5, with invalidity
      dominant, exactly as P-R5 already requires. This adds no new route; it
      names C-5's failures into the existing one.
```

### §3.5 Why the declassification model, and why it cannot launder

**Why not the restricted-derived-class model.** Both models were specified and
one had to be chosen, single-valued. The derived-class model would attach a
two-destination restriction to the digest and require that restriction to travel
with it. But the digest's two destinations are owned by contracts **outside this
packet's mandate**, and both feed further already-signed chains: the lease's
`prior_charge_event_sha256` is seeded to the `T_PROCESS_STARTED` entry hash
(`…GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:103-106`), and `t-process-record.v1`
is read by archival and verification surfaces the packet explicitly does not
constrain (v2 §3.2, archival sets `:88-97`). A restricted class travelling into
those chains would impose this packet's rules on contracts it does not own —
which is the *same* error shape as `YV2-C1` itself, one layer out. The
declassification model is closed **inside** this packet's scope: it names one
site, one operand shape, one output, and hands the output to the signed chain
that already governs `process_claim_sha256` everywhere it appears.

**Why it cannot launder the underlying fields.**

```text
WL-1  NO FIELD-LEVEL ROUTE EXISTS. ACC-4's operand is a governed mapping Name
      and ACC-5's operand is a carrier Name. Neither function body may contain
      a Subscript, slice, decode, split, regex, loop, comprehension, format, or
      branch over its operand (ACC-R5, checked by S-25k as a node-type match).
      Neither returns a field. So no AUTHORIZED route converts the hash path
      into either integer, and the check for that is syntactic, not semantic.
WL-2  THE INVERSE ROUTE FAILS EARLIER THAN THE HASH. Any attempt to recover a
      field by constructing candidate claims and comparing digests must first
      bind a candidate value for controller_pid or process_group_id. That
      binding is a fourth occurrence of a governed Name (S-25c) or a
      non-approved construction of a claim mapping (M-R4/S-25j) and is rejected
      before any hash expression is parsed.
WL-3  DISCLOSED RESIDUAL, STATED RATHER THAN GLOSSED. SHA-256 is one-way, but
      it is NOT a confidentiality barrier for a low-entropy unknown. An actor
      already holding the other eighteen canonical field values could enumerate
      candidate identity pairs and match the digest. A-P4c forces
      attested_pgid == attested_pid, so the search is over at most 4194304
      single values and is trivially exhaustible. THIS PACKET DOES NOT REST ANY
      CLAIM ON PREIMAGE RESISTANCE, and a reviewer should not have to discover
      this for themselves.
WL-4  WHY WL-3 IS NOT A NEW EXPOSURE, AND NOT A CAPABILITY TRANSFER.
      (a) The eighteen other canonical values are obtainable only by reading
          the claim. Its restricted-key reads are ACC-2-only and its whole-byte
          reads are pinned to MS-2/MS-6 with the carrier positions of CR-3, so
          no authorized route in the five roots yields them for this purpose.
      (b) Under A3 the supervisor is same-UID with every process in this
          contract and may already read every pid on the system from /proc
          unilaterally (v2 §5.6; composite :1942 "stop, kill, or delay any
          same-UID process", :1952 "Kernel power is admitted; Officina
          authorization is not conferred"). Recovering a pid therefore conveys
          ZERO operating-system information the actor did not already have.
      (c) A recovered value confers no AUTHORIZED addressing: no request field
          of any of the nine opcodes accepts a pid (composite :1240;
          A-R1..A-R8), and the moment such a value is bound it is class member
          (f) of §3.3, so every sink rule of §2.6 applies to it unchanged.
      (d) Therefore the digest transfers no capability and no authorization. It
          weakens no property v2 claimed, and WL-3 is a disclosure about what
          a hash does and does not buy — not a defect introduced by C-5.
```

### §3.6 The destination search, run exhaustively

`C-5`'s destination set was computed, not assumed. Every occurrence of
`process_claim_sha256` in the repository's committed markdown was examined:

| Occurrence | Status |
|---|---|
| `…GENERIC_HARNESS_CONTRACT_V2_DRAFT.md:101` | **`D-1`.** Governing: the signature accepts V2_DRAFT as corrected by v2.1/v2.2/v2.3/v2.3.1, none of which touches §2c. |
| `…T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:252` | **`D-2`.** Governing. |
| `…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:1156` and `…V2_DRAFT.md:354` — the `OK`/`CLAIM` reply detail keys `process_id, process_claim_sha256, process_sequence` | **Checked and excluded as a destination of this packet.** Both files are in the supervisor/control-channel chain, which the P1 operative composite's authority level 3 fixes as "immutable historical and provenance evidence only". The composite does not restate that reply matrix, and neither accepted peer contract (`…GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`, `…BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`) contains the key at all. **This packet neither constrains nor relaxes it**, on the `NC-1`..`NC-3` pattern of v2 §2.6.5. |
| `…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md:479` — cached reply bytes | same disposition, same chain. |

**Disclosure, because it bears on the model choice.** If a future round rules
that the `OK`/`CLAIM` reply matrix is live rather than historical, the
declassification model of `DC-1` accommodates it without amendment, because the
digest is not a restricted value and that carriage is governed by whichever
contract owns the reply. The derived-class model would have contradicted it and
would have re-created `YV2-C1` at a new site. **That is a second, independent
reason for the choice at `DC-1`**, and it is stated here rather than left for a
reviewer to find.

### §3.7 Reconciliation with Repair 1

The two repairs meet at exactly one place, and the seam is stated explicitly so
that no implementer has to infer it:

```text
RC-1  ACC-4/ACC-5 (MS-6/MS-7) ARE THE ONE EXPLICIT MAPPING-AND-BYTE CONSUMER
      EXEMPTED FROM THE FIELD-LEVEL ACCESSOR RULES. They are the only sites at
      which a governed mapping may be serialized wholesale and the only sites
      at which a value derived from a carrier is produced.
RC-2  THE EXEMPTION IS BOUNDED BY FOUR CONDITIONS, ALL SYNTACTIC:
        (i)   the operand is a governed mapping Name (ACC-4) or a carrier Name
              (ACC-5), and never a field, a slice, a projection, or a literal;
        (ii)  the mapping has passed MS-10 validation before MS-6 is reached;
        (iii) neither function binds, exposes, iterates, logs, compares, or
              returns either identity field individually (ACC-R5);
        (iv)  the carrier itself is confined to CR-3's four positions, so the
              exemption does not widen into a general byte-reading permission.
RC-3  THE EXEMPTION IS NOT AN EXCEPTION TO S-25j OR S-25k. MS-6 and MS-7 are
      rows of the same approved-call table those rules close over. There is one
      whitelist, not a whitelist plus a carve-out.
RC-4  C-5 CONSUMES NO KEY. It is a consumer of the RECORD, not of the FIELDS.
      That is why it can be authorized without weakening C-1..C-4: the
      field-level closure is untouched, and the record-level operation is
      pinned to one site with one operand and two destinations.
```

---

## §4. The amended rule texts — verbatim replacements

The following v2 rules are **replaced** by the texts below. Every other rule of
v2 stands as written.

### §4.1 `P-R1`, `P-R4`, `P-R5`

```text
P-R1  REPLACED. C-1..C-5 IS THE COMPLETE LIST. Any other read, in any
      production root, of key "controller_pid" or key "process_group_id" from
      any t-process-claim.v1 or t-active-lease.v1 object, and any other
      wholesale read of such an object or of its canonical bytes, is a static
      violation and, at runtime, an unreachable state.

P-R4  REPLACED. NO CONSUMER MAY ROUTE EITHER VALUE TO: a process-control
      primitive (_kill, _killpg, _waitpid, os.kill, os.killpg, os.waitpid); a
      request builder for any of the nine opcodes; a handle-table key, a handle
      selection, or any addressing; a journal key or a retry key; a capacity
      observation, a custody disposition, a spend fact, or a settlement input;
      a selection, qualification, comparison, blinding, Q or C input; a
      scientific datum, outcome, evidence, or Proof; a log, diagnostic, frame,
      or any record class other than the claim and the lease.
      THE SINGLE NAMED EXCEPTION IS C-5, WHICH CONSUMES THE COMPLETE CANONICAL
      BYTE STRING AND NEVER EITHER VALUE INDIVIDUALLY, AND WHOSE OUTPUT IS THE
      DECLASSIFIED LINEAGE DIGEST OF DC-1..DC-7 WITH EXACTLY THE TWO
      DESTINATIONS D-1 AND D-2. C-5 is not an exception to any sink prohibition
      above: a lineage digest is none of those sinks, and DC-4 forecloses each
      of them for the digest as well.

P-R5  REPLACED, one clause. "...or which is reached by a route not in C-1..C-5
      is routed RECORD-FIRST to the process-invalidity disposition of §P1-11.6
      and §P1-13.5..." Everything else in P-R5 is unchanged, including
      invalidity dominance and the closed list of what it is never.
```

### §4.2 `ACC-R1`..`ACC-R4`, and the new `ACC-R5`

```text
ACC-R1  REPLACED. Scoped by SCHEMA, per NC-1, and extended to every access
        form. In the five production roots:
          (a) a Subscript, .get, .pop, ChainMap, or any other access whose key
              operand is the string literal "controller_pid" or
              "process_group_id" against a t-process-claim.v1 or
              t-active-lease.v1 object appears ONLY inside ACC-2 and ACC-3,
              plus the C-1 Dict-literal key names at MS-4 and the C-2
              whole-mapping copy at MS-5;
          (b) an Attribute whose attr is controller_pid or process_group_id
              appears NOWHERE, on any object, in any position (M-R2);
          (c) EVERY access of ANY key of such an object, by ANY form, appears
              only at an approved call site of §2.4's table (M-R5);
          (d) a wholesale read, serialization, or byte-level access of such an
              object appears only at MS-2, MS-3, MS-6 and MS-12, with the
              carrier confined to CR-3.

ACC-R2  REPLACED. The returns of ACC-2 and ACC-3 are unpacked ONLY at:
          the C-3 lease/claim immutability comparison;
          the C-4 §Z4.6 conjunct-7 comparison;
          the §2.10.3 X-3 cross-field conjunct;
        and at no other site. Each unpacked Name occurs exactly once, inside
        its comparison expression, and each site yields a BOOLEAN ONLY. The
        third site was already required by v2 §2.10.3 and is named here so the
        rule is single-valued; it adds no consumer and falls inside C-3's
        operation class.

ACC-R3  REPLACED, extended. No accessor returns a mutable container, caches its
        result, stores it on an attribute, or has a default, fallback, or
        coercing branch. A missing or non-int key is a validation failure
        routed by P-R5. ACC-4 and ACC-5 additionally have no second parameter,
        no keyword parameter, no *args or **kwargs, and no conditional branch
        over their operand.

ACC-R4  REPLACED. ACC-1..ACC-5 are the complete accessor set:
          ACC-1  _identity_from_await_stop(fields)   the wire parse site
          ACC-2  _claim_identity_pair(mapping)       claim/occupant key reader
          ACC-3  _lease_identity_pair(mapping)       lease key reader
          ACC-4  _canonical_claim_bytes(mapping)     sole canonical serializer
          ACC-5  _process_claim_sha256(carrier)      sole hash accessor
        A SIXTH ACCESSOR IS A STATIC VIOLATION.

ACC-R5  NEW. As stated at §3.3.
```

### §4.3 `S-25d`, `S-25e`, `S-25g` — replaced texts

```text
S-25d  REPLACED. accessor closure: every access of a t-process-claim.v1 or
       t-active-lease.v1 object — by literal-key Subscript, by .get/.pop/
       ChainMap, by Attribute, by non-literal Subscript, or by any wholesale
       or byte-level form — occurs ONLY at an approved call site of §2.4's
       table, per ACC-R1(a)-(d)
       ⇒ "S-25d: restricted identity key or record read outside the accessor
          surface"

S-25e  REPLACED. persistent-consumer closure: the returns of ACC-2 / ACC-3 are
       unpacked only at the C-3, C-4 and X-3 comparison sites, each unpacked
       Name occurring exactly once inside its comparison expression and each
       site yielding a boolean; and the return of ACC-5 is consumed only at
       the two destinations D-1 and D-2 (lineage call site) or inside the X-4
       boolean conjunct (occupant call site), and nowhere else
       ⇒ "S-25e: restricted identity value or lineage digest used outside a
          whitelisted position"

S-25g  REPLACED. no value of RESTRICTED_PROCESS_IDENTITY appears in any record
       constructor other than the claim (C-1) and the lease (C-2), and in no
       logging, formatting, capacity, custody, spend, settlement, selection,
       Q, C, blinding or scientific expression; and the declassified lineage
       digest of C-5 appears in no such expression either, its only permitted
       record destinations being the T_PROCESS_STARTED event (D-1) and
       t-process-record.v1 (D-2)
       ⇒ "S-25g: restricted identity or lineage digest reaches an unauthorized
          record or decision"
```

### §4.4 The new rules, in the `S-` family's existing style

```text
S-25i  as stated in full at §2.2
       ⇒ "S-25i: reflective or name-indirection construct in a production root"
S-25j  as stated in full at §2.3.3
       ⇒ "S-25j: governed claim or lease mapping used outside its approved
          call sites"
S-25k  as stated in full at §2.5
       ⇒ "S-25k: canonical claim bytes bound or used outside the carrier
          positions"
S-25l  CLASSIFICATION CLOSURE. The value returned by ACC-5 at its lineage call
       site reaches only D-1 and D-2. It appears in no addressing, selection,
       signalling, waiting, process-control, request-builder, handle, journal-
       key, retry-key, capacity, custody, spend, settlement, qualification,
       comparison, blinding, Q, C, datum, evidence, outcome or Proof
       expression, and no numeric value is derived from it (DC-3..DC-6)
       ⇒ "S-25l: claim lineage digest reaches an unauthorized destination"
S-25m  COUNT CLOSURE. The five roots contain exactly five accessor definitions
       (ACC-1..ACC-5), exactly five persistent consumers (C-1..C-5), exactly
       three governed mapping Names (M-R3), exactly three carrier Names (CR-2),
       exactly twelve approved call-site rows (§2.4), and exactly two ACC-5
       call sites. Each count is asserted as a number, so an addition fails by
       arithmetic rather than by review
       ⇒ "S-25m: accessor, consumer, governed-name or call-site count changed"

DECIDABILITY. S-25i is a name match and a node-type match. S-25j, S-25k and
S-25m are occurrence counts and position matches over enumerated Names. S-25d,
S-25e, S-25g and S-25l are literal-key, call-site and destination matches over
the same single AST walk. NO RULE IN S-25a..S-25m REQUIRES A SOUND TAINT
ANALYSIS, A CALL GRAPH, OR A FIXPOINT.
```

---

## §5. The schema-reader audit, recomputed for the digest

v2 §2.6.4's table is unchanged and correct: exactly two durable schemas carry
the restricted values, and exactly one signed predicate reads one of them. The
audit is **extended** with the digest row it did not have:

| Schema / surface | Carries `controller_pid` / `process_group_id`? | Carries `process_claim_sha256`? | Disposition |
|---|---|---|---|
| `t-process-claim.v1` | **yes / yes** | no | `C-1`; its canonical bytes are `C-5`'s operand |
| `t-active-lease.v1` | **yes / yes** | no | `C-2`, `C-3` |
| the `T_PROCESS_STARTED` start event | no / no | **yes** | **`D-1`** — declassified digest only; never either integer |
| `t-process-record.v1` | no / no | **yes** | **`D-2`** — declassified digest only; v2 §3.2's finding that it does not inherit the keys is unchanged and correct |
| `t-review-record.v1` | no / no | no | unchanged |
| `t-runtime-invalidity.v1` | no / no | no | unchanged |
| `t-activation-claim.v1` | no / no | no | unchanged |
| `t-freeze-observation.v1` | no / no — own `pgid` key | no | unchanged; `C-4` compares it |
| the four §P1-5.1 singleton spawn records | name collision only, `NC-1`..`NC-3` | no | unchanged |
| `t-pcs.v1` request grammar | no / no | no | unchanged |
| the archival and batch-settlement readers | no / no | **content dependency only** | unchanged; v2 §3.2's row stands. `D-2`'s digest is what those surfaces already read, and its **value** changes with the claim's bytes exactly as v2 already stated |

**Therefore: two durable schemas carry the restricted integers; two further
durable surfaces carry the declassified digest and never the integers; one
signed predicate reads one integer. That is the complete durable surface,
computed rather than asserted.**

---

## §6. Amended counts, blast radius, and handoff

### §6.1 Consumer, accessor and rule counts

| Quantity | v2 | **v2.1** |
|---|---|---|
| persistent consumers | 4 — `C-1`..`C-4` | **5 — `C-1`..`C-5`** |
| centralized accessors | 3 — `ACC-1`..`ACC-3` | **5 — `ACC-1`..`ACC-5`** |
| verifier rules added by Option A | 8 — `S-25a`..`S-25h` | **13 — `S-25a`..`S-25m`** |
| behavioural tests added by Option A | 12 — `A-T1`..`A-T12` | **17 — `A-T1`..`A-T17`** |
| governed mapping Names | not pinned | **3** (`M-R3`) |
| carrier Names | not pinned | **3** (`CR-2`) |
| approved call sites | not tabulated | **12** (`MS-1`..`MS-12`) |
| declassifications from `RESTRICTED_PROCESS_IDENTITY` | 0, asserted | **exactly 1**, named and pinned (`DC-1`) |

### §6.2 Amendments to v2 §5.1, §5.4, §5.5 and the closure's blast-radius table

```text
B-A1  §5.4 "verifier: S-25a-S-25h (eight rules, up from four)"
        BECOMES  S-25a-S-25m (THIRTEEN rules, up from four)
B-A2  §5.4 / §5.5 "tests: A-T1-A-T12 (twelve)"
        BECOMES  A-T1-A-T17 (SEVENTEEN)
B-A3  §5.4 "supervisor code: one parse site; two accessors; four whitelisted
      consumers"
        BECOMES  one parse site; FIVE accessors; FIVE whitelisted consumers;
                 twelve approved call sites; three governed mapping Names and
                 three carrier Names, each occurrence-counted
B-A4  §5.5 blast radius, Option A, ADDS two items that v2 did not price:
        (i)  A ROOT-WIDE REFLECTIVE LOCKDOWN over generic_harness.py that
             S-7 did not previously reach (S-25i). This constrains the peer
             root beyond what the two identity fields strictly need, exactly as
             §2.8.2's J4 generalization constrains the other eight opcodes. It
             is disclosed here rather than hidden inside an identity-only rule.
        (ii) A PINNED IN-MEMORY REPRESENTATION for two peer record classes
             (M-R1), which forecloses a dataclass or attribute-bearing form for
             the claim and the lease. No durable format changes; this is an
             implementation-shape constraint, and it is counted as one.
B-A5  §5.8 "new residual", Option A, ADDS: the claim's canonical digest is a
      one-way lineage identifier whose preimage space for the identity fields
      is small enough to enumerate given the other eighteen fields (WL-3). It
      transfers no capability and no authorization (WL-4), and it is stated
      rather than glossed.
B-A6  UNCHANGED, AND NOT RE-PRICED: signed sentences amended (1); peer-owned
      durable record schemas superseded (0 for A, 2 for B); new durable schemas
      (0 for A); signed validity predicates reopened (0 for A); architectural
      rules inverted (0 for A); wire grammar changed (1 response grammar, no
      request grammar); durable formats changed (1 — P1's own J4);
      collision/idempotency rules changed (1 — EEXIST X-1..X-4); migration
      (none); SELECTABLE TODAY: A yes, B NO.
B-A7  OPTION B'S CORRECTED COUNT IS UNTOUCHED BY THIS CORRECTION: two record
      schemas superseded, one new schema created, one signed acceptance
      predicate reopened, one architectural rule inverted, one PCS write-
      surface property expanded. B remains NON-SELECTABLE behind sub-cells B-1
      and B-2, for authority reasons and not size reasons.
```

### §6.3 Amendments to the v1.3 handoff (v2 §7.2)

```text
STEP 5 AMENDED. "...adds A-R1...A-R8 to §P1-12 as a closed rule set, and
  RESTRICTED_PROCESS_IDENTITY with C-1..C-5, P-R1..P-R5, ACC-1..ACC-5,
  ACC-R1..ACC-R5, NC-1..NC-3, and — new in v2.1 — RESTRICTED_CLAIM_CANONICAL_
  BYTES with CR-1..CR-4, M-R1..M-R5, the MS-1..MS-12 approved call-site table,
  and DC-1..DC-7 as a new subsection of §P1-13."
STEP 6 AMENDED. "...adds S-25a...S-25m to §P1-14.6 CHANGE 3 and updates the
  edit surface from S-1...S-24b to S-1...S-25m."
STEP 7 AMENDED. "...adds A-T1...A-T17 as test rows 92-108."
STEP 11 NEW. "...records that S-25i's reflective-name lockdown applies to all
  five production roots, stated as its own rule so that S-7's committed bytes
  at :2581 are NOT edited and its two-root scope is preserved as written."
STEPS 1, 2, 3, 4, 8, 9, 10 ARE UNCHANGED.
```

---

## §7. Tests added by v2.1

`A-T1`..`A-T12` are unchanged in text, including `A-T9`'s five laundering
fixtures. Added:

```text
A-T13  REFLECTION LOCKDOWN. A build containing each of
           locals()["attested_pid"]
           globals()["attested_pgid"]
           vars(claim_obj)
           getattr(claim_mapping, "controller_pid")
           claim_obj.__dict__["controller_pid"]
           eval("attested_pid")
           dataclasses.asdict(claim_obj)
       is REJECTED STATICALLY, in generic_harness.py specifically and not only
       in the PCS and role roots, and the test asserts that S-25i (or, for the
       fourth and fifth, S-25i together with M-R2) fired by name.

A-T14  MAPPING INDIRECTION. A build containing each of
           _vals = list(claim_mapping.values()); _leaked = _vals[5]
           _leaked = claim_mapping.controller_pid
           a, b, *rest = claim_mapping.values()
           for k, v in claim_mapping.items(): ...
           for k in claim_mapping: ...
           merged = {**claim_mapping}
           f(**lease_mapping)
           [claim_mapping[k] for k in claim_mapping]
           sorted(claim_mapping.values())[5]
           next(iter(claim_mapping.values()))
           json.dumps(claim_mapping)          # outside MS-6
       is REJECTED STATICALLY, and the test asserts S-25j fired by name. The
       first three are the X line's demonstrated bypasses E1 and E3 and their
       destructuring variant, and are asserted individually rather than as a
       group.

A-T15  CARRIER AND C-5 CONFORMANCE.
       (a) the positive case: exactly one ACC-4 call and exactly two ACC-5 call
           sites exist; the lineage digest is computed only after MS-10 returns
           true; it is 64 lowercase hex; it reaches D-1 and D-2 and nothing
           else;
       (b) negative fixtures, each rejected statically with the named rule
           asserted:
             a hash over a partial field set or a single field       S-25k
             a second or alternate encoding before hashing           S-25k
             a second digest, truncated digest, or HMAC              S-25k/DC-6
             canonical_bytes[40:47]                                  S-25k
             claim_bytes.decode().split(":")[6]                      S-25k
             re.search(rb"controller_pid", canonical_bytes)          S-25k/S-25i
             a digest computed before MS-10 returns true             S-25k/DC-7

A-T16  DIGEST CLASSIFICATION. Builds routing process_claim_sha256 into a
       handle selection, a request builder, a journal key, a retry key, a
       capacity observation, a custody disposition, a spend or settlement
       input, a selection or qualification or comparison, a Q or C input, or a
       scientific datum/evidence/outcome/Proof expression are EACH rejected
       statically by S-25l, and the test asserts the rejection rather than the
       absence of an effect. The two permitted destinations D-1 and D-2 are
       asserted to pass.

A-T17  COUNT CLOSURE. The verifier asserts, as numbers: five accessor
       definitions, five persistent consumers, three governed mapping Names,
       three carrier Names, twelve approved call-site rows, two ACC-5 call
       sites, and exactly one declassification. Adding a sixth accessor, a
       fourth governed Name, or a thirteenth call site fails S-25m by
       arithmetic, and the test asserts that specific failure.
```

---

## §8. What v2.1 does not change

### §8.1 The eight findings both confirmation lines accepted as closed

| Finding | v2 locus that must remain intact | v2.1 effect |
|---|---|---|
| `X M-1` | §2.8.1 withdrawal; §2.8.2 thirteen-key `J4` vector with `E-1`..`E-4`; §2.8.3 `R-P1`..`R-P4`; §5.1/§5.5/§7.1/§7.2 step 8 | **none** |
| `X m-1` | §2.3 `A-P4a`..`A-P4d`, fresh `getpgid` authoritative, stored value a mandatory non-null cross-check, `setsid` equality mandatory, no other source | **none** |
| `X m-2` | §2.2 `PID_MAX_LIMIT = 4194304`, `G-1`..`G-6`, the stated platform premise, `A-T8` | **none** |
| `X m-3` | §6.1 Case 1 / Case 2 separated by actor, trigger, citation and status | **none** |
| `Y-C2` | §2.8.2 durable complete representation; §2.8.3 byte-identical redelivery | **none** |
| `Y-M1` | §2.10.1 withdrawal; §2.10.2 boundary-keyed matrix; §2.10.3 `X-1`..`X-4`; §2.10.4 `I-1`..`I-10` | **none in substance.** `ACC-R2` now names the `X-3` site and `§3.2` names the `X-4` occupant hash, so both are single-valued. No row of the matrix, no conjunct, and no routing changes. |
| `Y-M2` | §3.2 withdrawal of the `t-process-record.v1` inheritance claim; the corrected count of two superseded schemas | **none** |
| `Y-m1` | §1.5 `R-1`..`R-4` with `R-4`'s exact scope; §4 | **none** |

### §8.2 The preserved invariants, restated

```text
N-1   The identity conflict is real and loud (v2 §1).
N-2   Option A remains an EXPLICIT BOUNDED LEXICAL WEAKENING of the signed
      "cannot express a PID" sentence, with its own token, old and new text
      side by side, and a plain statement of the cost (v2 §2.12). v2.1 does not
      soften it, does not restate it as equivalent, and GRANTS NO PROCESS-
      CONTROL AUTHORITY. The post-A property remains SYNTACTIC, not dataflow.
N-3   Observing a PID/PGID confers no authorized process control (v2 §5.6,
      A-R1..A-R8). C-5 confers none either (DC-3, DC-4, WL-4).
N-4   Both-or-neither tuple semantics (G-4), the stopped/unreaped direct-child
      proof (A-P1..A-P6), the PID-reuse binding (§2.9), fail-closed absence
      (G-5, G-6, Z1-R6), the J4/replay durability (§2.8), the crash matrix
      (§2.10.2), EEXIST convergence (§2.10.3), the pinned PID bound (§2.2), the
      fresh-PGID rule (A-P4a..d), the fresh-PGID-at-stop-instant rationale, the
      corrected Option B count (§3.2, §5.5), and the corrected /proc rationale
      (§1.5) ALL HOLD UNCHANGED.
N-5   Option B remains NON-SELECTABLE behind sub-cells B-1 and B-2, on
      authority grounds, unchanged by any count in this correction.
N-6   The watchdog-freeze cell AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM remains
      ORTHOGONAL AND UNRESOLVED. v2.1 neither fixes nor worsens it, and P1
      remains non-operative until it is resolved even if A is selected.
N-7   T = NOT_ACTIVATED; the programme claim is OPEN.
N-8   NO SELECTION IS MADE. Neither I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_
      OBSERVATION_ONLY nor I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING
      is chosen, and P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 is neither
      minted nor accepted.
```

### §8.3 Withdrawals — none new

v2's four withdrawn v1 sentences (`W-1`..`W-4` at §8.2) stay withdrawn, and no
v2 sentence is withdrawn by this correction. Two v2 sentences are **replaced**
because the signed chain contradicts them as written:

```text
R-W1  v2 §2.6.2's "Exactly four consumers exist" and P-R1's "C-1..C-4 IS THE
      COMPLETE LIST"                                   REPLACED at §4.1 — the
      enumeration was incomplete against the signed hash lineage. The four
      listed FIELD-LEVEL consumers were and remain correct; what was missing is
      the RECORD-LEVEL consumer.
R-W2  v2 §2.6.1's "THERE IS NO DECLASSIFYING OPERATION"
                                                       REPLACED at §3.4 — there
      is exactly one, it is named, it is pinned to one site with one operand
      shape and two destinations, and it is not a laundering permission (WL-1,
      WL-2).
```

Neither replacement is restated anywhere in v2.1 in its old form.

---

## §9. Weakest points in v2.1, stated by the author

1. **`S-25i` is root-wide, which is broader than the two identity fields
   need.** A reviewer may reasonably hold that a bounded identity correction
   should not impose a reflective-name lockdown on the whole peer root. I chose
   root-wide scope because a function-scoped lockdown is not closed — a helper
   outside the scope could be called with a governed operand, and deciding that
   needs a call graph, which `X M-2` forbids. The cost is disclosed at `B-A4`
   and is not hidden inside an identity-only rule.
2. **`M-R1`'s representation pin is an implementation-shape constraint on a
   peer record class.** It forecloses a dataclass or attribute-bearing claim or
   lease. `S-25j` is deliberately scoped to **governed mapping Names only**, so
   ordinary peer idioms on other mappings are untouched — but a peer layer that
   already represents the claim as a dataclass would have to change shape.
3. **`DC-1`'s choice of the declassification model is mine**, resolved for
   single-valuedness. The reasons are stated at §3.5 and the `OK`/`CLAIM`
   disclosure at §3.6 is a second, independent reason — but a reviewer who
   prefers the restricted-derived-class model would have to reconcile it with
   the digest's onward signed chains, and I could not.
4. **`WL-3` is a real residual and I have not made it disappear.** The digest's
   preimage space for the identity fields is small. I argue at `WL-4` that this
   transfers no capability under A3 and no authorization under P1, and I believe
   that argument. A reviewer who weighs confidentiality rather than
   authorization will still see a one-way function that does not conceal a
   4-million-candidate secret, and should say so.
5. **`§3.6`'s disposition of the `OK`/`CLAIM` reply matrix rests on the
   composite's authority level 3** ("immutable historical and provenance
   evidence only") and on the key's absence from both accepted peer contracts.
   If a reviewer holds that the reply matrix is live under some other route, the
   destination count is three rather than two — and the model at `DC-1` survives
   that, which is exactly why I chose it, but the count sentence would need
   amending.
6. **`ACC-R2`'s new `X-3` site and `§3.2`'s second `ACC-5` call site were found
   by me, not by either reviewer.** They are bookkeeping precisions inside
   already-closed repairs, and I have marked them as such rather than quietly
   folding them in. If a reviewer considers either to be a substantive change to
   `Y-M1`'s closure, that is a finding I would accept.
7. **The five roots are a fixed list.** Everything here is decidable because
   `PRODUCTION_ROOTS` is exactly five paths (`CHANGE 1`, composite `:2558`). If
   a sixth production root is ever added, every count in `S-25m` and every
   closure in `§2` must be re-derived, not extended by analogy.

---

## §10. Negative space

This correction creates nothing executable and authorizes no selection, no X/Y
verdict, no implementation, no commit, no verifier or manifest edit, no code or
test artifact, no process, socket, pipe, fork, exec, signal, wait or `prctl`
operation, no supervisor, PCS, controller, worker or watchdog, no capability,
world, learner, entropy, capacity artifact, custody disposition, result
manifest, spend, datum, outcome, Proof or claim movement. It predicts no
qualification and no comparison outcome. `S-25i`..`S-25m` and `A-T13`..`A-T17`
are specification text, not artifacts. It selects neither option and mints no
token. No existing file was modified. `T` remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`; the watchdog-freeze cell remains unresolved and
orthogonal.
