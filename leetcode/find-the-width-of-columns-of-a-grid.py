class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        return [max([(len(str(e))) for e in lst]) for lst in grid]
