class Solution():
    def equalPairs(self, grid):
        n = len(grid)
        m = len(grid[0])
        transpose = [[grid[i][j] for i in range(n)] for j in range(n)]
        s = 0
        for i in range(n):
            for j in range(m):
                if grid[i] == transpose[j]:
                    s += 1
        return s
