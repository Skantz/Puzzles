from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        c1_1 = Counter(s1[::2])
        c1_2 = Counter(s1[1::2])
        c2_1 = Counter(s2[::2])
        c2_2 = Counter(s2[1::2])
        return c1_1 == c2_1 and c1_2 == c2_2
