class Solution:
    def differenceOfSum(self, nums) -> int:
        def f(x): return sum([int(e) for e in list(str(x))])
        return sum(nums) - sum(f(x) for x in nums)
