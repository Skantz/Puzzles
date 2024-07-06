from collections import Counter


class Solution:
    def closeStrings(self, x: str, y: str) -> bool:
        c1, c2 = Counter(x), Counter(y)
        return sorted(c1.values()) == sorted(c2.values()) and c1.keys() == c2.keys()
