from functools import cache


class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        #pp
        i = 0
        while i < len(p) and i < len(s) and (s[i] == p[i] or p[i] == '?'):
            i += 1
        s = s[i:]
        p = p[i:]
        #pp
        if len(p) < 1:
            return not s
        if p[0] != '*':
            return False
        sn = len(s)
        if sn < p.count('?') or sn < len(p.replace('*', "")):
            return False
        return self.isMatch(s, p.lstrip('*')) or self.isMatch(s[1:], p)
