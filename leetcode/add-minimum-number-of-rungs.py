from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        c = 0
        rungs = [0] + rungs
        def f(x, y): return x // y if x % y == 0 else x // y + 1
        for i in range(1, len(rungs)):
            d = rungs[i - 1] + dist - rungs[i]
            if d < 0:
                c += f(-d, dist)
        return c
