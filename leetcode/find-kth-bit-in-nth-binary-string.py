class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        m = 1
        s = '0'
        while m - 1 < n:
            s = s + '1' + ("".join('1' if e == '0' else '0' for e in s))[::-1]
            m += 1
        return s[k - 1]
