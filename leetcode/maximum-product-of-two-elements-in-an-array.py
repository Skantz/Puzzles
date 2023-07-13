class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (max(nums) - 1) * (max(next(nums for _ in nums.remove(max(nums)) or [-1])) - 1)
