import re


class Solution:
    def isMatch(self, s_: str, p: str) -> bool:
        def nodup(s):
            if not s:
                return ""
            ret = s[0]
            for e in s[1:]:
                ret += "" if e == ret[-1] == "*" else e
            return ret
        return re.fullmatch(nodup(p), s_)
