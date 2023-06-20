class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        return (lambda x, y, z: 0 + x + (z - 1 - y) - (1 if (x > y) else 0))(nums.index(1), nums.index(len(nums)), len(nums))
