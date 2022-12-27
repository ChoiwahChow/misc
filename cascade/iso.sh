
# order 11
k=11

mkdir -p parallel

mkdir -p working${k}
../../bin/splitModels -d${k} -f"../../bin/isofilter -ignore_constants" -m100 -oworking${k}/m${k}_ -tworking${k}/statistics_${k}.json -u16000000 -s1000 -r50 -l20 -x3000 -i"monoid_${k}.out" > filter${k}.log 2>&1 


