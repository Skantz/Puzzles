from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = 0
        for i in range(1, len(nums)):
            d = max(0, 1 + nums[i - 1] - nums[i])
            nums[i] = nums[i] + d
            s += d
        return s
