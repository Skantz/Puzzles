class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        x = nums[0]
        for e in nums: x |= e
        return x
