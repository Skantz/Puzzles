class Solution:
    def makeEqual(self, words) -> bool:
        from collections import Counter
        return all(e % len(words) == 0 for e in Counter("".join(words)).values())
