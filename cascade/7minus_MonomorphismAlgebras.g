
LoadPackage("magmaut");;

Read("outputs/monoids_6.g");
Read("non_iso/monoids_7.g");

x := models7;;

for y in [1..2] do
    x := Filtered(x, i->CreamMonomorphismAlgebras([monoids6[y]], [i]) = fail);;
od; time;

# prepare output file
fn := "outputs/monoids_7a.g";;
PrintTo(fn, "monoids7");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

