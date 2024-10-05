from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        naive = nums1 + nums2
        naive.sort()
        n = len(naive)
        if len(naive) % 2:
            return naive[n//2]
        return (naive[n//2 - 1] + naive[n//2])*0.5
