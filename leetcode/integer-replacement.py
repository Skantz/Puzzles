class Solution:
    def integerReplacement(self, n: int) -> int:
        def name(n):
            if n < 2:
                return 0
            if not n % 2:
                return 1 + name(n // 2)
            left = name(n + 1)
            right = name(n - 1)
            return 1 + min(left, right)
        return name(n)
