class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return (next(e for e in nums if nums.count(e) > 1), (set(list(range(1, len(nums) + 1))) - set(nums)).pop())
