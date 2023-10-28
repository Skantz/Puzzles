class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, e in enumerate(sorted(nums)) if e == target]
