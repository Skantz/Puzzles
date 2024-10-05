class Solution:
    def subArrayRanges(self, nums) -> int:
        n = len(nums)
        s = 0
        for i in range(n):
            maxx = - 10**10
            minn = 10 ** 10
            for j in range(i + 1, n):
                maxx = max(maxx, nums[i], nums[j])
                minn = min(minn, nums[i], nums[j])
                s += (maxx - minn)
        return s
