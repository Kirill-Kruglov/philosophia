"""NON-CITABLE GROKKING_PROBE_09: does a STANDARD learner grok Z/n equality?

Decisive first step of the actively-organized-contact line. Question: was the
Level-1 competence block a self-imposed design artifact (full-history O(B^2)),
or something deeper?

Method (NO src/ edits; dev world only; NON-CITABLE; no confirmatory datum):
  - Frozen Z/n equality task, modulus 66. Inputs via encode_pair; truth via
    oracle_eq. Panel/held-out DISJOINT from training (reuse frozen partition).
  - A SINGLE ContactTransformer (not the 4-member full-history committee).
  - Standard fixed-size MINIBATCHES, AdamW, class-balanced (balanced sampling),
    weight-decay ON and swept lightly {0.0, 0.01, 0.1, 1.0} (the grokking driver).
  - NO full history: cost is O(steps). Runs to a grokking-scale budget.

We reuse the frozen scoring floor verbatim (score_stratum / checkpoint_qualifies,
ACCURACY_MINIMUM, PANEL_STRATUM_COUNTS) and the reprprobe residue convention
(self-pair encode_pair(word,word); 66-way linear probe on pre-head readout).

Speed note: the frozen forward pads every pair to MODEL_INPUT_LENGTH=277 and runs
manual O(S^2) attention over mostly-padding, which is too slow for 10^5 steps on a
4060. We therefore train/eval THIS single learner with a self-consistent forward
that (a) crops leading PADs to the per-batch max content length (the last position
-- the equality readout slot -- is unchanged because encode_pair right-aligns
content) and (b) uses fused scaled_dot_product_attention. This does NOT touch src/
and the SAME forward is used for training and for every evaluation, so the learner
is internally consistent. Parameters/param-init/optimizer grouping mirror the
frozen model exactly; only the (mathematically standard) attention kernel and the
leading-pad crop differ, purely for throughput.

Writes successor/dev/GROKKING_PROBE_09.md and grokking_probe_09_results.json.
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

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
    MODEL_INPUT_LENGTH,
    PANEL_SIZE,
    PANEL_STRATUM_COUNTS,
    POOL_MULTIPLICITY,
)
from philosophia.level1.model import (  # noqa: E402
    D_MODEL,
    HEAD_WIDTH,
    HEADS,
    ContactTransformer,
    encode_pair,
)
from philosophia.level1.panel import DummyPanelBuilder  # noqa: E402
from philosophia.level1.pool import (  # noqa: E402
    partition_cells,
    realize_cell,
    verify_partition,
)
from philosophia.level1.scoring import (  # noqa: E402
    ACCURACY_MINIMUM,
    PanelObservation,
    checkpoint_qualifies,
    score_stratum,
)
from philosophia.level1.serialization import CounterStream, dummy_key  # noqa: E402
from philosophia.level1.world import fold, oracle_eq  # noqa: E402

import gpu_committee_runner as runner  # noqa: E402

# ---- Frozen world coordinates (same world/seeds as DIAG_01/02/04). --------
MODULUS = 66
WORLD_SLOT = 0
DEV_PUBLIC_LABEL = "successor-dev-competence-diag-01"
DEV_PANEL_LABEL = "successor-dev-competence-diag-01"

OUT_MD = _DEV / "GROKKING_PROBE_09.md"
OUT_JSON = _DEV / "grokking_probe_09_results.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
CHANCE_RESIDUE = 1.0 / MODULUS

# ---- Sweep / budget (grokking-scale; O(steps)). ---------------------------
SMOKE = os.environ.get("GROK_SMOKE", "0") == "1"
if SMOKE:
    WEIGHT_DECAYS = (1.0,)
    SEEDS = (0,)
    STEPS = 300
    CKPT_EVERY = 100
    TRAIN_UNEQUAL = 256
    HELDOUT_CAP = 400
    PROBE_PER_RESIDUE = 8
    RESIDUE_PROBE_EPOCHS = 40
else:
    WEIGHT_DECAYS = (0.0, 0.01, 0.1, 1.0)
    SEEDS = (0,)
    STEPS = int(os.environ.get("GROK_STEPS", "40000"))
    CKPT_EVERY = int(os.environ.get("GROK_CKPT", "2000"))
    TRAIN_UNEQUAL = 1256  # balances the ~1256 distinct acquisition equal pairs
    HELDOUT_CAP = 1600
    PROBE_PER_RESIDUE = 40
    RESIDUE_PROBE_EPOCHS = 120

MICROBATCH = 256          # standard fixed minibatch (128 equal + 128 unequal)
LR = 1e-3
BETAS = (0.9, 0.98)
EPS = 1e-8
PROBE_SEED = 90926


# ---------------------------------------------------------------------------
# Self-consistent fast forward (crop leading PAD + fused SDPA). No src/ edits.
# ---------------------------------------------------------------------------
def _crop(tokens: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    length = int(tokens.ne(0).sum(dim=1).max().item())
    cropped = tokens[:, MODEL_INPUT_LENGTH - length :]
    return cropped, cropped.ne(0)


def _prehead(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    """Pre-head readout final_ln(x)[:, -1, :] (the vector the equality head sees).

    Uses cropped positions + fused attention; last position is the final content
    token for every row because encode_pair right-aligns content.
    """
    cropped, key_mask = _crop(tokens)
    batch, seq = cropped.shape
    positions = torch.arange(seq, device=tokens.device)
    x = model.token_embedding[cropped] + model.position_embedding[positions][None, :, :]
    attn_mask = key_mask[:, None, None, :]  # (B,1,1,S) bool keep
    for layer in model.layers:
        n = layer.ln1(x)
        q = (n @ layer.W_Q).view(batch, seq, HEADS, HEAD_WIDTH).transpose(1, 2)
        k = (n @ layer.W_K).view(batch, seq, HEADS, HEAD_WIDTH).transpose(1, 2)
        v = (n @ layer.W_V).view(batch, seq, HEADS, HEAD_WIDTH).transpose(1, 2)
        a = F.scaled_dot_product_attention(q, k, v, attn_mask=attn_mask)
        a = a.transpose(1, 2).contiguous().view(batch, seq, D_MODEL)
        x = x + a @ layer.W_O
        n2 = layer.ln2(x)
        x = x + torch.relu(n2 @ layer.W_in + layer.b_in) @ layer.W_out + layer.b_out
    return model.final_ln(x)[:, -1, :]


def _logits(model: ContactTransformer, tokens: torch.Tensor) -> torch.Tensor:
    return _prehead(model, tokens) @ model.head_W + model.head_b


@torch.no_grad()
def _p_equal(model: ContactTransformer, tokens: torch.Tensor, *, chunk: int = 512) -> torch.Tensor:
    outs = []
    for start in range(0, tokens.shape[0], chunk):
        sl = tokens[start : start + chunk]
        outs.append(torch.softmax(_logits(model, sl), dim=-1)[:, 1])
    return torch.cat(outs, dim=0)


@torch.no_grad()
def _prehead_batched(model: ContactTransformer, tokens: torch.Tensor, *, chunk: int = 512) -> torch.Tensor:
    outs = []
    for start in range(0, tokens.shape[0], chunk):
        outs.append(_prehead(model, tokens[start : start + chunk]))
    return torch.cat(outs, dim=0)


def _make_optimizer(model: ContactTransformer, weight_decay: float) -> torch.optim.AdamW:
    """Mirror build_optimizer's param grouping; only the wd magnitude is swept."""
    decayed = []
    for layer in model.layers:
        decayed.extend((layer.W_Q, layer.W_K, layer.W_V, layer.W_O, layer.W_in, layer.W_out))
    decayed.append(model.head_W)
    non_decayed = [model.token_embedding, model.position_embedding]
    for layer in model.layers:
        non_decayed.extend((layer.ln1.weight, layer.ln1.bias, layer.ln2.weight, layer.ln2.bias))
    non_decayed.extend((model.final_ln.weight, model.final_ln.bias))
    for layer in model.layers:
        non_decayed.extend((layer.b_in, layer.b_out))
    non_decayed.append(model.head_b)
    return torch.optim.AdamW(
        [
            {"params": decayed, "weight_decay": weight_decay},
            {"params": non_decayed, "weight_decay": 0.0},
        ],
        lr=LR,
        betas=BETAS,
        eps=EPS,
    )


