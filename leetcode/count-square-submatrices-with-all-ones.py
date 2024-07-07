from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        grid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == j or i == 0:
                    grid[i][j] = int(matrix[i][j] == 1)
                # i, j > 0
                if matrix[i][j] == 0:
                    grid[i][j] = 0
                    continue
                left = grid[i - 1][j]
                right = grid[i][j - 1]
                mid = grid[i - 1][j - 1]
                v = min(left, right, mid) + 1
                grid[i][j] = v
        s = 0
        for r in grid:
            s += sum(r)
        return s
