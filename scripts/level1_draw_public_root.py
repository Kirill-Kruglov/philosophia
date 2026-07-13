from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import re
import secrets
import subprocess

import torch

from philosophia.level1.model import configure_canonical_runtime
from philosophia.level1.public_root import (
    atomic_create,
    build_claim,
    build_transcript,
    canonical_json,
    derive_public_allocations,
    load_durable_transcript,
    sha256_file,
)


TRANSCRIPT_RELATIVE = Path("experiments/level_1_contact/allocation/PUBLIC_ROOT_TRANSCRIPT.json")
CLAIM_RELATIVE = Path("experiments/level_1_contact/allocation/PUBLIC_ROOT_DRAW_CLAIM.json")
COMMIT_PENDING_RELATIVE = Path("experiments/level_1_contact/allocation/PUBLIC_ROOT_COMMIT_PENDING.json")
INVALIDITY_RELATIVE = Path("experiments/level_1_contact/allocation/PUBLIC_ROOT_INVALIDITY_REQUIRED.json")
REQUIRED_SPECS = (
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md"),
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md"),
)
GOVERNING_LINEAGE = (
    *REQUIRED_SPECS,
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md"),
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md"),
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_3_CORRECTION.md"),
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md"),
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_1_PANEL_CORRECTION.md"),
    Path("experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md"),
    Path("experiments/level_1_contact/PANEL_CONTRACT_SIGNATURE.md"),
)
REVIEWED_SOURCE_PATHS = (
    "scripts/level1_draw_public_root.py",
    "src/philosophia/level1/public_root.py",
    "src/philosophia/level1/allocation.py",
    "src/philosophia/level1/serialization.py",
    "src/philosophia/level1/model.py",
)