# ---------------------------------------------------------------------------
# Data (fixed train set from acquisition; held-out from reserved + panel).
# ---------------------------------------------------------------------------
def _pair_key(left: bytes, right: bytes) -> tuple[bytes, bytes]:
    return (left, right)


def _build_datasets(public_key, partition, panel):
    stream = CounterStream(public_key, ("L1", "grokking-09", "data"))

    # --- train equals: ALL acquisition equal-cell realizations (distinct) ---
    train_equal: list[tuple[bytes, bytes]] = []
    for cell in partition.acquisition:
        if cell.difference % MODULUS == 0:
            for left, right in realize_cell(public_key, cell):
                if not oracle_eq(left, right, MODULUS):
                    raise RuntimeError("equal-cell realization failed oracle_eq")
                train_equal.append((left, right))

    # --- train unequals: sample acquisition unequal-cell realizations --------
    unequal_cells = [c for c in partition.acquisition if c.difference % MODULUS != 0]
    train_unequal: list[tuple[bytes, bytes]] = []
    seen_uneq: set[tuple[bytes, bytes]] = set()
    while len(train_unequal) < TRAIN_UNEQUAL:
        cell = unequal_cells[stream.uniform(len(unequal_cells))]
        left, right = realize_cell(public_key, cell)[stream.uniform(POOL_MULTIPLICITY)]
        if oracle_eq(left, right, MODULUS):
            raise RuntimeError("unequal-cell realization satisfied oracle_eq")
        key = _pair_key(left, right)
        if key in seen_uneq:
            continue
        seen_uneq.add(key)
        train_unequal.append((left, right))

    train_pairs = {_pair_key(a, b) for a, b in train_equal} | set(seen_uneq)

    # --- held-out (reserved) equals + unequals, disjoint from train/panel ----
    panel_pairs = {_pair_key(i.left, i.right) for i in panel.items}
    held_equal: list[tuple[bytes, bytes]] = []
    held_unequal: list[tuple[bytes, bytes]] = []
    for cell in partition.reserved:
        for left, right in realize_cell(public_key, cell):
            key = _pair_key(left, right)
            if key in train_pairs or key in panel_pairs:
                continue
            if oracle_eq(left, right, MODULUS):
                if len(held_equal) < HELDOUT_CAP:
                    held_equal.append((left, right))
            else:
                if len(held_unequal) < HELDOUT_CAP:
                    held_unequal.append((left, right))
        if len(held_equal) >= HELDOUT_CAP and len(held_unequal) >= HELDOUT_CAP:
            break
    n_hold = min(len(held_equal), len(held_unequal))
    held_equal = held_equal[:n_hold]
    held_unequal = held_unequal[:n_hold]

    # --- residue-probe novel words (reserved + panel), self-paired -----------
    by_res: dict[int, list[bytes]] = defaultdict(list)
    seen_words: set[bytes] = set()

    def consider(word: bytes) -> None:
        if word in seen_words:
            return
        seen_words.add(word)
        r = fold(word, MODULUS)
        if len(by_res[r]) < PROBE_PER_RESIDUE:
            by_res[r].append(word)

    for item in panel.items:
        consider(item.left)
        consider(item.right)
    for cell in partition.reserved:
        for left, right in realize_cell(public_key, cell):
            consider(left)
            consider(right)
        if all(len(by_res[r]) >= PROBE_PER_RESIDUE for r in range(MODULUS)):
            break

    # disjoint stratified split of novel words (70/30) for the residue probe
    probe_train_w: list[bytes] = []
    probe_test_w: list[bytes] = []
    for r in range(MODULUS):
        words = list(by_res.get(r, []))
        if not words:
            continue
        order = list(range(len(words)))
        for i in range(len(order) - 1, 0, -1):
            j = stream.uniform(i + 1)
            order[i], order[j] = order[j], order[i]
        words = [words[i] for i in order]
        if len(words) == 1:
            probe_train_w.append(words[0])
            continue
        n_test = min(max(1, int(round(0.3 * len(words)))), len(words) - 1)
        probe_test_w.extend(words[:n_test])
        probe_train_w.extend(words[n_test:])

    return {
        "train_equal": train_equal,
        "train_unequal": train_unequal,
        "train_pairs": train_pairs,
        "panel_pairs": panel_pairs,
        "held_equal": held_equal,
        "held_unequal": held_unequal,
        "probe_train_w": probe_train_w,
        "probe_test_w": probe_test_w,
    }


