"""Establish the locked Level 0 runtime before test collection uses PyTorch."""

from philosophia.level0.config import configure_canonical_torch_runtime


configure_canonical_torch_runtime()
