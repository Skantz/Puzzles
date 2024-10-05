class Solution:
    def maxScore(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        costgrid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    costgrid[i][j] = - 10**5 - 1
                elif i == 0:
                    costgrid[i][j] = costgrid[i][j] - max(grid[i])
                    for k in range(j):
                        costgrid[i][j] = max(costgrid[i][j], grid[i][j] - grid[i][k])
                elif j == 0:
                    first_col = [e[0] for e in grid]
                    costgrid[i][j] = costgrid[i][j] - max(first_col)
                    for k in range(i):
                        costgrid[i][j] = max(costgrid[i][j], grid[i][j] - first_col[k])
                else:
                    d1 = (grid[i][j] - grid[i][j - 1])
                    d2 = (grid[i][j] - grid[i - 1][j])
                    x = costgrid[i][j - 1] + d1
                    y = costgrid[i - 1][j] + d2
                    costgrid[i][j] = max(x, y, d1, d2) #d1, d2: restart
        maxx = - 10**5 * 10**5 - 1
        for r in costgrid:
            for e in r:
                maxx = max(maxx, e)
        return maxx
