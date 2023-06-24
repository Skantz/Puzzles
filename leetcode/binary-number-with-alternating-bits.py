class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        val = n & 1
        n = n >> 1
        while (n):
            val = val ^ 1
            if (n & 1) ^ val:
                return False
            n >>= 1
        return True
