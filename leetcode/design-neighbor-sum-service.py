from functools import cache
from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.g = grid

    @cache
    def idx(self, v: int) -> (int, int):
        for i, r in enumerate(self.g):
            for j, c in enumerate(r):
                if c == v:
                    return (i, j)
        assert False

    def adjacentSum(self, value: int) -> int:
        (x, y) = self.idx(value)
        s = 0
        g = self.g
        grid = g
        s += grid[x - 1][y] if 0 < x else 0
        s += grid[x + 1][y] if x + 1 < len(g) else 0
        s += grid[x][y - 1] if 0 < y else 0
        s += grid[x][y + 1] if y + 1 < len(g[0]) else 0
        return s

    def diagonalSum(self, value: int) -> int:
        (x, y) = self.idx(value)
        s = 0
        g = self.g
        grid = g
        s += grid[x - 1][y - 1] if 0 < x and 0 < y else 0
        s += grid[x + 1][y + 1] if x + 1 < len(g) and y + 1 < len(g[0]) else 0
        s += grid[x + 1][y - 1] if 0 < y and x + 1 < len(g) else 0
        s += grid[x - 1][y + 1] if y + 1 < len(g[0]) and 0 < x else 0
        return s
