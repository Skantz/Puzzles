class Solution:
    def numberOfCuts(self, n: int) -> int:
        match (n, n % 2):
            case (1, _): return 0
            case (_, 0): return n // 2
            case _: return n
