class Solution:
    def intToRoman(self, num: int) -> str:
        mapp = {1:"I", 4: "IV", 5:"V", 9:"IX",
                10:"X", 40:"XL", 50:"L", 90:"XC",
                100:"C", 400:"CD", 500:"D", 900:"CM",
                1000:"M"}
        res = ""
        for e in sorted(mapp.keys())[::-1]:
            while num >= e:
                num = num - e
                res = res + mapp[e]
        return res
