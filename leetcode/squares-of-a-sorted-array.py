class Solution:
    def sortedSquares(self, nums):
        return sorted(e**2 for e in nums)[::1]
