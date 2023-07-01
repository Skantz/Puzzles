class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        xnum = num/2
        for _ in range(ceil(math.log2(num) + 1)):
            xnum = 0.5 * (xnum + num / xnum)
        return round(xnum) * round(xnum) == num
