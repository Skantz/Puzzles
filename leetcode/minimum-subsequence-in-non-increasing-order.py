class Solution:
    def minSubsequence(self, nums):
        m = sum(nums) // 2
        nums = sorted(nums)[::-1]
        ret = []
        for e in nums:
            ret.append(e)
            if m < sum(ret):
                return ret
        assert False
