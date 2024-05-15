from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        zet = set(nums)
        count = {e: 0 for e in zet}
        for e in nums:
            count[e] += 1
        return {s for s in zet
                if s - 1 not in zet
                and s + 1 not in zet
                and count[s] < 2}
