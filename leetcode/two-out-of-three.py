class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        A, B, C = set(nums1), set(nums2), set(nums3)
        return list((A & B) | (A & C) | (B & C))
