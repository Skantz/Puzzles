class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return max(e1 + e2 if max(str(e1)) == max(str(e2)) and i != j else -1 for i, e1 in enumerate(nums) for j, e2 in enumerate(nums))
