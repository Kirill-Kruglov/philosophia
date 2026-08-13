#!/usr/bin/env bash
# Phase-1 measurement 17 (NON-CITABLE): paired search-COST series, not a verdict.
#
# Why: every Phase-1 reading so far used a censored binary count (solved / not),
# which on a deterministic evaluator with an effective n well below 30 has no
# degrees of freedom. 16B and 16D both produced reading rules that could not
# fail. The fix named in those reports is to make the primary quantity
# continuous.
#
# Instrumentation (logged): minimo/learning/proofsearch.py now carries
# `mcts_expansions` on ProofSearchResult, summed over the outer search loop, and
# records it per problem. `iterations` was NOT a cost measure (0 on success,
# 1 on exhaustion). No algorithm, config default or theory file changed.
#
# ESTIMAND, fixed before the data exist:
#   per theorem, MCTS expansions consumed, censored at the budget (8000) when
#   the search fails; primary quantity = restricted mean expansions per
#   checkpoint over the same fixed 30 statements, compared pairwise against ck0.
#
# This run states NO binary verdict. It is a measurement with an uncertainty,
# not a test with a threshold — deliberately, because the previous two binary
# rules in this line were degenerate.
set -euo pipefail

MINIMO_LEARNING=/home/master/llm_projects/minimo/learning
VENV=/home/master/llm_projects/minimo/.venv/bin/python
CKPT_DIR=/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33
OUT=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_17
LOG=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_17_run.log

mkdir -p "$OUT"
: > "$LOG"
cd "$MINIMO_LEARNING"

export OMP_NUM_THREADS=16
export PYTHONUNBUFFERED=1

echo "phase1_extrinsic_17 start $(date -Is)" | tee -a "$LOG"

for ck in 0 1 2 3 4; do
  echo "===== ck${ck} budget 8000 instrumented $(date -Is) =====" | tee -a "$LOG"
  nice -n 10 "$VENV" ./proofsearch.py \
    task=eval \
    problemset=kleene \
    agent=mcts-lm \
    agent.max_mcts_nodes=8000 \
    agent.node_type=holophrasm \
    accumulate_library=false \
    +seed=0 \
    +agent_path="$CKPT_DIR/${ck}.pt" \
    job.wandb_project=null \
    +results_path="$OUT/checkpoint_${ck}.json" \
    "hydra.run.dir=$OUT/hydra_ck${ck}" \
    2>&1 | tee -a "$LOG"
done

echo "phase1_extrinsic_17 done $(date -Is)" | tee -a "$LOG"
