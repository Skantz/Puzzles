from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def primes(n):
            primes = [False, False] + [True for e in range(0, n - 2)]
            for i in range(2, int(n**0.5) + 1):
                if primes[i]:
                    for j in range(i**2, n, i):
                        primes[j] = False
            return [i for i, e in enumerate(primes) if e]
        ps = set(primes(n))
        rets = []
        for e in ps:
            if n < 2 * e:
                continue
            if n - e in ps:
                rets.append([e, n - e])
        return sorted(rets)
