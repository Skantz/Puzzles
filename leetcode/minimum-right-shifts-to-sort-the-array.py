from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        ret = sorted(nums)
        if nums == ret:
            return 0
        n = len(nums)
        for i in range(n):
            nums = [nums[(j - 1) % n] for j, _ in enumerate(nums)]
            if nums == ret:
                return i + 1
        return -1
