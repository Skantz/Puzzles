class Solution:
    def combinationSum3(self, k: int, n: int):
        t = list(range(1, 2**9 + 1))
        cs = []
        for e in t:
            b = bin(e)[2:][::-1]
            if b.count('1') != k:
                continue
            s = sum(i + 1 for i, g in enumerate(b) if g == '1')
            if s == n:
                cs.append([i + 1 for i, g in enumerate(b) if g == '1'])
        return set([tuple(e) for e in cs])
