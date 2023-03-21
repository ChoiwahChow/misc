#!/bin/bash

k=12
l=16
s=0
t=49

echo ""
echo ""

date

for ((i=${s}; i<=${t}; i++))
do
  cd infb_working_${k}_${l}_${i}
  ../rm_iso_h.sh ${i} >> mace.log 2>&1 &
  pids[${i}]=$!
  cd ..
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done

date

echo ""

cat non_iso_models_*.out | utils/mace4/rm_iso.py -o non_iso_models.out -m 19000000 -v 
