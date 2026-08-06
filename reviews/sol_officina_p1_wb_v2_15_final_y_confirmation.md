# Officina P1 W-B v2.15 final Y confirmation

## Verdict

`REVISE_OFFICINA_P1_WB_V2_15`

The mechanical figures reproduce, but the produced composite contains live
superseded-generation authority in its normative preamble. Because OR-4 leaves
that preamble text unchanged, the resolved output retains the collision. The
binding also retains a current proof sentence naming composite v1.13 as the
transform source while its complete v6 transform consumes composite v1.15.

This is an independent byte review. The authored closure was treated as an
untrusted locator only. No governing, history, code, test, signature or runtime
artifact was modified. No resolved output or MP-1 candidate was written to any
path.

## Input gate and repository boundary

All six pinned SHA-256 values recomputed exactly:

```text
6a00e058e35ab4f81d80b21d5a6680344596231f1299767a076813691723f26a  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_15_CORRECTION.md
e156d66293a608c9090994ae1016c1055a1c9071b71ea0384c58e7ab2595f4a8  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md
a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_15.md
c9db32bb8b87af691c71c51a6167883cc953a43700798c9654c39d84ad1c2ff2  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V6_DRAFT.md
279f59a2de2d3d382a30463b0c72e08108f93ad3ed15473fee145d6361ebc1f1  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V6_DRAFT.md
59ab82b5d3a7c2f5565d7545a882aad805979aa7d8bf3369fb93cbe1033c2852  reviews/opus5_officina_p1_wb_v2_15_final_repair_closure.md
```

The live checkout was `8d7d14a7609ec29fad81ce4c8e2881bbc33f0965`, one commit after the
requested `60d92dbdb252f0f3179387a1c90d1c61bb737a5d`. A path-restricted diff from
`60d92db` over all six pinned inputs was empty: the reviewed bytes are identical
to the requested commit's bytes. Pre-existing dirty and untracked work was not
touched.

## Delimited regions and composite regions

Each delimiter had cardinality one in each governing file. Extraction excluded
the delimiter lines and retained every intervening LF byte.

```text
HANDOFF
  composite delimiters 8529 / 8592; content lines 8530..8591
  amendment delimiters 1333 / 1396; content lines 1334..1395
  length 4168 bytes
  SHA-256 29a6d7e319335c6f4232d5936e24fae8b6830b83c4313bf1d882e060648e7bb4
  byte-identical across the pair: yes

JOINT
  composite delimiters 5157 / 8297; content lines 5158..8296
  amendment delimiters 1449 / 4589; content lines 1450..4588
  length 225448 bytes
  SHA-256 dcf1473d07638a8a103769bc85238d83bfa2575bf75bf49d626ab725726fde24
  byte-identical across the pair: yes

BODY       630161 bytes  fdd6386b53c0ea4918ff66d49aa23c2b911e2ad72fc0481f7effed5b03f940f5
GUARDDATA    1816 bytes  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
PROVENANCE  22039 bytes  4b7acefb10829c8f1dfef4ae506dc060ecf3306a1b08a7937a5892ab92928fbe
NORMATIVE  631977 bytes  0fd3d8b396a7de754f1b7df7159777e76702800b91f57b9cfbe7e17caea16c9d
H_FILE     668002 bytes  a41c142465c3ab0e3dfc565b6f2c1767f1b43481c28933544d72777d6e76113a
```

## Member and provenance accounting

```text
MS-2                    79 rows; 79 distinct paths; 79 distinct digests
MS-3                     7 rows;  7 distinct paths;  7 distinct digests
MS-2 intersection MS-3  0 paths
recorded M2+M3          86 rows; 86 distinct paths; 86 distinct digests
provenance              87 rows; 87 distinct paths; 87 distinct digests
provenance relation     MS-2 union MS-3 plus exactly
                        327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e
                        src/philosophia/officina/verification.py
```

All 86 recorded member paths existed and every recorded SHA-256 matched the
bytes on disk. There were zero missing paths and zero digest mismatches. The
joint block was byte-identical between the governing files, so these counts and
literal rows agree in both.

`MS-8` recomputed as `M1 2 + M2 79 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 93`.
The seven member classes remain pairwise disjoint by their literal path sets.

## Complete binding-v6 OR-4 reproduction

The eleven spans appeared in ascending order `S1` through `S11`; every source
identity matched, and each adjacent pair satisfied `end_i < begin_(i+1)`.

