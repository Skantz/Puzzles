from functools import cache

class Solution:
    def predictTheWinner(self, nums) -> bool:
        @cache
        def f(i, j):
            if j - 1 < i:
                return nums[j]
            x = nums[i]
            y = nums[j]
            left = f(i + 1, j)
            right = f(i, j - 1)
            return max(x - left, y - right)
        return 0 - 1 < f(0, len(nums) - 1)
