class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        b1 = all(s1[i] >= s2[i] for i in range(len(s1)))
        b2 = all(s1[i] <= s2[i] for i in range(len(s1)))
        return b1 | b2
