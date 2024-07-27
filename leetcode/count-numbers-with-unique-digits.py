class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 1: return 1
        n, f = min(9, n), self.countNumbersWithUniqueDigits
        def g(x): return 1 if x < 2 else x * g(x - 1)
        return 9 * g(9) // g(10 - n) + f(n - 1)
        # 9 * g(9) : no leading zero
