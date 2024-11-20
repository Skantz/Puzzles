class Solution:
    def maxAbsoluteSum(self, nums) -> int:
        minn, maxx, sum_1, sum_2 = 0, 0, 0, 0
        for e in nums:
            sum_1 = max(0, sum_1 + e)
            maxx = max(maxx, sum_1)
            sum_2 = min(0, sum_2 + e)
            minn = min(minn, sum_2)
        return max(maxx, 0 - minn)
