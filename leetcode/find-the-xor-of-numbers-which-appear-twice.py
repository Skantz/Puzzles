from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums = list({e for e in nums if nums.count(e) == 2})
        ret = 0
        for e in nums:
            ret ^= e
        return ret
