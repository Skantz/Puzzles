class Solution:
    mems = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        if n in self.mems:
            return self.mems[n]
        x = self.climbStairs(n - 1)
        y = self.climbStairs(n - 2)
        self.mems[n] = x + y
        return x + y
