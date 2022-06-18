class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return ([list(c) for c in permutations(nums)])
