class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = lambda x : 1 if x < 2 else x * (f (x - 1))
        return f(m + n - 2) // (f(m - 1) * f(n - 1))
