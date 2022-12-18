
LoadPackage("cream");;

Read("outputs/monoids_6.g");
Read("non_iso/monoids_7.g");

x := models7;;

for y in monoids6 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 

# prepare output file
fn := "outputs/monoids_7.g";;
PrintTo(fn, "monoids7");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

