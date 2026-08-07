"""NON-CITABLE B2 Stage-1 pilot (design-validation only). Implements
successor/dev/B2_PATH_VS_DESTINATION_DESIGN_V2.md EXACTLY for Stage 1:
2 seeds × arms {D, P0, P0-neg, P+, P_shuf}. NOT the 6-block Stage-2 call.

No src/ edits. GPU via equivalence-proven gpu_committee_runner.
Writes successor/dev/B2_PILOT_08.md.
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Sequence

import torch
import torch.nn.functional as F

_ROOT = Path(__file__).resolve().parents[2]
_SRC = _ROOT / "src"
_DEV = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_DEV) not in sys.path:
    sys.path.insert(0, str(_DEV))

from philosophia.level1.config import (  # noqa: E402
    BUDGET,
    CHECKPOINT_CADENCE,
    MODEL_INPUT_LENGTH,
    PANEL_SIZE,
    PANEL_STRATUM_COUNTS,
    PERSISTENCE_CHECKPOINTS,
)
from philosophia.level1.feasibility import _committee  # noqa: E402
from philosophia.level1.interlock import feasibility_v2_capability  # noqa: E402
from philosophia.level1.model import (  # noqa: E402
    D_MODEL,
    ContactTransformer,
    build_optimizer,
    committee_equal_probability,
    encode_pair,
)
from philosophia.level1.panel import DummyPanel, DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    partition_cells,
    realize_pool_index,
    verify_partition,
)
from philosophia.level1.scoring import (  # noqa: E402
    ACCURACY_MINIMUM,
    PanelObservation,
    StratumScore,
    checkpoint_qualifies,
    score_stratum,
)
from philosophia.level1.serialization import (  # noqa: E402
    CounterStream,
    DeterministicKey,
    dummy_key,
    sample_without_replacement,
    shuffled,
)
from philosophia.level1.world import (  # noqa: E402
    admissible_paddings,
    displacement,
    fold,
    oracle_eq,
    unrank_word,
    word_count,
    word_length,
)

import gpu_committee_runner as runner  # noqa: E402
from capacity_diag_04 import (  # noqa: E402
    DEV_PANEL_LABEL,
    DEV_PUBLIC_LABEL,
    MODULUS,
    WORLD_SLOT,
    curated_rich_equal_schedule,
)

OUT_MD = _DEV / "B2_PILOT_08.md"
OUT_JSON = _DEV / "b2_pilot_08_results.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----- Locked constants (register BEFORE run; Sol C4) -----
N_MAX = 2000  # DIAG_04 curated distinct labeled-pair count (verified at runtime)
K = N_MAX // 8  # floor(N_max/8) = 250; do not sweep
H_DEST = 500  # destination / oracle-stage horizon (pilot lock)
M_PATH = 600  # path updates (pilot lock)
PATH_BATCH = 32  # length-matched positive pairs per path step
M_ROADS = 4  # roads drawn per displacement group
VICREG_INV = 25.0
VICREG_VAR = 25.0
VICREG_COV = 1.0
CONTRAST_TEMP = 0.1
MICROBATCH = 128
PILOT_SEEDS = (0, 1)
READOUT_EPOCHS = 80
PROBE_EPOCHS = 60

# Path displacement support FIXED independently of n=66 (Sol C2).
_D_PATH_LO, _D_PATH_HI = -80, 80


# =============================================================================
# Path firewall: path code may read ONLY token counts + exact-d sameness.
# =============================================================================

_FORBIDDEN_PATH_NAMES = frozenset(
    {
        "modulus",
        "n_mod",
        "residue",
        "fold_val",
        "oracle",
        "oracle_eq",
        "panel",
        "panel_item",
        "truth",
        "label_oracle",
        "MODULUS",
    }
)


def _assert_path_clean(context: str, **kwargs: object) -> None:
    """Assert path pipeline kwargs never carry n/residue/oracle/panel."""
    bad = [k for k in kwargs if k in _FORBIDDEN_PATH_NAMES or k.lower() in _FORBIDDEN_PATH_NAMES]
    if bad:
        raise RuntimeError(f"path firewall violation in {context}: {bad}")
    # Values must not be the frozen modulus smuggled as an int named otherwise
    # when the caller explicitly tags them — checked by name above.
    _ = context


def _pair_key(left: bytes, right: bytes) -> tuple[bytes, bytes]:
    return (left, right)


def _hash_pairs(pairs: Sequence[tuple[bytes, bytes]]) -> str:
    digest = hashlib.sha256()
    for left, right in pairs:
        digest.update(left)
        digest.update(b"|")
        digest.update(right)
        digest.update(b";")
    return digest.hexdigest()[:16]


# =============================================================================
# Activations / encoding helpers
# =============================================================================


def encode_word_self(word: bytes) -> torch.Tensor:
    return encode_pair(word, word)


@torch.no_grad()
def prehead(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    key_mask = tokens.ne(0)
    positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
    x = model.token_embedding[tokens] + model.position_embedding[positions][None, :, :]
    for layer in model.layers:
        x = layer(x, key_mask)
    return model.final_ln(x)[:, -1, :]


def prehead_grad(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    """Pre-head with grad (path training)."""
    key_mask = tokens.ne(0)
    positions = torch.arange(MODEL_INPUT_LENGTH, device=tokens.device)
    x = model.token_embedding[tokens] + model.position_embedding[positions][None, :, :]
    for layer in model.layers:
        x = layer(x, key_mask)
    return model.final_ln(x)[:, -1, :]


def committee_mean_prehead(
    models: Sequence[ContactTransformer], tokens: torch.Tensor, *, chunk: int = 64
) -> torch.Tensor:
    outs = []
    with torch.no_grad():
        for start in range(0, tokens.shape[0], chunk):
            sl = tokens[start : start + chunk].to(DEVICE)
            vecs = torch.stack([prehead(m, sl) for m in models], dim=0).mean(dim=0)
            outs.append(vecs.cpu())
    return torch.cat(outs, dim=0)


# =============================================================================
# Path sampler (oracle-free; length-matched)
# =============================================================================


def _build_length_index() -> dict[int, list[tuple[int, int]]]:
    """length ℓ → list of (d, padding) with word_length(d,p)=ℓ. Skips empty (d=0,p=0)."""
    by_len: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for d in range(_D_PATH_LO, _D_PATH_HI + 1):
        for p in admissible_paddings(d):
            ell = word_length(d, p)
            if ell == 0:
                # d=0,p=0 → empty word; noted explicitly, excluded from path batches.
                continue
            if ell < 2:
                continue
            by_len[ell].append((d, p))
    # Keep lengths that admit ≥2 distinct displacements (for contrastive / variety).
    return {ell: vals for ell, vals in by_len.items() if len({d for d, _ in vals}) >= 2}


_LENGTH_INDEX = _build_length_index()
_LENGTHS = sorted(_LENGTH_INDEX.keys())


def _sample_word_at(d: int, padding: int, stream: CounterStream) -> bytes:
    _assert_path_clean("sample_word_at", d=d, padding=padding)
    n = word_count(d, padding)
    if n <= 0:
        raise RuntimeError("empty word_count")
    rank = stream.uniform(n)
    word = unrank_word(d, padding, rank)
    # Token-count check only (path-legal).
    if len(word) != abs(d) + 2 * padding:
        raise RuntimeError("token-count mismatch")
    if displacement(word) != d:
        raise RuntimeError("exact-displacement mismatch after unrank")
    return word


def sample_length_matched_positive_batch(
    stream: CounterStream,
    *,
    batch_pairs: int,
    roads_per_group: int,
    shuffle_groups: bool = False,
) -> tuple[list[bytes], list[bytes], list[int], int]:
    """Return (w1s, w2s, group_ids, length ℓ).

    Path-legal: uses only exact-d sameness + token counts. Never reads n/oracle/panel.
    If shuffle_groups: randomize pairing across groups (P_shuf fake ledger).
    """
    _assert_path_clean("sample_batch", batch_pairs=batch_pairs)
    ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
    options = _LENGTH_INDEX[ell]
    # Distinct displacements available at this length.
    d_to_pads: dict[int, list[int]] = defaultdict(list)
    for d, p in options:
        d_to_pads[d].append(p)
    ds = list(d_to_pads.keys())
    n_groups = max(2, batch_pairs // max(1, roads_per_group // 2))
    chosen_ds = []
    for _ in range(n_groups):
        chosen_ds.append(ds[stream.uniform(len(ds))])

    roads: list[tuple[bytes, int]] = []  # (word, group_idx)
    for g, d in enumerate(chosen_ds):
        pads = d_to_pads[d]
        for _ in range(roads_per_group):
            p = pads[stream.uniform(len(pads))]
            w = _sample_word_at(d, p, stream)
            # Ensure distinctness within group when possible.
            tries = 0
            while any(w == rw for rw, rg in roads if rg == g) and tries < 20:
                w = _sample_word_at(d, p, stream)
                tries += 1
            roads.append((w, g))

    # Form positive pairs within groups (true d-sameness), or shuffled.
    by_g: dict[int, list[bytes]] = defaultdict(list)
    for w, g in roads:
        by_g[g].append(w)

    w1s: list[bytes] = []
    w2s: list[bytes] = []
    gids: list[int] = []
    if shuffle_groups:
        # Fake ledger: pair random roads ignoring true group (no true invariance).
        flat = [w for w, _ in roads]
        for _ in range(batch_pairs):
            i = stream.uniform(len(flat))
            j = stream.uniform(len(flat))
            while j == i and len(flat) > 1:
                j = stream.uniform(len(flat))
            w1s.append(flat[i])
            w2s.append(flat[j])
            gids.append(-1)
    else:
        for g, ws in by_g.items():
            if len(ws) < 2:
                continue
            for i in range(len(ws) - 1):
                w1s.append(ws[i])
                w2s.append(ws[i + 1])
                gids.append(g)
                if len(w1s) >= batch_pairs:
                    break
            if len(w1s) >= batch_pairs:
                break
        # Top up if short.
        while len(w1s) < batch_pairs:
            g = chosen_ds[stream.uniform(len(chosen_ds))]
            # find group index
            gi = chosen_ds.index(g) if g in chosen_ds else 0
            ws = by_g[gi]
            if len(ws) < 2:
                pads = d_to_pads[g]
                p = pads[stream.uniform(len(pads))]
                a = _sample_word_at(g, p, stream)
                b = _sample_word_at(g, p, stream)
            else:
                a = ws[stream.uniform(len(ws))]
                b = ws[stream.uniform(len(ws))]
            w1s.append(a)
            w2s.append(b)
            gids.append(gi)

    return w1s[:batch_pairs], w2s[:batch_pairs], gids[:batch_pairs], ell


def sample_contrastive_batch(
    stream: CounterStream, *, batch_pairs: int
) -> tuple[list[bytes], list[bytes], list[bytes]]:
    """P0-neg: anchor, positive (same d), negative (different d), length-matched."""
    _assert_path_clean("contrastive_batch", batch_pairs=batch_pairs)
    ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
    options = _LENGTH_INDEX[ell]
    d_to_pads: dict[int, list[int]] = defaultdict(list)
    for d, p in options:
        d_to_pads[d].append(p)
    ds = list(d_to_pads.keys())
    anchors, poss, negs = [], [], []
    for _ in range(batch_pairs):
        d_pos = ds[stream.uniform(len(ds))]
        d_neg = ds[stream.uniform(len(ds))]
        while d_neg == d_pos and len(ds) > 1:
            d_neg = ds[stream.uniform(len(ds))]
        p_pos = d_to_pads[d_pos][stream.uniform(len(d_to_pads[d_pos]))]
        p_neg = d_to_pads[d_neg][stream.uniform(len(d_to_pads[d_neg]))]
        a = _sample_word_at(d_pos, p_pos, stream)
        b = _sample_word_at(d_pos, p_pos, stream)
        c = _sample_word_at(d_neg, p_neg, stream)
        anchors.append(a)
        poss.append(b)
        negs.append(c)
    return anchors, poss, negs


# =============================================================================
# Losses
# =============================================================================


def _off_diagonal(x: torch.Tensor) -> torch.Tensor:
    n, m = x.shape
    assert n == m
    return x.flatten()[:-1].view(n - 1, n + 1)[:, 1:].flatten()


def vicreg_pair_loss(z1: torch.Tensor, z2: torch.Tensor) -> torch.Tensor:
    """Positive-only: align paired roads + VICReg anti-collapse (no negatives)."""
    inv = F.mse_loss(z1, z2)
    std_z1 = torch.sqrt(z1.var(dim=0) + 1e-4)
    std_z2 = torch.sqrt(z2.var(dim=0) + 1e-4)
    var = torch.mean(F.relu(1.0 - std_z1)) / 2 + torch.mean(F.relu(1.0 - std_z2)) / 2
    z1c = z1 - z1.mean(dim=0)
    z2c = z2 - z2.mean(dim=0)
    cov1 = (z1c.T @ z1c) / max(1, z1.shape[0] - 1)
    cov2 = (z2c.T @ z2c) / max(1, z2.shape[0] - 1)
    cov = (
        _off_diagonal(cov1).pow(2).sum() / z1.shape[1]
        + _off_diagonal(cov2).pow(2).sum() / z2.shape[1]
    ) / 2
    return VICREG_INV * inv + VICREG_VAR * var + VICREG_COV * cov


def contrastive_loss(
    za: torch.Tensor, zp: torch.Tensor, zn: torch.Tensor, *, temp: float = CONTRAST_TEMP
) -> torch.Tensor:
    """Naive exact-d contrastive (P0-neg instrument)."""
    za = F.normalize(za, dim=-1)
    zp = F.normalize(zp, dim=-1)
    zn = F.normalize(zn, dim=-1)
    pos = (za * zp).sum(dim=-1) / temp
    neg = (za * zn).sum(dim=-1) / temp
    # Binary: prefer pos over neg
    logits = torch.stack([pos, neg], dim=-1)
    labels = torch.zeros(za.shape[0], dtype=torch.long, device=za.device)
    return F.cross_entropy(logits, labels)


# =============================================================================
# K-set / destination
# =============================================================================


def compute_n_max_and_k(public_key, partition) -> tuple[int, int, tuple[int, ...]]:
    schedule = curated_rich_equal_schedule(public_key, partition)
    n_max = len(schedule)
    if n_max != N_MAX:
        raise RuntimeError(f"N_max drifted: got {n_max}, locked {N_MAX}")
    k = n_max // 8
    if k != K:
        raise RuntimeError(f"K drifted: got {k}, locked {K}")
    print(f"N_max={n_max}; K=floor(N_max/8)={k}", flush=True)
    return n_max, k, schedule


def build_k_set(
    public_key,
    partition,
    schedule: tuple[int, ...],
    seed: int,
    k: int,
) -> tuple[list[tuple[bytes, bytes]], list[int], str]:
    """Label-balanced K distinct labeled pairs from DIAG_04 curated pool order.

    Path firewall: this is DESTINATION sampling — may use oracle_eq for labels.
    """
    stream = CounterStream(
        dummy_key(f"successor-dev-b2-pilot-seed-{seed}", purpose="public-root"),
        ("L1", "b2-pilot", "k-set", seed),
    )
    equals: list[tuple[bytes, bytes]] = []
    unequals: list[tuple[bytes, bytes]] = []
    # Walk shuffled schedule indices for diversity.
    order = shuffled(list(range(len(schedule))), stream)
    for idx in order:
        raw = realize_pool_index(partition, public_key, schedule[idx])
        pair = _pair_key(raw.left, raw.right)
        if oracle_eq(raw.left, raw.right, MODULUS):
            if pair not in equals:
                equals.append(pair)
        else:
            if pair not in unequals:
                unequals.append(pair)
        if len(equals) >= k // 2 and len(unequals) >= k - k // 2:
            break
    n_eq = k // 2
    n_neq = k - n_eq
    selected = equals[:n_eq] + unequals[:n_neq]
    if len(selected) != k:
        raise RuntimeError(f"could not build balanced K-set: got {len(selected)}")
    selected = shuffled(selected, stream)
    labels = [int(oracle_eq(a, b, MODULUS)) for a, b in selected]
    return selected, labels, _hash_pairs(selected)


def _stack_pairs(pairs: Sequence[tuple[bytes, bytes]]) -> torch.Tensor:
    return torch.stack([encode_pair(a, b) for a, b in pairs])


# =============================================================================
# Training loops
# =============================================================================


def new_committee(seed: int) -> list[ContactTransformer]:
    key = dummy_key(f"successor-dev-b2-pilot-seed-{seed}", purpose="public-root")
    models, _ = _committee(key, block=WORLD_SLOT)
    models = [m.to(DEVICE) for m in models]
    for m in models:
        m.train()
    return models


def path_train_p0(
    models: list[ContactTransformer],
    stream: CounterStream,
    *,
    steps: int,
    shuffle_groups: bool = False,
) -> float:
    """Positive-only VICReg path. Returns wall seconds."""
    opts = [build_optimizer(m) for m in models]
    t0 = time.perf_counter()
    for step in range(1, steps + 1):
        w1s, w2s, _, _ell = sample_length_matched_positive_batch(
            stream,
            batch_pairs=PATH_BATCH,
            roads_per_group=M_ROADS,
            shuffle_groups=shuffle_groups,
        )
        t1 = torch.stack([encode_word_self(w) for w in w1s]).to(DEVICE)
        t2 = torch.stack([encode_word_self(w) for w in w2s]).to(DEVICE)
        for model, opt in zip(models, opts):
            opt.zero_grad(set_to_none=True)
            z1 = prehead_grad(model, t1)
            z2 = prehead_grad(model, t2)
            loss = vicreg_pair_loss(z1, z2)
            loss.backward()
            opt.step()
        if step % 100 == 0:
            print(f"  path step={step}/{steps} loss={float(loss):.4f} ell={_ell}", flush=True)
    return time.perf_counter() - t0


def path_train_p0_neg(
    models: list[ContactTransformer], stream: CounterStream, *, steps: int
) -> float:
    opts = [build_optimizer(m) for m in models]
    t0 = time.perf_counter()
    for step in range(1, steps + 1):
        a, p, n = sample_contrastive_batch(stream, batch_pairs=PATH_BATCH)
        ta = torch.stack([encode_word_self(w) for w in a]).to(DEVICE)
        tp = torch.stack([encode_word_self(w) for w in p]).to(DEVICE)
        tn = torch.stack([encode_word_self(w) for w in n]).to(DEVICE)
        for model, opt in zip(models, opts):
            opt.zero_grad(set_to_none=True)
            za = prehead_grad(model, ta)
            zp = prehead_grad(model, tp)
            zn = prehead_grad(model, tn)
            loss = contrastive_loss(za, zp, zn)
            loss.backward()
            opt.step()
        if step % 100 == 0:
            print(f"  p0-neg step={step}/{steps} loss={float(loss):.4f}", flush=True)
    return time.perf_counter() - t0


def destination_train(
    models: list[ContactTransformer],
    pairs: Sequence[tuple[bytes, bytes]],
    labels: Sequence[int],
    *,
    horizon: int,
    freeze_trunk: bool = False,
) -> tuple[float, dict[int, bool], list[dict]]:
    """Oracle-stage CE on fixed K-set for `horizon` steps. Returns wall, qualifying, strip."""
    tokens = _stack_pairs(pairs)
    labs = torch.tensor(list(labels), dtype=torch.long)
    if freeze_trunk:
        for m in models:
            for name, p in m.named_parameters():
                p.requires_grad = name in ("head_W", "head_b")
    opts = [build_optimizer(m) for m in models]
    # Fresh capability per destination run (cap BUDGET).
    cap = feasibility_v2_capability()
    cap.claim_development_world(WORLD_SLOT)
    if horizon > BUDGET:
        raise RuntimeError("horizon exceeds trajectory cap")

    # Panel for checkpoints — loaded by caller via closure? Pass later.
    # We'll checkpoint outside; here only train and return.
    t0 = time.perf_counter()
    for step in range(1, horizon + 1):
        loss_result, _ = runner.memory_safe_class_balanced_feasibility_committee_step(
            models, opts, tokens, labs, cap, microbatch=MICROBATCH
        )
        if not loss_result.finite:
            raise RuntimeError(f"non-finite at dest step {step}")
        if step % 100 == 0:
            print(f"  dest step={step}/{horizon}", flush=True)
    wall = time.perf_counter() - t0
    if freeze_trunk:
        for m in models:
            for p in m.parameters():
                p.requires_grad = True
    return wall, {}, []


def score_panel_committee(models, panel: DummyPanel) -> tuple[bool, dict[str, StratumScore], dict]:
    for m in models:
        m.eval()
    toks = torch.stack(
        [encode_pair(it.left, it.right).to(DEVICE) for it in panel.items]
    )
    with torch.no_grad():
        probs = committee_equal_probability(models, toks).detach().cpu()
    obs = [
        PanelObservation(it.stratum, it.truth, float(p))
        for it, p in zip(panel.items, probs.tolist())
    ]
    by = {}
    for name in PANEL_STRATUM_COUNTS:
        vals = [o for o in obs if o.stratum == name]
        by[name] = score_stratum(name, vals)
    qualifies = checkpoint_qualifies(obs)
    detail = {
        name: {
            "correct": by[name].correct,
            "need": ACCURACY_MINIMUM[name],
            "abst": by[name].abstentions,
            "lies": by[name].confident_lies,
            "brier": by[name].brier,
            "qualifies": by[name].qualifies,
        }
        for name in PANEL_STRATUM_COUNTS
    }
    for m in models:
        m.train()
    return qualifies, by, detail


def fit_linear_equality_readout(
    models: list[ContactTransformer],
    stream: CounterStream,
    *,
    n_train: int = 2000,
    epochs: int = READOUT_EPOCHS,
) -> Callable[[torch.Tensor], torch.Tensor]:
    """Read-only linear equal? from frozen trunk; labels = exact-d sameness (path notion).

    Never uses oracle/modulus — path-legal labels only.
    """
    _assert_path_clean("fit_readout", n_train=n_train)
    w1s, w2s, _, _ = sample_length_matched_positive_batch(
        stream, batch_pairs=n_train // 2, roads_per_group=M_ROADS, shuffle_groups=False
    )
    # Negatives: reshuffle pairings across different groups → mostly different d.
    w1n, w2n, _, _ = sample_length_matched_positive_batch(
        stream, batch_pairs=n_train // 2, roads_per_group=M_ROADS, shuffle_groups=True
    )
    pairs = [(a, b, 1) for a, b in zip(w1s, w2s)] + [(a, b, 0) for a, b in zip(w1n, w2n)]
    # Exact label by displacement sameness (path signal).
    labeled = []
    for a, b, _ in pairs:
        labeled.append((a, b, int(displacement(a) == displacement(b))))
    toks = torch.stack([encode_pair(a, b) for a, b, _ in labeled])
    y = torch.tensor([lab for _, _, lab in labeled], dtype=torch.long)
    with torch.no_grad():
        for m in models:
            m.eval()
        x = committee_mean_prehead(models, toks)
    mean = x.mean(0, keepdim=True)
    std = x.std(0, keepdim=True).clamp_min(1e-6)
    x = (x - mean) / std
    W = torch.zeros(D_MODEL, 2, requires_grad=True)
    b = torch.zeros(2, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=0.05, weight_decay=1e-2)
    x_dev = x  # CPU ok for small probe
    for _ in range(epochs):
        logits = x_dev @ W + b
        loss = F.cross_entropy(logits, y)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()
    W_f, b_f, mean_f, std_f = W.detach(), b.detach(), mean, std

    def predict_p_equal(pair_tokens: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            for m in models:
                m.eval()
            acts = committee_mean_prehead(models, pair_tokens.cpu())
            acts = (acts - mean_f) / std_f
            probs = torch.softmax(acts @ W_f + b_f, dim=-1)[:, 1]
        return probs

    return predict_p_equal


def score_panel_readout(
    predict_p_equal: Callable[[torch.Tensor], torch.Tensor], panel: DummyPanel
) -> tuple[bool, dict, dict]:
    toks = torch.stack([encode_pair(it.left, it.right) for it in panel.items])
    probs = predict_p_equal(toks)
    obs = [
        PanelObservation(it.stratum, it.truth, float(p))
        for it, p in zip(panel.items, probs.tolist())
    ]
    by = {}
    for name in PANEL_STRATUM_COUNTS:
        vals = [o for o in obs if o.stratum == name]
        by[name] = score_stratum(name, vals)
    detail = {
        name: {
            "correct": by[name].correct,
            "need": ACCURACY_MINIMUM[name],
            "abst": by[name].abstentions,
            "lies": by[name].confident_lies,
            "brier": by[name].brier,
            "qualifies": by[name].qualifies,
        }
        for name in PANEL_STRATUM_COUNTS
    }
    # Per-item wrap diagnostics
    wrap_items = []
    for it, p in zip(panel.items, probs.tolist()):
        if it.truth and it.difference in (MODULUS, 2 * MODULUS):
            obs_i = PanelObservation(it.stratum, True, float(p))
            wrap_items.append(
                {
                    "stratum": it.stratum,
                    "diff": it.difference,
                    "p_equal": float(p),
                    "correct": obs_i.correct,
                    "anti_correct": (not obs_i.abstains) and (not obs_i.prediction),
                }
            )
    detail["_wrap"] = wrap_items
    return checkpoint_qualifies(obs), by, detail


def first_persistent_oracle_clock(qualifying: dict[int, bool], horizon: int) -> int | None:
    """Same rule as frozen first_persistent_step, on oracle clock 0..horizon."""
    steps = tuple(range(0, horizon + 1, CHECKPOINT_CADENCE))
    missing = [s for s in steps if s not in qualifying]
    if missing:
        raise RuntimeError(f"missing oracle checkpoint {missing[0]}")
    for i in range(len(steps) - PERSISTENCE_CHECKPOINTS + 1):
        window = steps[i : i + PERSISTENCE_CHECKPOINTS]
        if all(qualifying[s] for s in window):
            return window[0]
    return None


def destination_train_with_checkpoints(
    models: list[ContactTransformer],
    pairs: Sequence[tuple[bytes, bytes]],
    labels: Sequence[int],
    panel: DummyPanel,
    *,
    horizon: int,
    freeze_trunk: bool = False,
) -> tuple[float, int | None, dict, list]:
    tokens = _stack_pairs(pairs)
    labs = torch.tensor(list(labels), dtype=torch.long)
    if freeze_trunk:
        for m in models:
            for name, p in m.named_parameters():
                p.requires_grad = name in ("head_W", "head_b")
    opts = [build_optimizer(m) for m in models]
    cap = feasibility_v2_capability()
    cap.claim_development_world(WORLD_SLOT)
    qualifying: dict[int, bool] = {}
    strip: list[dict] = []
    t0 = time.perf_counter()

    def ckpt(step: int) -> None:
        q, _, detail = score_panel_committee(models, panel)
        qualifying[step] = q
        strip.append({"step": step, "qualifies": q, "strata": detail})
        print(
            f"  ckpt oracle_step={step} qualifies={q} "
            f"S3={detail['S3']['qualifies']} S2={detail['S2']['qualifies']}",
            flush=True,
        )

    ckpt(0)
    for step in range(1, horizon + 1):
        loss_result, _ = runner.memory_safe_class_balanced_feasibility_committee_step(
            models, opts, tokens, labs, cap, microbatch=MICROBATCH
        )
        if not loss_result.finite:
            raise RuntimeError(f"non-finite dest step {step}")
        if step % CHECKPOINT_CADENCE == 0:
            ckpt(step)
    wall = time.perf_counter() - t0
    if freeze_trunk:
        for m in models:
            for p in m.parameters():
                p.requires_grad = True
    persistent = first_persistent_oracle_clock(qualifying, horizon)
    final = strip[-1]["strata"] if strip else {}
    return wall, persistent, final, strip


# =============================================================================
# Mechanism probes (read-only)
# =============================================================================


def _fit_probe(x_tr, y_tr, x_te, y_te, n_classes: int, epochs: int = PROBE_EPOCHS) -> float:
    mean = x_tr.mean(0, keepdim=True)
    std = x_tr.std(0, keepdim=True).clamp_min(1e-6)
    x_tr = (x_tr - mean) / std
    x_te = (x_te - mean) / std
    W = torch.zeros(x_tr.shape[1], n_classes, requires_grad=True)
    b = torch.zeros(n_classes, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=0.05, weight_decay=1e-2)
    for _ in range(epochs):
        loss = F.cross_entropy(x_tr @ W + b, y_tr)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()
    with torch.no_grad():
        pred = (x_te @ W + b).argmax(-1)
        return float((pred == y_te).float().mean().item())


def run_mechanism_probes(
    models: list[ContactTransformer], stream: CounterStream, tag: str
) -> dict:
    """Displacement / length-control / sign(d) / residue probes on frozen acts."""
    print(f"  mechanism probes [{tag}]...", flush=True)
    for m in models:
        m.eval()

    # --- Build probe corpus of single words at controlled (d, length) ---
    words: list[bytes] = []
    ds: list[int] = []
    lengths: list[int] = []
    for _ in range(2400):
        ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
        opts = _LENGTH_INDEX[ell]
        d, p = opts[stream.uniform(len(opts))]
        w = _sample_word_at(d, p, stream)
        words.append(w)
        ds.append(d)
        lengths.append(ell)

    toks = torch.stack([encode_word_self(w) for w in words])
    acts = committee_mean_prehead(models, toks)

    # Exact-d classes: map to contiguous ids over observed ds (balanced subsample).
    unique_ds = sorted(set(ds))
    # Cap classes for tractability
    if len(unique_ds) > 40:
        unique_ds = unique_ds[:: max(1, len(unique_ds) // 40)][:40]
    d_to_id = {d: i for i, d in enumerate(unique_ds)}
    mask = [d in d_to_id for d in ds]
    x = acts[torch.tensor(mask)]
    y_d = torch.tensor([d_to_id[d] for d, m in zip(ds, mask) if m], dtype=torch.long)
    y_len = torch.tensor([lengths[i] for i, m in enumerate(mask) if m], dtype=torch.long)
    # Map lengths to ids
    uniq_l = sorted(set(y_len.tolist()))
    l_to_id = {l: i for i, l in enumerate(uniq_l)}
    y_l = torch.tensor([l_to_id[int(v)] for v in y_len.tolist()], dtype=torch.long)

    n = x.shape[0]
    perm = torch.randperm(n)
    n_te = max(1, n // 3)
    te, tr = perm[:n_te], perm[n_te:]
    d_acc = _fit_probe(x[tr], y_d[tr], x[te], y_d[te], len(d_to_id))
    len_acc = _fit_probe(x[tr], y_l[tr], x[te], y_l[te], len(l_to_id))
    # Within one length stratum (most populous)
    from collections import Counter

    len_counts = Counter(int(v) for v in y_len.tolist())
    top_ell = max(len_counts, key=len_counts.get)
    within = [i for i in range(n) if int(y_len[i]) == top_ell]
    if len(within) >= 60:
        xw = x[within]
        yw = y_d[within]
        # Remap d ids present
        present = sorted(set(yw.tolist()))
        remap = {old: i for i, old in enumerate(present)}
        yw2 = torch.tensor([remap[int(v)] for v in yw.tolist()], dtype=torch.long)
        pw = torch.randperm(len(within))
        n_te_w = max(1, len(within) // 3)
        d_within = _fit_probe(
            xw[pw[n_te_w:]],
            yw2[pw[n_te_w:]],
            xw[pw[:n_te_w]],
            yw2[pw[:n_te_w]],
            len(present),
        )
    else:
        d_within = float("nan")

    # sign(d) at matched |d|
    sign_x = []
    sign_y = []
    abs_set = sorted({abs(d) for d in unique_ds if d != 0})
    for abs_d in abs_set[:30]:
        for sign, lab in ((+1, 1), (-1, 0)):
            d = sign * abs_d
            if d not in d_to_pads_safe(abs_d):
                continue
            # sample words of this signed d at some shared length if possible
            for ell in _LENGTHS:
                opts = [(dd, pp) for dd, pp in _LENGTH_INDEX[ell] if dd == d]
                if not opts:
                    continue
                dd, pp = opts[0]
                for _ in range(8):
                    w = _sample_word_at(dd, pp, stream)
                    sign_x.append(w)
                    sign_y.append(lab)
                break
    if len(sign_x) >= 40:
        stx = committee_mean_prehead(
            models, torch.stack([encode_word_self(w) for w in sign_x])
        )
        sty = torch.tensor(sign_y, dtype=torch.long)
        sp = torch.randperm(len(sign_y))
        n_te_s = max(1, len(sign_y) // 3)
        sign_acc = _fit_probe(
            stx[sp[n_te_s:]], sty[sp[n_te_s:]], stx[sp[:n_te_s]], sty[sp[:n_te_s]], 2
        )
    else:
        sign_acc = float("nan")

    # Residue probe: train/test on DISJOINT exact-d values (different wrap cycles).
    # Label = fold(word, MODULUS) — this probe MAY use modulus (read-only mechanism,
    # not path training). Spec Sol M2.
    res_words, res_d, res_y = [], [], []
    for _ in range(3000):
        ell = _LENGTHS[stream.uniform(len(_LENGTHS))]
        opts = _LENGTH_INDEX[ell]
        d, p = opts[stream.uniform(len(opts))]
        w = _sample_word_at(d, p, stream)
        res_words.append(w)
        res_d.append(d)
        res_y.append(fold(w, MODULUS))
    # Split by disjoint d sets
    all_d = sorted(set(res_d))
    mid = len(all_d) // 2
    d_train_set = set(all_d[:mid])
    d_test_set = set(all_d[mid:])
    tr_idx = [i for i, d in enumerate(res_d) if d in d_train_set]
    te_idx = [i for i, d in enumerate(res_d) if d in d_test_set]
    rx = committee_mean_prehead(
        models, torch.stack([encode_word_self(w) for w in res_words])
    )
    if tr_idx and te_idx:
        residue_acc = _fit_probe(
            rx[tr_idx],
            torch.tensor([res_y[i] for i in tr_idx], dtype=torch.long),
            rx[te_idx],
            torch.tensor([res_y[i] for i in te_idx], dtype=torch.long),
            MODULUS,
            epochs=PROBE_EPOCHS,
        )
    else:
        residue_acc = float("nan")

    chance_d = 1.0 / max(1, len(d_to_id))
    return {
        "tag": tag,
        "exact_d_acc": d_acc,
        "exact_d_chance": chance_d,
        "length_only_acc": len_acc,
        "length_chance": 1.0 / max(1, len(l_to_id)),
        "exact_d_within_length_acc": d_within,
        "sign_d_acc": sign_acc,
        "sign_d_chance": 0.5,
        "residue_acc_disjoint_d": residue_acc,
        "residue_chance": 1.0 / MODULUS,
    }


def d_to_pads_safe(abs_d: int) -> set[int]:
    return {d for d in range(_D_PATH_LO, _D_PATH_HI + 1) if abs(d) == abs_d}


# =============================================================================
# Overlap report
# =============================================================================


def displacement_class_overlap(path_ds: set[int], panel: DummyPanel) -> dict:
    """Report |d| overlap between path support and panel cell differences."""
    panel_diffs = {it.difference for it in panel.items}
    # Path uses signed d; panel cells use nonnegative difference.
    path_abs = {abs(d) for d in path_ds}
    return {
        "path_abs_d_count": len(path_abs),
        "panel_diff_count": len(panel_diffs),
        "abs_d_intersect_panel_diff": sorted(path_abs & panel_diffs),
        "n_overlap": len(path_abs & panel_diffs),
        "note": (
            "word-level intersect=0 does not establish content independence: "
            "path road-pool and panel can still share displacement classes."
        ),
    }


# =============================================================================
# Arm runners
# =============================================================================


@dataclass
class ArmResult:
    arm: str
    seed: int
    k_hash: str
    path_wall_s: float = 0.0
    dest_wall_s: float = 0.0
    first_persistent_step: int | None = None
    strata: dict = field(default_factory=dict)
    probes: dict = field(default_factory=dict)
    wrap_anti_correct: int | None = None
    wrap_n: int | None = None
    scoring_mode: str = "committee_head"


def run_seed(
    seed: int,
    public_key,
    partition,
    panel: DummyPanel,
    schedule: tuple[int, ...],
    path_d_support: set[int],
) -> list[ArmResult]:
    results: list[ArmResult] = []
    pairs, labels, k_hash = build_k_set(public_key, partition, schedule, seed, K)
    panel_pairs = {_pair_key(it.left, it.right) for it in panel.items}
    if set(pairs) & panel_pairs:
        raise RuntimeError("K-set ∩ panel nonempty")
    print(f"\n=== SEED {seed} K={K} k_hash={k_hash} ===", flush=True)

    def path_stream(tag: str) -> CounterStream:
        return CounterStream(
            dummy_key(f"successor-dev-b2-pilot-seed-{seed}", purpose="public-root"),
            ("L1", "b2-pilot", "path", seed, tag),
        )

    # --- D ---
    print(f"[seed {seed}] arm D...", flush=True)
    models = new_committee(seed)
    probes_init = run_mechanism_probes(models, path_stream("probe-init"), "init")
    dest_wall, persistent, strata, _ = destination_train_with_checkpoints(
        models, pairs, labels, panel, horizon=H_DEST, freeze_trunk=False
    )
    probes_d = run_mechanism_probes(models, path_stream("probe-D"), "D")
    results.append(
        ArmResult(
            "D",
            seed,
            k_hash,
            dest_wall_s=dest_wall,
            first_persistent_step=persistent,
            strata=strata,
            probes={"init": probes_init, "D": probes_d},
            scoring_mode="committee_head",
        )
    )

    # --- P0 ---
    print(f"[seed {seed}] arm P0...", flush=True)
    models = new_committee(seed)
    path_wall = path_train_p0(
        models, path_stream("P0"), steps=M_PATH, shuffle_groups=False
    )
    probes_p0 = run_mechanism_probes(models, path_stream("probe-P0"), "P0")
    readout = fit_linear_equality_readout(models, path_stream("readout-P0"))
    _, _, detail = score_panel_readout(readout, panel)
    wrap = detail.pop("_wrap")
    anti = sum(1 for w in wrap if w["anti_correct"])
    results.append(
        ArmResult(
            "P0",
            seed,
            k_hash,
            path_wall_s=path_wall,
            first_persistent_step=None,  # no oracle stage
            strata=detail,
            probes={"P0": probes_p0},
            wrap_anti_correct=anti,
            wrap_n=len(wrap),
            scoring_mode="path_exact_d_linear_readout",
        )
    )

    # --- P0-neg ---
    print(f"[seed {seed}] arm P0-neg...", flush=True)
    models = new_committee(seed)
    path_wall = path_train_p0_neg(models, path_stream("P0-neg"), steps=M_PATH)
    readout = fit_linear_equality_readout(models, path_stream("readout-P0neg"))
    # For false-wall measure: also score with contrastive notion — use same
    # exact-d readout (sameness). Wrap anti-correct is the instrument.
    _, _, detail = score_panel_readout(readout, panel)
    wrap = detail.pop("_wrap")
    anti = sum(1 for w in wrap if w["anti_correct"])
    results.append(
        ArmResult(
            "P0-neg",
            seed,
            k_hash,
            path_wall_s=path_wall,
            first_persistent_step=None,
            strata=detail,
            probes={},
            wrap_anti_correct=anti,
            wrap_n=len(wrap),
            scoring_mode="path_exact_d_linear_readout",
        )
    )

    # --- P+ ---
    print(f"[seed {seed}] arm P+...", flush=True)
    models = new_committee(seed)
    path_wall = path_train_p0(
        models, path_stream("Pplus-path"), steps=M_PATH, shuffle_groups=False
    )
    probes_p0b = run_mechanism_probes(models, path_stream("probe-Pplus-pre"), "P0preP+")
    dest_wall, persistent, strata, _ = destination_train_with_checkpoints(
        models, pairs, labels, panel, horizon=H_DEST, freeze_trunk=True
    )
    probes_pp = run_mechanism_probes(models, path_stream("probe-Pplus"), "P+")
    results.append(
        ArmResult(
            "P+",
            seed,
            k_hash,
            path_wall_s=path_wall,
            dest_wall_s=dest_wall,
            first_persistent_step=persistent,
            strata=strata,
            probes={"P0pre": probes_p0b, "P+": probes_pp},
            scoring_mode="committee_head_frozen_trunk",
        )
    )

    # --- P_shuf ---
    print(f"[seed {seed}] arm P_shuf...", flush=True)
    models = new_committee(seed)
    path_wall = path_train_p0(
        models, path_stream("Pshuf-path"), steps=M_PATH, shuffle_groups=True
    )
    dest_wall, persistent, strata, _ = destination_train_with_checkpoints(
        models, pairs, labels, panel, horizon=H_DEST, freeze_trunk=True
    )
    results.append(
        ArmResult(
            "P_shuf",
            seed,
            k_hash,
            path_wall_s=path_wall,
            dest_wall_s=dest_wall,
            first_persistent_step=persistent,
            strata=strata,
            probes={},
            scoring_mode="committee_head_frozen_trunk",
        )
    )

    _ = path_d_support
    return results


# =============================================================================
# Report
# =============================================================================


def _fmt_strata_row(arm: str, seed: int, strata: dict, persistent, mode: str) -> str:
    cells = []
    for name in PANEL_STRATUM_COUNTS:
        s = strata.get(name, {})
        cells.append(
            f"{s.get('correct', '?')}/{s.get('need', '?')}"
            f"{'*' if s.get('qualifies') else ''}"
        )
    pers = "censored" if persistent is None else str(persistent)
    return (
        f"| {arm} | {seed} | " + " | ".join(cells) + f" | {pers} | {mode} |"
    )


def m3_check(p0_results: list[ArmResult]) -> tuple[bool, str]:
    """Pre-registered M3: P0 readout qualifies S1&S3; fails S2/S4/S5."""
    flags = []
    ok_all = True
    for r in p0_results:
        s = r.strata
        s1 = s["S1"]["qualifies"]
        s2 = s["S2"]["qualifies"]
        s3 = s["S3"]["qualifies"]
        s4 = s["S4"]["qualifies"]
        s5 = s["S5"]["qualifies"]
        expect = s1 and s3 and (not s2) and (not s4) and (not s5)
        if not expect:
            ok_all = False
            flags.append(
                f"seed{r.seed}: S1={s1} S2={s2} S3={s3} S4={s4} S5={s5} "
                f"(want S1&S3=True, S2/S4/S5=False) — DESIGN BUG FLAG"
            )
        else:
            flags.append(f"seed{r.seed}: M3 OK (S1&S3 qualify; S2/S4/S5 fail)")
    return ok_all, "; ".join(flags)


def write_report(
    all_results: list[ArmResult],
    overlap: dict,
    n_max: int,
    k: int,
    total_wall: float,
) -> str:
    p0s = [r for r in all_results if r.arm == "P0"]
    p0negs = [r for r in all_results if r.arm == "P0-neg"]
    m3_ok, m3_txt = m3_check(p0s)

    # Mechanism summary: sign(d) vs length control for P0
    mech_lines = []
    for r in all_results:
        for tag, pr in r.probes.items():
            mech_lines.append(
                f"| {r.arm} | {r.seed} | {tag} | "
                f"{pr['exact_d_acc']:.3f} | {pr['length_only_acc']:.3f} | "
                f"{pr.get('exact_d_within_length_acc', float('nan')):.3f} | "
                f"{pr['sign_d_acc']:.3f} | {pr['residue_acc_disjoint_d']:.3f} |"
            )

    # P+-over-P0 residue
    residue_delta_lines = []
    for seed in PILOT_SEEDS:
        p0 = next((r for r in all_results if r.arm == "P0" and r.seed == seed), None)
        pp = next((r for r in all_results if r.arm == "P+" and r.seed == seed), None)
        if p0 and pp and "P0" in p0.probes and "P+" in pp.probes:
            a0 = p0.probes["P0"]["residue_acc_disjoint_d"]
            a1 = pp.probes["P+"]["residue_acc_disjoint_d"]
            residue_delta_lines.append(
                f"- seed {seed}: P0 residue={a0:.3f}, P+ residue={a1:.3f}, "
                f"P+-over-P0 Δ={a1 - a0:+.3f}"
            )

    wrap_lines = []
    for r in p0negs + p0s:
        wrap_lines.append(
            f"- {r.arm} seed{r.seed}: anti-correct on wrap equals = "
            f"{r.wrap_anti_correct}/{r.wrap_n}"
        )

    rows = [
        _fmt_strata_row(
            r.arm, r.seed, r.strata, r.first_persistent_step, r.scoring_mode
        )
        for r in all_results
    ]

    lines = [
        "# B2_PILOT_08",
        "",
        "NON-CITABLE Stage-1 pilot (design-validation only). NOT the 6-block call.",
        "Implements `B2_PATH_VS_DESTINATION_DESIGN_V2.md` Stage 1. No src/ edits.",
        "No confirmatory datum.",
        "",
        "## Locked constants",
        "",
        f"- N_max (DIAG_04 curated distinct labeled pairs) = **{n_max}**",
        f"- K = floor(N_max/8) = **{k}** (not swept)",
        f"- H_DEST (oracle-stage horizon) = {H_DEST}",
        f"- M_PATH (path updates) = {M_PATH}",
        f"- PATH_BATCH={PATH_BATCH}, M_ROADS={M_ROADS}, VICReg "
        f"(inv={VICREG_INV}, var={VICREG_VAR}, cov={VICREG_COV})",
        f"- Path d-support = [{_D_PATH_LO},{_D_PATH_HI}] independent of n=66; "
        f"empty word (d=0,p=0) excluded from batches.",
        f"- Pilot seeds = {list(PILOT_SEEDS)}",
        f"- Total wall = {total_wall/60:.1f} min",
        "",
        "## Path firewall",
        "",
        "Path sampling/loss assert via `_assert_path_clean` that kwargs never "
        "include modulus/n/residue/fold/oracle/panel/truth. Path uses only "
        "`unrank_word` + `admissible_paddings` + token-count/`displacement` "
        "sameness checks. Oracle_eq and MODULUS appear only in destination "
        "K-set construction, panel scoring, and read-only residue probes.",
        "",
        "## Panel ⊥ train + displacement-class overlap",
        "",
        f"- K-set intersect panel word-pairs = 0 (asserted per seed).",
        f"- Displacement-class overlap: {overlap}",
        f"- {overlap['note']}",
        "",
        "## Per-arm per-stratum floor table",
        "",
        "correct/need with `*` if stratum qualifies. "
        "`first_persistent_step` on oracle-stage clock (censored if never); "
        "P0/P0-neg have no oracle stage.",
        "",
        "| arm | seed | S1 | S2 | S3 | S4 | S5 | first_persistent_step | scoring |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        *rows,
        "",
        "## M3 check (positive-path P0 read-only readout)",
        "",
        f"**M3_PASS = {m3_ok}**",
        "",
        m3_txt,
        "",
        "Pre-registered: S1 & S3 qualify; S2/S4/S5 fail. "
        "ANY deviation = design bug flag.",
        "",
        "## P0-neg false wall on 20 wrap items",
        "",
        *wrap_lines,
        "",
        "## Mechanism probes",
        "",
        "| arm | seed | tag | exact_d | length_only | d_within_len | sign(d) | residue(disjoint-d) |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        *mech_lines,
        "",
        "### P+-over-P0 residue",
        "",
        *(residue_delta_lines or ["- n/a"]),
        "",
        "## Clocks",
        "",
        "- Oracle-stage clock: destination CE steps (0..H_DEST), cadence 50.",
        "- Total-compute clock: path wall + dest wall (reported per arm in JSON).",
        f"- Device: {DEVICE}; runner: gpu_committee_runner (patched forward).",
        "",
        "## Verdict (pilot / design-validation)",
        "",
        (
            "M3 matched — pipeline consistent with displacement-mapping prediction; "
            "Stage-2 call may proceed if mechanism probes also show sign(d) "
            "surviving length control."
            if m3_ok
            else "M3 DEVIATION — treat as design bug; fix before Stage-2 call."
        ),
        "",
    ]
    report = "\n".join(lines)
    OUT_MD.write_text(report, encoding="utf-8")
    return report


def main() -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA required for B2 pilot")
    runner.patch_contact_transformer_device_guard()
    t_all = time.perf_counter()

    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel = DummyPanelBuilder(
        public_key, dummy_key(DEV_PANEL_LABEL, purpose="panel")
    ).build(MODULUS, world_slot=WORLD_SLOT)
    if len(panel.items) != PANEL_SIZE:
        raise RuntimeError("panel size drifted")

    n_max, k, schedule = compute_n_max_and_k(public_key, partition)
    path_d_support = set(range(_D_PATH_LO, _D_PATH_HI + 1))
    overlap = displacement_class_overlap(path_d_support, panel)
    print("displacement-class overlap:", overlap, flush=True)

    all_results: list[ArmResult] = []
    for seed in PILOT_SEEDS:
        all_results.extend(
            run_seed(seed, public_key, partition, panel, schedule, path_d_support)
        )

    total_wall = time.perf_counter() - t_all
    report = write_report(all_results, overlap, n_max, k, total_wall)

    serial = []
    for r in all_results:
        serial.append(
            {
                "arm": r.arm,
                "seed": r.seed,
                "k_hash": r.k_hash,
                "path_wall_s": r.path_wall_s,
                "dest_wall_s": r.dest_wall_s,
                "first_persistent_step": r.first_persistent_step,
                "strata": r.strata,
                "probes": r.probes,
                "wrap_anti_correct": r.wrap_anti_correct,
                "wrap_n": r.wrap_n,
                "scoring_mode": r.scoring_mode,
            }
        )
    OUT_JSON.write_text(
        json.dumps(
            {
                "N_max": n_max,
                "K": k,
                "H_DEST": H_DEST,
                "M_PATH": M_PATH,
                "overlap": overlap,
                "results": serial,
                "total_wall_s": total_wall,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote {OUT_MD} and {OUT_JSON}", flush=True)
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    main()
