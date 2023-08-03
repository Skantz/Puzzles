class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return len([(i, j) for i in range(len(nums)) for j in range(len(nums)) if (i < j and abs(nums[i] - nums[j]) == k)])
