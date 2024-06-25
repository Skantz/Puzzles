from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        x = Counter(s)
        y = Counter(t)
        z = x - y
        return sum(z.values())
