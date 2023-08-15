class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt
        if c == 0:
            return True
        for i in range(1, int(sqrt(c) + 1)):
            if sqrt(c - i**2) == int(sqrt(c - i**2)):
                return True
        return False
