
date;

rm -rf *_working_* 

k=12
l=16
n=60
a=infb
# number of threads
t=20
# cube stage: 0 (default) for all, 1 for gen cubes only, 2 for run cubes only
c=2

rm -f cubes/*
mkdir -p cubes
cp ../infb60/master_cubes/cubes_${k}_${l}ac cubes/cubes_${k}_${l}.out

echo ${a} ${k} ${l} ${n} ${t} ${c}

utils/mace4/bootstrap.py ${a} ${k} ${l} ${n} ${t} ${c}

echo "number of models processed: "
cat *_${k}_${l}_*/models_count.out | awk -F' ' '{sum+=$FF}; END{print sum}'
# cat *_12_16_*/models_count.out | awk -F' ' '{sum+=$FF}; END{print sum}'

echo "found non iso models: "
grep interp ./non_iso_models_${k}_${n}.out | wc -l

# rm -rf utils/mace4/working

echo ${a} ${k} ${l} ${n} ${t}
date

