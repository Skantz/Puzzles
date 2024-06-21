from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        c = 0
        for i, e in enumerate(nums):
            if c == s - c - e:
                return i
            c += e
        return -1
