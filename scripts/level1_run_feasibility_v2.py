#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import resource
import subprocess
import sys

import torch


REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from philosophia.level1.feasibility import (
    report_payload_v2,
    run_noncomparative_feasibility_v2,
)
from philosophia.level1.interlock import feasibility_v2_capability
from philosophia.level1.model import configure_canonical_runtime
from philosophia.level1.public_root import (
    atomic_create_no_replace,
    canonical_json,
    environment_fingerprint,
    sha256_file,
)
from philosophia.level1.serialization import DeterministicKey


AUTHORIZATION_SCHEMA = "philosophia.level1.feasibility-authorization.v2"
CLAIM_SCHEMA = "philosophia.level1.feasibility-run-claim.v2"
REPORT_SCHEMA = "philosophia.level1.noncomparative-feasibility.v2"
AUTHORIZATION_TOKEN = "I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2"
AUTHORIZATION_RELATIVE = Path(
    "experiments/level_1_contact/FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json"
)
TRANSCRIPT_RELATIVE = Path(
    "experiments/level_1_contact/allocation/PUBLIC_ROOT_TRANSCRIPT.json"
)
SIGNATURE_RELATIVE = Path(
    "experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md"
)
CANONICAL_OUTPUT_RELATIVE = Path("experiments/level_1_contact/feasibility_v2")
CLAIM_NAME = "LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2_CLAIM.json"
REPORT_NAME = "LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json"
SIGNATURE_SHA256 = "04a7c7c1ceac2a58c7469997d1fe25bdd5f80a9976e0b4838604b0e39252422b"
AMENDMENT_SHA256 = {
    "FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md": (
        "51d9833c79127c9a06b7e625b0f2af3c41cd0bdf54e5f63a950463ffc5c65fc8"
    ),
    "FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md": (
        "d9ed5b562cbebef3e3b0a9c72d2d9dda35c834a044faf593d52b96b20c89ca14"
    ),
    "FEASIBILITY_FLOOR_AMENDMENT_V2_2_CORRECTION.md": (
        "5b413bc36e3468cb57c78b8832c471c51013bf160d71dc216c095907b2556c9b"
    ),
}
V1_EVIDENCE_SHA256 = {
    "LEVEL1_NONCOMPARATIVE_FEASIBILITY_CLAIM.json": (
        "357baef22226bfb92b909192d2264420923facd55115b9c272bb2cb848c106ab"
    ),
    "LEVEL1_NONCOMPARATIVE_FEASIBILITY.json": (
        "1c3843ec66f57e8a7e05b88d5f942093113f11f5ac36746f202f1a6556820b7f"
    ),
}
REVIEWED_SOURCE_PATHS = (
    "scripts/level1_run_feasibility_v2.py",
    "src/philosophia/level1/feasibility.py",
    "src/philosophia/level1/interlock.py",
    "src/philosophia/level1/train.py",
    "src/philosophia/level1/public_root.py",
    "src/philosophia/level1/pool.py",
    "src/philosophia/level1/panel.py",
    "src/philosophia/level1/model.py",
    "src/philosophia/level1/acquisition.py",
    "src/philosophia/level1/config.py",
    "src/philosophia/level1/serialization.py",
    "src/philosophia/level1/scoring.py",
    "src/philosophia/level1/world.py",
)


def _git(repo: Path, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments],
        cwd=repo,
        check=check,
        capture_output=True,
        text=True,
    )


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


def _verify_current_environment(transcript: dict[str, object]) -> None:
    current = _environment()
    if current != transcript.get("environment"):
        raise RuntimeError("current environment differs from the public-root fingerprint")
    if environment_fingerprint(current) != transcript.get("environment_fingerprint"):
        raise RuntimeError("current environment fingerprint mismatch")


def _load_canonical(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict) or canonical_json(value) != raw:
        raise ValueError(f"artifact is not canonical JSON: {path}")
    return value


def _require_tracked(repo: Path, relatives: tuple[Path, ...]) -> None:
    for relative in relatives:
        tracked = _git(
            repo,
            "ls-files",
            "--error-unmatch",
            relative.as_posix(),
            check=False,
        )
        if tracked.returncode != 0:
            raise PermissionError(f"required lineage artifact is untracked: {relative}")


def _verify_lineage_hashes(repo: Path) -> None:
    if sha256_file(repo / SIGNATURE_RELATIVE) != SIGNATURE_SHA256:
        raise PermissionError("feasibility-floor signature record changed")
    amendment_root = repo / "experiments/level_1_contact"
    for name, expected in AMENDMENT_SHA256.items():
        if sha256_file(amendment_root / name) != expected:
            raise PermissionError(f"governing amendment hash changed: {name}")
    evidence_root = amendment_root / "feasibility"
    for name, expected in V1_EVIDENCE_SHA256.items():
        if sha256_file(evidence_root / name) != expected:
            raise PermissionError(f"immutable v1 evidence hash changed: {name}")


