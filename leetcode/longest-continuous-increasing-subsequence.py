class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        maxx = 1
        prev = nums[0]
        cur = 0
        for e in nums[1:]:
            if e > prev:
                cur += 1
            else:
                maxx = max(cur + 1, maxx)
                cur = 0
            prev = e
        return max(maxx, cur + 1)
