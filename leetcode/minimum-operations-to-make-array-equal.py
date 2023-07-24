class Solution:
    def minOperations(self, n: int) -> int:
        return (2 * n**2 - 1 + (-1)**n)//8
