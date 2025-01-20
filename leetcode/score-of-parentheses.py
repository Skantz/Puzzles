class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        r = 0
        l = []
        for e in s:
            if e == '(':
                l += [r]
                r = 0
                continue
            r = max(2 * r, 1) + l.pop()
        return r
