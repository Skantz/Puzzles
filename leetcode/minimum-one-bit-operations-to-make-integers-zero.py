from math import ceil, log2


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if not n: return 0
        m = n.bit_length()
        m = 2**ceil(log2(m))
        while m > 0:
            n = n ^ (n >> m)
            m = m // 2
        return n
