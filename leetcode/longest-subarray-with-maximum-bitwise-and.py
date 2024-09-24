class Solution:
    def longestSubarray(self, nums) -> int:
        maxx = max(nums)
        maxx_l = 1
        i = 0
        while i < len(nums):
            e = nums[i]
            j = 1
            while i + j < len(nums) and nums[i + j] == e == maxx:
                j += 1
            maxx_l = max(maxx_l, j)
            i += j
        return maxx_l
