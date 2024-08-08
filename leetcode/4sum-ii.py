from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        two1 = {}
        for i, e in enumerate(nums1):
            for j, f in enumerate(nums2):
                if e + f in two1:
                    two1[e + f] += 1
                else:
                    two1[e + f] = 1
        two2 = {}
        for i, e in enumerate(nums3):
            for j, f in enumerate(nums4):
                if e + f in two2:
                    two2[e + f] += 1
                else:
                    two2[e + f] = 1
        s = 0
        for k1 in two1:
            for k2 in two2:
                if k1 + k2 != 0:
                    continue
                s += two1[k1] * two2[k2]
        return s
