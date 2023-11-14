class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ") #1
        pos = s and s[0] != "-" #2
        if s and s[0] in ["+", "-"]:
            s = s[1:]
        new_s = ""
        for e in s:
            if not e.isnumeric():
                break
            new_s += e
        s = new_s #3
        if not s:
            return 0
        s = int(s) * (-1 if not pos else 1) #4
        s = max(-2**31, min(2**31 - 1, s)) #5
        return s #6
