class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s = start
        for i in range(1, n):
            start ^= (s + i*2)
        return start
