class Solution:
    def isFascinating(self, n: int) -> bool:
        x = ("".join(map(str, [n, 2 * n, 3 * n])))
        y = ("".join(map(str, list(range(1, 10)))))
        z = set(x) == set(y)
        w = all([x.count(e) == 1 for e in x]) and all([y.count(e) == 1 for e in y])
        return z and w
