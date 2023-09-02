class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for _ in range(32):
            m = m << 1
            if (n & 1) == 1:
                m = m | 1
            n = n >> 1
        return m
