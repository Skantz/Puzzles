class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        min_ = sum(abs(nums1[i] - nums2[i]) for i in range(len(nums1)))
        maxx = 0
        for i, _ in enumerate(nums1):
            z = abs(nums1[i] - nums2[i])
            if z < maxx:
                continue
            for j in range(len(nums2)):
                z_ = abs(nums1[j] - nums2[i])
                if z_ < z:
                    maxx = max(maxx, z - z_)
        return (min_ - maxx) % (10**9 + 7)
