class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        for i in range(1, 100 + 1):
            x = '0' * i in s
            y = '1' * i in s
            if (x and not y) or (not x and not y):
                return False
            if not x:
                return True
        assert False
