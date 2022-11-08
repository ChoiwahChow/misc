
LoadPackage("magmaut");;

Read("outputs/monoids_6.g");
Read("outputs/monoids_7.g");
Read("non_iso/monoids_8.g");

x := models8;;

for y in monoids6 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 

for y in monoids7 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 


# prepare output file
fn := "outputs/monoids_8.g";;
PrintTo(fn, "monoids8");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

