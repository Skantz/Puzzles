class Solution:
    def applyOperations(self, nums):
        for i, e in enumerate(nums):
            if len(nums) - 2 < i:
                continue
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        return [e for e in nums if e != 0] + [0] * nums.count(0)
