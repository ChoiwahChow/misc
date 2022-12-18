
LoadPackage("cream");;

Read("outputs/monoids_6.g");
Read("outputs/monoids_7.g");
Read("outputs/monoids_8.g");
Read("outputs/monoids_9.g");
Read("outputs/monoids_10.g");
Read("outputs/monoids_11.g");
Read("non_iso/monoids_12.g");

# prepare output file
fn := "outputs/monoids_12.g";;


x := models11;;

for y in monoids6 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od; 

Print("Done with order 6, length="); Print(Length(x)); Print("\n");

for y in monoids7 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od;
Print("Done with order 7, length="); Print(Length(x)); Print("\n");

for y in monoids8 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od;
Print("Done with order 8, length="); Print(Length(x)); Print("\n");

for y in monoids9 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od;
Print("Done with order 9, length="); Print(Length(x)); Print("\n");

for y in monoids10 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od;
Print("Done with order 10, length="); Print(Length(x)); Print("\n");

for y in monoids11 do
    x := Filtered(x, i->CreamMonomorphismAlgebras([y], [i]) = fail);;
od;
Print("Done with order 11, length="); Print(Length(x)); Print("\n");

# Print models
PrintTo(fn, "monoids12");; AppendTo(fn, " := [\n");;
for p in x do
  AppendTo(fn, p); AppendTo(fn, ",\n");
od;

AppendTo(fn, "];\n");

