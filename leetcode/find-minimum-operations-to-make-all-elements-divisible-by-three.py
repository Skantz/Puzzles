from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(map(lambda x: int(x % 3 != 0), nums))
