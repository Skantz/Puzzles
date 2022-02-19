from sys import stdin

names = {}
first_name_count = {}

for inp in stdin:
  name = inp.split()
  try:
    names[name[1]].append(name[0])
  except KeyError:
    names[name[1]] = [name[0]]
  try:
    first_name_count[name[0]] += 1
  except KeyError:
    first_name_count[name[0]] = 1

last_names = list(names.keys())
last_names.sort()

for name in last_names:
  bearers = names[name]
  if len(bearers) == 1:
    if first_name_count[bearers[0]] == 1:
      print(bearers[0])
    else:
      print(bearers[0],name)
  else:
    bearers.sort()
    for name in bearers:
      if first_name_count[name] == 1:
        print(name)
      else:
        print(bearers,name)
