class Solution:
    def isSumEqual(self, xs: str, ys: str, zs: str) -> bool:
        def f(x): return ord(x) - 97
        x = int("".join(map(str, map(f, xs))))
        y = int("".join(map(str, map(f, ys))))
        z = int("".join(map(str, map(f, zs))))
        return x + y == z