```text
SPAN  LINES       SOURCE LENGTH / SHA-256
                  REPLACEMENT LENGTH / SHA-256
S1      55..95     2184  db66c3ad454a9d4b3cba2e530e54348e02598c87bc824326679969d8a15071e8
                   2120  75dc9671eabbb480b5b95b6ccf82a0a6877c66693f23cec9e57ec776f3cbf0d7
S2     307..308     163  86d71bcdc7350e977e9f80932bbf155ec535688ac5adbcfda1fecdd58bb92230
                     61  fc9dd4e6ac6b5384ecb7bf1cbf6ccee407d41456ff40fbdd7cdcaa7cf9af6901
S3    1769..1776    598  2c32d95b7c09dce20b5c6c46dc7071877ed12dfd569a4ed988607e43cee1faf3
                    207  839ca35d35a1f3a17de9209721d1cd51a65f110aa7d06d7805f7819263d5723c
S4    1779..1783    298  563875704d64fb343bbc61c9414e9473ff0a79d87e244c2f2dbd156cd72e410e
                     22  7fdc2f4f305adb0895c0b6803f6dd7d43d1bfc9f776484294a549637fa4d878c
S5    2267..2270    299  31a3d866a0dfd3854965f4b064fc8c034f958c6f9f99d794ebeeb74e96c8e1c3
                     47  e60732e9219460a1cd9108862be6d29918558cfb12bb46ce3a4e250be7a4b0fa
S6    2292..2294    218  fb396762d308a44d0e6dc1e011ced63bcd270a1e1fb5d6f759bf262b9eac9292
                     61  78ea5f796aa53acdda9a72d62dd9932d1c3324ef0ddf5881116a3c3f830c801d
S7        4415      982  a33c284ebd09f4177ae8aff88409a26d8df27d38f5e440a9a9bdda4593d8fed1
                    727  bc68506c9c96db05688bdd76c98d78c21076e1d59e35655b1c2bbe70971ecd6b
S8    4698..4715   1329  dbbf9cbfaacd6edb0dd467a7cff908894768a287cd906cc24f07d297777baa39
                    440  bce8b980a104af6fbf186826fa41263667935bf27f17e56031f3209703100650
S9        8663      504  496d4747775c288bf021b16737857c35e25411319d08781027421d263905849c
                    271  55a62571cfce5192b9380a576639102663b1f836a0ac14460fec983dc071315b
S10       8691    20238  c11802cbba288f559a7713b293fe0c654693a1a9149ca91d18c83148928dd46a
                  20148  ffaa8ca597a1156002530018cbf0448f913b0ef993ce9013ca204a83d3df3052
S11       8702      449  75ed6f6f747c8b7a8119c985d788f27e5e4b94538c7575ecc85d5913043d47e2
                    315  37b63dcd369696ad6046e64e3bb4f32e89dd455809d4395d897559273203a539
```

For `S7`, the exact delete literal was 277 bytes and hashed to
`1f8cd74f65b97fa67d58ca9a196ec2388b97eb10e5af00732b1a0cfc10147232`;
the insert literal was 22 bytes and hashed to
`523a0dd8e7266f1da09379e8684291b3ec27e87a36e991ac24b031a96e8d9a9c`.
The corresponding delete/insert measurements for the other three single-line
spans were: S9 352/119 bytes, S10 155/65 bytes and S11 337/203 bytes, all with
their published substring digests and containing-line digests reproduced.

Byte arithmetic reproduced exactly: `668002 - 27262 + 24419 = 665159`.

```text
FULL RESOLVED OUTPUT
  665159 bytes
  e9577809cf41cc7b97a9f22a1f2929af225e0b31bf061ae46b7aafda71bc34be

RESOLVED BODY
  627382 bytes
  b1edf36c36a22c6398176e223b9453e4319fe36e1b5f9d4f760d70502d4fa8d6
RESOLVED GUARDDATA
    1816 bytes
  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
RESOLVED NORMATIVE
  629198 bytes
  d3bc574d9c0d7a3dde53af21073d8efe8c24f1fac4f180d546eeca1d94e3f1b4
```

Guarddata was directly byte-identical before and after the in-memory transform,
not merely digest-equal. HANDOFF and JOINT were likewise byte-identical among
composite v1.15, amendment v1.12 and the resolved candidate. Provenance was
unchanged at 22,039 bytes and
`4b7acefb10829c8f1dfef4ae506dc060ecf3306a1b08a7937a5892ab92928fbe`.

The source carried 13 `[W-A]`, 13 `[W-B]` and 9 `t-wd-freeze.v1`
occurrences. The resolved candidate carried one marker of each kind, both only
inside guarddata, and zero `t-wd-freeze.v1`. Outside guarddata the marker counts
were 0/0. D1 serialized to 926 bytes with 11 literals and digest
`d5b375c518c935d3a6935a1932bf6bfa237cb9c99c7b81913f4e1433142b6c1e`;
D2 serialized to 1,044 bytes with 13 literals and digest
`4e2120857dd67124095e5f5479d69cbf7ba703605abb3448a2fe414b3ff8a15c`.
Both produced zero matches against the resolved candidate minus guarddata.

