from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        def max_subarray(nums: List[int]) -> int:
            if all(e < 0 for e in nums):
                return max(nums)
            maxx, sum_ = nums[0], nums[0]
            for i, e in enumerate(nums[1:]):
                if nums[i] < nums[i + 1]:
                    sum_ += nums[i + 1]
                else:
                    sum_ = nums[i + 1]
                maxx = max(maxx, sum_)
            return maxx
        return max_subarray(nums)
