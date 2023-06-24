class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        idxs = [i for i, e in enumerate(nums) if e == 0]
        return max(idxs[i] - idxs[i - 1] - 1 for i in range(1, len(idxs)))
