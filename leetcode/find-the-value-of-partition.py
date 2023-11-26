class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        nums.sort()
        minn = max(nums) * 2 + 1
        i = 1
        prev = nums[0]
        while i < len(nums):
            cur = nums[i]
            if abs(cur - prev) < minn:
                minn = abs(cur - prev)
            prev = cur
            i += 1
        return minn
