from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(i - j) <= k and nums[i] == nums[j]:
                    return True
        return False
