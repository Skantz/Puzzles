from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        two1, two2 = {}, {}
        for (e, f) in ((e1, e2) for e1 in nums1 for e2 in nums2):
            two1[e + f] = two1[e + f] + 1 if (e + f) in two1 else 1
        for (e, f) in ((e3, e4) for e3 in nums3 for e4 in nums4):
            two2[e + f] = two2[e + f] + 1 if (e + f) in two2 else 1
        two1 = {k:two1[k] for k in two1 if -k in two2}
        return sum((two1[k1] * two2[k2] for k1 in two1 for k2 in two2 if k1 + k2 == 0))
