class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next([i, j] for i in range(10**4) for j in range(10**4) if "0" not in str(i) and "0" not in str(j) and i + j == n)
