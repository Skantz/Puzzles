class Solution:
    def findIntersectionValues(self, nums1, nums2):
        return [sum(1 for e in nums1 if e in nums2), sum(1 for e in nums2 if e in nums1)]
