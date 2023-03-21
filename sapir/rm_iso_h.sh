

cat *non_iso_models.out | ../utils/mace4/rm_iso.py -o ../non_iso_models_$1.out -v -t ../../infb0/master_non_iso/non_iso_models_s0.pkl -m 18000000

# cat *non_iso_models.out | ../utils/mace4/rm_iso.py -o non_iso_models_s0.out -v -t ../../infb0/master_non_iso/non_iso_models_s0.pkl -m 0 

# ../utils/mace4/rm_iso.py -i non_iso_models_s0.out -o non_iso_models_s1.out -v -t ../../infb0/master_non_iso/non_iso_models_s1.pkl -m 0 
# rm non_iso_models_s0.out

# ../utils/mace4/rm_iso.py -i non_iso_models_s1.out -o non_iso_models_s2.out -v -t ../../infb0/master_non_iso/non_iso_models_s2.pkl -m 0 
# rm non_iso_models_s1.out

# ../utils/mace4/rm_iso.py -i non_iso_models_s2.out -o non_iso_models_s3.out -v -t ../../infb0/master_non_iso/non_iso_models_s3.pkl -m 0 
# rm non_iso_models_s2.out

#../utils/mace4/rm_iso.py -i non_iso_models_s3.out -o non_iso_models_s4.out -v -t ../../infb0/master_non_iso/non_iso_models_s4.pkl -m 0 
#rm non_iso_models_s3.out

# ../utils/mace4/rm_iso.py -i non_iso_models_s3.out -o ../non_iso_models_$1.out -v -t ../../infb0/master_non_iso/non_iso_models_s4.pkl -m 0
# rm non_iso_models_s3.out
