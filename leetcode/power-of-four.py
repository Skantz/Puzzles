class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 4:
            return True
        if n <= 3:
            return False
        if n in [8, 12]:
            return False
        while n > 1:
            if not n % 4 == 0:
                return False
            n = n / 4
        return n == 1
