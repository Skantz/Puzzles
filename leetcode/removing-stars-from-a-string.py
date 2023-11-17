class Solution:
    def removeStars(self, s: str) -> str:
        n = s.count("*")
        while n > 0:
            idx = s.index("*")
            s = s[:idx - 1] + s[idx + 1:]
            n -= 1
        return s
