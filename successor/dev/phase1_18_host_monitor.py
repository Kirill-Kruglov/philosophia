#!/usr/bin/env python3
"""Periodic host-load sampler for PHASE1_18 Part B (amendment 4).

Modes:
  sample-loop --jsonl PATH --self-tag TAG [--interval 60]
  finalize --jsonl PATH --start PATH --end PATH --out PATH --wall-s N
"""
from __future__ import annotations
import argparse, json, os, time
from pathlib import Path


def read_proc_stat():
    procs_running = procs_blocked = None
    for line in Path("/proc/stat").read_text().splitlines():
        if line.startswith("procs_running "):
            procs_running = int(line.split()[1])
        elif line.startswith("procs_blocked "):
            procs_blocked = int(line.split()[1])
    return procs_running, procs_blocked


def other_phase_jobs(self_tag: str):
    me = os.getpid()
    jobs = []
    for line in Path("/proc").iterdir():
        if not line.name.isdigit():
            continue
        pid = int(line.name)
        if pid == me:
            continue
        try:
            cmd = (line / "cmdline").read_bytes().replace(b"\x00", b" ").decode("ascii", "replace")
        except Exception:
            continue
        if self_tag and self_tag in cmd:
            continue
        if "watch_phase1_18" in cmd or "phase1_18_host_monitor" in cmd:
            continue
        if any(s in cmd for s in (
            "proofsearch.py", "run_phase1_", "phase2_stage", "b2_instrument",
            "PHASE1_", "PHASE2_")):
            jobs.append({"pid": pid, "cmd": cmd[:240]})
    return jobs


def snapshot(when: str, self_tag: str) -> dict:
    load = os.getloadavg()
    proc = Path("/proc/loadavg").read_text().split()
    running, blocked = read_proc_stat()
    return {
        "when": when,
        "unix_s": time.time(),
        "nproc": os.cpu_count(),
        "loadavg_1_5_15": list(load),
        "proc_loadavg": proc[:3],
        "procs_running": running,
        "procs_blocked": blocked,
        "other_phase_jobs": other_phase_jobs(self_tag),
        "field_provenance": {
            "nproc": {"class": "MEASURED_IN_PROCESS"},
            "loadavg_1_5_15": {"class": "MEASURED_IN_PROCESS"},
            "procs_running": {"class": "MEASURED_IN_PROCESS"},
            "procs_blocked": {"class": "MEASURED_IN_PROCESS"},
            "other_phase_jobs": {"class": "MEASURED_IN_PROCESS"},
        },
    }


def sample_loop(jsonl: Path, self_tag: str, interval: float) -> None:
    jsonl.parent.mkdir(parents=True, exist_ok=True)
    # Immediate first sample, then every interval seconds.
    while True:
        row = snapshot("periodic", self_tag)
        with jsonl.open("a", encoding="ascii") as out:
            out.write(json.dumps(row, sort_keys=True) + "\n")
        time.sleep(interval)


def finalize(jsonl: Path, start_path: Path, end_path: Path, out_path: Path, wall_s: int) -> None:
    start = json.loads(start_path.read_text(encoding="ascii"))
    end = json.loads(end_path.read_text(encoding="ascii"))
    samples = []
    if jsonl.exists():
        for line in jsonl.read_text(encoding="ascii").splitlines():
            if line.strip():
                samples.append(json.loads(line))
    # Whole series: endpoints + periodic samples.
    series = [start] + samples + [end]
    any_jobs = any(s.get("other_phase_jobs") for s in series)
    loads1 = [float(s["loadavg_1_5_15"][0]) for s in series if s.get("loadavg_1_5_15")]
    max_load1 = max(loads1) if loads1 else None
    max_procs_running = max(
        (s["procs_running"] for s in series if s.get("procs_running") is not None),
        default=None,
    )
    idle = not any_jobs
    payload = {
        "wall_s": wall_s,
        "start": start,
        "end": end,
        "periodic_jsonl": str(jsonl),
        "n_periodic_samples": len(samples),
        "n_series_samples": len(series),
        "max_loadavg_1": max_load1,
        "max_procs_running": max_procs_running,
        "host_otherwise_idle": idle,
        "field_provenance": {
            "wall_s": {"class": "DERIVED", "inputs": ["unix_start", "unix_end"]},
            "start": {"class": "MEASURED_IN_PROCESS"},
            "end": {"class": "MEASURED_IN_PROCESS"},
            "n_periodic_samples": {"class": "DERIVED", "inputs": ["periodic_jsonl"]},
            "n_series_samples": {"class": "DERIVED", "inputs": ["start", "periodic_jsonl", "end"]},
            "max_loadavg_1": {"class": "DERIVED", "inputs": ["series.loadavg_1_5_15[0]"]},
            "max_procs_running": {"class": "DERIVED", "inputs": ["series.procs_running"]},
            "host_otherwise_idle": {
                "class": "DERIVED",
                "inputs": ["series.other_phase_jobs"],
                "rule": "true iff every series sample has empty other_phase_jobs",
            },
        },
    }
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print("host_load wall_s=%d n_periodic=%d max_load1=%s idle=%s" % (
        wall_s, len(samples), max_load1, idle))


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot")
    s.add_argument("--when", required=True)
    s.add_argument("--self-tag", required=True)
    s.add_argument("--out", required=True)
    loop = sub.add_parser("sample-loop")
    loop.add_argument("--jsonl", required=True)
    loop.add_argument("--self-tag", required=True)
    loop.add_argument("--interval", type=float, default=60.0)
    fin = sub.add_parser("finalize")
    fin.add_argument("--jsonl", required=True)
    fin.add_argument("--start", required=True)
    fin.add_argument("--end", required=True)
    fin.add_argument("--out", required=True)
    fin.add_argument("--wall-s", type=int, required=True)
    args = ap.parse_args()
    if args.cmd == "snapshot":
        Path(args.out).write_text(
            json.dumps(snapshot(args.when, args.self_tag), indent=2, sort_keys=True) + "\n",
            encoding="ascii")
        return 0
    if args.cmd == "sample-loop":
        sample_loop(Path(args.jsonl), args.self_tag, args.interval)
        return 0
    finalize(Path(args.jsonl), Path(args.start), Path(args.end), Path(args.out), args.wall_s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
