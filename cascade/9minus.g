
LoadPackage("smallsemi");;

# Load monoid multiplication tables
Read("outputs/monoids_6.g");;
Read("outputs/monoids_7.g");;
Read("outputs/monoids_8.g");;
Read("non_iso/monoids_9.g");;

# Construct monoids from multiplication tables
monoid_6 := List(monoids6, x->SemigroupByMultiplicationTable(x));;
monoid_7 := List(monoids7, x->SemigroupByMultiplicationTable(x));;
monoid_8 := List(monoids8, x->SemigroupByMultiplicationTable(x));;

# identify the monoids as semigroup number
monoid_6_id := Set(monoid_6, x->IdSmallSemigroup(x));;
monoid_7_id := Set(monoid_7, x->IdSmallSemigroup(x));;
monoid_8_id := Set(monoid_8, x->IdSmallSemigroup(x));;

# prepare output file
fn := "outputs/monoids_9.g";;
PrintTo(fn, "monoids9");; AppendTo(fn, " := [\n");;

# check each monoid of order 9 whether it contains a monoid of 
# order 6 or 7 or 8.  If not, prints it out.

counter := 0;;
x := 1;;

while x <= Length(models9) do

    monoid_9 := SemigroupByMultiplicationTable(models9[x]);;
    sem := monoid_9;;
    power:=Combinations(Elements(sem));;
    power2 :=Filtered(power,i->Size(i)>0);;
    power :=[];;
    for p in power2 do
        d := Semigroup(p);;
        power := Concatenation(power, [d]);;
    od;
    power:=Filtered(power, i->Size(i)<9 );; 
    power:=Set(power,i->IdSmallSemigroup(i));;
    if ForAny(monoid_6_id,i->i in power) or ForAny(monoid_7_id,i->i in power) or ForAny(monoid_8_id,i->i in power) then ;
    else 
        AppendTo(fn, models9[x]); AppendTo(fn, ",\n"); 
        counter := counter + 1; Print("Found "); Print(counter); Print("\n");
    fi;
    x := x + 1;;
    if x mod 1000 = 0 then Print("Working on "); Print(x); Print("\n"); fi;
od;

AppendTo(fn, "];\n");
