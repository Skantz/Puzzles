from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        s = 0
        for r in grid:
            for c in r:
                if c < 0:
                    s += 1
        return s
