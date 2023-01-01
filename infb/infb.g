
# file: infb.g

# power n
# usage:  gap -c "n:=3;;" < infb.g

all:=AllSmallGroups([1..12]);; 
fil:= Filtered(all,G->ForAll(G,g->g^(2*n)=g^n));; 

obj_name := Concatenation("groups[", String(n), "]");;
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
