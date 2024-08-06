class Solution:
    def minChanges(self, n: int, k: int) -> int:
        s = 0
        b = 1 << max(n.bit_length(), k.bit_length())
        while b:
            if (k & b) ^ (n & b):
                if k & b:
                    return -1
                s += 1
            b >>= 1
        return s
