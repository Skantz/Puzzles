class Solution:
    def no_dupe(self, list_of_list):
        return [list(e) for e in list(set([tuple(sorted(e)) for e in list_of_list]))]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        e = nums[0]
        r = [[e] + l for l in self.subsetsWithDup(nums[1:])] + self.subsetsWithDup(nums[1:])
        return self.no_dupe(r)
