
LoadPackage("cream");;

Read("outputs/sapir_6.g");
Read("non_iso/sapir_7.g");

x := models7;;
Print("\nNumber of sapir anit-monoids: "); Print(Length(x)); Print("\n");

for y in sapir6 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 6, Length: "); Print(Length(x)); Print("\n");

# prepare output file
fn := "outputs/sapir_7.g";;
PrintTo(fn, "sapir7");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

