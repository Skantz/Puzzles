class Solution:
    def triangularSum(self, nums) -> int:
        while 1 < len(nums):
            nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
        return nums.pop()