def _stack(pairs, device=None) -> torch.Tensor:
    t = torch.stack([encode_pair(a, b) for a, b in pairs])
    return t.to(device) if device is not None else t


# ---------------------------------------------------------------------------
# Residue linear probe (softmax, frozen activations; only W,b trained).
# ---------------------------------------------------------------------------
def _fit_residue_probe(x_tr, y_tr, x_te, y_te, *, epochs: int) -> dict:
    torch.manual_seed(PROBE_SEED)
    x_tr = x_tr.to(DEVICE).float()
    x_te = x_te.to(DEVICE).float()
    y_tr = y_tr.to(DEVICE)
    y_te = y_te.to(DEVICE)
    mean = x_tr.mean(dim=0, keepdim=True)
    std = x_tr.std(dim=0, keepdim=True).clamp_min(1e-6)
    x_tr = (x_tr - mean) / std
    x_te = (x_te - mean) / std
    W = torch.zeros(D_MODEL, MODULUS, device=DEVICE, requires_grad=True)
    b = torch.zeros(MODULUS, device=DEVICE, requires_grad=True)
    opt = torch.optim.Adam([W, b], lr=0.05, weight_decay=1e-2)
    n = x_tr.shape[0]
    for _ in range(epochs):
        perm = torch.randperm(n, device=DEVICE)
        for start in range(0, n, 256):
            idx = perm[start : start + 256]
            loss = F.cross_entropy(x_tr[idx] @ W + b, y_tr[idx])
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step()
    with torch.no_grad():
        tr_acc = float(((x_tr @ W + b).argmax(-1) == y_tr).float().mean())
        te_acc = float(((x_te @ W + b).argmax(-1) == y_te).float().mean())
    return {"train_acc": tr_acc, "test_acc": te_acc, "n_train": int(n), "n_test": int(x_te.shape[0])}


