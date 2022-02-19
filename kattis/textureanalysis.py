import sys

case = 1
for line in sys.stdin:
  a = line.strip()
  if a == "END":
    exit()
  try:
    a = a.split("*")[1:-1]
  except:
    pass
  try:
    if a.count(a[0]) == len(a):
      print(case, "EVEN")
    else:
      print(case, "NOT EVEN")
  except:
    print(case, "EVEN")
  case += 1

