
date;

rm -rf *_working_* 

k=12
l=12
n=11
a=infb
s=11111100
# cube stage: 0 (default) for all, 1 for gen cubes only, 2 for run cubes only
c=2

rm -f cubes/*
mkdir -p cubes
cp master_cubes/cubes_12_12.out cubes/cubes_12_12.out
# cp master_cubes/cubes_12_12aa cubes/cubes_12_12.out

echo ${a} ${k} ${l} ${n} ${s} ${c}

utils/mace4/bootstrap.py ${a} ${k} ${l} ${n} ${s} ${c}

echo "found non iso models: "
grep interp ./non_iso_models_${k}_${n}.out | wc -l

# rm -rf utils/mace4/working

echo ${a} ${k} ${l} ${n} ${s}
date