# ---------------------------------------------------------------------------
# Evaluation at a checkpoint.
# ---------------------------------------------------------------------------
@dataclass
class Checkpoint:
    step: int
    train_acc: float
    heldout_acc: float
    heldout_eq_acc: float
    heldout_neq_acc: float
    gap: float
    panel_qualifies: bool
    panel_strata_ok: int
    panel_stratum_acc: dict
    panel_stratum_correct: dict
    panel_mean_brier: float
    residue_probe_test: float
    residue_probe_train: float


def _eval_checkpoint(step, model, tensors, panel, probe_tokens, probe_y, n_probe_train) -> Checkpoint:
    model.eval()
    with torch.no_grad():
        tr_eq = _p_equal(model, tensors["train_eq_tok"])
        tr_neq = _p_equal(model, tensors["train_neq_tok"])
        train_acc = float(
            ((tr_eq >= 0.5).float().sum() + (tr_neq < 0.5).float().sum())
            / (tr_eq.numel() + tr_neq.numel())
        )
        h_eq = _p_equal(model, tensors["held_eq_tok"])
        h_neq = _p_equal(model, tensors["held_neq_tok"])
        held_eq_acc = float((h_eq >= 0.5).float().mean()) if h_eq.numel() else float("nan")
        held_neq_acc = float((h_neq < 0.5).float().mean()) if h_neq.numel() else float("nan")
        heldout_acc = float(
            ((h_eq >= 0.5).float().sum() + (h_neq < 0.5).float().sum())
            / (h_eq.numel() + h_neq.numel())
        )

        # Frozen floor on the panel (verbatim scoring rules).
        panel_p = _p_equal(model, tensors["panel_tok"]).clamp(0.0, 1.0).detach().cpu().tolist()
        observations = [
            PanelObservation(item.stratum, item.truth, float(p))
            for item, p in zip(panel.items, panel_p, strict=True)
        ]
        by_stratum = {}
        stratum_acc = {}
        stratum_correct = {}
        for name in PANEL_STRATUM_COUNTS:
            vals = [o for o in observations if o.stratum == name]
            sc = score_stratum(name, vals)
            by_stratum[name] = sc
            stratum_correct[name] = int(sc.correct)
            stratum_acc[name] = round(sc.correct / sc.count, 4)
        qualifies = checkpoint_qualifies(observations)
        strata_ok = sum(1 for s in by_stratum.values() if s.qualifies)
        mean_brier = sum(s.brier for s in by_stratum.values()) / len(by_stratum)

        # Residue linear probe on frozen pre-head activations at this step.
        acts = _prehead_batched(model, probe_tokens)
    residue = _fit_residue_probe(
        acts[:n_probe_train], probe_y[:n_probe_train],
        acts[n_probe_train:], probe_y[n_probe_train:],
        epochs=RESIDUE_PROBE_EPOCHS,
    )
    model.train()
    return Checkpoint(
        step=step,
        train_acc=round(train_acc, 4),
        heldout_acc=round(heldout_acc, 4),
        heldout_eq_acc=round(held_eq_acc, 4),
        heldout_neq_acc=round(held_neq_acc, 4),
        gap=round(train_acc - heldout_acc, 4),
        panel_qualifies=bool(qualifies),
        panel_strata_ok=int(strata_ok),
        panel_stratum_acc=stratum_acc,
        panel_stratum_correct=stratum_correct,
        panel_mean_brier=round(mean_brier, 6),
        residue_probe_test=round(residue["test_acc"], 4),
        residue_probe_train=round(residue["train_acc"], 4),
    )


