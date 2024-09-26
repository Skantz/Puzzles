class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        return min(nums[i]/2 + nums[n - i - 1]/2 for i in range(n//2))
