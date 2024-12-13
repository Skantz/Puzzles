class Solution:
    def minimumSumSubarray(self, nums, l: int, r: int) -> int:
        n = len(nums)
        minn = max(nums) * n
        done = False
        for i in range(n - l + 1):
            for d in range(l, r + 1):
                s = sum(nums[i: i + d])
                minn = min(minn, s) if 0 < s else minn
                done = True if 0 < s else done
        return minn if done else 0 - 1
