from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        z_idx = -1
        if nums.count(0) == 1:
            z_idx = nums.index(0)
        p = 1
        for i, e in enumerate(nums):
            if i != z_idx:
                p *= e
        if z_idx != -1:
            return [0 if i != z_idx else p for i, e in enumerate(nums)]
        # no zero
        rets = [int(p * e**(-1)) for i, e in enumerate(nums)]
        return rets
