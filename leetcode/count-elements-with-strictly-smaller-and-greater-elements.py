class Solution:
    def countElements(self, nums: List[int]) -> int:
        return len([e for e in nums if e not in [min(nums), max(nums)]])
