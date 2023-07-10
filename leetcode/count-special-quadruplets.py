class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return len([(i, j, k, l) for i in range(len(nums))
                                 for j in range(i + 1, len(nums))
                                 for k in range(j + 1, len(nums))
                                 for l in range(k + 1, len(nums))
                                 if nums[i] + nums[k] + nums[j] == nums[l]])
