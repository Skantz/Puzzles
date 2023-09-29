class Solution:
    def specialArray(self, nums: List[int]) -> int:
        return next(iter(filter(lambda x: len([e for e in nums if e >= x]) == x, list(range(1, len(nums) + 1)))), -1)
