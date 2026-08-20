# Lightweight RAM/VRAM sampler for PHASE1_MINIMO_REPRO_15. Not part of minimo.
import json, time, subprocess, os, sys
from pathlib import Path

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("phase1_resource_samples.jsonl")
pid = int(sys.argv[2]) if len(sys.argv) > 2 else None
interval = float(sys.argv[3]) if len(sys.argv) > 3 else 30.0

def sample():
    row = {"t": time.time()}
    try:
        r = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,utilization.gpu", "--format=csv,noheader,nounits"],
            text=True,
        ).strip()
        mem, util = r.split(",")
        row["vram_mib"] = float(mem.strip())
        row["gpu_util"] = float(util.strip())
    except Exception as e:
        row["gpu_err"] = str(e)
    try:
        import psutil  # optional
        row["ram_mib"] = psutil.virtual_memory().used / (1024 * 1024)
        row["ram_pct"] = psutil.virtual_memory().percent
        if pid:
            p = psutil.Process(pid)
            row["proc_rss_mib"] = p.memory_info().rss / (1024 * 1024)
            row["proc_cpu"] = p.cpu_percent(interval=0.0)
    except Exception:
        # fallback: wmic-ish via powershell unavailable; leave blank
        pass
    return row

with out.open("a", encoding="utf-8") as f:
    while True:
        if pid and not os.path.exists(f"/proc/{pid}") and sys.platform != "win32":
            break
        if pid and sys.platform == "win32":
            try:
                subprocess.check_output(["tasklist", "/FI", f"PID eq {pid}"], text=True)
                # tasklist always succeeds; check output
                outp = subprocess.check_output(["tasklist", "/FI", f"PID eq {pid}"], text=True, errors="ignore")
                if str(pid) not in outp:
                    break
            except Exception:
                break
        row = sample()
        f.write(json.dumps(row) + "\n")
        f.flush()
        time.sleep(interval)
