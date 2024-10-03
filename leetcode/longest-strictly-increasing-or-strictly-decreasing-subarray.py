class Solution:
    def longestMonotonicSubarray(self, nums) -> int:
        up = 1
        down = 1
        i = 1
        cup = 1
        cdown = 1
        while i < len(nums):
            prev = nums[i - 1]
            curr = nums[i]
            if prev < curr:
                cup += 1
                cdown = 1
                up = max(cup, up)
            elif curr < prev:
                cdown += 1
                cup = 1
                down = max(down, cdown)
            else:
                cup = 1
                cdown = 1
            i += 1
        return max(up, down)
