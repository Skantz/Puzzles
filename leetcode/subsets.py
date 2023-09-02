class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[]] if not nums else [] + [[nums[0]] + s for s in self.subsets(nums[1:])] + [[] + s for s in self.subsets(nums[1:])]
