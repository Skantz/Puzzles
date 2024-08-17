class Solution:
    def onesMinusZeros(self, grid):
        m = len(grid)
        n = len(grid[0])
        from functools import cache
        @cache
        def col(j): return[grid[i][j] for i in range(m)]
        @cache
        def comp1(i): return grid[i].count(1) - grid[i].count(0)
        @cache
        def comp2(j): return col(j).count(1) - col(j).count(0)
        return [[comp1(i) + comp2(j) for j in range(n)] for i in range(m)]
