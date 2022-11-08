
LoadPackage("magmaut");;

Read("outputs/monoids_6.g");
Read("outputs/monoids_7.g");
Read("non_iso/monoids_8.g");

x := models8;;

for y in [1..2] do
    x := Filtered(x, i->CreamMonomorphismAlgebras([monoids6[y]], [i]) = fail);;
od; time;

for y in [1..5] do
    x := Filtered(x, i->CreamMonomorphismAlgebras([monoids7[y]], [i]) = fail);;
od; time;


# prepare output file
fn := "outputs/monoids_8a.g";;
PrintTo(fn, "monoids8");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

