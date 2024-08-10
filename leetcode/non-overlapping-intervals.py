class Solution:
    def eraseOverlapIntervals(self, xs) -> int:
        if len(xs) < 1:
            return 0
        xs.sort(key = lambda x : x[1])
        c = 0
        (x_, y_) = xs[0]
        for i, (x, y) in enumerate(xs):
            if i < 1:
                continue
            if y_ - 1 < x:
                y_ = y
                c += 1
        return len(xs) - c - 1
