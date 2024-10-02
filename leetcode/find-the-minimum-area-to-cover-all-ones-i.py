class Solution:
    def minimumArea(self, grid) -> int:
        n = len(grid)
        l, d, u, r = n, 0, n, 0
        def update(i, j):
            nonlocal l, d, u, r
            if grid[i][j] < 1:
                return
            l = min(l, j)
            r = max(r, j)
            u = min(u, i)
            d = max(d, i)
        for i, r_ in enumerate(grid):
            for j, _ in enumerate(r_):
                update(i, j)
        h = 1 + d - u
        w = 1 + r - l
        return h * w
