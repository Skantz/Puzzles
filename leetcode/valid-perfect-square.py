class Solution:
    log = lambda x : 2**32 * x ** (1/2 ** 32) - 2**32
    log2 = lambda x : log(x) / log(2)
    def isPerfectSquare(self, num: int) -> bool:
        xnum = num/2
        for _ in range(ceil(log2(num) +1)):
            xnum = 0.5 * (xnum  + num / xnum)
        return round(xnum) * round(xnum) == num
