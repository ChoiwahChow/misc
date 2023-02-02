#!/bin/bash

k=12
s=66
t=70

date

for ((i=${s}; i<=${t}; i++))
do
  # mkdir -p working_${k}_${i}
  # cd working_${k}_${i}
  suf="\".${i}\""
  gap -o 5g -c "suffix := ${suf};;" < infb_12.g > logs/${i}.log &
  pids[${i}]=$!
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done

date
