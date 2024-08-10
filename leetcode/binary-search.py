class Solution:
    def bisect_left(self, lst, x, lb=None, ub=None):
        if len(lst) < 1:
            return -1
        if lb is None:
            assert ub is None
            lb, ub = 0, len(lst) - 1
        if lb == ub:
            return lb
        if ub - lb < 2:
            return lb if x < lst[ub] else ub
        idx = lb + (ub - lb)//2 + (ub - lb) % 2
        # assert (idx - 1 < ub)
        y = lst[idx]
        if y < x:
            return self.bisect_left(lst, x, idx, ub)
        return self.bisect_left(lst, x, lb, idx)

    def search(self, lst, x):
        i = self.bisect_left(lst, x)
        if i == len(lst) or lst[i] != x:
            return -1
        return i
