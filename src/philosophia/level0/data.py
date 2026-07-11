from __future__ import annotations

from dataclasses import dataclass
import hashlib

import torch

from .config import ModelConfig, PINNED_TORCH_VERSION, RunConfig


@dataclass(frozen=True)
class LearnerView:
    inputs: torch.Tensor
    targets: torch.Tensor
    indices: torch.Tensor


@dataclass(frozen=True)
class EvaluationView:
    inputs: torch.Tensor
    targets: torch.Tensor
    indices: torch.Tensor


@dataclass(frozen=True)
class DatasetBundle:
    learner: LearnerView
    evaluation: EvaluationView
    universe_hash: str
    split_hash: str
    torch_version: str


def _tensor_hash(*tensors: torch.Tensor, prefix: str = "") -> str:
    digest = hashlib.sha256(prefix.encode("ascii"))
    for tensor in tensors:
        value = tensor.detach().cpu().contiguous()
        digest.update(str(value.dtype).encode("ascii"))
        digest.update(str(tuple(value.shape)).encode("ascii"))
        digest.update(value.numpy().tobytes())
    return digest.hexdigest()


def ordered_modular_addition(model: ModelConfig) -> tuple[torch.Tensor, torch.Tensor]:
    residues = torch.arange(model.modulus, dtype=torch.long)
    a = residues.repeat_interleave(model.modulus)
    b = residues.repeat(model.modulus)
    equals = torch.full_like(a, model.equals_token)
    inputs = torch.stack((a, b, equals), dim=1)
    targets = (a + b).remainder(model.modulus)
    return inputs, targets


def build_dataset(config: RunConfig, *, require_pinned_torch: bool = True) -> DatasetBundle:
    torch_version = torch.__version__.split("+", maxsplit=1)[0]
    if require_pinned_torch and torch_version != PINNED_TORCH_VERSION:
        raise RuntimeError(
            f"split requires torch {PINNED_TORCH_VERSION}, found {torch.__version__}"
        )

    inputs, targets = ordered_modular_addition(config.model)
    generator = torch.Generator(device="cpu").manual_seed(config.split_seed)
    permutation = torch.randperm(inputs.shape[0], generator=generator)
    train_count = int(0.30 * inputs.shape[0])
    train_indices = permutation[:train_count]
    evaluation_indices = permutation[train_count:]

    version_tag = f"torch-randperm:{torch_version}:seed:{config.split_seed}"
    return DatasetBundle(
        learner=LearnerView(
            inputs=inputs[train_indices].clone(),
            targets=targets[train_indices].clone(),
            indices=train_indices.clone(),
        ),
        evaluation=EvaluationView(
            inputs=inputs[evaluation_indices].clone(),
            targets=targets[evaluation_indices].clone(),
            indices=evaluation_indices.clone(),
        ),
        universe_hash=_tensor_hash(inputs, targets, prefix="lexicographic-v1"),
        split_hash=_tensor_hash(
            train_indices,
            evaluation_indices,
            prefix=version_tag,
        ),
        torch_version=torch_version,
    )


def random_label_control(bundle: DatasetBundle, *, seed: int) -> DatasetBundle:
    generator = torch.Generator(device="cpu").manual_seed(seed)
    total = bundle.learner.targets.numel() + bundle.evaluation.targets.numel()
    labels = torch.randint(0, 113, (total,), generator=generator)
    learner_count = bundle.learner.targets.numel()
    learner_labels = labels[:learner_count]
    evaluation_labels = labels[learner_count:]
    control_tag = f"random-labels-v1:{seed}:{bundle.split_hash}"
    return DatasetBundle(
        learner=LearnerView(
            bundle.learner.inputs.clone(),
            learner_labels,
            bundle.learner.indices.clone(),
        ),
        evaluation=EvaluationView(
            bundle.evaluation.inputs.clone(),
            evaluation_labels,
            bundle.evaluation.indices.clone(),
        ),
        universe_hash=_tensor_hash(labels, prefix=control_tag),
        split_hash=bundle.split_hash,
        torch_version=bundle.torch_version,
    )
