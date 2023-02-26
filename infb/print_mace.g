

print_bin_mace := function(fn, m2, counter)
  local comma, el, el_counter, i, j, order, model;

  order := Length(m2);
  # Print header
  model := Concatenation("interpretation( ", String(order), ", [number=", String(counter), ", seconds=1], [\n  function(*(_,_), [\n");
  comma := ",";
  el_counter := 0;
  for i in [1..order] do
    model := Concatenation(model, "    ");
    for j in [1..order] do
      if el_counter = order * order - 1 then comma := ""; fi;
      el_counter := el_counter + 1;
      if m2[i][j] < 11:
        el := Concatenation(" ", String(m2[i][j]-1));
      else
        el := String(m2[i][j]-1);
      fi;
      model := Concatenation(model, el, comma);
    od;
    if i = order then
      model := Concatenation(model, " ])]).");
    fi;
    model := Concatenation(model, "\n");
  od;
  AppendTo(fn, model);
  return 1;
end;
