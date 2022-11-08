
LoadPackage("magmaut");;

Read("outputs/monoids_6.g");
Read("outputs/monoids_7.g");
Read("outputs/monoids_8.g");
Read("non_iso/monoids_9.g");

x := models9;;

for y in [1..2] do
    x := Filtered(x, i->CreamMonomorphismAlgebras([monoids6[y]], [i]) = fail);;
od; time;

for y in [1..5] do
    x := Filtered(x, i->CreamMonomorphismAlgebras([monoids7[y]], [i]) = fail);;
od; time;


for y in [1..3] do
    x := Filtered(x, i->CreamMonomorphismAlgebras([monoids8[y]], [i]) = fail);;
od; time;

# prepare output file
fn := "outputs/monoids_9a.g";;
PrintTo(fn, "monoids9");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

