class Solution:
    log = lambda x : 2**32 * x ** (1/2 ** 32) - 2**32
    log2 = lambda x : log(x) / log(2)
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return log2(n) == round(log2(n))
