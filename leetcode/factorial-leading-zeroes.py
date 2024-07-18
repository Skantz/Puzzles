class Solution:
    def trailingZeroes(self, n: int) -> int:
        s = 1
        while n:
            s *= n
            n -= 1
        r = 0
        while not s % 10:
            r += 1
            s = s // 10
        return r
