class Solution:
    def clearDigits(self, s: str) -> str:
        if not any(e.isdigit() for e in s):
            return s
        f = self.clearDigits
        for i, e in enumerate(s):
            if e.isdigit():
                return f(s[:i - 1] + s[i + 1:])
