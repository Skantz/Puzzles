class Solution:
    def checkString(self, s: str) -> bool:
        try:
            return s[:s.index("b")].count("b") == 0 and s[s.index("b"):].count("a") == 0
        except ValueError:
            return True
