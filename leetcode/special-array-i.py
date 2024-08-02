class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all([(e & 1) != (nums[i + 1] & 1) for i, e in enumerate(nums[:-1])])
