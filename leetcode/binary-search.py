class Solution:
    def bisect_left(self, f, x, lb, ub):
        assert 0 <= lb <= ub
        if lb == ub:
            return lb
        if ub - lb < 2:
            return lb if x < f(ub) else ub
        idx = lb + (ub - lb)//2 + (ub - lb) % 2
        # assert (idx - 1 < ub)
        y = f(idx)
        if y < x:
            return self.bisect_left(f, x, idx, ub)
        return self.bisect_left(f, x, lb, idx)

    def search(self, lst, x):
        def f(x): return lst[x]
        i = self.bisect_left(f, x, 0, len(lst) - 1)
        if i == len(lst) or lst[i] != x:
            return -1
        return i
