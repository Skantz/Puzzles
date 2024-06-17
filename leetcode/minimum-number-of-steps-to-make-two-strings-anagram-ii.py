from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        print(c1, c2)
        for k in c1:
            c1[k] = abs(c1[k] - c2[k])
        for k in c2:
            if k not in c1:
                c1[k] = c2[k]
        return sum(c1.values())
