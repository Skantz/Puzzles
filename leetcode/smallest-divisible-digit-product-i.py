class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 100 + 1):
            p = 1
            for e in str(i):
                p *= int(e)
            if p % t == 0:
                return i
        assert False
