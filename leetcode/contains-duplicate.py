class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sorted(nums) != sorted(list(set(nums)))
