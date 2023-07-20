class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        try:
            return next(i for i in range(len(nums)) if i % 10 == nums[i])
        except StopIteration:
            return -1