def _run_git(repo: Path, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments], cwd=repo, check=check, capture_output=True, text=True
    )


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _validate_head(value: str, name: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ValueError(f"{name} must be a full lowercase commit hash")


def _preflight(repo: Path, expected_head: str, reviewed_code_head: str) -> str:
    _validate_head(expected_head, "--expected-head")
    _validate_head(reviewed_code_head, "--reviewed-code-head")
    actual_root = Path(_run_git(repo, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    if actual_root != repo.resolve():
        raise RuntimeError("script path is not inside the expected repository root")
    actual_head = _run_git(repo, "rev-parse", "HEAD").stdout.strip()
    if actual_head != expected_head:
        raise RuntimeError(f"reviewed HEAD mismatch: expected {expected_head}, found {actual_head}")
    if _run_git(repo, "cat-file", "-e", f"{reviewed_code_head}^{{commit}}", check=False).returncode:
        raise RuntimeError("reviewed code HEAD is not a local commit")
    if _run_git(
        repo, "diff", "--quiet", reviewed_code_head, actual_head, "--", *REVIEWED_SOURCE_PATHS,
        check=False,
    ).returncode:
        raise RuntimeError("execution source bytes differ from the reviewed code HEAD")
    if _run_git(repo, "diff", "--quiet", check=False).returncode != 0:
        raise RuntimeError("tracked working tree must be clean before the draw")
    if _run_git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
        raise RuntimeError("git index must be empty before the draw")
    for relative in (
        TRANSCRIPT_RELATIVE,
        CLAIM_RELATIVE,
        COMMIT_PENDING_RELATIVE,
        INVALIDITY_RELATIVE,
    ):
        final = repo / relative
        temporary = final.with_name(f".{final.name}.tmp")
        if final.exists() or temporary.exists():
            raise FileExistsError(f"one-shot root artifact already exists: {relative}")
    for path in GOVERNING_LINEAGE:
        if not (repo / path).is_file():
            raise FileNotFoundError(path)
    return actual_head


def _environment() -> dict[str, object]:
    return {
        "python_build": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "torch_build": torch.__version__,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "device": "cpu",
        "dtype": "float32",
        "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
        "torch_threads": torch.get_num_threads(),
        "torch_interop_threads": torch.get_num_interop_threads(),
    }


def _record_invalidity(repo: Path, expected_head: str, error: BaseException) -> None:
    path = repo / INVALIDITY_RELATIVE
    if path.exists():
        return
    payload = {
        "schema": "philosophia.level1.public-root-invalidity-required.v1",
        "scientific_outcome": False,
        "expected_head": expected_head,
        "recorded_utc": _utc_now(),
        "error_type": type(error).__name__,
        "error": str(error),
        "required_action": "signed invalidity decision; never redraw",
    }
    atomic_create(path, canonical_json(payload))


def _record_commit_pending(repo: Path, expected_head: str, error: BaseException) -> None:
    path = repo / COMMIT_PENDING_RELATIVE
    if path.exists():
        return
    transcript = repo / TRANSCRIPT_RELATIVE
    payload = {
        "schema": "philosophia.level1.public-root-commit-pending.v1",
        "scientific_outcome": False,
        "expected_head": expected_head,
        "recorded_utc": _utc_now(),
        "transcript_sha256": sha256_file(transcript),
        "error_type": type(error).__name__,
        "error": str(error),
        "required_action": "root durable; complete a reviewed git commit; never redraw",
    }
    atomic_create(path, canonical_json(payload))


def _route_post_draw_failure(repo: Path, expected_head: str, error: BaseException) -> str:
    try:
        load_durable_transcript(repo / TRANSCRIPT_RELATIVE, expected_head=expected_head)
    except (FileNotFoundError, OSError, ValueError, json.JSONDecodeError):
        _record_invalidity(repo, expected_head, error)
        return "root not durably recoverable; signed invalidity required; never redraw"
    _record_commit_pending(repo, expected_head, error)
    return "root is durable; commit pending; complete a reviewed recovery commit; never redraw"


def _commit_transcript(repo: Path) -> None:
    paths = (CLAIM_RELATIVE.as_posix(), TRANSCRIPT_RELATIVE.as_posix())
    if _run_git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
        raise RuntimeError("git index changed after preflight")
    _run_git(repo, "add", "--", *paths)
    staged = tuple(
        line for line in _run_git(repo, "diff", "--cached", "--name-only").stdout.splitlines()
        if line
    )
    if staged != paths:
        raise RuntimeError(f"unexpected staged paths: {staged!r}")
    message = [
        "Draw the one-shot Level 1 public root",
        "Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>",
        "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>",
        "Co-Authored-By: GPT-5.6 Sol <noreply@openai.com>",
        "Co-Authored-By: Codex GPT-5.5 <noreply@openai.com>",
    ]
    arguments = ["commit", "--no-gpg-sign"]
    for paragraph in message:
        arguments.extend(("-m", paragraph))
    _run_git(repo, *arguments)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--reviewed-code-head", required=True)
    arguments = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]

    actual_head = _preflight(repo, arguments.expected_head, arguments.reviewed_code_head)
    configure_canonical_runtime()
    environment = _environment()
    required_spec_hashes = {
        path.as_posix(): sha256_file(repo / path) for path in REQUIRED_SPECS
    }
    governing_lineage_hashes = {
        path.as_posix(): sha256_file(repo / path) for path in GOVERNING_LINEAGE
    }
    claim = build_claim(
        expected_head=actual_head,
        reviewed_code_head=arguments.reviewed_code_head,
        created_utc=_utc_now(),
        transcript_path=TRANSCRIPT_RELATIVE.as_posix(),
    )
    try:
        atomic_create(repo / CLAIM_RELATIVE, canonical_json(claim))
    except BaseException as error:
        if (repo / CLAIM_RELATIVE).exists():
            _record_invalidity(repo, actual_head, error)
            raise RuntimeError(
                "public-root claim state is ambiguous; do not rerun; obtain a signed invalidity decision"
            ) from error
        raise

    try:
        root = secrets.token_bytes(32)
        allocations = derive_public_allocations(root)
        transcript = build_transcript(
            root=root,
            git_head=actual_head,
            reviewed_code_head=arguments.reviewed_code_head,
            timestamp_utc=_utc_now(),
            environment=environment,
            required_spec_hashes=required_spec_hashes,
            governing_lineage_hashes=governing_lineage_hashes,
            allocations=allocations,
        )
        atomic_create(repo / TRANSCRIPT_RELATIVE, canonical_json(transcript))
        _commit_transcript(repo)
    except BaseException as error:
        route = _route_post_draw_failure(repo, actual_head, error)
        raise RuntimeError(route) from error

    committed_head = _run_git(repo, "rev-parse", "HEAD").stdout.strip()
    print(json.dumps({
        "kind": "level1-public-root-draw",
        "scientific_outcome": False,
        "transcript": TRANSCRIPT_RELATIVE.as_posix(),
        "commit": committed_head,
        "push_required": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
