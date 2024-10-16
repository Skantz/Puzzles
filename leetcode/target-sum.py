from functools import cache

class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        n = len(nums)
        @cache
        def f(i, y):
            if n - 1 < i:
                return int(y == 0)
            x = nums[i]
            return f(i + 1, y + x) + f(i + 1, y - x)
        return f(0, target)
