class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        import itertools
        return list([list(c) for c in set([tuple(list(c)) for c in itertools.permutations(nums)])])
