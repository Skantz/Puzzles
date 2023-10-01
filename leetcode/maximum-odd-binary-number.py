class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n, m = len(s), s.count("1")
        return "1" * (m - 1) + "0" * (n - m) + "1"
