class Solution:
    def lastRemaining(self, n: int) -> int:
        if n <= 1:
            return n
        nxt = 2 * self.lastRemaining(n // 2)
        return n - nxt + 2 - (1 if n % 2 else 0)
