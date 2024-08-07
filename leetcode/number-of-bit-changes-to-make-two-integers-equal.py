class Solution:
    def minChanges(self, n: int, k: int) -> int:
        s, b = 0, 1 << (1 + max(n.bit_length(), k.bit_length()))
        while (b := b >> 1):
            if (k & b) ^ (n & b):
                if k & b:
                    return -1
                s += 1
        return s
