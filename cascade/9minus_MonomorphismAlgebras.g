
LoadPackage("magmaut");;

Read("outputs/monoids_6.g");
Read("outputs/monoids_7.g");
Read("outputs/monoids_8.g");
Read("non_iso/monoids_9.g");

x := models9;;

for y in monoids6 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 

for y in monoids7 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od;


for y in monoids8 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od;

# prepare output file
fn := "outputs/monoids_9.g";;
PrintTo(fn, "monoids9");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

