class Solution:
    def hasIncreasingSubarrays(self, nums, k: int) -> bool:
        n = len(nums)
        def f(x): return all(x[i - 1] < x[i] for i in range(1, len(x)))
        for i in range(n - k * 2 + 1):
            if f(nums[i : i + k]) and f(nums[i + k : i + k + k]):
                return True
        return False
