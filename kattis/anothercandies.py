cases_n = int(input())
for _ in range(cases_n):
  _ = input()
  n = int(input())
  sum_ = 0
  for _ in range(n):
    sum_ += int(input())
  if sum_ % n == 0:
    print("YES")
  else:
    print("NO")
