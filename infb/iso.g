

non_iso := [];;
while Length(monoids12) > 0 do
  y := monoids12[1];
  Add(non_iso, y);
  Remove(monoids12, 1);
  monoids12 := Filtered(monoids12, x->IsomorphismAlgebras([x], [y])=fail);
od;
