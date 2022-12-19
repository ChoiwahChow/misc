
# order 11
k=11
t=30
for ((i=3; i<=${t}; i++))
do
  mkdir -p working_${k}_${i}
  cd working_${k}_${i}
  ../../../bin/mace4 -n${k} -N${k} -A1 -m-1 -f ../inputs/monoid_${i}.in >> ${k}_${i}.log &
  pids[${i}]=$!
  cd ..
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done
