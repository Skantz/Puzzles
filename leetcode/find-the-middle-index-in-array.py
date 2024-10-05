class Solution:
    def findMiddleIndex(self, nums) -> int:
        try:
            return next(i for i in range(len(nums)) if sum(nums[:i]) == sum(nums[i + 1:]))
        except StopIteration:
            return -1
