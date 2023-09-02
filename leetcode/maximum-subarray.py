class Solution: #kadane
    def maxSubArray(self, nums: List[int]) -> int:
        if all(e < 0 for e in nums):
            return max(nums)
        maxx, sum_ = 0, 0
        for e in nums:
            sum_ = max(0, sum_ + e)
            maxx = max(maxx, sum_)
        return maxx
