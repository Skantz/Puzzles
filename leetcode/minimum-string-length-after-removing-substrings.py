class Solution:
    def minLength(self, s: str) -> int:
        s_old = s + "AB"
        while s_old != s:
            s_old = s
            s = (s.replace("AB", '').replace("CD", ''))
        return len(s)
