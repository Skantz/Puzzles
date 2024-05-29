from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        mems = {}

        def can_pick(nums_idx, t):
            if t < 0 or nums_idx > len(nums) - 1:
                return False
            if t == 0:
                return True
            x = nums[nums_idx]
            tupl = (nums_idx + 1, t - x)
            left = mems[tupl] if tupl in mems else can_pick(nums_idx + 1, t - x)
            if left:
                return True
            mems[tupl] = left
            tupl = (nums_idx + 1, t)
            right = mems[tupl] if tupl in mems else can_pick(nums_idx + 1, t)
            mems[tupl] = right
            return left or right
        s = sum(nums)
        sdiv2 = s//2
        if s % 2:
            return False
        return can_pick(0, sdiv2)
