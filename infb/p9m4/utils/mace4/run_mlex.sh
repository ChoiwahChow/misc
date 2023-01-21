

mofiles=`find . -name "models.out*"`

for mo in $mofiles; do
  fs0=$(wc -l $mo | awk '{print $1}')
  if [ $fs0 -gt 0 ]; then
    ../../bin/mlex -b1lrumi < $mo >> non_iso_models.out
  fi
  rm $mo
done

if [ ! -f "non_iso_models.out" ]; then
  >> non_iso_models.out
fi

fs=$(wc -l "non_iso_models.out" | awk '{print $1}')

if [ $fs -gt 140000000 ]
then
  ../../bin/mlex -b1lrumid < non_iso_models.out >> level1_non_iso_models.out
  rm non_iso_models.out

  fs1=$(wc -l "level1_non_iso_models.out" | awk '{print $1}')

  if [ $fs1 -gt 700000000 ]
  then
    ../../bin/mlex -b1lrumid < level1_non_iso_models.out >> level2_non_iso_models.out
    rm level1_non_iso_models.out
  fi
fi
