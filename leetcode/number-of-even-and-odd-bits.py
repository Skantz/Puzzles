class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s, c = [0, 0], 0
        while n:
            s[c] += 1 & n
            n = n >> 1
            c = (c + 1) % 2
        return s
