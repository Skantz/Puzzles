class Solution:
    def pivotInteger(self, n: int) -> int:
        return int((n * (n + 1) // 2)**0.5) if int((n * (n + 1) // 2)**0.5)**2 == n * (n + 1) // 2 else -1
