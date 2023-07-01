class Solution:
    def maxProfitNaive(self, prices: List[int]) -> int:
        n = len(prices)
        maxx = 0
        for i in range(n):
            for j in range(i + 1, n):
                maxx = max(maxx, prices[j] - prices[i])
        return maxx
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxx = 0
        minn = max(prices)
        for i in range(0, n):
            maxx = max(maxx, prices[i] - minn)
            minn = min(minn, prices[i])
        return maxx
