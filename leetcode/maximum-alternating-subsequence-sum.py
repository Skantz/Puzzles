from functools import cache


class Solution:
    def maxAlternatingSum(self, nums, flip=False) -> int:
        self.nums = nums
        self.n = len(nums)
        return self.max_alternating_sum(0, False)

    @cache
    def max_alternating_sum(self, i, flip=False):
        if self.n - 1 < i:
            return 0
        right = (-1)**flip * self.nums[i] + self.max_alternating_sum(i + 1, not flip)
        left = self.max_alternating_sum(i + 1, flip)
        return max(left, right)
