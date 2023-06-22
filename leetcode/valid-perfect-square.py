class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return 0
        xnum = num/2
        for _ in range(20):
            xnum = 0.5 * (xnum  + num / xnum)
        return round(xnum)*round(xnum) == num