def _preflight(
    repo: Path,
    expected_head: str,
    output_dir: Path,
) -> tuple[dict[str, object], dict[str, object]]:
    head = _git(repo, "rev-parse", "HEAD").stdout.strip()
    if head != expected_head:
        raise RuntimeError("HEAD does not match the reviewed v2 execution command")
    if _git(repo, "diff", "--quiet", check=False).returncode != 0:
        raise RuntimeError("tracked working tree must be clean")
    if _git(repo, "diff", "--cached", "--quiet", check=False).returncode != 0:
        raise RuntimeError("git index must be empty")

    canonical_output = (repo / CANONICAL_OUTPUT_RELATIVE).resolve()
    if output_dir.resolve() != canonical_output:
        raise ValueError("v2 feasibility output directory is frozen")

    amendment_relatives = tuple(
        Path("experiments/level_1_contact") / name for name in AMENDMENT_SHA256
    )
    evidence_relatives = tuple(
        Path("experiments/level_1_contact/feasibility") / name
        for name in V1_EVIDENCE_SHA256
    )
    _require_tracked(
        repo,
        (
            AUTHORIZATION_RELATIVE,
            TRANSCRIPT_RELATIVE,
            SIGNATURE_RELATIVE,
            *amendment_relatives,
            *evidence_relatives,
        ),
    )
    _verify_lineage_hashes(repo)

    authorization = _load_canonical(repo / AUTHORIZATION_RELATIVE)
    if authorization.get("schema") != AUTHORIZATION_SCHEMA:
        raise ValueError("v2 feasibility authorization schema mismatch")
    if authorization.get("token") != AUTHORIZATION_TOKEN:
        raise PermissionError("Kirill v2 feasibility authorization token is absent")
    if authorization.get("scientific_outcome") is not False:
        raise ValueError("v2 authorization must declare scientific_outcome false")
    if authorization.get("execution_once") is not True:
        raise ValueError("v2 authorization must be one-shot")
    if authorization.get("arm") != "RANDOM-STATIC":
        raise ValueError("v2 authorization arm must be RANDOM-STATIC")
    if authorization.get("caps") != {
        "development_worlds": 1,
        "trajectory_steps": 2000,
        "scorer_steps": 0,
        "wall_seconds": 129600,
    }:
        raise ValueError("v2 authorization caps differ from the signed contract")
    if authorization.get("development_world") != {"pair_slot": 0, "modulus": 66}:
        raise ValueError("v2 authorization development world changed")
    if authorization.get("output_directory") != CANONICAL_OUTPUT_RELATIVE.as_posix():
        raise ValueError("v2 authorization output directory changed")
    if authorization.get("governing_signature_sha256") != SIGNATURE_SHA256:
        raise ValueError("v2 authorization signature hash changed")
    if authorization.get("governing_amendment_sha256") != AMENDMENT_SHA256:
        raise ValueError("v2 authorization amendment hashes changed")
    if authorization.get("v1_evidence_sha256") != V1_EVIDENCE_SHA256:
        raise ValueError("v2 authorization v1 evidence hashes changed")
    reviewed_head = authorization.get("reviewed_code_head")
    if not isinstance(reviewed_head, str) or len(reviewed_head) != 40:
        raise ValueError("reviewed v2 code HEAD is missing")
    source_diff = _git(
        repo,
        "diff",
        "--quiet",
        reviewed_head,
        head,
        "--",
        *REVIEWED_SOURCE_PATHS,
        check=False,
    )
    if source_diff.returncode != 0:
        raise RuntimeError("reviewed v2 feasibility source bytes changed")

    transcript = _load_canonical(repo / TRANSCRIPT_RELATIVE)
    if transcript.get("schema") != "philosophia.level1.public-root.v1":
        raise ValueError("public-root transcript schema mismatch")
    if transcript.get("scientific_outcome") is not False:
        raise ValueError("public-root transcript is not non-outcome")
    transcript_environment = transcript.get("environment")
    if not isinstance(transcript_environment, dict):
        raise ValueError("public-root environment is missing")
    if transcript.get("environment_fingerprint") != environment_fingerprint(
        transcript_environment
    ):
        raise ValueError("public-root environment fingerprint is internally inconsistent")
    if transcript.get("forbidden_derivations") != [
        "real evaluator panel",
        "panel raw realizations",
        "panel ordering",
        "encryption salt",
        "escrow plaintext",
    ]:
        raise ValueError("public-root forbidden derivations changed")

    claim_path = output_dir / CLAIM_NAME
    report_path = output_dir / REPORT_NAME
    if claim_path.exists() or report_path.exists():
        raise FileExistsError("refusing to repeat v2 feasibility execution")
    for forbidden in (
        repo / "experiments/level_1_contact/comparative_scout",
        repo / "experiments/level_1_contact/N3_SELECTION.json",
        repo / "experiments/level_1_contact/PREREG.lock",
        repo / "experiments/level_1_contact/escrow/REAL_PANEL.enc",
        repo / "experiments/level_1_contact/outcomes/decision.json",
    ):
        if forbidden.exists():
            raise RuntimeError(f"later-gate artifact already exists: {forbidden}")
    return authorization, transcript


