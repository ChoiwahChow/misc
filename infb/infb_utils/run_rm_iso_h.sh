#!/bin/bash

k=12
n=40
s=0
t=5

date

for ((i=${s}; i<=${t}; i++))
do
  cd infb_working_${k}_${n}_${i}
  ../rm_iso_h.sh ${i} >> mace.log 2>&1 &
  pids[${i}]=$!
  cd ..
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done

date
