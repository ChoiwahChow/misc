
fs0=$(wc -l models.out | awk '{print $1}')
if [ $fs0 -gt 0 ]; then
    sed -i '/(_)/d' models.out
    ../../../bin/mlex -mud < models.out >> non_iso_models.out
    wc -l models.out >> models_count.out
fi
rm -f models.out

touch non_iso_models.out
#if [ ! -f "non_iso_models.out" ]; then
#  >> non_iso_models.out
#fi

fs=$(wc -l "non_iso_models.out" | awk '{print $1}')

if [ $fs -gt 28000000 ]
then
  ../utils/mace4/rm_iso.py -i non_iso_models.out -o level1_non_iso_models.out -m 3000000 
  rm non_iso_models.out

  fs1=$(wc -l "level1_non_iso_models.out" | awk '{print $1}')

  if [ $fs1 -gt 70000000 ]
  then
    ../utils/mace4/rm_iso.py -i level1_non_iso_models.out -o level2_non_iso_models.out -m 5000000
    rm level1_non_iso_models.out
  fi
fi
