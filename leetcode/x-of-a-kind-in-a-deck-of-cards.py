class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        from collections import Counter
        from math import gcd
        c = Counter(deck)
        return 1 < gcd(*c.values())
