class Solution:
    def maxProductDifference(self, nums) -> int:
        return max(nums) * (max(next(nums for _ in nums.remove(max(nums)) or [-1]))) - min(nums) * (min(next(nums for _ in nums.remove(min(nums)) or [-1])))
