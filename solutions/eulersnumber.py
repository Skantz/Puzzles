#https://open.kattis.com/problems/eulersnumber
fac = lambda x: 1 if x <= 1 else x * fac(x - 1)
print(sum([1/fac(n) for n in range(min(20, int(input()) + 1))]))
#Done
