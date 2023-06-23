class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(nums.count(n) % 2 == 0 for n in nums)
