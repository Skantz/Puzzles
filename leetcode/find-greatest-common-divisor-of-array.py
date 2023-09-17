class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n = max(nums)
        m = min(nums)
        return n if m < 1 else self.findGCD([m, n % m])
