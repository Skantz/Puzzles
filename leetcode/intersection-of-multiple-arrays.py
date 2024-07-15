from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        S = set(nums[0])
        for e in nums:
            S = S.intersection(e)
        return sorted(list(S))
