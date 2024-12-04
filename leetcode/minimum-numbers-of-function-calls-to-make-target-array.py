class Solution:
    def minOperations(self, xs) -> int:
        n1 = max(x.bit_length() for x in xs)
        n2 = sum(x.bit_count() for x in xs)
        return max(0, n1 + n2 - 1)
