from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return 1 < len([e for e in nums if not e & 1])
