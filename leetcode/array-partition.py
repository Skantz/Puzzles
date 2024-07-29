class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[len(nums) - 2::-2])
