class Solution:
    def myPow(self, x: float, n: int) -> float:
        c = x
        if not 0 - 1 < n:
            c = 1/c
        r = 1
        for i, e in enumerate(bin(n)[2:][::-1]):
            r *= (c if e == '1' else 1)
            c *= c
        return r
