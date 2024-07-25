from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        zet = set()
        for e in nums:
            if e in zet: return e
            zet.add(e)
        assert False
