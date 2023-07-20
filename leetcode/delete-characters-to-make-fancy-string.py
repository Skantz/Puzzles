class Solution:
    def makeFancyString(self, s: str) -> str:
        s_ = set(s)
        for e in s_:
            while e * 3 in s:
                s = s.replace(e*3, e*2)
        return s
