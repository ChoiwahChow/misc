
# order 11
k=11

mkdir -p working${k}
../../splitModels/splitModels -d${k} -f"../../bin/isofilter -ignore_constants" -m100 -oworking${k}/m11_ -tworking${k}/statistics_${k}.json -u16000000 -s1000 -r50 -l20 -x3000 -i"monoid_11.out" > filter${k}.log 2>&1 


