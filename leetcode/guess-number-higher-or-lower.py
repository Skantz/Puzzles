from random import randint
class Solution:
    def guessNumber(self, n: int) -> int:
        lb = 1
        ub = n
        while True:
            g = randint(lb, ub)
            ans = guess(g)
            if ans == 0:
                return g
            elif ans < 0:
                ub = g
            elif ans > 0:
                lb = g
            else:
                assert False
