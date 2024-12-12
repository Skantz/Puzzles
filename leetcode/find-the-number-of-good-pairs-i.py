class Solution:
    def numberOfPairs(self, nums1, nums2, k: int) -> int:
        return len([(i, j) for i, e in enumerate(nums1) for j, g in enumerate(nums2) if e % (g * k) == 0])
