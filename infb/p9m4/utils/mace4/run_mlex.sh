


fs0=$(wc -l models.out | awk '{print $1}')
if [ $fs0 -gt 0 ]; then
    ../../bin/mlex -b1lrmiuH < models.out >> non_iso_models.out
    wc -l models.out >> models_count.out
    rm models.out
fi

if [ ! -f "non_iso_models.out" ]; then
  >> non_iso_models.out
fi

fs=$(wc -l "non_iso_models.out" | awk '{print $1}')

if [ $fs -gt 28000000 ]
then
  ../utils/mace4/rm_iso.py -i non_iso_models.out -o level1_non_iso_models.out -t level1.pkl -m 3000000 -p
  rm non_iso_models.out

  fs1=$(wc -l "level1_non_iso_models.out" | awk '{print $1}')

  if [ $fs1 -gt 70000000 ]
  then
    ../utils/mace4/rm_iso.py -i level1_non_iso_models.out -o level2_non_iso_models.out
    rm level1_non_iso_models.out
  fi
fi
