class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd
        return gcd(max(nums), min(nums))
