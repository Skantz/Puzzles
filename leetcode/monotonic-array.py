from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x = [nums[i + 1] >= nums[i] for i in range(len(nums) - 1)]
        y = [nums[i + 1] <= nums[i] for i in range(len(nums) - 1)]
        return all(x) | all(y)
