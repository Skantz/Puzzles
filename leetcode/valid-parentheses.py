class Solution:
    def isValid(self, s: str) -> bool:
        starts = ["(", "{", "["]
        ends = [")", "}", "]"]
        ss = "(" + s + ")"
        while s != ss:
            for b in starts:
                ss = s
                s = s.replace(b + ends[starts.index(b)], "")
        if len(s) % 2 != 0:
            return False
        for i in range(len(s) //2):
            if s[i] in ends or ends[starts.index(s[i])] != s[len(s) - i - 1]:
                return False
        return True
