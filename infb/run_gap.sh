#!/usr/bin/bash

k=12
t=9

for ((i=0; i<=${t}; i++))
do
  # mkdir -p working_${k}_${i}
  # cd working_${k}_${i}
  suf="\".${i}\""
  gap -o 3g -c "suffix := ${suf};;" < infb_12.g > logs/${i}.log &
  pids[${i}]=$!
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done
