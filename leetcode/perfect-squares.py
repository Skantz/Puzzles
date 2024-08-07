from collections import Counter


class Solution:
    def numSquares(self, n: int) -> int:

        # Trivial
        if int(n**0.5)**2 == n:
            return 1

        mems = {}

        def is_prime(n):
            if n in mems:
                return mems[n]
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    mems[n] = False
                    return False
            mems[n] = True
            return True

        factors = list()

        for i in range(1, n + 1):
            if is_prime(i) and n % i == 0:
                c = 0
                m = n
                while m % i == 0:
                    m //= i
                    c += 1
                factors += c * [i]

        c = Counter(factors)

        # Fermat
        if not any((e % 4 == 3 and c[e] % 2) for e in c):
            return 2

        # Legendre
        m = n
        while not m % 4:
            m //= 4
        if (m - 7) % 8 != 0:
            return 3

        # Lagrange
        return 4
