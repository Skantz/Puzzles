class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        c = [n for n in nums1 if n in nums2]
        if c != []:
            return min(c)
        a, b = min(nums1), min(nums2)
        return int(str(min(a, b)) + str(max(a, b)))
