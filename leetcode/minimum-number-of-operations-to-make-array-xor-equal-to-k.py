from typing import List


class Solution:

    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()

    def minOperations(self, nums: List[int], k: int) -> int:
        if not nums:
            assert False
        x = nums[0]
        for e in nums[1:]:
            x ^= e
        d = self.hammingDistance(x, k)
        return d
