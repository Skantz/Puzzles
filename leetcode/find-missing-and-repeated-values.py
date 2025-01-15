class Solution:
    def findMissingAndRepeatedValues(self, grid):
        def flatten(x):
            if not x:
                return []
            ret = []
            for r in x:
                for e in r:
                    ret.append(e)
            return ret
        grid = flatten(grid)
        return [next(e for e in range(1, len(grid) + 1) if 1 < grid.count(e)), next(e for e in range(1, len(grid) + 1) if e not in grid)]
