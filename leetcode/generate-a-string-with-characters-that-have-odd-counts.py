class Solution:
    def generateTheString(self, n: int) -> str:
        if not n % 2:
            return 'a' * (n - 1) + 'b'
        return 'a' * n
