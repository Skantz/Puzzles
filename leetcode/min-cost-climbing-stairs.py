class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        grid = [0 for _ in range(len(cost))]
        grid[0] = cost[0]
        grid[1] = cost[1]
        for i, e in enumerate(cost[2:]):
            grid[i + 2] = e + min(grid[i + 1], grid[i])
        return min(grid[-1], grid[-2])
