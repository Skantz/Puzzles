class Solution:
    def arrangeCoins(self, n: int, m: Optional[int] = 1) -> int:
        return 0 if n <= 0 or n < m else 1 + self.arrangeCoins(n - m, m + 1)
