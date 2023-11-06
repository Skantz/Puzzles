class Solution:
    def romanToInt(self, s: str) -> int:
        mapp_rev = {1:"I", 4: "IV", 5:"V", 9:"IX",
                    10:"X", 40:"XL", 50:"L", 90:"XC",
                    100:"C", 400:"CD", 500:"D", 900:"CM",
                    1000:"M"}
        mapp = {mapp_rev[v]:v for v in mapp_rev}
        roman = sorted(list(mapp), key=lambda k: (-len(k), -mapp[k]))
        n = 0
        while s:
            for e in roman:
                t = s
                s = s.replace(e, "", 1)
                if t != s:
                    n += mapp[e]
                    break
        return n
