class Solution:
    def smallestRangeI(self, nums, k: int) -> int:
        x, y = min(nums), max(nums)
        return max(0, y - x - 2 * k)
