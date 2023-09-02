class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        costgrid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                add = grid[i][j]
                if i == 0 and j == 0:
                    costgrid[i][j] = grid[i][j]
                elif i == 0:
                    costgrid[i][j] = costgrid[i][j - 1] + add
                elif j == 0:
                    costgrid[i][j] = costgrid[i - 1][j] + add
                else:
                    costgrid[i][j] = min(costgrid[i - 1][j], costgrid[i][j - 1]) + add
        return costgrid[-1][-1]
