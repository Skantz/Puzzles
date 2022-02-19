from math import factorial

def n_choose_k(n, k):
    f = lambda x: factorial(x)
    return f(n) // f(k) // f(n - k)

for _ in range(int(input())):
    x, y = [int(p) for p in input().strip().split()]
    print(n_choose_k(x, y - 1))