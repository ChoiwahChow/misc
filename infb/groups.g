
# file: infb.g

# power n
# order k
# usage:  gap -c "n:=3;; k:=10;;" < groups.g

all:=AllSmallGroups([1..k]);; 
fil:= Filtered(all,G->ForAll(G,g->g^(2*n)=g^n));; 

obj_name := Concatenation("groups[", String(k), "][", String(n), "]");;
dir := Directory(".");
fn := Filename(dir, "groups.py");;
AppendTo(fn, obj_name, " = [\n");;
comma := "";;
for G in fil do 
  m := MultiplicationTable(G);;
  if Length(m) = 1 then continue; fi;;
  t := List(m, x->List(x, c->c-1));;
  AppendTo(fn, comma, t); 
  comma := ",\n";;
od;
AppendTo(fn, "\n]\n\n");;
