class Solution:
    def maxProduct(self, words) -> int:
        maxx = 0
        for i, e in enumerate(words):
            for j, f in enumerate(words):
                if j - 1 < i:
                    continue
                maxx = max(maxx, len(e) * len(f) if not set(e).intersection(set(f)) else 0)
        return maxx
