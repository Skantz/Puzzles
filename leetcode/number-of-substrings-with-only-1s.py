class Solution:
    def numSub(self, s: str) -> int:
        s = s.split("0")
        ret = 0
        for e in s:
            n = len(e)
            ret += n * (n + 1)//2
        return ret % (10**9 + 7)
