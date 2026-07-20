"""Governance and deterministic world primitives for the Officina successor.

The signed WP-3/WP-4 build surface exposes no real-world, entropy, training,
qualification, or outcome entry point. All executable world contacts remain
explicitly test-only until a separately reviewed T-activation gate.
"""

from .canonical import canonical_json, sha256_bytes, sha256_file
from .interlock import ExecutionNotAuthorized

__all__ = [
    "ExecutionNotAuthorized",
    "canonical_json",
    "sha256_bytes",
    "sha256_file",
]
