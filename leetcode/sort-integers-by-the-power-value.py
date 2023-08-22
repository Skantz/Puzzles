class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l = list(range(lo, hi + 1))
        f = lambda x : 0 if x <= 1 else 1 + f(x // 2) if not x % 2 else 1 + f(3 * x + 1)
        return sorted(l, key=f)[k - 1]
