#!/usr/bin/env bash
# Phase-1d evaluation-variance probe (NON-CITABLE).
# Question: is ck1's 19/30 at budget 8000 stable under re-seeding of the SEARCH,
# or is evaluation variance large enough to explain the 19-vs-11 gap?
#
# Nothing is retrained. Only the evaluation seed changes. ck1 and ck2 are the
# pair that produced 19 vs 11 at seed 0; both are re-run at seeds 1, 2, 3.
# Everything else identical to 16b/16c: problemset=kleene, budget 8000,
# accumulate_library=false, same 30 statements, same run dir.
#
# Reading rule, fixed before these data exist:
#   EVAL_VARIANCE_DOMINATES := ck1's solved count at seeds 1-3 overlaps ck2's
#                              range, i.e. the 19-vs-11 ordering is not stable.
#   CHECKPOINT_DIFFERENCE_STABLE := ck1 > ck2 at every seed.
# Neither outcome is an evidential verdict: 30 items, one training seed.
set -euo pipefail

MINIMO_LEARNING=/home/master/llm_projects/minimo/learning
VENV=/home/master/llm_projects/minimo/.venv/bin/python
CKPT_DIR=/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33
OUT=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_16d
LOG=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_16d_run.log

mkdir -p "$OUT"
: > "$LOG"
cd "$MINIMO_LEARNING"

export OMP_NUM_THREADS=16
export PYTHONUNBUFFERED=1

echo "phase1_extrinsic_16d start $(date -Is)" | tee -a "$LOG"

for seed in 1 2 3; do
  for ck in 1 2; do
    echo "===== ck${ck} seed ${seed} budget 8000 $(date -Is) =====" | tee -a "$LOG"
    nice -n 10 "$VENV" ./proofsearch.py \
      task=eval \
      problemset=kleene \
      agent=mcts-lm \
      agent.max_mcts_nodes=8000 \
      agent.node_type=holophrasm \
      accumulate_library=false \
      +seed="$seed" \
      +agent_path="$CKPT_DIR/${ck}.pt" \
      job.wandb_project=null \
      +results_path="$OUT/checkpoint_${ck}_seed${seed}.json" \
      "hydra.run.dir=$OUT/hydra_ck${ck}_seed${seed}" \
      2>&1 | tee -a "$LOG"
  done
done

echo "phase1_extrinsic_16d done $(date -Is)" | tee -a "$LOG"
