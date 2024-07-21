from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        def flatten(x):
            if not x:
                return []
            ret = []
            for r in x:
                for e in r:
                    ret.append(e)
            return ret
        lst = flatten(grid)
        del grid
        if not len({e % x for e in lst}) < 2:
            return -1
        mid = sorted(lst)[len(lst) // 2]
        return sum(abs(e - mid)//x for e in lst)
