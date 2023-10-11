class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = 0
        for i in range(1, n + 1):
            s += (i if (i % m) else -i)
        return s
