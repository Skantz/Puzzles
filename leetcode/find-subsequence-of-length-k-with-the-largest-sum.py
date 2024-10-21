class Solution:
    def maxSubsequence(self, nums, k: int):
        from collections import Counter
        nums_ = sorted(nums)[::-1][:k]
        cs = Counter(nums_)
        ret = []
        for e in nums:
            if e in nums_ and 0 < cs[e]:
                ret.append(e)
                cs[e] -= 1
        return ret
