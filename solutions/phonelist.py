#https://open.kattis.com/problems/phonelist
import sys

cases_n = int(sys.stdin.readline())

for i in range(cases_n):
  numbers_n = int(sys.stdin.readline())
  numbers = set()
  for j in range(numbers_n):
    numbers.add(sys.stdin.readline().strip())

  dup = False
  for n in numbers:
    for i in range(1, len(n)):
      if n[:i] in numbers:
        dup = True
        break
    if dup:
      break

  if not dup:
    print("YES")
  else:
    print("NO")
#done
