class Solution:
    def targetIndices(self, nums, target: int) -> int:
        return [i for i, e in enumerate(sorted(nums)) if e == target]
