from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n_noneq = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                n_noneq += 1
        if n_noneq < 1:
            return True
        else:
            return n_noneq < 2 and (len(nums) < 2 or nums[0] >= nums[-1])