def _train_one(weight_decay, seed, tensors, panel, probe_tokens, probe_y, n_probe_train):
    model_key = dummy_key(f"successor-dev-grokking-09-seed-{seed}", purpose="public-root")
    model = ContactTransformer(model_key, block=WORLD_SLOT, replicate=1, member=0).to(DEVICE)
    opt = _make_optimizer(model, weight_decay)
    model.train()

    eq_tok = tensors["train_eq_tok"]
    neq_tok = tensors["train_neq_tok"]
    n_eq = eq_tok.shape[0]
    n_neq = neq_tok.shape[0]
    half = MICROBATCH // 2
    gen = torch.Generator(device=DEVICE)
    gen.manual_seed(1000 + seed)

    records: list[Checkpoint] = []
    t0 = time.perf_counter()
    rec0 = _eval_checkpoint(0, model, tensors, panel, probe_tokens, probe_y, n_probe_train)
    records.append(rec0)
    print(
        f"[wd={weight_decay} seed={seed}] step 0: train={rec0.train_acc} "
        f"held={rec0.heldout_acc} (eq={rec0.heldout_eq_acc}/neq={rec0.heldout_neq_acc}) "
        f"resid={rec0.residue_probe_test} qualifies={rec0.panel_qualifies}",
        flush=True,
    )

    for step in range(1, STEPS + 1):
        ei = torch.randint(0, n_eq, (half,), generator=gen, device=DEVICE)
        ni = torch.randint(0, n_neq, (half,), generator=gen, device=DEVICE)
        batch = torch.cat([eq_tok[ei], neq_tok[ni]], dim=0)
        labels = torch.cat(
            [torch.ones(half, dtype=torch.long, device=DEVICE),
             torch.zeros(half, dtype=torch.long, device=DEVICE)]
        )
        opt.zero_grad(set_to_none=True)
        with torch.autocast("cuda", dtype=torch.bfloat16, enabled=(DEVICE.type == "cuda")):
            loss = F.cross_entropy(_logits(model, batch), labels)
        loss.backward()
        opt.step()

        if step % CKPT_EVERY == 0:
            rec = _eval_checkpoint(step, model, tensors, panel, probe_tokens, probe_y, n_probe_train)
            records.append(rec)
            elapsed = time.perf_counter() - t0
            print(
                f"[wd={weight_decay} seed={seed}] step {step}/{STEPS} "
                f"({elapsed/60:.1f}m): train={rec.train_acc} held={rec.heldout_acc} "
                f"(eq={rec.heldout_eq_acc}/neq={rec.heldout_neq_acc}) gap={rec.gap} "
                f"resid={rec.residue_probe_test} strata_ok={rec.panel_strata_ok}/5 "
                f"qualifies={rec.panel_qualifies} brier={rec.panel_mean_brier}",
                flush=True,
            )
    wall = time.perf_counter() - t0
    return records, wall


def _fmt_pct(x: float) -> str:
    return "n/a" if x != x else f"{100.0 * x:.2f}%"