MP-1 reproduced byte-exactly. The whole-line anchor had cardinality one. Its
four-line payload was 195 bytes with SHA-256
`ee8a830d46f709ff2ffd95238600437e885c32d84bf268a1658950cd5ed63d2f`.
The candidate was 665,354 bytes with SHA-256
`6cbd6e2d2bea49854d63ae2108e1187fe8a210f6dc84526f8273db9a2bd8c09b`.
It retained guarddata identity, had zero D1/D2 matches and zero markers outside
guarddata, but failed PO-0 as required.

## Handoff-v6 operational audit

The handoff's own current-authority table pairs the current amendment,
composite and binding paths with the three correct full digests above. Its
repeated governing-pair path/digest loci at `R-1` and `§H2.2` agree. Its sole
precedence rule is internally single-valued: governing v1.12/v1.15 clauses over
binding v6, and binding v6 over handoff v6. No handoff-v6 operational sentence
delegates to an older binding, amendment, composite or handoff; its older-path
mentions are explicitly history or named counterexamples.

The handoff's resolved-output, resolved-region, guarddata, D1, D2 and MP-1
constants all reproduced. Its D-6 and T-14 cardinality loci agree with binding
v6 PR-4: 93 passes; exactly `63, 69, 73, 77, 81, 85, 89` are the negative
enumerations; 93 appears in none of the three negative lists. Other handoff
cardinality loci also agree: token/terminal/qualifier 7/3/2; synthetic partition
72 with `24+32+4+6+6`; failure/check sets 25/15; schema key sets
11/13/5/21/10; parser state/layout/suffix figures 9/1/50 and positions
1/2/3/20.

Operational path-state assertions matched the worktree: the two allowed code
modules, their two tests and fixture directory are absent; two of five
production roots exist tracked, `generic_harness.py` exists untracked, and two
roots are absent; the verifier baseline exists; both M6 modules, Stage A,
Stage B, its signature, M4 and M7 are absent; the four MS-13 project modules
exist; no `test_p1_row_NNN_` function exists. No current path/digest mismatch,
retired current cardinality or inconsistent precedence rule was found inside
handoff v6 itself.

That internally consistent handoff nevertheless directs the implementer to the
defective current composite and grants binding v6 transform precedence over the
handoff. It therefore cannot neutralize the findings below.

## Findings by severity

### Major Y15-M1 — the current composite delegates live authority to retired amendment v1.9

Composite v1.15 lines 126..131 declare amendment v1.9 a live authority surface
that owns peer-layer behaviour and is accepted jointly with the composite.
Lines 148..154 repeat that v1.9 path as the amendment with which the composite
must be accepted. These are live normative preamble clauses, not provenance or
named counterexamples. They directly collide with amendment v1.12 `DA-4`, the
joint block's current `MS-1` paths, the byte-identical H-1 handoff preamble and
handoff v6's current-authority table.

The loci are outside `REGION(BODY)` and outside every OR-4 span. They therefore
survive unchanged in the otherwise byte-exact resolved output. An implementer
following the composite's own hierarchy opens superseded v1.9 for behaviour;
one following MS-1 opens v1.12. This is a current/superseded authority collision
and independently requires revision.

### Major Y15-M2 — the resolved composite carries two incompatible replacement generations

Composite v1.15 lines 8..10 call it the full replacement for v1.13. The S1
replacement, correctly extracted from binding v6, changes the later Cell-2
notice to call the same resolved composite a finished replacement for v1.14.
OR-4 does not touch lines 8..10. The pinned resolved output thus retains both
claims, while the current pair and accounting explicitly supersede composite
v1.14. This is another live current/superseded-generation collision in the
produced bytes.

### Major Y15-M3 — binding v6's live PO-9 proof names the wrong transform source

Binding v6 lines 984..990 state, as the current proof for the detector boundary,
that the resolved output is a total function of composite v1.13's bytes and the
eleven spans. Its own complete executable transform at §2.2 consumes composite
v1.15, whose source spans, output and digest reproduce exactly. Handoff v6 calls
binding v6 the transform authority and makes it govern the handoff on a
difference. The live v1.13 source claim is therefore not an innocuous historical
citation: it collides with the actual transform source inside the current
authority surface.

### Minor

None separately recorded. The three Major findings already extend the loop.

## Search disposition

Apart from Y15-M1 through Y15-M3, older-generation paths, digests and counts in
the four searched files were confined to literal M2/provenance rows, explicit
supersession history, retired-value narratives or named negative
counterexamples. No other wrong current path/digest pairing, stale live
cardinality, or cardinality-negative fixture containing the current 93 was
found. The complete transform figures, including S7 and MP-1, reproduced.

## Next boundary

Author acceptance is not reached. Repair the current composite's normative
preamble so it names only the v1.12/v1.15 pair and consistently supersedes
v1.14, repair binding v6's live transform-source claim, regenerate every
dependent digest and byte witness, and submit the new identical bytes to a fresh
bounded X/Y confirmation round.

This review does not permit Kirill to consider
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12`.
It authorizes no scaffold, code, test, key, OR step, install or activation.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
```
