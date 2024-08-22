class Solution:
    def countHillValley(self, nums) -> int:
        c = 0
        nums = [e for i, e in enumerate(nums) if i == 0 or nums[i] != nums[i - 1]]
        for i in range(1, len(nums) - 1):
            c += 1 if (nums[i - 1] < nums[i]) == (nums[i + 1] < nums[i]) else 0
        return c
