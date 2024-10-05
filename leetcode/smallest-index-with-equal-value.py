class Solution:
    def smallestEqual(self, nums) -> int:
        try:
            return next(i for i in range(len(nums)) if i % 10 == nums[i])
        except StopIteration:
            return -1
