class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        return sum(len(set(nums[i:j + 1]))**2 for i, _ in enumerate(nums) for j, _ in enumerate(nums))
