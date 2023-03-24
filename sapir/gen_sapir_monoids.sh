

for t in {5..11}; do
  tp1=$((t+1))
  ./gen_sapir_monoids.py anti_monoids/anti_monoids_${t}.out | ../../bin/mlex -m | grep -v "%" > sapir_monoids/monoids_${tp1}.out
done