def main() -> None:
    runner.patch_contact_transformer_device_guard()
    if DEVICE.type == "cuda":
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True

    public_key = dummy_key(DEV_PUBLIC_LABEL, purpose="public-root")
    partition = partition_cells(public_key)
    verify_partition(partition)
    panel = DummyPanelBuilder(public_key, dummy_key(DEV_PANEL_LABEL, purpose="panel")).build(
        MODULUS, world_slot=WORLD_SLOT
    )
    if len(panel.items) != PANEL_SIZE:
        raise RuntimeError("panel size drifted from frozen PANEL_SIZE")

    print("building datasets...", flush=True)
    data = _build_datasets(public_key, partition, panel)

    # Disjointness (report + hard assert).
    tp = data["train_pairs"]
    pp = data["panel_pairs"]
    held = {_pair_key(a, b) for a, b in data["held_equal"] + data["held_unequal"]}
    acq_cells = set(partition.acquisition)
    panel_cell_overlap = any(item.cell in acq_cells for item in panel.items)
    disjoint = {
        "n_train_equal": len(data["train_equal"]),
        "n_train_unequal": len(data["train_unequal"]),
        "n_train_pairs": len(tp),
        "n_panel_pairs": len(pp),
        "n_heldout_equal": len(data["held_equal"]),
        "n_heldout_unequal": len(data["held_unequal"]),
        "train_intersect_panel": len(tp & pp),
        "train_intersect_heldout": len(tp & held),
        "heldout_intersect_panel": len(held & pp),
        "panel_cell_in_acquisition": bool(panel_cell_overlap),
        "n_probe_train_words": len(data["probe_train_w"]),
        "n_probe_test_words": len(data["probe_test_w"]),
    }
    print("disjointness:", json.dumps(disjoint), flush=True)
    for k in ("train_intersect_panel", "train_intersect_heldout", "heldout_intersect_panel"):
        if disjoint[k] != 0:
            raise RuntimeError(f"disjointness violated: {k}={disjoint[k]}")
    if panel_cell_overlap:
        raise RuntimeError("panel used an acquisition cell")

    # Precompute tensors (kept on device).
    tensors = {
        "train_eq_tok": _stack(data["train_equal"], DEVICE),
        "train_neq_tok": _stack(data["train_unequal"], DEVICE),
        "held_eq_tok": _stack(data["held_equal"], DEVICE),
        "held_neq_tok": _stack(data["held_unequal"], DEVICE),
        "panel_tok": _stack([(i.left, i.right) for i in panel.items], DEVICE),
    }
    probe_words = data["probe_train_w"] + data["probe_test_w"]
    probe_tokens = torch.stack([encode_pair(w, w) for w in probe_words]).to(DEVICE)
    probe_y = torch.tensor([fold(w, MODULUS) for w in probe_words], dtype=torch.long)
    n_probe_train = len(data["probe_train_w"])

    all_results = {"disjointness": disjoint, "config": {
        "modulus": MODULUS, "world_slot": WORLD_SLOT, "device": str(DEVICE),
        "microbatch": MICROBATCH, "steps": STEPS, "ckpt_every": CKPT_EVERY,
        "lr": LR, "betas": list(BETAS), "eps": EPS,
        "weight_decays": list(WEIGHT_DECAYS), "seeds": list(SEEDS),
        "forward": "cropped-leading-pad + fused SDPA (self-consistent; train==eval)",
        "public_label": DEV_PUBLIC_LABEL, "panel_label": DEV_PANEL_LABEL,
        "torch": torch.__version__,
        "device_name": torch.cuda.get_device_name(0) if DEVICE.type == "cuda" else "cpu",
    }, "runs": []}

    total_wall = 0.0
    for wd in WEIGHT_DECAYS:
        for seed in SEEDS:
            records, wall = _train_one(
                wd, seed, tensors, panel, probe_tokens, probe_y, n_probe_train
            )
            total_wall += wall
            best_held = max(r.heldout_acc for r in records)
            ever_qual = any(r.panel_qualifies for r in records)
            best_resid = max(r.residue_probe_test for r in records)
            all_results["runs"].append({
                "weight_decay": wd,
                "seed": seed,
                "wall_s": round(wall, 1),
                "best_heldout_acc": best_held,
                "best_residue_probe": best_resid,
                "ever_cleared_floor": ever_qual,
                "checkpoints": [asdict(r) for r in records],
            })
            OUT_JSON.write_text(json.dumps(all_results, indent=2), encoding="utf-8")
            print(
                f"== wd={wd} seed={seed} done: best_held={best_held} "
                f"best_resid={best_resid} ever_floor={ever_qual} wall={wall/60:.1f}m",
                flush=True,
            )

    all_results["total_wall_s"] = round(total_wall, 1)
    OUT_JSON.write_text(json.dumps(all_results, indent=2), encoding="utf-8")

    report = _compose_report(all_results)
    OUT_MD.write_text(report, encoding="utf-8")
    print(f"wrote {OUT_MD}", flush=True)
    sys.stdout.buffer.write((report + "\n").encode("utf-8", errors="replace"))
    sys.stdout.buffer.flush()


