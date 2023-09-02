class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list({i for i in nums1 if i in nums2})
