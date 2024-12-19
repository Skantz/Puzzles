class Solution:
    def smallestNumber(self, n: int) -> int:
        if n.bit_length() == n.bit_count():
            return n
        m = n
        i = 1
        while 0 < n:
            m |= i
            i = i << 1
            n = n >> 1
        return m
