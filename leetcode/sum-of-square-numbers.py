class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(1, int(sqrt(c) + 1)):
            if (c - i**2)**0.5 == int((c - i**2)**0.5):
                return True
        return False
