class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5
        # 1/n : 1.0
        # 1/n : 0.0
        # (n - 2)/n : f(n - 1)
        # => 0.5
