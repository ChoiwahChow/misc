
LoadPackage("cream");;

Read("outputs/anti_monoids_5.g");
Read("outputs/anti_monoids_6.g");
Read("outputs/anti_monoids_7.g");
Read("outputs/anti_monoids_8.g");
Read("outputs/anti_monoids_9.g");
Read("outputs/anti_monoids_10.g");
Read("non_iso/sapir_11.g.0");

x := models11;;
Print("\nNumber of Sapir anti-monoids: "); Print(Length(x)); Print("\n");

for y in anti_monoids5 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 5, Length: "); Print(Length(x)); Print("\n");

for y in anti_monoids6 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 6, Length: "); Print(Length(x)); Print("\n");

for y in anti_monoids7 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 7, Length: "); Print(Length(x)); Print("\n");

for y in anti_monoids8 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 8, Length: "); Print(Length(x)); Print("\n");

for y in anti_monoids9 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 9, Length: "); Print(Length(x)); Print("\n");

for y in anti_monoids10 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 
Print("\nDone order 10, Length: "); Print(Length(x)); Print("\n");

# prepare output file
fn := "outputs/anti_monoids_11.g";;
PrintTo(fn, "anti_monoids11");; AppendTo(fn, " := [\n");;

for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

fn := "outputs/anti_monoids_11.out";;
Read("print_mace.g");;
for p in [1..Length(x)] do
    print_bin_mace(fn, x[p], p);
od;
