class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = int(num)
        r = n % 10
        while r == 0:
            n = n // 10
            r = n % 10
        return str(n)
