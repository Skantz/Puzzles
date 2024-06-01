from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        counts_r = [0] * n
        counts_c = [0] * m
        s = 0
        for i, r in enumerate(grid):
            for j, e in enumerate(r):
                counts_r[i] += e
                counts_c[j] += e
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    s += (counts_r[i] - 1) * (counts_c[j] - 1)
        return s
