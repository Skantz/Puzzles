class Solution:
    def numOfSubarrays(self, arr) -> int:
        x = 0
        y = 0
        s = 0
        for e in arr:
            s += e
            x += 1 if s % 2 else 0
            y += 0 if s % 2 else 1
        return ((y + 1) * x) % (10**9 + 7)