def _development_world(transcript: dict[str, object]) -> tuple[int, int]:
    allocations = transcript.get("allocations")
    if not isinstance(allocations, dict):
        raise ValueError("public-root allocations are missing")
    pairs = allocations.get("development_pairs")
    if not isinstance(pairs, list) or len(pairs) != 6:
        raise ValueError("signed development-pair allocation changed")
    first = pairs[0]
    if not isinstance(first, dict):
        raise ValueError("development pair is malformed")
    slot, modulus = first.get("slot"), first.get("lower")
    if not isinstance(slot, int) or not isinstance(modulus, int):
        raise ValueError("development pair lacks integer slot/modulus")
    return slot, modulus


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-head", required=True)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=CANONICAL_OUTPUT_RELATIVE,
    )
    args = parser.parse_args()
    output_dir = args.output_dir if args.output_dir.is_absolute() else REPO / args.output_dir
    authorization, transcript = _preflight(REPO, args.expected_head, output_dir)

    configure_canonical_runtime()
    _verify_current_environment(transcript)
    root_hex = transcript.get("root_hex")
    if not isinstance(root_hex, str) or len(root_hex) != 64:
        raise ValueError("public root is malformed")
    key = DeterministicKey(bytes.fromhex(root_hex), purpose="public-root", test_only=False)
    pair_slot, modulus = _development_world(transcript)
    if authorization["development_world"] != {
        "pair_slot": pair_slot,
        "modulus": modulus,
    }:
        raise ValueError("authorized v2 world differs from public-root allocation")

    claim = {
        "schema": CLAIM_SCHEMA,
        "status": "started-no-delete-no-rerun",
        "scientific_outcome": False,
        "git_head": args.expected_head,
        "authorization_sha256": sha256_file(REPO / AUTHORIZATION_RELATIVE),
        "public_root_transcript_sha256": sha256_file(REPO / TRANSCRIPT_RELATIVE),
        "governing_signature_sha256": SIGNATURE_SHA256,
        "governing_amendment_sha256": AMENDMENT_SHA256,
        "v1_evidence_sha256": V1_EVIDENCE_SHA256,
        "arm": "RANDOM-STATIC",
        "development_world": {"pair_slot": pair_slot, "modulus": modulus},
        "learner_policy": "full-history-mean-ce-one-update-per-answer",
        "censored_at_b_status": "unset-until-valid-terminal-report",
    }
    atomic_create_no_replace(output_dir / CLAIM_NAME, canonical_json(claim))

    capability = feasibility_v2_capability()
    run = run_noncomparative_feasibility_v2(
        key,
        pair_slot=pair_slot,
        modulus=modulus,
        capability=capability,
    )
    capability.check_wall()

    report = {
        "schema": REPORT_SCHEMA,
        "kind": "level1-noncomparative-feasibility-v2",
        "scientific_outcome": False,
        "interpretation": "resource-and-binary-feasibility-only-no-arm-inference",
        "validity": "valid-scientific-terminal",
        "git_head": args.expected_head,
        "authorization_sha256": sha256_file(REPO / AUTHORIZATION_RELATIVE),
        "public_root_transcript_sha256": sha256_file(REPO / TRANSCRIPT_RELATIVE),
        "governing_signature_sha256": SIGNATURE_SHA256,
        "governing_amendment_sha256": AMENDMENT_SHA256,
        "v1_evidence_sha256": V1_EVIDENCE_SHA256,
        "arm": "RANDOM-STATIC",
        "development_world": {"pair_slot": pair_slot, "modulus": modulus},
        "replicate": 1,
        "learner_policy": "full-history-mean-ce-one-update-per-answer",
        "caps": {
            "development_worlds": 1,
            "trajectory_steps": 2000,
            "scorer_steps": 0,
            "wall_seconds": 129600,
        },
        "measurements": report_payload_v2(run),
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "contamination_guards": {
            "second_arm": False,
            "arm_contrast": False,
            "v1_v2_contrast": False,
            "scorer_repeated": False,
            "real_panel": False,
            "escrow": False,
            "n3_selection": False,
            "preregistration_lock": False,
            "outcome_decision": False,
            "query_series_persisted": False,
            "loss_series_persisted": False,
            "solve_series_persisted": False,
        },
        "authorization": {
            "schema": authorization["schema"],
            "token": authorization["token"],
            "reviewed_code_head": authorization["reviewed_code_head"],
        },
    }
    atomic_create_no_replace(output_dir / REPORT_NAME, canonical_json(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
