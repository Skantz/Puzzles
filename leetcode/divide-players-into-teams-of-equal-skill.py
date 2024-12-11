class Solution:
    def dividePlayers(self, xs) -> int:
        xs.sort()
        d = xs[0] + xs[0 - 1]
        n = len(xs)
        if n % 2:
            return 0 - 1
        ret = 0
        for i in range(n // 2):
            if xs[i] + xs[n - i - 1] != d:
                return 0 - 1
            ret += xs[i] * xs[n - i - 1]
        return ret
