
LoadPackage("cream");;

Read("outputs/anti_monoids_5.g");
Read("non_iso/sapir_6.g.0");

x := models6;;
Print("\nNumber of Sapir anti-monoids: "); Print(Length(x)); Print("\n");

for y in anti_monoids5 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 5, Length: "); Print(Length(x)); Print("\n");

# prepare output file
fn := "outputs/anti_monoids_6.g";;
PrintTo(fn, "anti_monoids6");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

