class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def primes(n):
            primes = [False, False] + [True for e in range(0, n - 2)]
            for i in range(2, int(n**0.5) + 1):
                if primes[i]:
                    for j in range(i**2, n, i):
                        primes[j] = False
            return [i for i, e in enumerate(primes) if e]
        ps_n = len(primes(n + 1))
        def f(x): return 1 if x < 1 else x * f(x - 1)
        return (f(ps_n) * f(n - ps_n)) % (10**9 + 7)
