class Solution:
    def isValid(self, s: str) -> bool:
        s_p = s
        s = s + "abc"
        while s_p != s:
            s = s_p
            s_p = s_p.replace("abc", "")
        return s_p == ""
