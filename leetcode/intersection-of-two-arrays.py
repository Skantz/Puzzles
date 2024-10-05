class Solution:
    def intersection(self, nums1, nums2):
        return list({i for i in nums1 if i in nums2})
