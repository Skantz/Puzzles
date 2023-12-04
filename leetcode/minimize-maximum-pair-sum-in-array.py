class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxx = -1
        for i in range(len(nums) // 2):
            e = nums[i] + nums[len(nums) - i - 1]
            maxx = max(maxx, e)
        return maxx
