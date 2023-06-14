class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return [] if not nums else set(range(len(nums) + 1)).difference(set(nums)).pop()
