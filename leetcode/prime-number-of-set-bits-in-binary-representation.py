class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                for j in range(i**2, n + 1, i):
                    if j == n:
                        return False
            return True

        def is_prime_(n):
            if n < 2:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        s = 0
        for i in range(left, right + 1):
            s += int(is_prime(i.bit_count()))
        return s
