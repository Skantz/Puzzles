class Solution:
    mems = {}
    def tribonacci(self, n: int) -> int:
        match n:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 1
            case _:
                if n in self.mems:
                    return self.mems[n]
                self.mems[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
                return self.mems[n]
