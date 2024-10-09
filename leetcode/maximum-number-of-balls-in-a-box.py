class Solution:
    def countBalls(self, lb: int, ub: int) -> int:
        r = range(lb, ub + 1)
        def f(x): return sum(int(e) for e in str(x))
        from collections import Counter
        c = Counter(f(x) for x in r)
        return max(c.values())