def _compose_report(res: dict) -> str:
    dj = res["disjointness"]
    cfg = res["config"]
    runs = res["runs"]

    # Best run = highest held-out accuracy, tiebreak residue probe.
    best_run = max(runs, key=lambda r: (r["best_heldout_acc"], r["best_residue_probe"]))
    grokked = best_run["best_heldout_acc"] >= 0.85
    any_floor = any(r["ever_cleared_floor"] for r in runs)

    if grokked:
        tag = "COMPETENT-LEARNER-EXISTS"
        body = (
            f"COMPETENT-LEARNER-EXISTS: a single standard ContactTransformer trained "
            f"with fixed-size minibatches + AdamW (weight_decay={best_run['weight_decay']}, "
            f"seed={best_run['seed']}) GENERALIZES to held-out DISJOINT pairs, reaching "
            f"held-out equality accuracy {_fmt_pct(best_run['best_heldout_acc'])} "
            f"(chance 50%) with a residue-mod-{MODULUS} linear probe rising to "
            f"{_fmt_pct(best_run['best_residue_probe'])} (chance {_fmt_pct(CHANCE_RESIDUE)}). "
            f"The Level-1 competence block was therefore a self-imposed artifact of the "
            f"full-history O(B^2) design, not a property of the world/task. "
            f"Frozen-floor clearance at any checkpoint (stringent bar): "
            f"{'YES' if any_floor else 'NO'} (reported separately from held-out accuracy). "
            f"ACTIVE experiment is unblocked."
        )
    else:
        tag = "NO-COMPETENCE"
        body = (
            f"NO-COMPETENCE: across the weight-decay sweep {list(cfg['weight_decays'])} "
            f"(seed(s) {list(cfg['seeds'])}, up to {cfg['steps']} steps), no single "
            f"standard learner grokked. Best held-out equality accuracy = "
            f"{_fmt_pct(best_run['best_heldout_acc'])} (chance 50%) at "
            f"weight_decay={best_run['weight_decay']}, and the residue-mod-{MODULUS} "
            f"linear probe peaked at {_fmt_pct(best_run['best_residue_probe'])} "
            f"(chance {_fmt_pct(CHANCE_RESIDUE)}) -- the modular circuit did not form. "
            f"Frozen-floor clearance at any checkpoint: {'YES' if any_floor else 'NO'}. "
            f"Removing full-history did not unlock competence, so the block is deeper "
            f"(floor/world/task), not merely the O(B^2) training design -- escalate."
        )

    lines = [
        "# GROKKING_PROBE_09",
        "",
        "NON-CITABLE grokking probe. Dev world only. No confirmatory datum. "
        "No src/ edits (world.py / scoring.py / encode_pair / oracle_eq / floor / "
        "panel / config reused verbatim).",
        "",
        f"env: torch={cfg['torch']}; device={cfg['device_name']}; "
        f"cuda_available={cfg['device']=='cuda'}.",
        "",
        "## Question",
        "",
        "Was the Level-1 competence block a self-imposed design artifact "
        "(full-history O(B^2) committee), or something deeper? Test whether a "
        "STANDARD single-model learner GROKS the Z/n equality task (modulus "
        f"{MODULUS}) without full history.",
        "",
        "## Learner / training",
        "",
        f"- architecture: a SINGLE ContactTransformer (d_model={D_MODEL}, heads={HEADS}, "
        "2 layers) -- NOT the 4-member full-history committee.",
        f"- objective: class-balanced CE via BALANCED minibatches "
        f"({MICROBATCH//2} equal + {MICROBATCH//2} unequal per step; equal pairs are "
        "~1.5% of the pool, so balanced sampling prevents majority collapse per DIAG_01).",
        f"- optimizer: AdamW lr={cfg['lr']} betas={tuple(cfg['betas'])} eps={cfg['eps']}; "
        "weight_decay ON attention/MLP/head_W, 0.0 on embeddings/LN/biases (mirrors "
        "build_optimizer grouping). weight_decay is the grokking driver -- swept "
        f"{list(cfg['weight_decays'])}.",
        f"- budget: NO full history -> O(steps); {cfg['steps']} minibatch steps per run, "
        f"checkpoint every {cfg['ckpt_every']}. seeds {list(cfg['seeds'])}.",
        f"- forward: {cfg['forward']} -- mathematically standard attention; the SAME "
        "forward is used for training and for every evaluation (residue probe, panel "
        "floor, held-out), so the learner is internally consistent. Parameters and "
        "initialization are the frozen ContactTransformer's.",
        "",
        "## Panel <-> train disjointness",
        "",
        f"- train pairs (acquisition only): {dj['n_train_pairs']} "
        f"({dj['n_train_equal']} equal + {dj['n_train_unequal']} unequal).",
        f"- held-out pairs (reserved, balanced): {dj['n_heldout_equal']} equal + "
        f"{dj['n_heldout_unequal']} unequal.",
        f"- panel pairs: {dj['n_panel_pairs']} (frozen PANEL_SIZE={PANEL_SIZE}).",
        f"- train ∩ panel = {dj['train_intersect_panel']}; "
        f"train ∩ held-out = {dj['train_intersect_heldout']}; "
        f"held-out ∩ panel = {dj['heldout_intersect_panel']}; "
        f"panel-cell-in-acquisition = {dj['panel_cell_in_acquisition']} (all must be "
        "0/False).",
        f"- residue-probe novel words: train={dj['n_probe_train_words']}, "
        f"test={dj['n_probe_test_words']} (disjoint, stratified by residue).",
        "",
        f"Total wall-clock (all runs): {res.get('total_wall_s', 0.0):.1f} s "
        f"({res.get('total_wall_s', 0.0)/3600:.2f} h).",
        "",
        "## Sweep summary",
        "",
        "| weight_decay | seed | best held-out acc | best residue probe | "
        "ever cleared floor | wall (min) |",
        "| ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for r in runs:
        lines.append(
            f"| {r['weight_decay']} | {r['seed']} | {_fmt_pct(r['best_heldout_acc'])} | "
            f"{_fmt_pct(r['best_residue_probe'])} | {r['ever_cleared_floor']} | "
            f"{r['wall_s']/60:.1f} |"
        )
    lines += [
        "",
        f"chance: held-out equality = 50.00%; residue-mod-{MODULUS} probe = "
        f"{_fmt_pct(CHANCE_RESIDUE)}. Frozen floor (stringent, per stratum): "
        + ", ".join(f"{k}>={v}/{PANEL_STRATUM_COUNTS[k]}" for k, v in ACCURACY_MINIMUM.items())
        + ", abstain<=2, brier<=0.10.",
        "",
        f"## Grokking curve (best run: weight_decay={best_run['weight_decay']}, "
        f"seed={best_run['seed']})",
        "",
        "| step | train acc | held-out acc | held eq | held neq | gap | "
        f"residue probe | panel strata_ok | panel qualifies | mean brier |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for c in best_run["checkpoints"]:
        lines.append(
            f"| {c['step']} | {_fmt_pct(c['train_acc'])} | {_fmt_pct(c['heldout_acc'])} | "
            f"{_fmt_pct(c['heldout_eq_acc'])} | {_fmt_pct(c['heldout_neq_acc'])} | "
            f"{c['gap']:+.4f} | {_fmt_pct(c['residue_probe_test'])} | "
            f"{c['panel_strata_ok']}/5 | {c['panel_qualifies']} | {c['panel_mean_brier']:.4f} |"
        )

    lines += [
        "",
        "### Best-run per-stratum held-out (panel) accuracy vs step (S1-S5)",
        "",
        "| step | " + " | ".join(PANEL_STRATUM_COUNTS.keys()) + " |",
        "| ---: | " + " | ".join("---:" for _ in PANEL_STRATUM_COUNTS) + " |",
    ]
    for c in best_run["checkpoints"]:
        cells = [str(c["step"])]
        for name in PANEL_STRATUM_COUNTS:
            cells.append(_fmt_pct(c["panel_stratum_acc"][name]))
        lines.append("| " + " | ".join(cells) + " |")

    lines += ["", "## Verdict", "", f"**{tag}**", "", body, ""]
    return "\n".join(lines)


if __name__ == "__main__":
    main()
