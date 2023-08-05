class Solution:
    mems = {}
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n > target:
            return 0
        elif target > n * k:
            return 0
        elif n == target:
            return 1
        s = 0
        for i in range(1, k + 1):
            if ((n - 1, k, target - i)) in self.mems:
                e = self.mems[(n - 1, k, target - i)]
            else:
                e = self.numRollsToTarget(n - 1, k, target - i)
                self.mems[(n - 1, k, target - i)] = e
            s += e
        return s % (10**9 + 7)
