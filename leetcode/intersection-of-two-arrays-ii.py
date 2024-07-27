from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for e in set(nums1).intersection(nums2):
            for _ in range(min(nums1.count(e), nums2.count(e))):
                ret.append(e)
        return ret
