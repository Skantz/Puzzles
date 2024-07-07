from functools import cache


class Solution:
    @cache
    def numWays(self, steps: int, arr_len: int, pos=0) -> int:
        if steps < pos or pos < 0 or arr_len - 1 < pos:
            return 0
        if steps < 1:
            return int(pos == 0)
        f = self.numWays
        left = f(steps - 1, arr_len, pos - 1)
        right = f(steps - 1, arr_len, pos + 1)
        mid = f(steps - 1, arr_len, pos)
        return (left + right + mid) % (10**9 + 7)
