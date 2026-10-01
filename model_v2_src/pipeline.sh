#!/bin/bash
# Full build: calibrate -> build -> recalc -> sensitivities -> final build -> recalc
set -e
cd "$(dirname "$0")"
RECALC=${RECALC:-/root/.claude/skills/synced/887303c2-e0e7-4b94-b4ea-b783a659f80d_89eb92af-36fd-4c2d-9bf8-29f3636f2094/xlsx/scripts/recalc.py}   # path to a LibreOffice recalc script
rm -f calib.json sens_results.json
python3 build_v2.py model_v2.xlsx
timeout 600 python3 $RECALC model_v2.xlsx 300 | grep -E '"total_errors"|"status"'
python3 calibrate.py model_v2.xlsx
python3 build_v2.py model_v2.xlsx
timeout 600 python3 $RECALC model_v2.xlsx 300 | grep -E '"total_errors"|"status"'
timeout 900 python3 sens_v2.py model_v2.xlsx
python3 build_v2.py model_v2.xlsx
timeout 600 python3 $RECALC model_v2.xlsx 300 | grep -E '"total_errors"|"status"|total_formulas'
