cases_n = int(input())

def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return n > 1

def happy(n):
  seen = {}
  while n != 1:
    n = str(n)
    n_temp = 0
    for c in n:
      n_temp += int(c)**2
    n = n_temp
    try:
      seen[n]
      return False
    except KeyError:
      pass

    seen[n] = 1
  return True

for i in range(1,cases_n+1):
  n = input().split()
  n = int(n[1])
  if is_prime(n) and happy(n):
    print(i, n, "YES")
  else:
    print(i, n, "NO")
