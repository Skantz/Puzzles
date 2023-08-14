class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        grid = [n for _ in range(n)]
        grid[0] = 0
        for i in range(1, min(n, nums[0] + 1)):
            grid[i] = 1
        for i, e in enumerate(nums):
            for j in range(0, e + 1):
                if i + j >= n:
                    continue
                grid[i + j] = min(grid[i + j], grid[i] + 1)
        return grid[-1]
