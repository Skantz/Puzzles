from functools import cache


class Solution:
    @cache
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 0
        if len(s) < 3:
            return 0 if s[0] == s[-1] else 1
        f = self.minInsertions
        if s[0] == s[-1]:
            return f(s[1:len(s) - 1])
        left = 1 + f(s[1:len(s)])
        right = 1 + f(s[0:len(s) - 1])
        return min(left, right)
