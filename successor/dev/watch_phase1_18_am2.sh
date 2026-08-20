#!/usr/bin/env bash
# Watch parent: after structural OMP=1 gate file, kill before full OMP=16; launch am2/am5.
# Amendment 3 D3: trigger on OMP1_GATE_OK file only (analyze writes file before printing).
# Amendment 5: set-equality vs PHASE1_17 pins is not a stop; only STRUCTURAL_DEFECT stops.
set -euo pipefail
DEV=/home/master/llm_projects/philosophia/successor/dev
LOG="$DEV/phase1_18_part_b_run.log"
OUTER="$DEV/phase1_18_part_b_outer.log"
PARENT_PID="${1:?parent pid}"
GATE_OK="$DEV/phase1_18_part_b/OMP1_GATE_OK"

echo "am2_watcher start parent=$PARENT_PID $(date -Is)" | tee -a "$OUTER"

launch_am2() {
  echo "am2_watcher: launching amendment5 continuation $(date -Is)" | tee -a "$OUTER"
  nohup "$DEV/run_phase1_18_part_b_am2.sh" >> "$OUTER" 2>&1 &
  echo "am2_continuation_pid=$!" | tee -a "$OUTER"
}

while kill -0 "$PARENT_PID" 2>/dev/null; do
  if grep -q "STOP: STRUCTURAL_DEFECT" "$LOG" 2>/dev/null; then
    echo "am2_watcher: structural gate failed; not launching am2 $(date -Is)" | tee -a "$OUTER"
    exit 2
  fi
  if [[ -f "$GATE_OK" ]]; then
    echo "am2_watcher: gate file present; stopping parent before full OMP16 $(date -Is)" | tee -a "$OUTER"
    pkill -P "$PARENT_PID" 2>/dev/null || true
    kill "$PARENT_PID" 2>/dev/null || true
    sleep 2
    pkill -f "checkpoint_[0-4]_omp16\\.json" 2>/dev/null || true
    pkill -f "hydra_ck[0-4]_omp16" 2>/dev/null || true
    launch_am2
    exit 0
  fi
  if grep -q "===== config omp16 start" "$LOG" 2>/dev/null; then
    echo "am2_watcher: omp16 started; killing and switching to am2 $(date -Is)" | tee -a "$OUTER"
    pkill -P "$PARENT_PID" 2>/dev/null || true
    kill "$PARENT_PID" 2>/dev/null || true
    pkill -f "checkpoint_[0-4]_omp16\\.json" 2>/dev/null || true
    sleep 2
    launch_am2
    exit 0
  fi
  sleep 5
done

echo "am2_watcher: parent exited without gate file $(date -Is)" | tee -a "$OUTER"
if [[ -f "$DEV/phase1_18_part_b/checkpoint_4_omp1.json" ]]; then
  if [[ ! -f "$GATE_OK" ]]; then
    /home/master/llm_projects/minimo/.venv/bin/python \
      "$DEV/phase1_18_part_b_analyze.py" --gate-omp1-only >> "$OUTER" 2>&1 || true
  fi
  if [[ -f "$GATE_OK" ]]; then
    launch_am2
  fi
fi
exit 0
