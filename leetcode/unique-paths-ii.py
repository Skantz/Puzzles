class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        if not obstacle_grid or not obstacle_grid[0]:
            return 0
        n = len(obstacle_grid)
        m = len(obstacle_grid[0])
        # TODO remove 2 extra cases?
        if m == 1:
            return 1 if all(e == [0] for e in obstacle_grid) else 0
        if n == 1:
            return 1 if all(e == 0 for e in obstacle_grid[0]) else 0
        grid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    grid[i][j] = 1 if not obstacle_grid[i][j] else 0
                else:
                    grid[i][j] += grid[i - 1][j] if not obstacle_grid[i - 1][j] and not obstacle_grid[i][j] else 0
                    grid[i][j] += grid[i][j - 1] if not obstacle_grid[i][j - 1] and not obstacle_grid[i][j] else 0
        return grid[-1][-1]
