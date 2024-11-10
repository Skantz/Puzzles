class Solution:
    def similarPairs(self, ws) -> int:
        from collections import Counter
        c = Counter("".join(sorted(list(set(w)))) for w in ws)
        return sum(e * (e - 1) // 2 for e in c.values() if 1 < e)
