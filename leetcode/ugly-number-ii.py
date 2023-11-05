class Solution:
    def nthUglyNumber(self, n: int) -> int:
        rets = []
        for i in range(35):
            for j in range(25):
                for k in range(20):
                    rets.append(2**i * 3**j * 5**k)
        rets.sort()
        return rets[n - 1]
