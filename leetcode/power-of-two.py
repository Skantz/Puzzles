from math import log2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return log2(n) == round(log2(n))
