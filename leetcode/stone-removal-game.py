class Solution:
    def canAliceWin(self, n: int) -> bool:
        d = 10
        b = False
        while d - 1 < n:
            n -= d
            d -= 1
            b ^= True
        return b
