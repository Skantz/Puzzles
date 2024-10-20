class Solution:
    def findWinners(self, ms):
        from collections import Counter
        ws = set(m[0] for m in ms)
        ls = set(m[1] for m in ms)
        cs = Counter(m[1] for m in ms)
        y = [e for e in ls if cs[e] == 1]
        return [sorted(list(ws - ls)), sorted(y)]
